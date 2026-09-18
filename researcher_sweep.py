#!/usr/bin/env python3
"""
researcher_sweep.py — batch-catalog researcher names from index.json into the
living-library researcher index. Scouts run this after big harvests so the
researcher map keeps growing with the archive.

Idempotent: skips names already curated. Safe: only adds, never overwrites.
Usage: python3 researcher_sweep.py [min_docs]
"""
import json, re, sys, os
from collections import Counter
from datetime import datetime, timezone

LL = os.environ.get("LL_DIR", "/root/workspace/.letta/agents/agent-b73ac550-5671-471e-b3e1-721f948ea063/living-library")
ROOT = os.path.dirname(os.path.abspath(__file__))

def main():
    min_docs = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    import index_io
    idx = index_io.load()
    res_path = os.path.join(LL, "database/entities/researcher-index.json")
    res = json.load(open(res_path))
    cur = res.get("researchers", {})

    people = Counter()
    person_cats = {}
    for e in idx:
        p = (e.get("primary_person") or "").strip()
        if p and not re.match(r"^[\d\s]+$", p):
            people[p] += 1
            person_cats.setdefault(p, Counter()).update(e.get("categories") or [])

    name_re = re.compile(r"^[A-Z][A-Za-z.\-]+( [A-Z][A-Za-z.\-]+)+$")
    candidates = []
    for name, cnt in people.items():
        if name in cur:
            continue
        if cnt >= min_docs and (name_re.match(name) or cnt >= 3):
            candidates.append((name, cnt))
    candidates.sort(key=lambda x: -x[1])

    added = 0
    for name, cnt in candidates:
        if len(cur) >= 2000:
            break
        topsubs = [c for c, _ in person_cats[name].most_common(3)]
        cur[name] = {
            "id": "auto-" + re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:40],
            "name": name,
            "type": ["researcher"],
            "domains": topsubs or ["Archive"],
            "source_count": cnt,
            "patents": 0,
            "sources": [],
            "auto_cataloged": True,
            "note": "Batch-cataloged from primary_person field across the archive",
        }
        added += 1

    res["researchers"] = cur
    res["_meta"]["count"] = len(cur)
    # Stamp the real time — but only when something actually changed. This used
    # to be a hardcoded literal, which silently overwrote the true timestamp with
    # a frozen date on every sweep — the count moved while the metadata lied about
    # when. Now it is stamped truthfully, and left alone on a no-op sweep so a
    # zero-add run does not leave a timestamp-only diff in the shared repo.
    if added:
        res["_meta"]["last_updated"] = datetime.now(timezone.utc).isoformat()
    # indent=2 matches the file's existing formatting; indent=1 rewrote all
    # ~36k lines as a whitespace-only diff on every run, burying real changes.
    payload = json.dumps(res, indent=2, ensure_ascii=False) + "\n"
    with open(res_path, "r", encoding="utf-8") as f:
        current = f.read()
    # Compare ignoring trailing newline: the committed file has none (last written
    # by a different tool), so a strict compare would rewrite on every checkout.
    if payload.rstrip("\n") == current.rstrip("\n"):
        # Nothing to say — do not rewrite. Writing here left living-library (a
        # shared memory repo) permanently dirty on every zero-add sweep, which
        # breaks other lanes' `git pull --rebase` in that repo.
        print(f"researcher_sweep: {added} added, {len(cur)} total in index (no change; not rewritten)")
        return
    with open(res_path, "w", encoding="utf-8") as f:
        f.write(payload)
    print(f"researcher_sweep: {added} added, {len(cur)} total in index")

if __name__ == "__main__":
    main()
