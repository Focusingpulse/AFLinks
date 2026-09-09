#!/usr/bin/env python3
"""
crawl_rsarchive.py — Rudolf Steiner Archive (rsarchive.org) harvester.

Steiner's corpus is huge and GA-numbered (Gesamtausgabe = Complete Works):
  /Books/GA001/...      — books (foundational, harvest first)
  /Lectures/GA053/...   — ~300+ lecture volumes, index page per GA lists
                          dated lecture pages (e.g. 19041215p01.html)
  /Articles/GA029/...   — essays/articles

The content IS the HTML pages (full text online, public charity project).
We harvest metadata + 600-char preview per content page into
rsarchive_org_progress.json (merge_all_progress.py format) so entries land
in index.json like every other source. Full text stays at rsarchive via
source_url (live working links — the site's pattern).

Dedup: within a GA, lecture pages appear in multiple presentation dirs
(SOL/, Singles/, HCL1933/ = different editions/translations). We keep ONE
entry per (GA, basename) — first seen wins.

Phases:
  catalog  — parse /Volumes.html + /Books/ + /Lectures/ for the GA list
  harvest  — per GA: fetch index, fetch content pages, extract, append
  status   — print progress summary

Usage:
  python3 crawl_rsarchive.py catalog
  python3 crawl_rsarchive.py harvest --max-pages 60
  python3 crawl_rsarchive.py harvest --ga GA053
  python3 crawl_rsarchive.py status

State files (all in SCRIPT_DIR):
  rsarchive_catalog.json    — GA list + book/lecture counts
  rsarchive_crawl_state.json — harvested GAs + page checkpoint (idempotent)
  rsarchive_org_progress.json — entries for merge_all_progress.py
"""

import os, re, json, time, sys, html, urllib.parse, urllib.request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = "https://rsarchive.org"
CATALOG_PATH = os.path.join(SCRIPT_DIR, "rsarchive_catalog.json")
STATE_PATH = os.path.join(SCRIPT_DIR, "rsarchive_crawl_state.json")
PROGRESS_PATH = os.path.join(SCRIPT_DIR, "rsarchive_org_progress.json")
CHECKPOINT_EVERY = 10          # pages between state saves
FETCH_DELAY = 0.4              # be gentle — charity server
PREVIEW_LEN = 600

# --- Steiner-aware category tagging -----------------------------------------
# Primary category for everything Steiner; cross-tags by topic keywords so
# the corpus connects to existing domains (connective tissue).
STEINER_CAT = "Anthroposophy / Rudolf Steiner"
STEINER_META = "Rudolf Steiner & Anthroposophy"
CROSS_KW = {
    "Agriculture": ["biodynamic", "agriculture course", "soil", "farm", "dornach agriculture",
                    "preparation 500", "horn manure", "horn silica", "demeter"],
    "Biology / Health": ["medicine", "healing", "therapy", "anthroposophic medicine",
                         "nurse", "illness", "remedy", "cure"],
    "Goethean Science": ["goethe", "goethean", "morpholog", "plant", "colour theory",
                         "metamorphosis"],
    "Education": ["waldorf", "education", "school", "curriculum", "teaching", "child"],
    "Optics / Colour Therapy": ["colour", "color", "light course"],
    "Sacred / Projective Geometry": ["geometry", "projective"],
    "Aether Physics": ["etheric", "aether", "ether body"],
    "Harmonics, Rhythms & Cycles": ["rhythm", "cycle", "eurythmy"],
}

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")


def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept": "text/html,*/*;q=0.8"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="ignore")


def strip_html(raw):
    body = re.sub(r"<script.*?</script>|<style.*?</style>", "", raw, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", body)
    return html.unescape(re.sub(r"\s+", " ", text)).strip()


def categorize(title, text):
    combined = (title + " " + text[:2000]).lower()
    cats = [STEINER_CAT]
    metas = [STEINER_META]
    for cat, kws in CROSS_KW.items():
        if any(kw in combined for kw in kws):
            cats.append(cat)
    return cats, metas


def parse_page(raw, url):
    """Extract title, date, preview from a lecture/book/article page."""
    m = re.search(r"<title>(.*?)</title>", raw, re.S)
    title = html.unescape(m.group(1)).strip() if m else url
    title = re.sub(r"\s*—\s*Rudolf Steiner Archive\s*$", "", title).strip()
    text = strip_html(raw)
    # Skip nav junk: content starts after the date line or the [ 1 ] marker.
    # Date pattern: "15 December 1904, Berlin" or "GA 53" header block.
    m2 = re.search(r"(\d{1,2}\s+(?:January|February|March|April|May|June|July|"
                   r"August|September|October|November|December)\s+\d{4})", text)
    date = m2.group(1) if m2 else ""
    start = m2.end() if m2 else 0
    if start == 0:
        m3 = re.search(r"\[\s*1\s*\]", text)
        start = m3.end() if m3 else min(250, len(text))
    preview = text[start:start + PREVIEW_LEN].strip()
    if not preview:
        preview = text[:PREVIEW_LEN]
    return title, date, preview


def load_json(path, default):
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return default


def save_json(path, obj):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False)
    os.replace(tmp, path)


# --- catalog -----------------------------------------------------------------

def do_catalog():
    """Build the GA volume list from /Volumes.html + /Books/ + /Lectures/."""
    gas = {}  # ga -> {"books": n, "lectures": n, "articles": n}
    for section, path in (("books", "/Books/"), ("lectures", "/Lectures/"),
                          ("articles", "/Articles/")):
        try:
            raw = fetch(BASE + path)
        except Exception as e:
            print(f"  {section}: fetch failed ({e})")
            continue
        found = re.findall(r'href="' + path + r'(GA[0-9]+[a-zA-Z_]*)/"', raw)
        uniq = sorted(set(found))
        for ga in uniq:
            gas.setdefault(ga, {})[section] = gas.get(ga, {}).get(section, 0) + 1
        print(f"  {section}: {len(uniq)} GA volumes")
    catalog = {"generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               "gas": gas}
    save_json(CATALOG_PATH, catalog)
    print(f"catalog: {len(gas)} GA volumes -> {os.path.basename(CATALOG_PATH)}")
    return catalog


def ga_index_urls(ga):
    """Possible index pages for a GA (books/lectures/articles roots)."""
    return [f"{BASE}/Books/{ga}/", f"{BASE}/Lectures/{ga}/", f"{BASE}/Articles/{ga}/"]


# --- harvest -----------------------------------------------------------------

def do_harvest(max_pages=60, only_ga=None):
    catalog = load_json(CATALOG_PATH, None)
    if not catalog:
        print("no catalog — run `python3 crawl_rsarchive.py catalog` first")
        sys.exit(1)
    state = load_json(STATE_PATH, {"done_gas": [], "pages_this_run": 0})
    progress = load_json(PROGRESS_PATH, {"entries": []})
    seen_urls = {e.get("source_url") for e in progress["entries"]}
    done_gas = set(state["done_gas"])
    gas_list = sorted(catalog["gas"].keys())
    if only_ga:
        gas_list = [g for g in gas_list if g == only_ga]

    pages = 0
    added = 0
    gas_done_this_run = []

    def harvest_page(url, ga):
        """Fetch one content page, append entry. Returns True if new entry."""
        nonlocal pages, added
        if url in seen_urls or pages >= max_pages:
            return False
        try:
            praw = fetch(url)
        except Exception:
            return False
        time.sleep(FETCH_DELAY)
        title, date, preview = parse_page(praw, url)
        cats, metas = categorize(title, preview)
        progress["entries"].append({
            "filename": os.path.basename(urllib.parse.urlparse(url).path),
            "title": title,
            "type": "document",
            "extension": ".html",
            "size_bytes": len(praw),
            "source_url": url,
            "categories": cats,
            "meta_categories": metas,
            "patent_numbers": [],
            "primary_person": "Rudolf Steiner",
            "content_preview": preview,
            "steiner_ga": ga,
            "steiner_date": date,
        })
        seen_urls.add(url)
        added += 1
        pages += 1
        if pages % CHECKPOINT_EVERY == 0:
            save_json(PROGRESS_PATH, progress)
            save_json(STATE_PATH, state)
        return True

    def walk_index(idx_url, ga, depth=0):
        """Fetch an index page; harvest its content pages; recurse into
        subdirectory links (books nest: GA -> language -> edition -> chapters)."""
        nonlocal pages
        if pages >= max_pages or depth > 2:
            return 0
        try:
            raw = fetch(idx_url)
        except Exception:
            return 0
        time.sleep(FETCH_DELAY)
        hrefs = sorted(set(re.findall(r'href="(/[^"]+)"', raw)))
        # content pages: .html under this GA path, skip nav/toc
        content = [h for h in hrefs if h.endswith(".html") and f"/{ga}/" in h
                   and not re.search(r"(index|_nav|\.toc)", h, re.I)]
        # subdirectory links under this GA path (recurse)
        subdirs = [h for h in hrefs if h.endswith("/") and f"/{ga}/" in h
                   and h != idx_url.split(BASE)[1]]
        # dedup by basename within GA (alternate editions collapse)
        by_base = {}
        for h in content:
            by_base.setdefault(os.path.basename(h), h)
        n = 0
        for rel in by_base.values():
            if pages >= max_pages:
                break
            if harvest_page(BASE + rel, ga):
                n += 1
        for sub in subdirs:
            if pages >= max_pages:
                break
            n += walk_index(BASE + sub, ga, depth + 1)
        return n

    for ga in gas_list:
        if ga in done_gas and not only_ga:
            continue
        ga_pages = 0
        for idx_url in ga_index_urls(ga):
            if pages >= max_pages:
                break
            ga_pages += walk_index(idx_url, ga)
        if ga_pages and not only_ga:
            done_gas.add(ga)
            state["done_gas"] = sorted(done_gas)
        gas_done_this_run.append((ga, ga_pages))
        if pages >= max_pages:
            break

    state["pages_this_run"] = pages
    state["last_run"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    save_json(PROGRESS_PATH, progress)
    save_json(STATE_PATH, state)
    print(f"harvest: {pages} pages fetched, {added} new entries, "
          f"{len(progress['entries'])} total in progress file")
    for ga, n in gas_done_this_run:
        if n:
            print(f"  {ga}: {n} pages")


def do_status():
    catalog = load_json(CATALOG_PATH, {"gas": {}})
    state = load_json(STATE_PATH, {"done_gas": []})
    progress = load_json(PROGRESS_PATH, {"entries": []})
    total = len(catalog.get("gas", {}))
    done = len(state.get("done_gas", []))
    print(f"GA volumes in catalog: {total}")
    print(f"GA volumes harvested:  {done} ({100*done/max(total,1):.0f}%)")
    print(f"entries in progress:   {len(progress.get('entries', []))}")
    remaining = [g for g in sorted(catalog.get("gas", {})) if g not in set(state.get("done_gas", []))]
    print(f"next up: {', '.join(remaining[:8])}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] == "status":
        do_status()
    elif args[0] == "catalog":
        do_catalog()
    elif args[0] == "harvest":
        max_pages = 60
        only_ga = None
        if "--max-pages" in args:
            max_pages = int(args[args.index("--max-pages") + 1])
        if "--ga" in args:
            only_ga = args[args.index("--ga") + 1]
        do_harvest(max_pages, only_ga)
    else:
        print(__doc__)
