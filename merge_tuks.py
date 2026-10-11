#!/usr/bin/env python3
"""
Merge tuks_entries.json into index.json and push to GitHub.
Run after all tuks.nl files are processed.
"""
import json, os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(SCRIPT_DIR, "index.json")
ENTRIES_PATH = os.path.join(SCRIPT_DIR, "tuks_entries.json")

# Load existing index
with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    existing = json.load(f)
print(f"Existing index: {len(existing)} entries")

# Load new entries
with open(ENTRIES_PATH, 'r', encoding='utf-8') as f:
    new_entries = json.load(f)
print(f"New tuks.nl entries: {len(new_entries)}")

# Merge
merged = existing + new_entries
print(f"Merged total: {len(merged)} entries")

# Save
with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)
print(f"Saved to {INDEX_PATH}")

# Stats
previews = sum(1 for e in merged if e.get('content_preview'))
print(f"Total with previews: {previews}/{len(merged)} ({100*previews//len(merged)}%)")
