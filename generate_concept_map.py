#!/usr/bin/env python3
"""Generate taxonomy/concept-map.json from concepts.json + search_index.json.

Computes domain (theme) → category co-occurrence strengths by scanning
the tagged documents. Each concept in concepts.json has a 'theme' field;
each doc in search_index.json has 'categories' and 'concepts' fields.

Output format matches the builder's expected concept_map structure:
{
  "domains": {
    "<theme_name>": {
      "co_occur_categories": {"<cat>": strength, ...}
    },
    ...
  }
}

Run once to bootstrap the concept-map; subsequent runs can refresh
as the archive grows.
"""
import json
import os
import sys
import glob
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
CONCEPTS_PATH = os.path.join(HERE, "taxonomy", "concepts.json")
INDEX_PATH = os.path.join(HERE, "search_index.json")
SHARD_GLOB = os.path.join(HERE, "index_shards", "shard_*.json")
OUT_PATH = os.path.join(HERE, "taxonomy", "concept-map.json")


def main():
    concepts = json.load(open(CONCEPTS_PATH, encoding="utf-8"))["concepts"]
    # Build concept_id -> theme mapping
    concept_to_theme = {}
    theme_names = set()
    for c in concepts:
        cid = c["id"]
        theme = c.get("theme", "Uncategorized")
        concept_to_theme[cid] = theme
        theme_names.add(theme)

    # Scan docs for co-occurrence (prefer shards, fall back to search_index.json)
    docs = []
    shard_files = sorted(glob.glob(SHARD_GLOB))
    if shard_files:
        import glob as _glob
        for shard_path in shard_files:
            docs.extend(json.load(open(shard_path, encoding="utf-8")))
    else:
        docs = json.load(open(INDEX_PATH, encoding="utf-8"))
    # domain -> {category: count}
    co_occur = defaultdict(lambda: defaultdict(int))

    for d in docs:
        doc_concepts = d.get("concepts") or []
        doc_cats = d.get("categories") or []
        if not doc_concepts or not doc_cats:
            continue
        # Find themes for this doc
        doc_themes = set()
        for cid in doc_concepts:
            theme = concept_to_theme.get(cid)
            if theme:
                doc_themes.add(theme)
        # Increment co-occurrence for each (theme, category) pair
        for theme in doc_themes:
            for cat in doc_cats:
                co_occur[theme][cat] += 1

    # Build output structure
    domains = {}
    for theme in sorted(theme_names):
        cat_counts = co_occur.get(theme, {})
        # Sort by count descending, keep top N
        sorted_cats = sorted(cat_counts.items(), key=lambda kv: -kv[1])[:20]
        domains[theme] = {
            "co_occur_categories": {cat: cnt for cat, cnt in sorted_cats}
        }

    out = {"domains": domains, "generated_from": "generate_concept_map.py"}
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"Wrote {OUT_PATH} with {len(domains)} domains")
    for dn, info in domains.items():
        n_cats = len(info.get("co_occur_categories", {}))
        if n_cats:
            print(f"  {dn}: {n_cats} categories")


if __name__ == "__main__":
    main()
