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

PREVIEW_LEN = 220
SLIM_FIELDS = ["id", "title", "filename", "categories", "meta_categories",
               "primary_person", "patent_numbers", "type", "size_bytes",
               "source_site", "content_preview"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chunk", type=int, default=500)
    ap.add_argument("--input", default="index.json")
    ap.add_argument("--outdir", default=".")
    args = ap.parse_args()

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


if __name__ == "__main__":
    main()