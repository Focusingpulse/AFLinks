#!/usr/bin/env python3
"""Build the AFLinks site's "Living Library" feed from the living-library DB.

The living-library grows continuously (polyglot scouts -> sources/,
translation curator -> translations/, entity extractor -> database/).
This script reads that shared repo and produces library_feed.json for the
AFLinks site, so the public site grows as the database grows.

Writes to /root/workspace/AFLinks/library_feed.json (or $AFLINKS_DIR).
Pure stdlib. Runs inside the aflinks cron; safe to run any time.

NOTE (2026-08-29, patched by Forge / translation-qc):
  This script was patched to be more robust when run on different machines
  (cloud sandbox vs Sandra's Windows machine). Changes:
    - declassified_finds: searches several locations for the declassified
      folder, and if none is found PRESERVES the previous feed value instead
      of zeroing the counter. May still be imperfect: if the declassified
      files live only in a cloud-only path, this counter may lag until a
      cloud run refreshes it.
    - Book5 copy: only overwrites the site's Book5_full_translation.md when
      the incoming source has MORE [pN] page markers than the published copy
      (or the destination is missing). A truncated in-progress assembly (e.g.
      first half of the book) is a strict subset of the fuller published copy
      and will not clobber it. Not perfect: if pages are ever re-numbered or
      a full rewrite has fewer markers than the old copy, it will be skipped
      with a WARN instead of published — check the log.
    - pages_translated: warns (does not hard-fail) when the computed value
      drops far below the previous feed value, so a silent regression is
      visible in the log.
  If you see odd counters after this patch, that is expected to be a
  path/layout issue rather than a content problem — check the earlier feed
  values before "fixing" the script.
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

# ─── Agent fleet: cool names + missions, shown on the site HUD ───
AGENT_FLEET = [
    {"member": "polyglot-scout-a", "name": "The Night Scout", "real_name": "Polyglot Scout A",
     "mission": "Hunts the global web in 2-3 rotating languages overnight for rare and vanishing research.",
     "schedule": "nightly 10pm MDT", "icon": "🌙"},
    {"member": "polyglot-scout-b", "name": "The Dawn Scout", "real_name": "Polyglot Scout B",
     "mission": "Second overnight sweep in a different set of languages — catches what the first pass missed.",
     "schedule": "nightly 2am MDT", "icon": "🌅"},
    {"member": "translation-curator", "name": "The Scribe", "real_name": "Translation Curator",
     "mission": "Produces first-ever full English translations and archives a durable copy of every source.",
     "schedule": "daily, offset hours", "icon": "✒️"},
    {"member": "translation-sweeper", "name": "The Weaver", "real_name": "Translation Sweeper",
     "mission": "Budget-burning full-document translator — weaves chunk by chunk until the whole text is English.",
     "schedule": "every 2h + overnight", "icon": "🧵"},
    {"member": "db-entity-extractor", "name": "The Archivist", "real_name": "DB Entity Extractor",
     "mission": "Catalogs every researcher and work into the dual-index database with practical-applicability flags.",
     "schedule": "daily 6pm MDT", "icon": "🗂️"},
    {"member": "aflinks", "name": "The Harmonizer", "real_name": "AFLinks Sync",
     "mission": "Keeps the vault and the library in tune — refreshes legacy indexes from the live archive.",
     "schedule": "daily 3am MDT", "icon": "🎵"},
    {"member": "archive-raid", "name": "The Rescuer", "real_name": "Archive Raid",
     "mission": "Deep hunts for disappearing, endangered, and rare texts before they vanish from the web.",
     "schedule": "weekly Sunday", "icon": "🚁"},
    {"member": "patent-watch", "name": "The Sentinel", "real_name": "Patent Watch",
     "mission": "Scans global patent databases for quiet new filings across the target domains.",
     "schedule": "weekly Thursday", "icon": "📜"},
    {"member": "wizard", "name": "The Diver", "real_name": "Deep-Dive Morning",
     "mission": "Morning deep dive across all topics plus a per-country declassified-documents sweep.",
     "schedule": "daily 9am MDT", "icon": "🤿"},
    {"member": "book5-translate", "name": "The Chronicler", "real_name": "Book5 Translate",
     "mission": "Long-haul translation of Atsyukovsky Book 5 — one chunk at a time, through the night.",
     "schedule": "overnight hourly", "icon": "📖"},
    {"member": "translation-qc", "name": "The Review Gate", "real_name": "Forge (Translation QC)",
     "mission": "Quality-checks every translation, assembles the chunks, publishes to the site, and researches the outer rings (radiesthesia, heart intelligence, subtle bioenergetics).",
     "schedule": "4h sessions + daily research", "icon": "⚒️"},
    {"member": "scout", "name": "The Scout Growth Captain", "real_name": "Scooter (Growth Scout)",
     "mission": "Scouts the archive seas for foreign-language and vanishing research, runs OCR on scanned works, grows the archive — and reads the subtle signals others miss (shape power, radiesthesia, bioenergetics) across rotating languages.",
     "schedule": "every 4h + rotating subtle-energy sweeps", "icon": "🔭"},
]


def find_cron_ledger():
    """Resolve the shared cron-coordination ledger (sibling shared repo)."""
    candidates = []
    if "MEMORY_DIR" in os.environ:
        candidates.append(os.path.join(os.environ["MEMORY_DIR"], "..", "cron-coordination", "cron_ledger.json"))
    candidates += [
        "/root/workspace/.letta/agents/agent-75b8d29e-76c1-4223-89f5-b2f8708be460/cron-coordination/cron_ledger.json",
        "/root/workspace/cron-coordination/cron_ledger.json",
    ]
    for cand in candidates:
        if os.path.isfile(cand):
            return cand
    return None


def parse_activity_log(path):
    """Parse ACTIVITY-LOG.md into {date, time, agent, summary} entries, newest first."""
    entries = []
    try:
        with open(path, encoding="utf-8") as f:
            raw = f.read()
    except Exception:
        return entries
    current_date = None
    for line in raw.splitlines():
        dm = re.match(r"^## (\d{4}-\d{2}-\d{2})$", line.strip())
        if dm:
            current_date = dm.group(1)
            continue
        em = re.match(r"^### (.+?) — (\d{2}:\d{2}) UTC$", line.strip())
        if em and current_date:
            agent = em.group(1).strip()
            time = em.group(2)
            entries.append({"date": current_date, "time": time, "agent": agent, "summary": ""})
            continue
        if entries and current_date:
            last = entries[-1]
            sm = re.match(r"^\*\*\+?([\d.,]+)\s*([^*]+?)\*\*\s*[—-]?\s*(.*)$", line.strip())
            if sm:
                if not last["summary"]:
                    last["summary"] = f"+{sm.group(1)} {sm.group(2).strip()}" + (f" — {sm.group(3).strip()}" if sm.group(3).strip() else "")
            elif line.strip() and not line.strip().startswith(("-", ">", "#", "---")):
                if not last["summary"]:
                    last["summary"] = line.strip()[:220]
    entries = [e for e in entries if e["summary"]]
    # Strip markdown backticks + link syntax for clean display on the site
    for e in entries:
        s = e["summary"]
        s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
        s = s.replace("`", "")
        e["summary"] = s.strip()
    entries.sort(key=lambda e: (e["date"], e["time"]), reverse=True)
    return entries[:50]


def parse_declassified(roots):
    """Collect declassified finds across candidate roots.

    Returns (found_dir, finds). found_dir is True if any root actually has a
    declassified/ folder (even if it parses to zero finds); False means none
    of the roots have one, so the caller should consider preserving the
    previous feed value instead of zeroing the counter.
    """
    found_dir = False
    for root in roots:
        ddir = os.path.join(root, "declassified")
        if not os.path.isdir(ddir):
            continue
        found_dir = True
        finds = []
        for path in sorted(glob.glob(os.path.join(ddir, "*", "*.md"))):
            if os.path.basename(path) in ("INDEX.md", "README.md"):
                continue
            country = os.path.basename(os.path.dirname(path))
            meta, title, body = parse_md_frontmatter(path)
            description = meta.get("description", "")
            finds.append({
                "country": country,
                "title": title,
                "description": description[:180],
                "file": f"declassified/{country}/{os.path.basename(path)}",
            })
        if finds:
            return (True, finds)
    return (found_dir, [])

def load_json(path, default=None):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default if default is not None else {}


def load_concepts(path=None):
    """Load the curated concept vocabulary (taxonomy/concepts.json)."""
    path = path or os.path.join(AFLINKS, "taxonomy", "concepts.json")
    data = load_json(path, {})
    return data.get("concepts", [])

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
        "agents": [],
        "activity_log": [],
        "declassified": [],
    }
    # Previous feed (if any): used to preserve counts that can't be derived on
    # this machine (e.g. declassified finds living in a cloud-only path) and to
    # warn on large regressions instead of silently publishing them.
    prev_feed = load_json(os.path.join(AFLINKS, "library_feed.json"))

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
        "translations": 0,
        "pages_translated": 0,
        "declassified_finds": 0,
        "active_agents": 0,
    }

    # --- 1b. Atsyukovsky book set (preserved PDFs + translation progress) ---
    books_dir = os.path.join(AFLINKS, "books", "atsyukovsky")
    ats_dir = os.path.join(LL, "sources", "atsyukovsky")
    bookset = []
    book5_pages = 0
    if os.path.isdir(books_dir) and os.path.isdir(ats_dir):
        titles = {
            "Book1": "Methodological Crisis of Modern Theoretical Physics",
            "Book2": "Methodology of Ether Dynamics & Structure of Matter",
            "Book3": "Etherdynamic Foundations of Cosmology & Cosmogony",
            "Book4": "Etherdynamic Foundations of Electromagnetic & Optical Phenomena",
            "Book5": "Initial Etherdynamic Experiments and Technologies",
        }
        for bn, title in titles.items():
            pdf = os.path.join(books_dir, f"Atsyukovsky_{bn}.pdf")
            if os.path.exists(pdf):
                entry = {
                    "volume": bn.replace("Book", ""),
                    "title": title,
                    "pdf": f"books/atsyukovsky/{os.path.basename(pdf)}",
                    "size_mb": round(os.path.getsize(pdf) / 1e6, 1),
                }
                bookset.append(entry)
        # translation progress
        manifest = os.path.join(ats_dir, "chunks", "manifest.json")
        translation_ok = False
        if os.path.exists(manifest):
            mf = load_json(manifest)
            done = 0
            for c in mf.get("chunks", []):
                if os.path.exists(os.path.join(ats_dir, "chunks", c["file"].replace(".txt", ".en.txt"))):
                    done += 1
            if done > 0:
                translation_ok = True
                book5_pages = done
                # Publish the assembled translation into the site repo.
                # Guard: only overwrite when the incoming source has MORE
                # [pN] page markers than what's already published (or the
                # destination is missing). A truncated in-progress assembly
                # (e.g. first half of the book) is a STRICT SUBSET of the
                # fuller published copy and must never clobber it — size is
                # not a reliable proxy, page markers are.
                try:
                    import shutil
                    src_asm = os.path.join(ats_dir, "Book5_full_translation.md")
                    dst_asm = os.path.join(AFLINKS, "sources", "atsyukovsky", "Book5_full_translation.md")
                    if os.path.isfile(src_asm):
                        with open(src_asm, encoding="utf-8") as f:
                            src_markers = len(re.findall(r"\[p\s*\d+\]", f.read()))
                        dst_markers = 0
                        if os.path.isfile(dst_asm):
                            with open(dst_asm, encoding="utf-8") as f:
                                dst_markers = len(re.findall(r"\[p\s*\d+\]", f.read()))
                        if not os.path.isfile(dst_asm) or (src_markers > dst_markers and src_markers > 0):
                            os.makedirs(os.path.dirname(dst_asm), exist_ok=True)
                            shutil.copy2(src_asm, dst_asm)
                            print(f"  Book5 assembly updated ({src_markers} [pN] markers vs {dst_markers} before)", flush=True)
                        else:
                            print(f"  WARN: skipping Book5 overwrite (src {src_markers} [pN] markers <= dst {dst_markers}); keeping fuller existing copy", flush=True)
                    else:
                        print("  WARN: Book5_full_translation.md not found in library; leaving site copy as-is", flush=True)
                except Exception as e:
                    print(f"  WARN: could not publish assembled translation: {e}", flush=True)
            bookset.append({
                "volume": "5",
                "title": "Book 5 — Full English Translation (in progress)",
                "progress_done": done,
                "progress_total": mf.get("total_chunks", 220),
                "assembled": "sources/atsyukovsky/Book5_full_translation.md" if translation_ok else None,
            })
    feed["atsuyskovsky_books"] = bookset

    # --- 2. Latest translations ---
    tdir = os.path.join(LL, "translations")
    translations_outdir = os.path.join(AFLINKS, "translations")
    translations_done = 0
    pages_translated = book5_pages
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
    # Count only translations PUBLISHED in the site repo (files that actually
    # exist after the copy), so the counter never claims more than is readable.
    if os.path.isdir(translations_outdir):
        for pub in sorted(glob.glob(os.path.join(translations_outdir, "*.md")), reverse=True):
            translations_done += 1
            try:
                with open(pub, encoding="utf-8") as f:
                    raw = f.read()
            except Exception:
                continue
            # Count pages: use [pN] page markers when present, else estimate by length
            markers = re.findall(r"\[p\s*\d+\]", raw)
            if markers:
                nums = [int(m.replace("[p", "").replace("]", "").strip()) for m in markers]
                pages_translated += max(nums)
            else:
                pages_translated += max(1, round(len(raw) / 3000))
    feed["library"]["translations"] = translations_done
    feed["library"]["pages_translated"] = pages_translated
    # Warn on a large unexplained regression vs the previous feed (e.g. the
    # declassified / Book5 path issues above) so it is visible in the cron log.
    prev_pages = ((prev_feed or {}).get("library") or {}).get("pages_translated")
    if prev_pages and pages_translated < prev_pages * 0.6:
        print(f"  WARN: pages_translated dropped {prev_pages} -> {pages_translated}; check paths / counting before trusting this feed", flush=True)

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

    # --- 6. AFLinks index count (live) + meta-category counts for the vault ---
    try:
        with open(os.path.join(AFLINKS, "index.json"), encoding="utf-8") as f:
            docs = json.load(f)
        feed["library"]["archive_entries"] = len(docs)
        mc = {}
        for d in docs:
            for m in (d.get("meta_categories") or []):
                if m:
                    mc[m] = mc.get(m, 0) + 1
        feed["library"]["meta_counts"] = mc
    except Exception:
        feed["library"]["archive_entries"] = None
        feed["library"]["meta_counts"] = {}

    # --- 7. Seam index for the Vesica (compare/contrast) lens ---
    # Compact: meta-category -> [doc ids] + id -> title. Lets the vault compute
    # the REAL overlap between any two categories (documents tagged with BOTH) in
    # memory, without loading the full multi-MB index. Grows safely with the archive.
    # Also carries the sub-category layer (meta_cats + doc_cats) so the vault can
    # surface *crossings* — documents that share ground with BOTH themes even when
    # no doc is tagged with both (fixes the empty-seam problem from the data model).
    cat_index = {}
    doc_titles = {}
    meta_cats = {}
    doc_cats = {}
    concept_names = {}
    meta_concepts = {}
    doc_concepts = {}
    try:
        for x in docs:
            did = x.get("id")
            if did is None:
                continue
            sid = str(did)
            title = (x.get("title") or x.get("filename") or "").strip()
            subs = x.get("categories") or []
            con = x.get("concepts") or []
            doc_titles[sid] = title
            doc_cats[sid] = subs
            doc_concepts[sid] = con
            for mc in (x.get("meta_categories") or []):
                if mc:
                    cat_index.setdefault(mc, []).append(sid)
                    if mc not in meta_cats:
                        meta_cats[mc] = set()
                    meta_cats[mc].update(subs)
                    for cid in con:
                        meta_concepts.setdefault(mc, set()).add(cid)
        vocab = load_concepts() if os.path.exists(os.path.join(AFLINKS, "taxonomy", "concepts.json")) else []
        concept_names = {c["id"]: c.get("name") or c["id"] for c in vocab}
    except Exception:
        cat_index, doc_titles, meta_cats, doc_cats = {}, {}, {}, {}
        meta_concepts, concept_names = {}, {}
    feed["seam"] = {
        "category_index": cat_index,
        "doc_titles": doc_titles,
        "meta_cats": {k: sorted(v) for k, v in meta_cats.items()},
        "doc_cats": doc_cats,
        "meta_concepts": {k: sorted(v) for k, v in meta_concepts.items()},
        "concept_names": concept_names,
        "doc_concepts": doc_concepts,
    }

    # --- 8. Agent fleet (HUD) + activity log + declassified finds ---
    ledger_path = find_cron_ledger()
    members = load_json(ledger_path, {}).get("members", {}) if ledger_path else {}
    fleet = []
    for a in AGENT_FLEET:
        rec = members.get(a["member"], {})
        fleet.append({
            **a,
            "last_run": rec.get("last_run"),
            "last_status": rec.get("last_status"),
            "last_summary": rec.get("last_summary", ""),
        })
    feed["agents"] = fleet
    feed["library"]["active_agents"] = sum(1 for a in fleet if a.get("last_run"))

    feed["activity_log"] = parse_activity_log(os.path.join(LL, "ACTIVITY-LOG.md"))

    # Declassified finds: search several roots; if none has a declassified/
    # folder on this machine, preserve the previous feed value (the files may
    # live in a cloud-only path) instead of silently zeroing the counter.
    d_roots = [LL, os.path.join(AFLINKS, "sources"), AFLINKS]
    d_found, d_finds = parse_declassified(d_roots)
    prev_declassified = (prev_feed or {}).get("declassified", [])
    if not d_found and prev_declassified:
        print(f"  WARN: no declassified/ dir found on this machine; preserving previous count ({len(prev_declassified)})", flush=True)
        d_finds = prev_declassified
    feed["declassified"] = d_finds
    feed["library"]["declassified_finds"] = len(d_finds)

    out = os.path.join(AFLINKS, "library_feed.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(feed, f, ensure_ascii=False, indent=2)
    print(f"library_feed.json written: {translations_done} published translations, "
          f"{len(feed['latest_finds'])} scout reports, {len(feed['top_researchers'])} researchers, "
          f"{len(feed['domains'])} domains")
    print(f"DB: {feed['library']['researchers']} researchers, {feed['library']['patents']} patents, "
          f"{feed['library']['categories']} categories")

if __name__ == "__main__":
    main()