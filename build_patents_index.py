#!/usr/bin/env python3
"""Build the patents index for the AFLinks site.

Reads index.json and produces:
  - patents.json: site data for the patents pavilion
  - Updates living-library patent-index.json (the DB)

Run this before build_library_feed.py so the patent counter is correct.
"""
import json
import os
import re
from datetime import datetime

AFLINKS = os.environ.get("AFLINKS_DIR", "/root/workspace/AFLinks")

def find_living_library():
    """Find the living-library shared repo."""
    candidates = []
    if "MEMORY_DIR" in os.environ:
        candidates.append(os.path.join(os.environ["MEMORY_DIR"], "..", "living-library"))
    candidates += [
        "/root/workspace/.letta/agents/agent-b73ac550-5671-471e-b3e1-721f948ea063/living-library",
        "/root/workspace/living-library",
    ]
    try:
        agents_root = os.path.join(os.path.expanduser("~"), ".letta", "agents")
        if os.path.isdir(agents_root):
            for a in os.listdir(agents_root):
                cand = os.path.join(agents_root, a, "living-library")
                if os.path.isdir(cand):
                    candidates.append(cand)
    except Exception:
        pass
    for cand in candidates:
        if os.path.isdir(os.path.join(cand, "database")):
            return cand
    return None

def main():
    # Load index.json
    import index_io
    try:
        data = index_io.load()
    except FileNotFoundError:
        print("ERROR: master index not found")
        return

    print(f"Loaded {len(data)} documents from index.json")

    # Extract patents
    patents = {}  # patent_number -> {docs: [{id, title, person, categories}], countries: set()}

    for doc in data:
        patent_nums = doc.get("patent_numbers", [])
        if not patent_nums:
            continue

        doc_id = doc.get("id")
        title = doc.get("title", "Untitled")
        person = doc.get("primary_person", "")
        categories = doc.get("categories", [])
        meta_categories = doc.get("meta_categories", [])

        for pn in patent_nums:
            pn = pn.strip()
            if not pn:
                continue

            # Normalize: ensure prefix (US, RU, etc.)
            # Some patent numbers in the index are bare digits
            if re.match(r'^\d+$', pn):
                # Bare number — assume US patent if 7-8 digits
                if len(pn) >= 7:
                    pn = f"US{pn}"

            if pn not in patents:
                patents[pn] = {
                    "number": pn,
                    "docs": [],
                    "countries": set(),
                    "persons": set(),
                    "categories": set(),
                }

            patents[pn]["docs"].append({
                "id": doc_id,
                "title": title,
                "person": person,
                "categories": categories,
                "meta_categories": meta_categories,
            })
            if person:
                patents[pn]["persons"].add(person)
            for c in categories:
                patents[pn]["categories"].add(c)

            # Extract country prefix
            m = re.match(r'^([A-Z]{2})', pn.upper())
            if m:
                patents[pn]["countries"].add(m.group(1))

    print(f"Extracted {len(patents)} unique patent numbers")

    # Convert sets to lists for JSON
    for pn, rec in patents.items():
        rec["countries"] = sorted(rec["countries"])
        rec["persons"] = sorted(rec["persons"])
        rec["categories"] = sorted(rec["categories"])

    # Sort patents by number
    patents_list = sorted(patents.values(), key=lambda x: x["number"])

    # Write patents.json for the site
    out_path = os.path.join(AFLINKS, "patents.json")
    site_data = {
        "_meta": {
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "count": len(patents_list),
            "source": "index.json",
        },
        "patents": patents_list,
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(site_data, f, ensure_ascii=False, indent=2)
    print(f"Wrote {out_path}")

    # Update living-library patent-index.json (the DB)
    LL = find_living_library()
    if LL:
        db_path = os.path.join(LL, "database", "patents", "patent-index.json")
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        # DB format: mapping patent number -> {domains, researchers, doc_ids}
        db_data = {
            "_meta": {
                "focal_entity": "The Force of Aether",
                "version": 1,
                "last_updated": datetime.utcnow().isoformat() + "Z",
                "description": "Patent index mapping patent numbers to domains and researchers",
                "count": len(patents_list),
            },
            "patents": {},
        }
        for rec in patents_list:
            db_data["patents"][rec["number"]] = {
                "domains": rec["categories"],
                "researchers": list(rec["persons"]),
                "doc_ids": [d["id"] for d in rec["docs"]],
            }

        with open(db_path, "w", encoding="utf-8") as f:
            json.dump(db_data, f, ensure_ascii=False, indent=2)
        print(f"Updated {db_path}")
    else:
        print("WARN: living-library not found, skipping DB update")

    print(f"Done. {len(patents_list)} patents indexed.")

if __name__ == "__main__":
    main()
