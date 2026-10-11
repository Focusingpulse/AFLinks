#!/usr/bin/env python3
"""build_archive_graph.py — emit the entity graph contract + curated-core bindings.

Phase 1 (architecture debate verdict): the archive's pattern-spotting payoff
needs doc→concept→person bindings that agents can read WITHOUT re-deriving
joins across four files. This emits:

  archive-graph.json           — nodes (person/work/translation/concept/lang)
                                + typed edges, versioned, served by the site.
  database/curated-core-bindings.json (living-library) — per-work bindings:
                                work -> persons, concepts, language,
                                translations. Fills the empty seam for the
                                curated core (translations + research works).

Typed edges (v1):
  authored_by       work -> person        (research-index author_ids)
  translated        translation -> work   (matched by url / normalized title)
  domain            work -> concept       (research-index domains)
  concept           translation -> concept (translation domain -> concept)
  language          work -> lang:<code>
  refs              work -> work          (research-index cross_references if any)

Usage: python3 build_archive_graph.py [--aflinks .] [--ll LL] [--out archive-graph.json]
Pure stdlib. Safe to run any time; the aflinks-sync cron can rebuild it.
"""
import argparse, glob, json, os, re, sys, datetime

def load_json(path, default=None):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default

def norm(s):
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

FRONT_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
def parse_frontmatter(path):
    try:
        raw = open(path, encoding="utf-8").read()
    except Exception:
        return {}, ""
    meta = {}
    m = FRONT_RE.match(raw)
    body = raw
    if m:
        fm, body = m.group(1), raw[m.end():]
        for line in fm.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"').strip("'")
    for line in body.splitlines()[:12]:
        bm = re.match(r"^- \*\*([^:*]+):\*\*\s*(.*)$", line.strip())
        if bm:
            meta.setdefault(bm.group(1).strip(), bm.group(2).strip())
    return meta, body

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--aflinks", default="/root/workspace/AFLinks")
    ap.add_argument("--ll", default=None)
    ap.add_argument("--out", default="archive-graph.json")
    args = ap.parse_args()

    ll = args.ll or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
    ll = os.path.realpath(ll)
    db = os.path.join(ll, "database")
    feed = load_json(os.path.join(args.aflinks, "library_feed.json"), {})

    # ---- nodes ----
    concepts = {}
    for cid, cname in (feed.get("seam", {}).get("concept_names", {}) or {}).items():
        concepts[cid] = cname or cid
    concept_map = load_json(os.path.join(db, "taxonomy", "concept-map.json"), {})
    for dn in (concept_map.get("domains", {}) or {}):
        concepts.setdefault("d_" + norm(dn), dn)
    concept_nodes = [{"id": cid, "name": cname} for cid, cname in sorted(concepts.items())]

    person_idx = load_json(os.path.join(db, "persons", "person-index.json"), {})
    persons = person_idx.get("persons", {}) if isinstance(person_idx, dict) else {}
    person_nodes = []
    person_by = {}
    for name, rec in persons.items():
        pid = rec.get("id") or ("p_" + norm(name))
        person_by.setdefault(norm(name), pid)
        person_by.setdefault(pid, pid)
        person_nodes.append({
            "id": pid,
            "name": rec.get("romanized_name") or name,
            "known_as": rec.get("known_as", [])[:3],
            "domains": (rec.get("primary_contributions") or [])[:3],
        })

    work_idx = load_json(os.path.join(db, "research", "research-index.json"), {})
    works = work_idx.get("works", {}) if isinstance(work_idx, dict) else {}
    work_nodes, work_edges = [], []
    work_by_url, work_by_title = {}, {}
    for wid, rec in works.items():
        work_nodes.append({
            "id": wid,
            "title": rec.get("title_en") or rec.get("title"),
            "lang": rec.get("language"),
            "authors": rec.get("authors", [])[:3],
            "url": rec.get("url"),
            "host": rec.get("host"),
            "domains": rec.get("domains", [])[:4],
        })
        for aid in rec.get("author_ids", []) or []:
            work_edges.append({"type": "authored_by", "from": "work:" + wid, "to": "person:" + aid})
        for d in rec.get("domains", []) or []:
            work_edges.append({"type": "domain", "from": "work:" + wid, "to": "concept:" + concepts.setdefault("d_" + norm(d), d)})
        if rec.get("url"):
            work_by_url[norm(rec["url"])] = wid
        if rec.get("title_en") or rec.get("title"):
            work_by_title[norm(rec.get("title_en") or rec.get("title"))] = wid

    # ---- translations ----
    tdir = os.path.join(ll, "translations")
    translation_nodes, trans_edges, bindings = [], [], []
    by_key = {}
    for path in sorted(glob.glob(os.path.join(tdir, "*.md")), reverse=True):
        meta, _ = parse_frontmatter(path)
        title = meta.get("name") or os.path.basename(path)
        key = norm(title)
        if key not in by_key:  # newest revision wins
            by_key[key] = (path, meta, title)
    for path, meta, title in by_key.values():
        tid = "t_" + (re.sub(r"^[\d-]*", "", os.path.basename(path)).replace(".md", "") or norm(title)[:40])
        lang = meta.get("source_language") or meta.get("language") or ""
        src = meta.get("Source URL") or meta.get("source_url") or ""
        domain = meta.get("domain") or ""
        translation_nodes.append({"id": tid, "title": title, "lang": lang, "source_url": src, "domain": domain, "file": os.path.basename(path)})
        if lang:
            trans_edges.append({"type": "language", "from": "translation:" + tid, "to": "lang:" + norm(lang)})
        if domain:
            trans_edges.append({"type": "concept", "from": "translation:" + tid, "to": "concept:" + concepts.setdefault("d_" + norm(domain), domain)})
        # link to work by url or EXACT normalized title — a loose matcher
        # would attach everything to whichever work has the longest title,
        # which is worse than no link (under-promise, don't fabricate edges).
        wid = work_by_url.get(norm(src)) if src else None
        if not wid:
            wid = work_by_title.get(key)
        if wid:
            trans_edges.append({"type": "translated", "from": "translation:" + tid, "to": "work:" + wid})
        # person mentions: known_as/romanized name appearing in the title
        tnorm = norm(title)
        for pnode in person_nodes:
            pnames = [pnode["name"]] + pnode.get("known_as", [])
            if any(norm(pn) and norm(pn) in tnorm for pn in pnames if len(norm(pn)) > 5):
                trans_edges.append({"type": "mentions", "from": "translation:" + tid, "to": "person:" + pnode["id"]})
                break
        # curated-core binding
        bindings.append({
            "work_id": wid,
            "translation_id": tid,
            "title": title,
            "language": lang,
            "domain": domain,
            "source_url": src,
            "persons": work_nodes and (works.get(wid, {}).get("author_ids", []) or []) or [],
            "translation_file": os.path.basename(path),
            "date": os.path.basename(path)[:10],
        })

    nodes = {
        "concept": concept_nodes,
        "person": person_nodes,
        "work": work_nodes,
        "translation": translation_nodes,
    }
    edges = work_edges + trans_edges
    graph = {
        "_meta": {
            "schema": "aflinks-graph-v1",
            "version": 1,
            "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        },
        "stats": {k: len(v) for k, v in nodes.items()} | {"edges": len(edges)},
        "nodes": nodes,
        "edges": edges,
    }
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, indent=1)
    print(f"archive-graph.json: {graph['stats']}")

    # curated-core-bindings.json → living-library/database/
    out_bind = os.path.join(db, "curated-core-bindings.json")
    with open(out_bind, "w", encoding="utf-8") as f:
        json.dump({
            "_meta": {"schema": "curated-core-bindings-v1", "version": 1,
                      "generated_at": graph["_meta"]["generated_at"]},
            "bindings": bindings,
        }, f, ensure_ascii=False, indent=1)
    print(f"curated-core-bindings.json: {len(bindings)} bindings -> {out_bind}")

if __name__ == "__main__":
    main()