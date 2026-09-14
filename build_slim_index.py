#!/usr/bin/env python3
"""build_slim_index.py — generate a slim, fast-loading search index for AFLinks.

Full index.json is 21MB+ and growing; loading it on a phone is slow. This
builds two artifacts from index.json:

  search_index.json   — slim per-doc records: id, title, filename, categories,
                        meta_categories, primary_person, patent_numbers,
                        type, size_bytes, source_site, and a shortened preview
                        (first 220 chars). Used by index.html for instant
                        search + list rendering.
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

PREVIEW_LEN = 220
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
        rec["content_preview"] = pv[:220]
        rec["search_text"] = pv[:600]
        slim.append(rec)

    out_slim = os.path.join(args.outdir, "search_index.json")
    with open(out_slim, "w", encoding="utf-8") as f:
        json.dump(slim, f)
    slim_mb = os.path.getsize(out_slim) / 1e6

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
    print(f"slim: {len(slim)} docs -> search_index.json ({slim_mb:.1f} MB)")
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