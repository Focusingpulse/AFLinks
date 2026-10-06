#!/usr/bin/env python3
"""Id-safe archive merge: append <site>_entries.json into index.json with FRESH ids above the CURRENT index max.
Usage: python3 merge_id_safe.py <site_entries_json>
Safety (learned 2026-09-09 18:15Z collision):
  * NEVER blind-append by stored id (concurrent workers share id space).
  * Recompute ids on top of the index.json max at merge time.
  * Dump compact: ensure_ascii=False + separators=(',',':') (pretty crosses GitHub 100MiB).
"""
import json, sys, time

entries_path = sys.argv[1]
with open('index.json', encoding='utf-8') as f:
    idx = json.load(f)

with open(entries_path, encoding='utf-8') as f:
    entries = json.load(f)

cur_max = max(e['id'] for e in idx)
# drop the stored ids entirely and reassign
fresh = []
nid = cur_max + 1
added = 0
for e in entries:
    e['id'] = nid
    nid += 1
    fresh.append(e)
    added += 1

idx.extend(fresh)
with open('index.json', 'w', encoding='utf-8') as f:
    json.dump(idx, f, ensure_ascii=False, separators=(',', ':'))

print(f"merged {added} entries; index.json now has {len(idx)} entries; new max id {nid-1}")