#!/usr/bin/env python3
"""
merge_all_progress.py — merge every site's processed entries into the master index.

Standalone, idempotent, safe to run on every cron cycle. Unlike run_queue.py
(which merges inline AFTER processing a batch, inside the 280s timeout), this
script merges whatever progress already exists on disk — so even when a crawl
batch times out mid-processing, the entries it saved still land in the index.

2026-09-12: the master index moved from monolithic index.json (95.89 MiB,
~1 MiB under GitHub's 100 MiB hard push limit) to index_shards/ via index_io.
Browsers never fetch the master index, so the split has zero front-end impact.

Usage:
    python3 merge_all_progress.py          # merge all *_progress.json found
    python3 merge_all_progress.py --dry    # report only, write nothing
"""
import glob
import json
import os
import sys

import index_io

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DRY = "--dry" in sys.argv

existing = index_io.load()
existing_urls = {e.get("source_url", "") for e in existing if e.get("source_url")}
max_id = 0
for e in existing:
    i = e.get("id") or 0
    if isinstance(i, int) and i > max_id:
        max_id = i

progress_files = sorted(glob.glob(os.path.join(SCRIPT_DIR, "*_progress.json")))
added_total = 0
per_site = {}

for pf in progress_files:
    name = os.path.basename(pf).replace("_progress.json", "")
    try:
        with open(pf, "r", encoding="utf-8") as f:
            progress = json.load(f)
    except Exception as exc:
        print(f"  {name}: skipped ({exc})")
        continue
    entries = progress.get("entries", []) if isinstance(progress, dict) else []
    if not entries:
        print(f"  {name}: 0 entries in progress file")
        continue
    added = 0
    for entry in entries:
        url = entry.get("source_url", "")
        if url and url not in existing_urls:
            max_id += 1
            entry["id"] = max_id
            existing.append(entry)
            existing_urls.add(url)
            added += 1
            added_total += 1
    per_site[name] = added
    print(f"  {name}: +{added} new entries")

print(f"Total index: {len(existing)} entries ({len(per_site)} sites checked)")

if DRY:
    print("DRY RUN — nothing written")
    sys.exit(0)

if added_total > 0:
    n = index_io.save(existing)
    print(f"Saved {n} shards ({len(existing)} entries)")
else:
    print("No new entries to merge — index already up to date")
