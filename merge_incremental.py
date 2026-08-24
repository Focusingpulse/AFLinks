#!/usr/bin/env python3
"""
Incremental merge: merge new tuks.nl entries into index.json and push.
Safe to run repeatedly - only adds entries not already in index.json.
This makes the live site update after each cron run.
"""
import json, os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(SCRIPT_DIR, "index.json")
PROGRESS_PATH = os.path.join(SCRIPT_DIR, "tuks_progress.json")

# Load existing index
with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    existing = json.load(f)
print(f"Existing index: {len(existing)} entries")

# Track existing source URLs to avoid duplicates
existing_urls = set()
for e in existing:
    url = e.get('source_url', '')
    if url:
        existing_urls.add(url)

# Load progress entries
if not os.path.exists(PROGRESS_PATH):
    print("No progress file found - nothing to merge")
    sys.exit(0)

with open(PROGRESS_PATH, 'r', encoding='utf-8') as f:
    progress = json.load(f)

new_entries = progress.get("entries", [])
print(f"Progress entries: {len(new_entries)}")

# Filter to only new entries (not already in index)
added = 0
for entry in new_entries:
    url = entry.get('source_url', '')
    if url and url not in existing_urls:
        # Re-assign ID to continue from existing index
        entry['id'] = max(e['id'] for e in existing) + 1 + added
        existing.append(entry)
        existing_urls.add(url)
        added += 1

print(f"New entries added: {added}")
print(f"Total index: {len(existing)} entries")

if added > 0:
    # Save merged index
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    print(f"Saved updated index.json ({len(existing)} entries)")
    
    # Stats
    previews = sum(1 for e in existing if e.get('content_preview'))
    pct = 100 * previews // len(existing) if existing else 0
    print(f"Total with previews: {previews}/{len(existing)} ({pct}%)")
    
    # Source site breakdown
    sites = {}
    for e in existing:
        site = e.get('source_site', 'rexresearch.com')
        sites[site] = sites.get(site, 0) + 1
    print("By source:")
    for s, n in sorted(sites.items(), key=lambda x: -x[1]):
        print(f"  {s}: {n}")
else:
    print("No new entries to add - index already up to date")
