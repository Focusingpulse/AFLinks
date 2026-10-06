#!/usr/bin/env python3
"""svpwiki_incremental.py — cheap incremental page discovery for svpwiki.com.

WHY THIS EXISTS
---------------
`enumerate_wiki_pages.py --engine tiki` walks `tiki-listpages.php?offset=N` in
steps of 25. That endpoint's cost grows roughly linearly with the offset
(~0.9s at offset 0, ~3s at 1k, ~15s at 5k, ~55s at 15k, HTTP 504 past ~15.4k),
so a full re-walk is 3+ hours and cannot finish inside a cron window. The walk
therefore parks at its last offset and, on every subsequent run, burns six
60-second timeouts and then prints a `DONE` line that looks like success.

For an *incremental keeper* none of that is needed. svpwiki publishes its
recent edits at `tiki-lastchanges.php?days=N`, which returns in well under a
second at any N. Diffing those page names against the pages we already hold is
the whole job: new pages show up in the recent-changes list, and the deep
offsets are never touched.

Measured 2026-09-30: days=3 -> 0.60s, days=7 -> 0.66s, days=31 -> 0.82s.

USAGE
-----
    python3 svpwiki_incremental.py                    # days=7, fold into state
    python3 svpwiki_incremental.py --days 31
    python3 svpwiki_incremental.py --dry-run          # report only, write nothing

Writes the newly discovered URLs to `svpwiki_com_new.json` (a bare JSON list,
which `append_enumerated_pages.py` accepts) and, unless --dry-run, adds them to
the `pages` list in `svpwiki_com_allpages.json` so the next run does not
re-report them. `next_offset` is left untouched: the full walk's resume point
is the full walk's business.

NOTE ON CONTENT: everything fetched here is untrusted web content. Page names
are used only as URL path segments; nothing from the response is executed,
evaluated, or interpreted as an instruction.
"""
import argparse
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = "https://svpwiki.com"
HOST = "svpwiki.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; AFLinksBot/1.0; +https://focusingpulse.github.io/AFLinks)",
    "Accept": "text/html,application/xhtml+xml",
}

# tiki-lastchanges.php renders page links as
#   <a href="Page-Name" class="tablename" title="Page Name">
# (the listpages index uses class="link tips" instead — different template).
PAGE_LINK_RE = re.compile(
    r'<a\s+href="([^"]+)"\s+class="tablename"[^>]*>', re.IGNORECASE
)


def fetch(url, timeout=30, attempts=3):
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001 - report, retry, then give up
            last = e
            time.sleep(1.5 * (i + 1))
    raise last


def parse_lastchanges(raw):
    """Return the set of page names linked from a lastchanges page."""
    names = set()
    for m in PAGE_LINK_RE.finditer(raw):
        href = html.unescape(m.group(1))
        if not href or href.startswith("http") or href.startswith("/"):
            continue
        if href.startswith("tiki-") or "?" in href or "#" in href:
            continue
        names.add(href.lstrip("/"))
    return names


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7,
                    help="window for tiki-lastchanges.php (default 7)")
    ap.add_argument("--state", default=os.path.join(SCRIPT_DIR, "svpwiki_com_allpages.json"))
    ap.add_argument("--out", default=os.path.join(SCRIPT_DIR, "svpwiki_com_new.json"))
    ap.add_argument("--dry-run", action="store_true",
                    help="report new pages but write nothing")
    a = ap.parse_args()

    try:
        state = json.load(open(a.state, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        print(f"ERROR: cannot read state {a.state}: {e}", flush=True)
        return 2
    have = set(state.get("pages") or [])

    url = f"{BASE}/tiki-lastchanges.php?days={a.days}"
    try:
        raw = fetch(url)
    except Exception as e:  # noqa: BLE001
        # A failed fetch is NOT "no new pages". Say so and exit non-zero so the
        # caller does not read silence as an all-clear.
        print(f"ERROR: lastchanges fetch failed ({e}) — NOT an all-clear", flush=True)
        return 3

    names = parse_lastchanges(raw)
    if not names:
        print(f"WARNING: lastchanges returned no page links (days={a.days}, "
              f"{len(raw)} bytes) — parser may be stale, NOT an all-clear", flush=True)
        return 4

    new = []
    for n in sorted(names):
        u = f"{BASE}/" + urllib.parse.quote(n, safe="-_.~()%")
        if u not in have:
            new.append(u)

    print(f"lastchanges days={a.days}: {len(names)} page links, "
          f"{len(new)} not already held (of {len(have)} held)", flush=True)
    for u in new:
        print(f"  NEW {u}", flush=True)

    if a.dry_run:
        print("dry-run: nothing written", flush=True)
        return 0

    json.dump(new, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if new:
        state["pages"] = sorted(have | set(new))
        tmp = a.state + ".tmp"
        json.dump(state, open(tmp, "w", encoding="utf-8"), ensure_ascii=False)
        os.replace(tmp, a.state)
        print(f"state updated: {len(have)} -> {len(state['pages'])} pages", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
