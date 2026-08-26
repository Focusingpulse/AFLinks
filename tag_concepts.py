#!/usr/bin/env python3
"""Tag the AFLinks archive with concepts from taxonomy/concepts.json.

Layer-1 -> Layer-2 pass: reads each document's title + filename + content
preview, matches against normalized concept aliases, and writes the matched
concept ids back to index.json under `concepts`. Pure stdlib, no LLM — cheap
enough to run inside the 3h scrape cron as the archive grows.

Usage:
    python3 tag_concepts.py          # tag archive in place (index.json)
    python3 tag_concepts.py --report # only print coverage stats

Writes a `concepts` field (list of concept ids) onto each doc that has a
match. Documents with no match get [] and keep whatever thin meta-tags they
had — the pipeline does NOT overwrite existing categories/meta_categories; the
concept field is additive, so a future re-derivation of themes can layer on top
without destroying the original filing.
"""
import json, re, os, sys

HEREPATH = os.path.dirname(os.path.abspath(__file__))
CONCEPTS_PATH = os.path.join(HEREPATH, "taxonomy", "concepts.json")
INDEX_PATH = os.path.join(HEREPATH, "index.json")


def load_concepts(path=CONCEPTS_PATH):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data["concepts"]


def build_matchers(concepts):
    """Return list of (concept_id, compiled alias regex)."""
    matchers = []
    for c in concepts:
        # Escape aliases so punctuation (hyphens, parens) is literal; treat
        # spaces as flexible so "free energy" matches "free-energy".
        for alias in c.get("aliases", []):
            pat = re.sub(r"[-\s]+", r"[\\s\\-]+", re.escape(alias.strip()))
            try:
                matchers.append((c["id"], re.compile(r"\b" + pat, re.IGNORECASE)))
            except re.error:
                continue
    return matchers, concepts


def doc_haystack(doc):
    parts = [
        doc.get("title") or "",
        doc.get("filename") or "",
        doc.get("primary_person") or "",
        doc.get("content_preview") or "",
    ]
    return "\n".join(parts).lower()


def main():
    report_only = "--report" in sys.argv
    concepts = load_concepts()
    matchers, _ = build_matchers(concepts)

    with open(INDEX_PATH, encoding="utf-8") as f:
        docs = json.load(f)

    hits = {}
    for cid in {m[0] for m in matchers}:
        hits[cid] = 0

    for doc in docs:
        hay = doc_haystack(doc)
        found = []
        for cid, rx in matchers:
            if rx.search(hay) and cid not in found:
                found.append(cid)
        if found:
            doc["concepts"] = found
            for cid in found:
                hits[cid] += 1
        else:
            doc["concepts"] = []

    if not report_only:
        with open(INDEX_PATH, "w", encoding="utf-8") as f:
            json.dump(docs, f, ensure_ascii=False, indent=2)
        print(f"index.json updated in place: {len(docs)} docs")

    tagged = sum(1 for d in docs if d.get("concepts"))
    print(f"{tagged}/{len(docs)} docs now carry >=1 concept tag ({tagged/len(docs):.0%})")
    print("top concepts by doc coverage:")
    for cid, n in sorted(hits.items(), key=lambda kv: -kv[1])[:18]:
        print(f"  {n:5d}  {cid}")


if __name__ == "__main__":
    main()