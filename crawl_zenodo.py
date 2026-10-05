#!/usr/bin/env python3
"""
crawl_zenodo.py — build the filelist for the Recursive Harmonic cluster from the
Zenodo API (records from Kulik's Nexus/RHA corpus, Bolt/Carker group's RHC
papers, and the Awen Grid authors — a living 2025-26 aether-revival ecosystem).

Queries are scoped to the cluster vocabulary + named authors, paginated, then
deduped by conceptrecid (keeping the newest version of each work). Output is a
filelist in the same {url, filename} shape the generic processor expects, plus
rich Zenodo metadata (title, authors, doi, publication_date, abstract) that
process_zenodo.py uses to build better index entries.

Usage:
    python3 crawl_zenodo.py          # build/replace zenodo-rh_filelist.json
    python3 crawl_zenodo.py --count  # just print how many records matched
"""
import json, os, sys, time, urllib.parse, urllib.request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE = "zenodo-rh"
OUT = os.path.join(SCRIPT_DIR, f"{SITE}_filelist.json")

UA = "Mozilla/5.0 (research archive harvesting; contact via GitHub Focusingpulse)"
API = "https://zenodo.org/api/records"

# Cluster-scoped queries. Title queries catch the corpus regardless of how
# author names are spelled; author-name queries (field: creators.name) catch
# records whose titles don't use the cluster vocabulary. Common names (Barker,
# Cooper, Bolt) are always combined with title filters to avoid hauling in
# unrelated work. NOTE: use creators.name, NOT creators.person_or_org.name —
# the longer field silently returns zero matches.
QUERIES = [
    'title:"recursive harmonic"',
    'title:"harmonic codex"',
    'title:"nexus framework" AND (title:"recursive" OR title:"harmonic" OR title:"mark1")',
    'title:"recursive harmonic architecture"',
    'creators.name:"Kulik, Dean"',
    'creators.name:"Ceisiwr"',
    'creators.name:"Aureon"',
    'creators.name:"Tassan"',
    'creators.name:"Barker" AND title:"harmonic"',
    'creators.name:"LaPointe" AND (title:"harmonic" OR title:"recursive")',
    'creators.name:"Cooper" AND title:"harmonic" AND title:"orton"',
]


def api_get(params):
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch_all(query):
    """Paginate one query to its full result set.

    Unauthenticated Zenodo requests cap page size at 25 (400 beyond that);
    sort=mostrecent keeps pagination stable across pages.
    """
    hits, page, size = [], 1, 25
    while True:
        try:
            data = api_get({"q": query, "size": size, "page": page, "sort": "mostrecent"})
        except urllib.error.HTTPError as e:
            print(f"    HTTP {e.code}: {e.read().decode()[:200]}")
            break
        batch = data.get("hits", {}).get("hits", [])
        hits.extend(batch)
        total = data.get("hits", {}).get("total", 0)
        if page * size >= total or not batch:
            break
        page += 1
        time.sleep(0.4)
    return hits


def clean_title(t):
    t = (t or "").strip()
    t = " ".join(t.split())
    return t


def clean_abstract(desc):
    """Zenodo description is HTML — strip tags for a plain preview."""
    import re
    if not desc:
        return ""
    text = re.sub(r"<[^>]+>", " ", desc)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&quot;", '"', text)
    text = re.sub(r"&lt;", "<", text)
    text = re.sub(r"&gt;", ">", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:2000]


def main():
    seen_concept = {}
    raw = []

    for query in QUERIES:
        try:
            records = fetch_all(query)
        except Exception as e:
            print(f"  query failed ({e}): {query}")
            continue
        print(f"  {query}: {len(records)} raw hits")
        raw.extend(records)
        time.sleep(0.4)

    # Dedupe by conceptrecid, keep the newest version of each work.
    for rec in raw:
        cr = rec.get("conceptrecid") or rec.get("id")
        cur = seen_concept.get(cr)
        if cur is None or rec.get("id", 0) > cur.get("id", 0):
            seen_concept[cr] = rec

    filelist = []
    for cr, rec in sorted(seen_concept.items(), key=lambda kv: kv[1].get("id", 0)):
        md = rec.get("metadata", {})
        files = rec.get("files", [])
        pdfs = [f for f in files if (f.get("key") or "").lower().endswith(".pdf")]
        if not pdfs:
            continue  # no PDF artifact — nothing to archive
        pdf = max(pdfs, key=lambda f: f.get("size", 0))  # main PDF
        dl = (pdf.get("links") or {}).get("self") or ""
        if not dl:
            continue
        authors = [c.get("name", "") for c in md.get("creators", []) if c.get("name")]
        doi = md.get("doi") or ""
        filelist.append({
            "url": dl,
            "filename": pdf.get("key", ""),
            "record_id": rec.get("id"),
            "conceptrecid": cr,
            "title": clean_title(md.get("title")),
            "authors": authors,
            "doi": doi,
            "publication_date": (md.get("publication_date") or "")[:10],
            "abstract": clean_abstract(md.get("description")),
            "landing_url": f"https://zenodo.org/records/{rec.get('id')}",
            "type": (md.get("resource_type") or {}).get("title", ""),
        })

    if "--count" in sys.argv:
        print(f"total concept-deduped PDF records: {len(filelist)}")
        return

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(filelist, f, ensure_ascii=False, indent=1)
    print(f"wrote {len(filelist)} records -> {OUT}")


if __name__ == "__main__":
    main()