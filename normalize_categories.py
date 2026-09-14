#!/usr/bin/env python3
"""normalize_categories.py — collapse near-duplicate archive categories.

Pure additive: keeps ALL existing labels working (both old and new search),
but canonicalizes the visible label on every doc + derived artifacts.

Pairs (verified zero-overlap in index.json on 2026-08-31):
  Biology / Health    -> Biology
  Water / Hydrogen    -> Water
  Environmental       -> Environment / Climate

Usage: python3 normalize_categories.py [--apply]
(default is DRY-RUN; pass --apply to write index.json + concept-map.json)
"""
import json, os, sys, copy

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(HERE, "index.json")
CMAP = "/root/workspace/.letta/agents/agent-b73ac550-5671-471e-b3e1-721f948ea063/living-library/database/taxonomy/concept-map.json"

CANON = {
    "Biology / Health": "Biology",
    "Water / Hydrogen": "Water",
    "Environmental": "Environment / Climate",
}
APPLY = "--apply" in sys.argv

# --- index.json ---
idx = json.load(open(INDEX, encoding="utf-8"))
moved = 0
for e in idx:
    cats = e.get("categories") or []
    new = [CANON.get(c, c) for c in cats]
    # dedupe preserving order (merges can now duplicate)
    seen, out = set(), []
    for c in new:
        if c not in seen:
            seen.add(c); out.append(c)
    if out != cats:
        e["categories"] = out
        moved += 1

# report counts after
from collections import Counter
cnt = Counter(c for e in idx for c in (e.get("categories") or []))
print(f"index.json: {len(idx)} docs, {moved} docs remapped, {len(cnt)} distinct categories now")
for c in sorted(cnt, key=lambda x: -cnt[x])[:12]:
    print(f"  {cnt[c]:6}  {c}")

if APPLY:
    json.dump(idx, open(INDEX, "w", encoding="utf-8"), ensure_ascii=False)
    print("index.json written")

# --- concept-map.json: remap co_occur_categories keys (additive merge) ---
if os.path.isfile(CMAP):
    cm = json.load(open(CMAP, encoding="utf-8"))
    remapped_domains = 0
    for dname, info in cm.get("domains", {}).items():
        occ = info.get("co_occur_categories")
        if not isinstance(occ, dict):
            continue
        new_occ = {}
        for k, v in occ.items():
            ck = CANON.get(k, k)
            new_occ[ck] = new_occ.get(ck, 0) + v
        if new_occ != occ:
            info["co_occur_categories"] = new_occ
            remapped_domains += 1
    # same for meta_domains
    for dname, info in cm.get("meta_domains", {}).items():
        occ = info.get("co_occur_categories")
        if isinstance(occ, dict):
            new_occ = {}
            for k, v in occ.items():
                ck = CANON.get(k, k)
                new_occ[ck] = new_occ.get(ck, 0) + v
            if new_occ != occ:
                info["co_occur_categories"] = new_occ
                remapped_domains += 1
    print(f"concept-map.json: {remapped_domains} domain records remapped")
    if APPLY:
        json.dump(cm, open(CMAP, "w", encoding="utf-8"), ensure_ascii=False)
        print("concept-map.json written")
else:
    print(f"concept-map.json not found at {CMAP} (skipping)")
    if APPLY:
        raise SystemExit("concept-map not found — aborting apply")
