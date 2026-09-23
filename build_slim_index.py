#!/usr/bin/env python3
"""build_slim_index.py — generate a slim, fast-loading search index for AFLinks.

Full index.json is 21MB+ and growing; loading it on a phone is slow. This
builds two artifacts from index.json:

  search_index_${NNN}.json — slim per-doc records: id, title, filename, categories,
                        meta_categories, primary_person, patent_numbers,
                        type, size_bytes, source_site, and a shortened preview
                        (first PREVIEW_LEN chars). Split into byte-budgeted parts
                        (60 MiB each) because GitHub rejects any single blob >=
                        100 MiB; search_index_manifest.json lists the parts.
                        Used by index.html for instant search + list rendering.
  full_${NNNN}.json   — one chunk file per N chunks of FULL records (full
                        content_preview, source_url, concepts), fetched only
                        when the user opens the detail modal.

Usage:
  python3 build_slim_index.py [--chunk 500] [--input index.json] [--outdir .]
"""
import argparse
import json
import os
import re

PREVIEW_LEN = 160
# Byte budget per shard of the slim index. GitHub rejects any single blob
# >= 100 MiB (GH001), which is what froze the monolithic search_index.json at
# ~82.5k docs on 2026-09-22. 60 MiB leaves ~40% headroom under the hard limit.
DEFAULT_PART_MAX_BYTES = 60 * 1024 * 1024
SLIM_FIELDS = ["id", "title", "filename", "categories", "meta_categories",
               "primary_person", "patent_numbers", "type", "size_bytes",
               "source_site", "source_url", "last_modified", "content_preview"]

# Phase 2: tokenized rarity-ranked search. Build a compact token index:
# token -> {ids:[docId...], df:n} over the metadata + a short preview slice.
# Tokens too common (df > cap) are dropped — they carry no signal. Stopwords
# and short tokens are excluded. Size target: well under 1MB gzipped.
TOKEN_MAX_DF = 6000
TOKEN_PREVIEW_CHARS = 70
STOPWORDS = set("""the and for with from von der die das und des que les une est et les
this that these those has had was were are is of in on at to a an it its as by or
not no be been being but do does did done have having will would can could should
may might must shall about into over under again further then once here there when
where why how all any both each few more most other some such only own same so
than too very s t can just don now""".split())


def tokenize(text):
    toks = re.findall(r"[a-z0-9]{3,}", (text or "").lower())
    return [t for t in toks if t not in STOPWORDS]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chunk", type=int, default=500)
    ap.add_argument("--input", default="index.json")
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--part-max-bytes", type=int, default=DEFAULT_PART_MAX_BYTES,
                    help="byte budget per slim-index shard (default 60 MiB)")
    args = ap.parse_args()

    if args.input == "index.json":
        import index_io
        docs = index_io.load()
    else:
        with open(args.input, encoding="utf-8") as f:
            docs = json.load(f)

    slim = []
    for d in docs:
        rec = {k: d.get(k) for k in SLIM_FIELDS}
        pv = d.get("content_preview") or ""
        # Truncated preview kept under the SAME field name so list render +
        # search keep working unchanged; search_text holds a longer slice so
        # search quality degrades far less than the renderable preview.
        # PREVIEW_LEN must actually be USED here: commit ad633e2f (2026-09-17,
        # "trim PREVIEW_LEN 220->160, Chris decision") changed the constant
        # only, while this line stayed hard-coded at 220 -- so the trim was a
        # silent no-op for three days. Wired up 2026-09-20.
        rec["content_preview"] = pv[:PREVIEW_LEN]
        rec["search_text"] = pv[:600]
        slim.append(rec)

    # Sharded slim index. GitHub rejects any single blob >= 100 MiB, and the
    # monolithic search_index.json crossed that wall at ~82.5k docs (2026-09-22,
    # GH001: "File search_index.json is 101.35 MB; this exceeds GitHub's file
    # size limit of 100.00 MB"). The index could then no longer be published at
    # all, so desktop search silently froze while the phone path stayed current.
    #
    # Fix: split the slim records into byte-budgeted parts + a manifest. Same
    # origin as the site, so no CORS; no external host, no account, no cost. The
    # front-end fetches search_index_manifest.json, then every part in parallel,
    # and falls back to the legacy monolithic file if the parts are absent.
    #
    # Compact + UTF-8 (no \uXXXX escaping) still matters: it is what keeps each
    # part small. Measured 2026-09-17: default separators + ensure_ascii=True
    # cost ~15% for no benefit -- browsers fetch these with response.json().
    PART_MAX_BYTES = args.part_max_bytes
    parts = []
    cur = []
    cur_bytes = 2  # len("[]")
    for rec in slim:
        rec_bytes = len(
            json.dumps(rec, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        ) + 1  # +1 for the joining comma
        if cur and cur_bytes + rec_bytes > PART_MAX_BYTES:
            parts.append(cur)
            cur = []
            cur_bytes = 2
        cur.append(rec)
        cur_bytes += rec_bytes
    if cur:
        parts.append(cur)

    import datetime
    slim_ver = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d%H%M%S")
    slim_manifest = {
        "version": 1,
        "v": slim_ver,  # cache-buster the front-end appends to each part URL
        "total": len(slim),
        "part_max_bytes": PART_MAX_BYTES,
        "parts": [],
    }
    slim_total_bytes = 0
    start = 0
    for i, part in enumerate(parts):
        fname = f"search_index_{i:03d}.json"
        fpath = os.path.join(args.outdir, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(part, f, ensure_ascii=False, separators=(",", ":"))
        nbytes = os.path.getsize(fpath)
        slim_total_bytes += nbytes
        slim_manifest["parts"].append(
            {"file": fname, "start": start, "count": len(part), "bytes": nbytes}
        )
        start += len(part)
    out_slim = os.path.join(args.outdir, "search_index_manifest.json")
    with open(out_slim, "w", encoding="utf-8") as f:
        json.dump(slim_manifest, f, indent=1)
    slim_mb = slim_total_bytes / 1e6
    biggest_part = max(slim_manifest["parts"], key=lambda p: p["bytes"])
    # NOTE: the monolithic search_index.json is deliberately NO LONGER written.
    # It cannot be pushed once it exceeds 100 MiB, so regenerating it only dirties
    # the tree with an unpushable blob and forces the sync lane to hold it back.
    # The last pushable copy stays in the repo as the front-end's fallback.

    # chunked full records
    full = []
    for d in docs:
        full.append(d)
    n = args.chunk
    chunks = [full[i:i + n] for i in range(0, len(full), n)]
    manifest = {"version": 1, "chunk_size": n, "total": len(full),
                "chunks": []}
    for i, c in enumerate(chunks):
        fname = f"full_{i:04d}.json"
        with open(os.path.join(args.outdir, fname), "w", encoding="utf-8") as f:
            json.dump(c, f)
        manifest["chunks"].append({"file": fname, "start": i * n,
                                   "count": len(c)})
    with open(os.path.join(args.outdir, "full_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1)

    total_mb = sum(os.path.getsize(os.path.join(args.outdir, c["file"])) for c in manifest["chunks"]) / 1e6
    print(f"slim: {len(slim)} docs -> {len(parts)} shard(s) ({slim_mb:.1f} MB total; "
          f"biggest {biggest_part['file']} {biggest_part['bytes']/1e6:.1f} MB) + search_index_manifest.json")
    print(f"full: {len(full)} docs -> {len(chunks)} chunks ({total_mb:.1f} MB total)")
    print(f"manifest: full_manifest.json")

    # Chunked search by meta-category: the default phone path. Each
    # meta-category gets its own slim chunk (a doc in N categories appears in
    # N chunks) + a manifest so the front-end can lazy-fetch only the active
    # lens's slice of the archive instead of the whole 18MB index. Chunk
    # records DROP search_text (the 600-char slice) — category browsing
    # matches on title/filename/person/patents/categories/preview, and the
    # full search_index.json (with search_text) remains the "search all"
    # fallback. Keeps the biggest chunk ~2MB raw instead of ~9MB.
    chunk_dir = os.path.join(args.outdir, "search_chunks")
    os.makedirs(chunk_dir, exist_ok=True)
    by_meta = {}
    for rec in slim:
        mcs = rec.get("meta_categories") or []
        if not mcs:
            mcs = ["Uncategorized"]
        for mc in mcs:
            r = dict(rec)
            r.pop("search_text", None)
            by_meta.setdefault(mc, []).append(r)
    search_manifest = {"version": 2, "generated_at": None, "chunks": {}}
    import datetime
    search_manifest["generated_at"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for mc, recs in sorted(by_meta.items()):
        slug = re.sub(r"[^a-z0-9]+", "-", mc.lower()).strip("-") or "uncategorized"
        fname = f"{slug}.json"
        with open(os.path.join(chunk_dir, fname), "w", encoding="utf-8") as f:
            json.dump(recs, f)
        search_manifest["chunks"][mc] = {"file": f"search_chunks/{fname}", "count": len(recs)}
    with open(os.path.join(args.outdir, "search_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(search_manifest, f, indent=1)
    chunk_kb = sum(os.path.getsize(os.path.join(chunk_dir, c["file"].split("/")[-1])) for c in search_manifest["chunks"].values()) / 1024
    biggest = max(search_manifest["chunks"].values(), key=lambda c: c["count"])
    print(f"search chunks: {len(search_manifest['chunks'])} meta-categories -> search_chunks/ ({chunk_kb:.0f} KB total; biggest: {biggest['count']} docs)")

    # Phase 2: compact token index for rarity-ranked search. {token: {ids, df}}
    # from title/filename/person/patents/categories/meta + short preview slice.
    df = {}
    post = {}
    for rec in slim:
        did = rec.get("id")
        if did is None:
            continue
        hay = " ".join([
            str(rec.get("title") or ""),
            str(rec.get("filename") or ""),
            str(rec.get("primary_person") or ""),
            " ".join(rec.get("patent_numbers") or []),
            " ".join(rec.get("categories") or []),
            " ".join(rec.get("meta_categories") or []),
            (rec.get("content_preview") or "")[:TOKEN_PREVIEW_CHARS],
        ])
        seen = set(tokenize(hay))
        for t in seen:
            post.setdefault(t, []).append(did)
    token_index = {"N": len(slim), "tokens": {}}
    for t, ids in post.items():
        n = len(ids)
        if n <= 1 or n > TOKEN_MAX_DF:
            continue  # singletons add only noise; ultra-common add no rank signal
        token_index["tokens"][t] = {"df": n, "ids": ids}
    out_tok = os.path.join(args.outdir, "token_index.json")
    with open(out_tok, "w", encoding="utf-8") as f:
        json.dump(token_index, f, separators=(",", ":"))
    tok_kb = os.path.getsize(out_tok) / 1024
    print(f"token index: {len(token_index['tokens'])} tokens -> token_index.json ({tok_kb:.0f} KB)")

    _emit_taxonomy_counts(slim, args.outdir)
    _bake_live_stats()


def _emit_taxonomy_counts(slim, outdir):
    """Emit a small taxonomy_counts.json (category/meta-category counts + the
    subject→category map) so the sidebar and the Key & Chest dial can render
    with real numbers WITHOUT downloading the 65MB search_index.json. This is
    the backbone of the lazy-loading first paint."""
    import collections
    meta_counts = collections.Counter()
    cat_counts = collections.Counter()
    subjects = collections.defaultdict(collections.Counter)  # meta -> {cat: n}
    for rec in slim:
        for mc in (rec.get("meta_categories") or []):
            if mc:
                meta_counts[mc] += 1
        cats = rec.get("categories") or []
        for c in cats:
            if c:
                cat_counts[c] += 1
        for mc in (rec.get("meta_categories") or []):
            if mc:
                for c in cats:
                    if c:
                        subjects[mc][c] += 1
    payload = {
        "meta_categories": dict(meta_counts),
        "categories": dict(cat_counts),
        "subjects": {mc: dict(c) for mc, c in subjects.items()},
    }
    out = os.path.join(outdir, "taxonomy_counts.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)
    print(f"taxonomy counts: {len(meta_counts)} meta / {len(cat_counts)} cats -> taxonomy_counts.json ({os.path.getsize(out)/1024:.0f} KB)")


def _bake_live_stats() -> None:
    """Stamp fresh counts + cache-busting versions into the site HTML.

    Ensures raw HTML always carries the current archive numbers, so bots and
    agents that never execute JS still see the truth. Called automatically at
    the end of every build — the cron prose checklist is not the only guard.
    """
    import subprocess
    import sys
    from pathlib import Path

    here = Path(__file__).resolve().parent
    subprocess.run(
        [sys.executable, str(here / "bake_stats.py")],
        cwd=here,
        check=True,
    )


if __name__ == "__main__":
    main()