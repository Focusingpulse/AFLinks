#!/usr/bin/env python3
"""Build the AFLinks site's "Living Library" feed from the living-library DB.

The living-library grows continuously (polyglot scouts -> sources/,
translation curator -> translations/, entity extractor -> database/).
This script reads that shared repo and produces library_feed.json for the
AFLinks site, so the public site grows as the database grows.

Writes to /root/workspace/AFLinks/library_feed.json (or $AFLINKS_DIR).
Pure stdlib. Runs inside the aflinks cron; safe to run any time.
"""
import json, os, re, sys, glob, datetime, urllib.request

# --- Resolve living-library mount (portable: shared memory first) ---
def find_living_library():
    candidates = []
    if "MEMORY_DIR" in os.environ:
        candidates.append(os.path.join(os.environ["MEMORY_DIR"], "..", "living-library"))
    candidates += [
        "/root/workspace/.letta/agents/agent-b73ac550-5671-471e-b3e1-721f948ea063/living-library",
        "/root/workspace/living-library",
    ]
    for cand in candidates:
        if os.path.isdir(os.path.join(cand, "database")):
            return cand
    return None

LL = find_living_library()
AFLINKS = os.environ.get("AFLINKS_DIR", "/root/workspace/AFLinks")

def load_json(path, default=None):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default if default is not None else {}

def parse_md_frontmatter(path):
    """Parse markdown with YAML-ish frontmatter. Returns (meta dict, title, body)."""
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    meta = {}
    body = raw
    title = os.path.basename(path).replace(".md", "")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", raw, re.DOTALL)
    if m:
        fm, body = m.group(1), m.group(2)
        for line in fm.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    # First heading as title
    h = re.search(r"^# (.+)$", body, re.MULTILINE)
    if h:
        title = h.group(1).strip()
    return meta, title, body

def main():
    if not LL:
        print("ERROR: living-library not found; aborting")
        sys.exit(1)
    if not os.path.isdir(AFLINKS):
        print(f"ERROR: AFLINKS dir missing: {AFLINKS}; aborting")
        sys.exit(1)

    feed = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "library": {},
        "latest_translations": [],
        "latest_finds": [],
        "top_researchers": [],
        "domains": [],
    }

    # --- 1. Database counts ---
    tax = load_json(os.path.join(LL, "database/taxonomy/taxonomy.json"))
    researchers = load_json(os.path.join(LL, "database/entities/researcher-index.json"))
    patents = load_json(os.path.join(LL, "database/patents/patent-index.json"))
    concept = load_json(os.path.join(LL, "database/taxonomy/concept-map.json"))

    feed["library"] = {
        "researchers": researchers.get("total_entities", len(researchers.get("entities", {}))),
        "patents": patents.get("total_patents", len(patents.get("patents", {}))),
        "categories": len(tax.get("categories", {})),
        "meta_categories": len(tax.get("meta_categories", {})),
        "aflinks_docs": tax.get("aflinks_total_docs"),
    }

    # --- 2. Latest translations ---
    tdir = os.path.join(LL, "translations")
    translations_outdir = os.path.join(AFLINKS, "translations")
    if os.path.isdir(tdir):
        os.makedirs(translations_outdir, exist_ok=True)
        for path in sorted(glob.glob(os.path.join(tdir, "*.md")), reverse=True):
            meta, title, body = parse_md_frontmatter(path)
            domain = meta.get("Domain") or meta.get("domain") or ""
            src = meta.get("Source URL") or meta.get("source_url") or ""
            lang = meta.get("Language") or meta.get("language") or ""
            fname = os.path.basename(path)
            # Copy the full translation into the site repo so the page can serve it
            try:
                import shutil
                shutil.copy2(path, os.path.join(translations_outdir, fname))
            except Exception as e:
                print(f"  WARN: could not copy translation {fname}: {e}", flush=True)
            feed["latest_translations"].append({
                "date": fname[:10],
                "title": title,
                "domain": domain,
                "source_url": src,
                "language": lang,
                "file": fname,
                "content_file": f"translations/{fname}",
                "excerpt": body.strip()[:220],
            })

    # --- 3. Latest finds (scout sources) ---
    sdir = os.path.join(LL, "sources")
    if os.path.isdir(sdir):
        for path in sorted(glob.glob(os.path.join(sdir, "*.md")), reverse=True):
            meta, title, body = parse_md_frontmatter(path)
            languages = meta.get("languages", "")
            scout = meta.get("scout", "")
            # Extract find entries: numbered items with a **Title** line
            finds = []
            for m in re.finditer(r"^\d+\.\s+\*\*(.+?)\*\*\s*(?:—|-)+\s*(.+?)$", body, re.MULTILINE):
                t = m.group(1).strip()
                desc = m.group(2).strip()
                # Grab the URL line after
                url_match = re.search(r"URLs?: (https?://\S+)", body[m.end():m.end()+600])
                url = url_match.group(1) if url_match else ""
                finds.append({"title": t, "description": desc, "url": url})
            feed["latest_finds"].append({
                "date": os.path.basename(path)[:10],
                "file": os.path.basename(path),
                "scout": scout,
                "languages": languages,
                "finds": finds[:8],
            })

    # --- 4. Top researchers (by source_count) ---
    ents = researchers.get("entities", {})
    ranked = sorted(
        ents.items(),
        key=lambda kv: (kv[1].get("source_count", 0), len(kv[1].get("patents", []))),
        reverse=True,
    )[:12]
    feed["top_researchers"] = [
        {
            "name": name.title(),
            "domains": rec.get("domains", [])[:3],
            "sources": rec.get("sources", [])[:2],
            "source_count": rec.get("source_count", 0),
            "patents": len(rec.get("patents", [])),
        }
        for name, rec in ranked
    ]

    # --- 5. Domains from concept map ---
    for dn, info in concept.get("domains", {}).items():
        feed["domains"].append({
            "name": dn,
            "categories": info.get("categories", [])[:6],
            "connections": [
                {"to": conn, "shared": strength}
                for conn, strength in info.get("connected_to", {}).items()
            ][:5],
        })

    # --- 6. AFLinks index count (live) ---
    try:
        with open(os.path.join(AFLINKS, "index.json"), encoding="utf-8") as f:
            feed["library"]["archive_entries"] = len(json.load(f))
    except Exception:
        feed["library"]["archive_entries"] = None

    out = os.path.join(AFLINKS, "library_feed.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(feed, f, ensure_ascii=False, indent=2)
    print(f"library_feed.json written: {len(feed['latest_translations'])} translations, "
          f"{len(feed['latest_finds'])} scout reports, {len(feed['top_researchers'])} researchers, "
          f"{len(feed['domains'])} domains")
    print(f"DB: {feed['library']['researchers']} researchers, {feed['library']['patents']} patents, "
          f"{feed['library']['categories']} categories")

if __name__ == "__main__":
    main()