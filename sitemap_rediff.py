#!/usr/bin/env python3
"""sitemap_rediff.py — re-diff a site's sitemap against its filelist, live-verified.

WHY: a filelist built from a sitemap silently under-collects when the sitemap is
capped, paginated, or rots. Re-fetching it later is append-only and safe — it
never overwrites the filelist, it only proposes additions. Two traps this tool
exists to handle:

  1. MALFORMED HREFS. Some sites emit doubly-prefixed links, e.g.
     i-sis.org.uk's sitemap.php contains
         <A HREF='https://www.i-sis.org.uk/http://www.i-sis.org.uk/X.php'>
     A naive urljoin+diff reports those as brand-new pages, and live-verifying
     the mangled form always 404s (the path is garbage). Here the bogus outer
     prefix is stripped and the inner URL is used, so the diff sees the real
     target. On i-sis this turned 15 false candidates into 3 real ones.

  2. ROTTED LINKS. Sitemaps accumulate dead entries. Every candidate is
     live-verified with a GET and dropped unless it returns 200 with a real
     <title> and no 404/"not found" in it.

Output is a BARE JSON LIST OF URL STRINGS, which is exactly what
append_enumerated_pages.py accepts (it skips non-str entries silently).

Usage:
    python3 sitemap_rediff.py i-sis.org.uk https://www.i-sis.org.uk/sitemap.php
    python3 sitemap_rediff.py svpwiki.com https://svpwiki.com/sitemap.xml --no-verify

Then, if the output is non-empty:
    python3 append_enumerated_pages.py <site> <out.json>
    # append_enumerated_pages.py re-dumps with indent=1; the repo convention is
    # indent=2, so re-dump afterwards or the diff becomes whitespace churn.
"""
import argparse
import html
import json
import os
import re
import subprocess
import sys
import urllib.parse

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

ASSET_EXT = (".css", ".jpg", ".jpeg", ".gif", ".png", ".svg", ".ico", ".js",
             ".zip", ".mp3", ".mp4", ".pdf", ".doc", ".xls", ".xml", ".txt")
META_PATHS = ("about.php", "contact.php", "menu.php", "search.php",
              "sitemap.php", "onlinestore", "coloursofwater")
UA = "Mozilla/5.0 (compatible; AFLinks-archiver/1.0)"

# Matches the bogus '/http://...' or '/https://...' tail of a doubly-prefixed href.
_DOUBLE_PREFIX = re.compile(r"^/(https?):/(/?)(.*)$", re.S)


def fetch(url, timeout=60):
    r = subprocess.run(["curl", "-sS", "-L", "--max-time", str(timeout),
                        "-A", UA, url],
                       capture_output=True, text=True, timeout=timeout + 20)
    return r.stdout


def repair_double_prefix(parsed):
    """Strip a bogus outer prefix and return the inner parsed URL.

    'https://www.i-sis.org.uk/http://www.i-sis.org.uk/X.php' -> the inner URL.
    Returns (parsed_url, was_repaired).
    """
    m = _DOUBLE_PREFIX.match(parsed.path)
    if not m:
        return parsed, False
    inner = m.group(1) + "://" + m.group(3)
    return urllib.parse.urlparse(inner), True


def canonical(url):
    """Comparison key: host-less path, lowercased, trailing slash trimmed."""
    p = urllib.parse.urlparse(url if "://" in url
                              else "https://example.invalid/" + url.lstrip("/"))
    return p.path.lower().rstrip("/")


def collect_existing(filelist):
    """Every URL-ish string anywhere in the filelist (url/filename/link, nested)."""
    found = set()

    def walk(o):
        if isinstance(o, str):
            found.add(o)
        elif isinstance(o, dict):
            for k in ("url", "path", "link"):
                if isinstance(o.get(k), str):
                    found.add(o[k])
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(filelist)
    return found


def live_ok(url, timeout=45):
    """True only for a 200 with a real title and no 404 marker in it."""
    try:
        body = fetch(url, timeout)
    except Exception:
        return False, "fetch-error"
    m = re.search(r"<title[^>]*>(.*?)</title>", body, re.I | re.S)
    title = html.unescape(re.sub(r"\s+", " ", m.group(1))).strip() if m else ""
    if not title:
        return False, "no-title"
    if re.search(r"\b404\b|not found", title, re.I):
        return False, f"title-says-404 ({title[:50]})"
    if len(body) <= 500:
        return False, f"body-too-small ({len(body)}B)"
    return True, title[:70]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("site", help="site slug as used by the filelist, e.g. i-sis.org.uk")
    ap.add_argument("sitemap_url", help="sitemap URL to re-diff")
    ap.add_argument("--out", default=None, help="output JSON path (bare URL list)")
    ap.add_argument("--no-verify", action="store_true",
                    help="skip live verification (candidates are unverified)")
    args = ap.parse_args()

    slug = args.site.replace(".", "_").replace("/", "_")
    out_path = args.out or f"/tmp/{slug}_rediff_urls.json"
    fl_path = os.path.join(SCRIPT_DIR, f"{slug}_filelist.json")

    raw = fetch(args.sitemap_url)
    if not raw:
        print(f"ERROR: empty response from {args.sitemap_url}", file=sys.stderr)
        return 1

    hrefs = re.findall(r'href\s*=\s*["\']([^"\']+)["\']', raw, re.I)
    base = urllib.parse.urljoin(args.sitemap_url, ".")
    host = urllib.parse.urlparse(args.sitemap_url).netloc.lower().split(":")[0]
    site_host = host[4:] if host.startswith("www.") else host

    urls, repaired, foreign = set(), 0, set()
    for h in hrefs:
        h = html.unescape(h.strip())
        if not h or h.startswith(("mailto:", "javascript:", "#")):
            continue
        p, was_repaired = repair_double_prefix(urllib.parse.urlparse(urllib.parse.urljoin(base, h)))
        repaired += int(was_repaired)
        if p.scheme not in ("http", "https"):
            continue
        netloc = p.netloc.lower()
        if not (netloc == site_host or netloc.endswith("." + site_host)):
            foreign.add(netloc)
            continue
        path = p.path
        if path.lower().endswith(ASSET_EXT):
            continue
        low = path.lower()
        if any(m in low for m in META_PATHS):
            continue
        norm = f"{p.scheme}://{p.netloc}{path}"
        if p.query:
            norm += "?" + p.query
        urls.add(norm)

    if not os.path.exists(fl_path):
        print(f"ERROR: filelist not found: {fl_path}", file=sys.stderr)
        return 1
    existing = collect_existing(json.load(open(fl_path, encoding="utf-8")))
    existing_keys = {canonical(u) for u in existing}

    candidates = sorted(u for u in urls if canonical(u) not in existing_keys)

    print(f"sitemap hrefs={len(hrefs)} double-prefix-repaired={repaired} "
          f"filtered={len(urls)} foreign-hosts={sorted(foreign)}")
    print(f"filelist paths={len(existing_keys)} candidates={len(candidates)}")

    verified, dropped = [], []
    for u in candidates:
        if args.no_verify:
            verified.append(u)
            print(f"  UNVERIFIED  {u}")
            continue
        ok, note = live_ok(u)
        (verified if ok else dropped).append(u)
        print(f"  {'KEEP' if ok else 'DROP'}  {note:<40} {u}")

    json.dump(verified, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nverified live: {len(verified)}  dropped: {len(dropped)}")
    print(f"wrote {out_path}")
    if not verified:
        print("no candidates survived — nothing to append (merge is still worth running)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
