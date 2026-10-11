#!/usr/bin/env python3
"""ID-safe filtered merge for quantumaetherdynamics_org backfill.

Appends ONLY entries from <site>_entries.json whose id is above the master
index's current max id, and whose source_url is not already in the index.
Uses index_io.save() so shards + manifest stay consistent.
"""
import json
import sys
import index_io

SITE = "quantumaetherdynamics_org"

def main():
    docs = index_io.load()
    mx = max((d.get("id") or 0) for d in docs)
    urls = {d.get("source_url", "") for d in docs if d.get("source_url")}
    print(f"index docs={len(docs)} max_id={mx}")

    with open(f"{SITE}_entries.json", encoding="utf-8") as f:
        entries = json.load(f)
    print(f"entries file: {len(entries)}")

    new = [e for e in entries if (e.get("id") or 0) > mx and e.get("source_url") not in urls]
    new.sort(key=lambda e: e["id"])

    dup_ids = len(new) - len({e["id"] for e in new})
    dup_urls = len(new) - len({e["source_url"] for e in new})
    empty_title = sum(1 for e in new if not (e.get("title") or "").strip())
    empty_preview = sum(1 for e in new if not (e.get("content_preview") or "").strip())
    print(f"to merge: {len(new)}  (dup_ids={dup_ids} dup_urls={dup_urls} empty_title={empty_title} empty_preview={empty_preview})")
    if new:
        print(f"id range: {new[0]['id']}..{new[-1]['id']}")
    if dup_ids or dup_urls:
        print("ABORT: duplicate ids/urls in the merge batch")
        sys.exit(1)

    docs.extend(new)
    index_io.save(docs)
    print(f"SAVED. new index total = {len(docs)}")

if __name__ == "__main__":
    main()
