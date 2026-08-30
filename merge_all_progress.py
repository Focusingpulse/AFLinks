#!/usr/bin/env python3
"""
merge_all_progress.py — merge every site's processed entries into index.json.

Standalone, idempotent, safe to run on every cron cycle. Unlike run_queue.py
(which merges inline AFTER processing a batch, inside the 280s timeout), this
script merges whatever progress already exists on disk — so even when a crawl
batch times out mid-processing, the entries it saved still land in index.json.

Usage:
    python3 merge_all_progress.py          # merge all *_progress.json found
    python3 merge_all_progress.py --dry    # report only, write nothing
"""
import json, os, sys, glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(SCRIPT_DIR, "index.json")
DRY = "--dry" in sys.argv

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    existing = json.load(f)

existing_urls = set()
for e in existing:
    u = e.get("source_url", "")
    if u:
        existing_urls.add(u)

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
            entry["id"] = max(e["id"] for e in existing) + 1 + added_total
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
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    print(f"Saved updated index.json ({len(existing)} entries)")
else:
    print("No new entries to merge — index already up to date")