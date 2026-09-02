#!/usr/bin/env python3
"""
build_paradigm_lenses.py — the Paradigm Map (second dimension).

The 24 filing lenses are SILO buckets (where a doc sits). The paradigm
lenses are the WAY its authors think — cross-cutting schools that connect
the silos. For each paradigm concept in taxonomy/concepts.json (p_* ids):

  docs       = archive docs tagged with it (from index.json `concepts`)
  af_posts   = Aetherforce posts whose title/categories match its aliases
  silo_span  = how many of the 24 filing lenses contain at least one doc
               tagged with it (cross-correlation = how wide the bridge is)
  pct        = af_posts / all AF posts (founding group's weight in this lane)

Writes paradigm_lenses.json consumed by the dial's Paradigm Map mode.
Rebuild after tag_concepts.py or af_catalog.json changes.
"""
import json, re, os, sys

HEREPATH = os.path.dirname(os.path.abspath(__file__))

def load_json(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)

def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()

def build_matchers(concepts):
    """(concept_id, set-of-normed-alias-tokens-or-phrases)"""
    matchers = []
    for c in concepts:
        aliases = [a for a in c.get("aliases", []) if len(a) > 3]
        matchers.append((c["id"], aliases))
    return matchers

def match_aliases(aliases, text_norm):
    return any(a in text_norm for a in aliases)

def main():
    concepts = {c["id"]: c for c in load_json(os.path.join(HEREPATH, "taxonomy", "concepts.json"))["concepts"]}
    paradigm_ids = [cid for cid in concepts if cid.startswith("p_")]
    idx = load_json(os.path.join(HEREPATH, "index.json"))
    catalog = load_json(os.path.join(HEREPATH, "af_catalog.json")) if os.path.exists(os.path.join(HEREPATH, "af_catalog.json")) else []
    feed = load_json(os.path.join(HEREPATH, "library_feed.json"))

    # AF category map: id -> name (cached), so AF posts score on categories too
    af_cats = {}
    cats_path = os.path.join(HEREPATH, "af_cats.json")
    if os.path.exists(cats_path):
        try:
            af_cats = load_json(cats_path)
        except Exception:
            af_cats = {}
    catname = lambda cid: af_cats.get(str(cid), "") if isinstance(cid, (int, str)) else ""

    total_af = len(catalog)

    out = {}
    for cid in paradigm_ids:
        rec = concepts[cid]
        aliases = [norm(a) for a in rec.get("aliases", []) if len(a) > 3]
        # ---- archive docs: concept tag OR category name match OR title/preview match ----
        doc_ids, spans = [], set()
        for d in idx:
            cs = d.get("concepts") or []
            if cid in cs:
                doc_ids.append(str(d.get("id")))
                spans |= set(d.get("meta_categories") or [])
                continue
            hay = norm((d.get("title") or "") + " " + " ".join(d.get("categories") or []) + " " + (d.get("content_preview") or ""))
            if any(a in hay for a in aliases):
                doc_ids.append(str(d.get("id")))
                spans |= set(d.get("meta_categories") or [])
        # ---- AF posts: title OR AF category name ----
        af_hits = []
        for p in catalog:
            t = norm(p["title"]) + " " + " ".join(norm(catname(cid2)) for cid2 in p.get("cats", []))
            if any(a in t for a in aliases):
                af_hits.append(p)
        out[cid] = {
            "name": rec.get("name", cid),
            "docs": len(doc_ids),
            "af_posts": len(af_hits),
            "pct": round(100 * len(af_hits) / total_af, 1) if total_af else 0,
            "silo_span": len(spans),
            "spans": sorted(spans)[:12],
        }

    artifacts = {
        "generated_at": "2026-09-02T16:30:00Z",
        "method": "paradigm concepts (p_*) from taxonomy/concepts.json × archive tags × AF catalog",
        "total_af_posts": total_af,
        "archive_docs": len(idx),
        "lenses": out,
    }
    with open(os.path.join(HEREPATH, "paradigm_lenses.json"), "w", encoding="utf-8") as f:
        json.dump(artifacts, f, indent=1, ensure_ascii=False)

    print("paradigm_lenses.json written")
    print(f"\n{'concept':26s} {'docs':>6s} {'AF':>4s} {'%':>5s} {'span':>5s}  lane")
    for cid, d in sorted(out.items(), key=lambda x: -x[1]["af_posts"]):
        bar = "#" * max(1, d["af_posts"] // 3)
        print(f"{d['name'][:26]:26s} {d['docs']:6d} {d['af_posts']:4d} {d['pct']:5.1f} {d['silo_span']:5d}  {bar}")

if __name__ == "__main__":
    main()
