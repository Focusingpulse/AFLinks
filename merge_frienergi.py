#!/usr/bin/env python3
"""ID-safe merge: append entries from frienergi_alternativkanalen_entries.json
whose id > current max in index.json. Never re-appends."""
import json, sys
idx = json.load(open('index.json'))
new = json.load(open('frienergi_alternativkanalen_entries.json'))
max_id = max(int(e['id']) for e in idx)
fresh = [e for e in new if int(e['id']) > max_id]
ids = [int(e['id']) for e in fresh]
assert len(ids) == len(set(ids)), "duplicate ids in fresh!"
before = len(idx)
idx.extend(fresh)
json.dump(idx, open('index.json','w'), ensure_ascii=False)
print(f"merged {len(fresh)} (ids {min(ids) if ids else '-'}..{max(ids) if ids else '-'}), index {before} -> {len(idx)}")
