#!/usr/bin/env python3
"""content_extract.py — extract REAL document text from a harvested page.

WHY THIS EXISTS
---------------
The first-generation harvest (`process_generic_cloud.fetch_html_text`) stripped
HTML by deleting `<script>`/`<style>` and then replacing *every* remaining tag
with a space. That works on a page whose body is only article text, and fails on
every real site: navigation menus, sidebars, breadcrumbs, login forms and
"Jump to content / Main page / Random page / Recent changes" chrome come out as
prose. 17% of the harvested previews in the index carry that contamination, and
since previews are truncated to the FIRST 1500-2000 characters, on the worst
sites the chrome *is* the whole document.

This module does what the naive stripper should have: find the element that
actually holds the document, delete the chrome inside it, then flatten to text.

    title, text = extract_content(html, url)
    title, text = extract_content(html, url, max_chars=2000)

Design constraints (deliberate):
  * stdlib ONLY. The harvest runs on cloud cron turns and on the Windows box;
    neither is guaranteed to have bs4/lxml, and pip is not always available.
  * Balance-aware. Regex alone cannot find the end of `<div id="mw-content-text">`
    because it contains nested divs; we walk tag depth instead.
  * Site-aware first, generic second. Wikipedia-family, TikiWiki and vBulletin
    each expose a stable content container; use it when present.
  * Conservative last resort. If nothing matches, fall back to a paragraph
    harvest (nav menus are `<li><a>`, prose is `<p>`) and then to plain
    tag-stripping — never worse than the old behaviour.

Verified against: wiki.naturalphilosophy.org (MediaWiki), svpwiki.com (TikiWiki),
energeticforum.com (vBulletin 5), viXra.org, rexresearch.com.
"""
import html as _html
import re

# --------------------------------------------------------------------------
# tag walking
# --------------------------------------------------------------------------
TAG_RE = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9:-]*)((?:\"[^\"]*\"|'[^']*'|[^>])*?)(/?)>")


def find_element_end(html, body_start, tag):
    """Given the index just past `<tag ...>`, return the index just before the
    matching `</tag>`. Nested same-name elements are counted. Returns len(html)
    if the document is unbalanced/truncated."""
    depth = 1
    for m in TAG_RE.finditer(html, body_start):
        if m.group(2).lower() != tag:
            continue
        if m.group(1) == "/":
            depth -= 1
            if depth == 0:
                return m.start()
        elif not m.group(4):  # not self-closing
            depth += 1
    return len(html)


def _iter_open_tags(html, tag):
    """Yield (start, end, attrs) for each non-self-closing `<tag ...>`."""
    pat = re.compile(r"<(%s)\b((?:\"[^\"]*\"|'[^']*'|[^>])*?)(/?)>" % tag, re.I)
    for m in pat.finditer(html):
        if m.group(3):
            continue
        yield m.start(), m.end(), m.group(2)


def drop_elements(html, tag, attr_pattern=None):
    """Remove every balanced `<tag>` element (optionally only those whose
    attribute string matches attr_pattern). Keeps any nested content that is
    not itself inside a matched element."""
    if attr_pattern is None and not re.search(r"<%s\b" % tag, html, re.I):
        return html
    out = []
    i = 0
    for start, end, attrs in _iter_open_tags(html, tag):
        if start < i:
            continue
        if attr_pattern and not re.search(attr_pattern, attrs, re.I | re.S):
            continue
        out.append(html[i:start])
        i = find_element_end(html, end, tag)
        # skip the matching close tag
        cm = re.compile(r"</%s\s*>" % tag, re.I).match(html, i)
        if cm:
            i = cm.end()
    out.append(html[i:])
    return "".join(out)


# --------------------------------------------------------------------------
# site containers — (name, regex for the OPENING tag)
# --------------------------------------------------------------------------
# Every pattern must match a COMPLETE opening tag (ending in `>`) so that
# find_element_end() starts from the right offset and no attribute text leaks
# into the extracted body.
SITE_CONTAINERS = [
    # MediaWiki (Wikipedia, naturalphilosophy, svpwiki's semantic layer, ...)
    ("mediawiki", r'<div[^>]+id="mw-content-text"[^>]*>'),
    ("mediawiki", r'<div[^>]+class="[^"]*mw-parser-output[^"]*"[^>]*>'),
    # TikiWiki (svpwiki, tiki-index)
    ("tikiwiki", r'<article[^>]+id="top"[^>]*>'),
    ("tikiwiki", r'<div[^>]+class="[^"]*wikitext[^"]*"[^>]*>'),
    ("tikiwiki", r'<div[^>]+id="tiki-content"[^>]*>'),
    # vBulletin 4/5 (energeticforum)
    ("vbulletin", r'<div[^>]+class="[^"]*js-post__content-text[^"]*"[^>]*>'),
    ("vbulletin", r'<div[^>]+class="[^"]*postcontent[^"]*"[^>]*>'),
    ("vbulletin", r'<div[^>]+id="postlist"[^>]*>'),
    # phpBB
    ("phpbb", r'<div[^>]+class="[^"]*postbody[^"]*"[^>]*>'),
    # WordPress / generic blogs
    ("wordpress", r'<div[^>]+class="[^"]*(?:entry-content|post-content|article-content)[^"]*"[^>]*>'),
    ("wordpress", r'<article[^>]*>'),
    # structural fallbacks
    ("html5", r"<main[^>]*>"),
    ("html5", r'<div[^>]+id="bodyContent"[^>]*>'),
    ("html5", r'<div[^>]+id="content"[^>]*>'),
    ("html5", r'<div[^>]+class="[^"]*content[^"]*"[^>]*>'),
]

# Chrome that lives INSIDE a content container and must go.
CHROME_TAGS = ("script", "style", "noscript", "svg", "iframe", "form", "nav", "aside",
               "header", "footer", "button", "select")

CHROME_ATTRS = (
    r"class=\"[^\"]*(?:nav|menu|sidebar|breadcrumb|crumb|footer|header|toc|"
    r"editsection|mw-jump|jump-|printfooter|catlinks|mw-indicators|vector-|"
    r"mw-portlet|pagenav|pager|pagination|toolbar|share|social|userinfo|author|"
    r"avatar|signature|notice|widget|module-title|module-buttons|tabbar|"
    r"attachment|poll|rating|reputation|postbit|b-sharing|b-meter|b-post__menu|"
    r"controls|actions|options|login|register|search|sidebar-toggle|"
    r"poster|quote-bar|thread-tools|site-|page-actions|tiki-actions|"
    r"searchbox|breadcrumbs|topbar|banner|advert|promo|cookie)[^\"]*\""
)

# Exact nav labels that can survive as their own line (short tokens only).
NAV_LABELS = {
    "jump to content", "main menu", "move to sidebar", "hide", "show", "navigation",
    "main page", "random page", "recent changes", "recently added", "browse",
    "contents", "toggle the table of contents", "toggle", "personal tools",
    "log in", "log out", "create account", "request account", "request an account",
    "search", "appearance", "page", "discussion", "view source", "view history",
    "read", "edit", "tools", "what links here", "related changes", "special pages",
    "printable version", "permanent link", "page information", "cite this page",
    "wikidata item", "download as pdf", "languages", "donate", "shop", "funding",
    "books", "articles", "lectures", "date", "home", "about", "contact us",
    "privacy policy", "terms of service", "disclaimer", "disclaimers",
    "powered by mediawiki", "powered by", "cookie", "cookies", "faq", "members",
    "calendar", "homepage", "page actions", "share", "send link", "print", "pdf",
    "loading...", "username", "password", "capslock is on", "i forgot my password",
    "next", "previous", "template", "collapse", "expand", "filter", "show all",
    "announcement", "no announcement yet", "posts", "latest activity", "photos",
    "wiki to-do list", "suggest content", "all categories", "categories",
    "site map", "advanced search", "search forums", "what's new", "new posts",
    "forums", "threads", "today's posts", "mark forums read", "go to page",
    "top", "bottom", "index", "site navigation", "watch", "unwatch",
    # MediaWiki / Vector navigation that survives as its own line
    "scientists by output", "live sessions", "our organization", "talks",
    "conferences", "journals", "papers", "request an account", "suggest content",
    "all categories", "wiki to-do list", "english", "actions", "general",
    "retrieved from", "category", "scientific paper", "read in full",
    "link to paper", "read the full paper here", "author(s)", "keywords",
    "published", "journal", "volume", "number", "no. of pages", "pages",
    "toggle the table of contents", "in other projects", "print/export",
    "download as pdf", "browse", "about", "contact us", "live sessions",
    # SVPwiki / TikiWiki plumbing
    "loading...", "log in", "sympathetic vibratory physics",
    "bridging science and spirituality", "i forgot my password",
    "pdf print share send link", "page actions", "send link",
    # rsarchive
    "donate", "funding", "shop", "books", "articles", "lectures", "date",
    "the rudolf steiner archive", "a project of steiner online library",
    "donate books to help fund our work", "previous", "table of contents",
}


def _clean_ws(s):
    return re.sub(r"\s+", " ", s).strip()


def clean_title(raw, url=""):
    """Strip the site-name suffix TikiWiki/MediaWiki append to <title>."""
    t = _clean_ws(raw)
    if not t:
        return ""
    for sep in (" | ", " – ", " — ", " :: ", " - "):
        if sep in t:
            parts = [p.strip() for p in t.split(sep) if p.strip()]
            if len(parts) >= 2:
                # whichever side is NOT a bare site name is the title; prefer
                # the longest fragment, which is nearly always the page title.
                t = max(parts, key=len)
            break
    return t


def _html_to_text(frag):
    """Flatten an HTML fragment to text, preserving block boundaries."""
    frag = re.sub(r"(?is)<(script|style|noscript|svg|iframe)\b.*?</\1\s*>", " ", frag)
    frag = re.sub(r"(?is)<br\s*/?>", "\n", frag)
    frag = re.sub(r"(?is)</?(p|div|li|tr|h[1-6]|blockquote|section|article|pre|dd|dt|"
                  r"table|thead|tbody|ul|ol|figure|figcaption)\b[^>]*>", "\n", frag)
    frag = re.sub(r"(?s)<[^>]+>", " ", frag)
    frag = _html.unescape(frag)
    frag = frag.replace("\xa0", " ")
    # tidy each line, drop nav-label-only lines
    lines = []
    for ln in frag.split("\n"):
        ln = _clean_ws(ln)
        if not ln:
            continue
        if len(ln) <= 40 and ln.lower().strip(" .:»«-—") in NAV_LABELS:
            continue
        lines.append(ln)
    return "\n".join(lines)


def _paragraph_harvest(html):
    """Generic fallback: nav menus are list items and links; prose is
    paragraphs. Keep only paragraphs with real sentence-length text."""
    html = re.sub(r"(?is)<(script|style|noscript|svg|iframe|nav|aside|header|footer|form)\b.*?</\1\s*>",
                  " ", html)
    out = []
    for m in re.finditer(r"(?is)<p\b[^>]*>(.*?)</p\s*>", html):
        txt = _clean_ws(_html.unescape(re.sub(r"(?s)<[^>]+>", " ", m.group(1))))
        if len(txt) >= 40:
            out.append(txt)
    return "\n".join(out)


def _find_container(html):
    """Return (site_kind, inner_html) for the best matching content container."""
    for kind, pat in SITE_CONTAINERS:
        m = re.search(pat, html, re.I)
        if not m:
            continue
        tag = re.match(r"<([a-zA-Z0-9]+)", m.group(0)).group(1).lower()
        end = find_element_end(html, m.end(), tag)
        inner = html[m.end():end]
        # guard: a container that yields almost nothing is a bad match
        if len(_html_to_text(inner)) >= 200 or kind in ("mediawiki", "tikiwiki"):
            return kind, inner
    return "", ""


def extract_content(html, url="", max_chars=2000, want_title=True):
    """Return (title, text) with site chrome removed.

    Never returns less than the old naive stripper did: if every strategy comes
    up short, it falls back to whole-document tag stripping.
    """
    if not html:
        return "", ""

    title = ""
    if want_title:
        m = re.search(r"(?is)<title[^>]*>(.*?)</title\s*>", html)
        if m:
            title = clean_title(_html.unescape(m.group(1)), url)
        if not title:
            m = re.search(r'(?is)<meta[^>]+property="og:title"[^>]+content="([^"]*)"', html)
            if m:
                title = clean_title(_html.unescape(m.group(1)), url)

    kind, body = _find_container(html)

    if body:
        for t in CHROME_TAGS:
            body = drop_elements(body, t)
        for t in ("div", "ul", "ol", "span", "table", "section"):
            body = drop_elements(body, t, CHROME_ATTRS)
        text = _html_to_text(body)
        if len(text) >= 200:
            return title, text[:max_chars]

    # strategy 2: paragraph harvest on the whole document
    ph = _html_to_text(_paragraph_harvest(html))
    # strategy 3: plain strip (the old behaviour) as a floor
    flat = _html_to_text(html)

    best = max((ph, flat), key=len)
    if body:
        bt = _html_to_text(body)
        best = max(best, bt, key=len)
    return title, best[:max_chars]


def chrome_score(text):
    """Score how much navigation chrome a text blob still carries.

    Used in two places: to decide which harvested previews need repair, and to
    prove a repair worked. Two signals, because chrome shows up in two shapes:

      1. Phrase hits — menu labels survive as prose when the page was flattened.
         A curated list, not a broad keyword match: "Papers" alone is a menu
         item, "the papers were published in 1994" is content.

      2. Structural density — when an extractor keeps block boundaries, chrome
         arrives as a run of very short label-like lines ("Scientists /
         Scientists by output / Papers / Journals / Conferences / Live
         sessions"). Prose does not look like that. A head of >=8 lines where
         >=80% are under 45 chars and most are not sentences scores as chrome.

    A page can be 100% chrome and score 0 on phrases alone (that was a real
    miss: a MediaWiki stub whose entire body was menu labels), which is why the
    structural signal exists.
    """
    if not text:
        return 0
    low = text.lower()
    hits = sum(1 for m in CHROME_MARKERS if m in low)

    lines = [l.strip() for l in text.split("\n") if l.strip()]
    if len(lines) >= 8:
        head = lines[:25]
        short = sum(1 for l in head if len(l) <= 45)
        sentencey = sum(1 for l in head if re.search(r"[.!?]\s|,\s|\b(?:the|and|of|is|was|are)\b", l, re.I))
        if short / len(head) >= 0.8 and sentencey <= max(2, len(head) // 5):
            hits += 3

    # NOTE: there is deliberately no structural check for single-blob text.
    # First-generation previews were whitespace-collapsed to ONE line, so
    # splitting them on separators is just chopping prose at punctuation — a
    # padded padrak.com abstract scored 2 chrome hits with zero markers present.
    # Phrase markers are reliable on any text; structural density is only
    # meaningful when real line structure exists (which the extractor produces).
    return hits


CHROME_MARKERS = (
    "jump to content", "main menu", "move to sidebar", "recent changes",
    "random page", "toggle the table of contents", "personal tools",
    "view source", "what links here", "special pages", "permanent link",
    "printable version", "page information", "powered by mediawiki",
    "if this is your first visit", "register before you can post",
    "announcement collapse", "latest activity", "page actions",
    "i forgot my password", "capslock is on", "site map", "privacy policy",
    "wiki to-do list", "suggest content", "all categories",
    "scientists by output", "live sessions", "our organization",
    "request an account", "retrieved from", "this page was last edited",
    # login/account plumbing — only appears as chrome in practice
    "username :", "password :", "log in", "create account",
    # forum chrome
    "be sure to check out the faq", "to start viewing messages",
    "posts latest activity", "page of 1", "time all time today",
    "discussions only", "photos only", "videos only", "links only",
    # wiki/article footer plumbing
    "in other projects", "print/export", "download as pdf",
    "cookie", "terms of service", "disclaimer",
    # svpwiki / tiki
    "pdf print share send link", "i forgot my password",
    "140,000 single items or in bulk",
    # rsarchive
    "donate books to help fund", "steiner online library, a public charity",
)


STUB_MARKER = "[catalogued — no readable full-text preview available from source]"


if __name__ == "__main__":
    import sys
    src = sys.argv[1]
    with open(src, encoding="utf-8", errors="replace") as fh:
        raw = fh.read()
    t, x = extract_content(raw, src, max_chars=int(sys.argv[2]) if len(sys.argv) > 2 else 2000)
    print("TITLE:", t)
    print("CHROME SCORE:", chrome_score(x))
    print("-" * 70)
    print(x)