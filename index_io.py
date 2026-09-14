#!/usr/bin/env python3
"""
index_io.py — sharded master index for AFLinks (replaces monolithic index.json).

WHY: index.json crossed 95 MiB heading for GitHub's 100 MiB hard push limit
(GH001). It is a BUILD-TIME file only — browsers never fetch it (the site uses
search_index.json / search_chunks / full_* shards) — so it can be split freely
with zero front-end impact.

LAYOUT:
    index_shards/manifest.json   {"version": 1, "shard_size": N, "total": T,
                                 "next_id": X, "shards": ["shard_0000.json", ...]}
    index_shards/shard_0000.json  ...compact JSON arrays of entries

API (drop-in for the old open(json.load) pattern):
    import index_io
    docs = index_io.load()          # full list (build-time only)
    index_io.save(docs)             # re-shard + write manifest
    index_io.count()                # O(1) total, no big parse
    index_io.next_id()              # next free integer id
    index_io.iter_docs()            # streaming iteration, low memory
    index_io.url_set()              # set of source_urls (dedupe checks)

WRITERS using this module: merge_all_progress.py, run_queue.py, tag_concepts.py.
READERS using this module: bake_stats.py, build_doc_pages.py,
build_paradigm_lenses.py, build_patents_index.py, build_library_feed.py,
researcher_sweep.py, wayback_scavenger.py, process_zenodo.py,
process_generic_cloud.py, extract_previews2.py, ocr_previews.py, fix_previews.py.

MIGRATION: if index.json still exists and index_shards/ does not, load()
transparently reads the monolith (one-time). Call save() once to convert.
After conversion, any script still opening index.json directly will fail
loudly with FileNotFoundError — that is intentional: it must be migrated.
Legacy one-shot merge scripts (merge_id_safe, merge_tgd_safe, merge_frienergi,
merge_tuks, merge_incremental, process_tuks) are retired; the generic pipeline
(merge_all_progress + run_queue) supersedes them.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SHARD_DIR = os.path.join(HERE, "index_shards")
MANIFEST_PATH = os.path.join(SHARD_DIR, "manifest.json")
LEGACY_PATH = os.path.join(HERE, "index.json")
SHARD_SIZE = 10000  # docs per shard — biggest observed ~20 MiB (dense previews), far under 100 MiB


def _write_compact(path, data):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def _load_manifest():
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        return json.load(f)


def has_shards():
    return os.path.isfile(MANIFEST_PATH)


def load():
    """Return the full doc list. Build-time use only (parses everything)."""
    if not has_shards():
        if os.path.isfile(LEGACY_PATH):
            with open(LEGACY_PATH, encoding="utf-8") as f:
                return json.load(f)
        raise FileNotFoundError(
            "No master index found (neither index_shards/manifest.json nor index.json). "
            "Run: python3 index_io.py migrate"
        )
    m = _load_manifest()
    docs = []
    for name in m["shards"]:
        with open(os.path.join(SHARD_DIR, name), encoding="utf-8") as f:
            docs.extend(json.load(f))
    return docs


def iter_docs():
    """Yield docs one shard at a time — low-memory streaming read."""
    if not has_shards():
        for d in load():
            yield d
        return
    m = _load_manifest()
    for name in m["shards"]:
        with open(os.path.join(SHARD_DIR, name), encoding="utf-8") as f:
            for d in json.load(f):
                yield d


def count():
    """O(1) doc count from the manifest."""
    if has_shards():
        return _load_manifest()["total"]
    return len(load())


def next_id():
    """Next free integer doc id (max existing id + 1)."""
    mx = 0
    for d in iter_docs():
        i = d.get("id") or 0
        if isinstance(i, int) and i > mx:
            mx = i
    return mx + 1


def url_set():
    """Set of source_urls — for dedupe checks without holding all docs."""
    return {d.get("source_url", "") for d in iter_docs() if d.get("source_url")}


def save(docs):
    """Write docs as shards + manifest. Deletes the legacy monolith if the
    shard layout is complete, so it can never silently reappear."""
    os.makedirs(SHARD_DIR, exist_ok=True)
    old = set()
    if has_shards():
        old = set(_load_manifest()["shards"])
    shards = []
    for i in range(0, len(docs), SHARD_SIZE):
        name = f"shard_{i // SHARD_SIZE:04d}.json"
        _write_compact(os.path.join(SHARD_DIR, name), docs[i:i + SHARD_SIZE])
        shards.append(name)
    manifest = {
        "version": 1,
        "shard_size": SHARD_SIZE,
        "total": len(docs),
        "shards": shards,
    }
    _write_compact(MANIFEST_PATH, manifest)
    # remove shards no longer needed (shrinking index)
    for name in old - set(shards):
        try:
            os.remove(os.path.join(SHARD_DIR, name))
        except OSError:
            pass
    # legacy monolith must die — a stale one would resurrect as the
    # source of truth on the next clone and blow the push limit again
    if os.path.isfile(LEGACY_PATH):
        os.remove(LEGACY_PATH)
    return len(shards)


def migrate():
    """One-time: monolith -> shards."""
    if has_shards():
        print(f"Already migrated: {count()} docs in {len(_load_manifest()['shards'])} shards")
        return
    if not os.path.isfile(LEGACY_PATH):
        print("Nothing to migrate: no index.json found")
        return
    docs = load()
    n = save(docs)
    print(f"Migrated {len(docs)} docs into {n} shards (legacy index.json removed)")


def status():
    if has_shards():
        m = _load_manifest()
        total_kb = sum(
            os.path.getsize(os.path.join(SHARD_DIR, s)) for s in m["shards"]
        ) / 1024
        biggest = max(
            m["shards"],
            key=lambda s: os.path.getsize(os.path.join(SHARD_DIR, s)),
        )
        print(
            f"sharded: {m['total']} docs in {len(m['shards'])} shards "
            f"({total_kb / 1024:.1f} MiB total; biggest shard {biggest} "
            f"{os.path.getsize(os.path.join(SHARD_DIR, biggest)) / 1048576:.1f} MiB)"
        )
    elif os.path.isfile(LEGACY_PATH):
        sz = os.path.getsize(LEGACY_PATH) / 1048576
        print(f"legacy monolith: index.json {sz:.1f} MiB (100 MiB GitHub hard limit)")
    else:
        print("no master index found")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "migrate":
        migrate()
    elif cmd == "status":
        status()
    elif cmd == "count":
        print(count())
    else:
        print(f"usage: index_io.py [status|migrate|count]")
