#!/usr/bin/env python3
"""reconcile_index.py — merge my repaired+grown local index with the remote index.

State: remote (origin/main) moved during this fire to ad3e1cc9 (preview-cleaner
"de-menu-ed" + AFLinks feed sync). Remote index = 97,746 docs with 34,803
improved (shorter, menu-de-stripped) previews + all 27 filestore docs.

My local index = 97,852 with 106 keelynet URLs the remote LACKS:
  - 25 chroma/index pages restored from the good 1ba2715 shard_0006
    (the remote AFLinks-sync rebuild dropped them)
  - 81 newly harvested keelynet news entries (this fire)

Goal: final index = remote docs (keep cleaner previews) + my 106 extra
keelynet URLs, assigned fresh ids above remote max. Verify id/url uniqueness.
"""
import json
import subprocess
import sys

sys.path.insert(0, ".")
import index_io


def load_ref(ref):
    m = json.loads(subprocess.run(
        ["git", "show", f"{ref}:index_shards/manifest.json"], capture_output=True).stdout)
    docs = []
    for s in m["shards"]:
        r = subprocess.run(["git", "show", f"{ref}:index_shards/{s}"],
                           capture_output=True).stdout
        docs.extend(json.loads(r))
    return docs


remote = load_ref("origin/main")
local = index_io.load()

rurl = {e.get("source_url") for e in remote}
lurl = {e.get("source_url") for e in local}
extra = [e for e in local if e.get("source_url") and e.get("source_url") not in rurl]
print(f"remote: {len(remote)} | local: {len(local)} | extras(local-only): {len(extra)}")

max_id = max(e.get("id") or 0 for e in remote if isinstance(e.get("id"), int))
print(f"remote max id: {max_id}")

# Assign fresh ids to extras
used = {e.get("id") for e in remote}
assigned = []
for e in extra:
    max_id += 1
    e["id"] = max_id
    assigned.append(e)

final = remote + assigned
print(f"FINAL total: {len(final)}")

ids = [e.get("id") for e in final if isinstance(e.get("id"), int)]
assert len(ids) == len(set(ids)), "ID COLLISION!"
# Pre-existing URL duplicates in the archive are allowed (e.g. rexresearch
# variants); only guarantee that extras never collide with remote URLs.
extra_urls = [e.get("source_url") for e in assigned if e.get("source_url")]
assert len(extra_urls) == len(set(extra_urls)), "EXTRA URL DUPLICATE!"
print(f"ids unique ({len(ids)}); {len(extra_urls)} extras all URL-fresh")

n = index_io.save(final)
print(f"Saved {n} shards ({len(final)} entries)")
