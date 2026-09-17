#!/usr/bin/env python3
"""enumerate_wiki_pages.py — enumerate every page of a wiki archive.

WHY: link-following crawlers under-collect on wiki sites. Pages not linked from
the crawl seed are never discovered, and sitemap.xml is often truncated
(svpwiki.com's lists 500 of ~15,000 pages). The wiki's own page index is the
authoritative enumeration.

Supports:
  --engine tiki    tiki-listpages.php?offset=N     (TikiWiki, e.g. svpwiki.com)
  --engine mediawiki  api.php?action=query&list=allpages  (MediaWiki)

State is checkpointed to a JSON file so a run killed by a cron time budget
resumes at the next offset instead of starting over.

Usage:
    python3 enumerate_wiki_pages.py --base https://svpwiki.com --engine tiki \
        --state svpwiki_com_allpages.json --out svpwiki_com_allpages.txt
"""
import argparse
import json
import os
import re
import time
import urllib.parse
import urllib.request

HEADERS = {"User-Agent": "Mozilla/5.0 (AFLinks enumerator; research archive)"}


def fetch(url, timeout=60):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="replace")


def parse_tiki(html):
    """TikiWiki page links: <a href="Page-Name" class="link tips" title="X:View page">"""
    out = []
    for m in re.finditer(r'<a\s+href="([^"]+)"\s+class="link tips"[^>]*title="[^"]*:View page"', html):
        h = m.group(1)
        if h.startswith("http") or h.startswith("tiki-") or "?" in h:
            continue
        out.append(h.lstrip("/"))
    return out


def parse_mediawiki(payload):
    d = json.loads(payload)
    return [p["title"] for p in d.get("query", {}).get("allpages", [])]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True, help="site root, e.g. https://svpwiki.com")
    ap.add_argument("--engine", default="tiki", choices=["tiki", "mediawiki"])
    ap.add_argument("--step", type=int, default=25, help="pages per request (tiki)")
    ap.add_argument("--max-offset", type=int, default=40000)
    ap.add_argument("--state", required=True)
    ap.add_argument("--out", required=True, help="text file, one URL per line")
    ap.add_argument("--checkpoint-every", type=int, default=500)
    a = ap.parse_args()

    base = a.base.rstrip("/")
    pages, offset = set(), 0
    if os.path.exists(a.state):
        try:
            st = json.load(open(a.state))
            pages = set(st.get("pages", []))
            offset = st.get("next_offset", 0)
            print(f"resume from offset {offset}, {len(pages)} pages so far", flush=True)
        except Exception:
            pass

    empty_streak = 0
    while offset <= a.max_offset:
        if a.engine == "tiki":
            url = f"{base}/tiki-listpages.php?offset={offset}"
        else:
            url = (f"{base}/api.php?action=query&list=allpages&aplimit=500"
                   f"&apcontinue={urllib.parse.quote(str(offset))}&format=json")
        try:
            raw = fetch(url)
        except Exception as e:
            print(f"ERR offset={offset}: {e}", flush=True)
            time.sleep(2)
            empty_streak += 1
            if empty_streak > 5:
                break
            # Do NOT advance the offset on a fetch failure. svpwiki's
            # listpages endpoint legitimately takes 17-25s, so a timeout is
            # usually transient: retry the same offset. Advancing here would
            # silently skip that page range and the row would never be
            # discovered, because resume reads next_offset.
            continue

        if a.engine == "tiki":
            found = parse_tiki(raw)
        else:
            found = parse_mediawiki(raw)
            if not found:
                break

        for h in found:
            pages.add(base + "/" + urllib.parse.quote(h, safe="-_.~()%"))
        empty_streak = empty_streak + 1 if not found else 0

        if offset % a.checkpoint_every == 0:
            print(f"offset={offset} total={len(pages)}", flush=True)
            json.dump({"pages": sorted(pages), "next_offset": offset + a.step}, open(a.state, "w"))
            with open(a.out, "w", encoding="utf-8") as f:
                f.write("\n".join(sorted(pages)))

        if empty_streak >= 3:
            print(f"stopping: 3 empty pages at offset {offset}", flush=True)
            break
        offset += a.step
        time.sleep(0.12)

    json.dump({"pages": sorted(pages), "next_offset": offset}, open(a.state, "w"))
    with open(a.out, "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(pages)))
    print(f"DONE pages={len(pages)} last_offset={offset}", flush=True)


if __name__ == "__main__":
    main()