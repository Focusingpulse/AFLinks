#!/usr/bin/env python3
"""append_enumerated_pages.py — fold a site's enumerated page list into its filelist.

WHY: the generic crawler under-collects on TikiWiki/MediaWiki sites (it follows
links from a seed, so it misses pages that aren't linked from the crawl paths).
sitemap.xml is often capped (svpwiki's lists 500 of ~15,000 pages). The reliable
enumeration is the wiki's own index: tiki-listpages.php?offset=N for TikiWiki.

This merges an enumerated page list into <site>_filelist.json, preserving the
existing order (so progress indices stay valid) and appending only new URLs.

Usage:
    python3 append_enumerated_pages.py svpwiki.com /tmp/svp_pages.json
"""
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    site, enum_path = sys.argv[1], sys.argv[2]
    slug = site.replace(".", "_").replace("/", "_")
    fl_path = os.path.join(SCRIPT_DIR, f"{slug}_filelist.json")
    fl = json.load(open(fl_path, encoding="utf-8"))
    have = {e.get("url") for e in fl}
    pages = json.load(open(enum_path, encoding="utf-8"))
    # Accept either a bare JSON list of URLs or the enumeration STATE dict
    # ({"pages": [...], "next_offset": N}) written by enumerate_wiki_pages.py.
    if isinstance(pages, dict):
        pages = pages.get("pages") or []
    if not isinstance(pages, list):
        pages = []
    added = 0
    for u in pages:
        # Defensive: only ever fold in real URLs.
        if not isinstance(u, str) or not u.startswith("http"):
            continue
        if u in have:
            continue
        fl.append({"url": u, "filename": u.rstrip("/").split("/")[-1] or "index"})
        have.add(u)
        added += 1
    if added:
        tmp = fl_path + ".tmp"
        json.dump(fl, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        os.replace(tmp, fl_path)
    print(f"{site}: filelist {len(fl)} entries (+{added} new of {len(pages)} enumerated)")


if __name__ == "__main__":
    main()