#!/usr/bin/env python3
"""repair_manifest_regression.py — fix the 03:39Z rescue-sweep manifest regression.

The rescue-sweep (0e1cb7e) rewrote index_shards/manifest.json to 7 shards / 62,625
and truncated shard_0006.json to 2,625 entries, while the repo holds 10 shards and
the real archive is ~97,771 (recoverable from 1ba2715). This rebuilds the index:

  - HEAD shards 0000-0005, 0007, 0008, 0009 (keeps legit OCR preview backfills in
    0003/0004/0008, which share ids with 1ba2715)
  - good shard_0006 from git blob 1ba2715 (10,000 entries)
  - re-append the 27 filestore.orgfree.com entries from the truncated shard_0006
    with FRESH ids (they collided with the restored range)

Saves via index_io.save() which re-shards + rewrites the manifest.
Idempotent-safe: run only once.
"""
import json
import subprocess
import sys

sys.path.insert(0, ".")
import index_io

GOOD_COMMIT = "1ba2715"

# 1. Load all HEAD shards except 0006
docs = []
for i in ["0000", "0001", "0002", "0003", "0004", "0005", "0007", "0008", "0009"]:
    sh = json.load(open(f"index_shards/shard_{i}.json"))
    docs.extend(sh)
print(f"loaded HEAD shards (excl 0006): {len(docs)}")

# 2. Load the good shard_0006 from 1ba2715
raw = subprocess.run(
    ["git", "show", f"{GOOD_COMMIT}:index_shards/shard_0006.json"],
    capture_output=True,
).stdout
good6 = json.loads(raw)
print(f"good shard_0006 from {GOOD_COMMIT}: {len(good6)}")
docs.extend(good6)

urls = {e.get("source_url") for e in docs if e.get("source_url")}
max_id = max(e.get("id") or 0 for e in docs if isinstance(e.get("id"), int))
print(f"pre-append max id: {max_id}")

# 3. Re-append the 27 filestore entries with fresh ids
cur = json.load(open("index_shards/shard_0006.json"))
added = 0
for e in cur:
    u = e.get("source_url", "")
    if u and u not in urls:
        max_id += 1
        e["id"] = max_id
        docs.append(e)
        urls.add(u)
        added += 1
print(f"filestore re-appended: {added}")
print(f"FINAL total: {len(docs)}  max id: {max_id}")

ids = [e.get("id") for e in docs if isinstance(e.get("id"), int)]
assert len(ids) == len(set(ids)), "ID COLLISION in reconstruction!"
# URL duplicates are pre-existing in the archive (e.g. rexresearch variants);
# only id uniqueness is required for a valid index. New filestore URLs are fresh.
print(f"ids unique ({len(ids)}); {len(urls)} unique urls (pre-existing dups allowed)")

n = index_io.save(docs)
print(f"Saved {n} shards ({len(docs)} entries) — manifest rewritten")
