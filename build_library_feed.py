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
    - refresh_shared_repo (Wizard, 2026-08-29): before reading either shared
      repo (cron-coordination ledger OR living-library), fast-forward the
      local projection to origin/main on a best-effort basis. This kills the
      stale-ledger bug class — a rebuild machine whose cron_ledger.json copy
      predates fleet members used to emit "awaiting first run" for Rescuer /
      Sentinel even after they had real runs. cron_job.sh also refreshes the
      coordination repo before the family gate, so the gate itself is fresh.
  If you see odd counters after this patch, that is expected to be a
  path/layout issue rather than a content problem — check the earlier feed
  values before "fixing" the script.
"""
import json, os, re, sys, glob, datetime, urllib.request, subprocess


def refresh_shared_repo(path):
    """Best-effort fast-forward of a shared-memory repo before reading from it.

    The feed builder runs on machines whose local projection of the shared
    repos can lag behind origin (the stale-ledger bug class: Rescuer/Sentinel
    showed 'awaiting first run' because the rebuild machine's local copy of
    cron_ledger.json predated those members). Try to fast-forward to
    origin/main so the feed is always built from fresh state.

    Never raises and never leaves the repo broken: on any failure we simply
    fall through and read what is on disk (the never-regress guard in the
    fleet section still protects against blanking existing dots).
    """
    if not path or not os.path.isdir(os.path.join(path, ".git")):
        return path
    try:
        subprocess.run(["git", "-C", path, "fetch", "--quiet", "origin"],
                       capture_output=True, timeout=90)
        r = subprocess.run(["git", "-C", path, "merge", "--ff-only", "--quiet", "origin/main"],
                           capture_output=True, timeout=90)
        if r.returncode != 0:
            # local branch may not be named main; fall back to a plain pull
            subprocess.run(["git", "-C", path, "pull", "--ff-only", "--quiet"],
                           capture_output=True, timeout=90)
    except Exception:
        pass
    return path

# --- Resolve living-library mount (portable: shared memory first) ---
def find_living_library():
    candidates = []
    if "MEMORY_DIR" in os.environ:
        candidates.append(os.path.join(os.environ["MEMORY_DIR"], "..", "living-library"))
    candidates += [
        "/root/workspace/.letta/agents/agent-b73ac550-5671-471e-b3e1-721f948ea063/living-library",
        "/root/workspace/living-library",
    ]
    # Portable fallback: any local agent projection of the shared living-library
    # repo (e.g. on a desktop machine where the fleet's shared repos are mounted
    # under other agents' directories).
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
            # Keep the library projection fresh before we read translations,
            # sources, and the activity log — same bug class as the stale
            # ledger, one layer down.
            refresh_shared_repo(cand)
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
    {"member": "cure-8er", "name": "The Synthesist", "real_name": "Cure 8er",
     "mission": "Connects what the fleet collects — cross-references researchers and works across languages, traces lines of science through the archive, writes synthesis documents, reviews translations for errors, and proposes the next lines of inquiry.",
     "schedule": "daily review + every 2h/6h translation gears", "icon": "🔗"},
    {"member": "drunvalo", "name": "The Pattern Keeper", "real_name": "Drunvalo",
     "mission": "Wisdom council and quality gate of the Living Library — keeps the Village growing, audits translations and data integrity, scouts the far corners of the web, weaves cross-domain synthesis, and keeps the archive's pattern true.",
     "schedule": "4h QC · 6h synthesis · 8h village growth · 12h scout/audit · daily refresh (cloud)", "icon": "🪷"},
]


def find_cron_ledger():
    """Resolve the shared cron-coordination ledger (sibling shared repo),
    refreshing its git repo first so a stale local projection can never
    produce 'awaiting first run' for members that have already run."""
    candidates = []
    if "MEMORY_DIR" in os.environ:
        candidates.append(os.path.join(os.environ["MEMORY_DIR"], "..", "cron-coordination", "cron_ledger.json"))
    candidates += [
        "/root/workspace/.letta/agents/agent-75b8d29e-76c1-4223-89f5-b2f8708be460/cron-coordination/cron_ledger.json",
        "/root/workspace/cron-coordination/cron_ledger.json",
    ]
    for cand in candidates:
        if os.path.isfile(cand):
            # cand is <repo>/cron_ledger.json → the repo root is its parent
            refresh_shared_repo(os.path.dirname(cand))
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
    """Parse markdown with YAML-ish frontmatter. Returns (meta dict, title, body).

    MemFS-validated shared-memory repos restrict frontmatter keys to name +
    description, so translation files carry their original metadata (domain,
    source_url, language, date, author...) as a "- **key:** value" block in
    the body. This reader fills meta from frontmatter first, then from that
    body block, and falls back to the `name` key for the title.
    """
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
                meta[k.strip()] = v.strip().strip('"').strip("'")
    # title from frontmatter `name` (memfs schema)
    if meta.get("name"):
        title = meta["name"]
    # body metadata block: "- **key:** value" lines
    for line in body.splitlines():
        bm = re.match(r"^- \*\*([^:*]+):\*\*\s*(.*)$", line.strip())
        if bm:
            k, v = bm.group(1).strip(), bm.group(2).strip()
            meta.setdefault(k, v)
            meta.setdefault(k.lower(), v)
            meta.setdefault(k.lower().replace(" ", "_"), v)
    # First heading as title (only if we have no name yet)
    if not meta.get("name"):
        h = re.search(r"^# (.+)$", body, re.MULTILINE)
        if h:
            title = h.group(1).strip()
    return meta, title, body


# ── Honest counting: translations are WORKS, not files ──────────────────────
# Revision passes (sweeper, curator QC, re-runs) re-publish the same document
# under new dated filenames. Counting every file inflates the real output
# (97 files ≈ 30 distinct works). Dedupe by normalized title; newest revision
# wins per work. The site's counters then under-promise instead of
# over-promising — the direction Chris asked for.
def _norm_key(s):
    """Dedupe key for translation works: lower, strip date prefix and noise."""
    s = re.sub(r"^(19|20)\d{2}[-_]\d{2}[-_]\d{2}[-_.]", "", (s or "").lower())
    s = re.sub(r"[^a-z0-9]+", " ", s)
    for w in ("on", "of", "the", "a", "to", "from", "and", "en", "fr", "it",
              "ru", "de", "es", "el", "pt", "ja", "zh", "pl", "cs", "sr",
              "uk", "ar", "nl", "full", "complete", "theory", "theorie",
              "volume", "vol", "compendium", "translation", "translations"):
        s = (" " + s + " ").replace(" " + w + " ", " ")
    return re.sub(r"\s+", " ", s).strip()


LANG_NAMES = {
    "fr": "French", "de": "German", "it": "Italian", "ru": "Russian",
    "es": "Spanish", "el": "Greek", "pt": "Portuguese", "pl": "Polish",
    "cs": "Czech", "sr": "Serbian", "uk": "Ukrainian", "ar": "Arabic",
    "ja": "Japanese", "zh": "Chinese", "nl": "Dutch",
}

def _lang_label(lang):
    lang = (lang or "").strip()
    if not lang:
        return ""
    code = lang.lower()
    if code in LANG_NAMES:
        return LANG_NAMES[code]
    return lang.title() if re.fullmatch(r"[a-z]{2}", code) else lang


# Hosts that die quietly: free/personal blog platforms. A find living there
# is endangered regardless of the content's importance.
FRAGILE_HOSTS = re.compile(
    r"over-blog\.net|blogspot\.|wordpress\.com|free\.fr|tripod\.|geocities|"
    r"nativeweb|angelfire|wixsite|weebly|\.info", re.I)

def _declass_slug(filepath):
    return re.sub(r"[^A-Za-z0-9]+", "-", filepath or "").strip("-")

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
        "news": [],
    }
    # Previous feed (if any): used to preserve counts that can't be derived on
    # this machine (e.g. declassified finds living in a cloud-only path) and to
    # warn on large regressions instead of silently publishing them.
    prev_feed = load_json(os.path.join(AFLINKS, "library_feed.json"))

    # --- 1. Database counts ---
    tax = load_json(os.path.join(LL, "database/taxonomy/taxonomy.json"))
    researchers = load_json(os.path.join(LL, "database/entities/researcher-index.json"))
    persons = load_json(os.path.join(LL, "database/persons/person-index.json"))
    patents = load_json(os.path.join(LL, "database/patents/patent-index.json"))
    concept = load_json(os.path.join(LL, "database/taxonomy/concept-map.json"))

    # Unified researcher table for counts + top-researcher ranking.
    # The dual-index person-index (database/persons/person-index.json) is now canonical;
    # the legacy researcher-index is a fallback during the transition.
    person_recs = persons.get("persons", {}) if isinstance(persons, dict) else {}
    legacy_recs = researchers.get("researchers", {}) if isinstance(researchers, dict) else {}
    # Legacy files also carried the older "entities"/"total_entities" shape.
    if not isinstance(person_recs, dict) or not person_recs:
        person_recs = {}
    if not isinstance(legacy_recs, dict) or not legacy_recs:
        legacy_recs = researchers.get("entities", {}) if isinstance(researchers, dict) else {}
        if not isinstance(legacy_recs, dict):
            legacy_recs = {}
    # Union the two tables by name so neither writer's additions are lost
    # (person-index is canonical and preferred for ranking; the legacy table may
    # hold swept names not yet curated into the person index).
    researchers_by_name = dict(person_recs)
    for name, rec in legacy_recs.items():
        researchers_by_name.setdefault(name, rec)
    researcher_count_cataloged = len(researchers_by_name)

    # Archive-scale researcher count: distinct named authors (primary_person)
    # in the current index.json. This is the number the site's stats band shows
    # ("Researchers"): an honest, derived figure that tracks the whole archive,
    # where the cataloged table is the curated subset.
    researcher_count = researcher_count_cataloged
    idx_path = os.path.join(AFLINKS, "index.json")
    if os.path.isfile(idx_path):
        try:
            with open(idx_path, encoding="utf-8") as f:
                idx = json.load(f)
            seen = set()
            for e in idx:
                p = (e.get("primary_person") or "").strip()
                if p and not re.match(r"^[\d\s]+$", p):
                    seen.add(p)
            if seen:
                researcher_count = len(seen)
        except Exception as exc:
            print(f"WARN: could not scan index.json for distinct authors: {exc}")
    # Prefer the archive count, but never regress below the cataloged table.
    researcher_count = max(researcher_count, researcher_count_cataloged)

    feed["library"] = {
        "researchers": researcher_count,
        "researchers_cataloged": researcher_count_cataloged,
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
            book5_complete = done >= mf.get("total_chunks", 220)
            bookset.append({
                "volume": "5",
                "title": f"Book 5 — Full English Translation ({'complete' if book5_complete else 'in progress'})",
                "progress_done": done,
                "progress_total": mf.get("total_chunks", 220),
                "assembled": "sources/atsyukovsky/Book5_full_translation.md" if translation_ok else None,
            })
            feed["library"]["book5_complete"] = book5_complete
    feed["atsuyskovsky_books"] = bookset

    # --- 2. Latest translations (counted as distinct WORKS, not files) ---
    # Revision passes re-publish the same document under new dated filenames;
    # group by normalized title and keep the newest revision per work so the
    # counter and the list never claim more than is truly translated.
    tdir = os.path.join(LL, "translations")
    translations_outdir = os.path.join(AFLINKS, "translations")
    translation_works = []
    translation_files = 0
    pages_translated = book5_pages
    if os.path.isdir(tdir):
        os.makedirs(translations_outdir, exist_ok=True)
        by_key = {}
        for path in sorted(glob.glob(os.path.join(tdir, "*.md")), reverse=True):
            meta, title, body = parse_md_frontmatter(path)
            fname = os.path.basename(path)
            key = _norm_key(title or fname)
            # reverse-sorted glob → first per key is the newest; keep the whole
            # group so metadata can be inherited from older, richer revisions
            by_key.setdefault(key, []).append((path, meta, title, body, fname))
        for group in by_key.values():
            path, meta, title, body, fname = group[0]
            domain = meta.get("Domain") or meta.get("domain") or ""
            src = meta.get("Source URL") or meta.get("source_url") or ""
            # Language: newest revision first, else inherit from any revision
            # of the same work, else scan the metadata/title text for a name.
            lang = ""
            for _path, _meta, _title, _body, _fname in group:
                lang = (_meta.get("source_language") or _meta.get("Language")
                        or _meta.get("language") or "")
                if lang:
                    break
            if not lang:
                hay = (meta.get("description", "") + " " + title + " "
                       + body[:300])
                low = hay.lower()
                for name in LANG_NAMES.values():
                    if name.lower() in low:
                        lang = name
                        break
            # Copy the newest revision into the site repo so the page can serve it
            try:
                import shutil
                shutil.copy2(path, os.path.join(translations_outdir, fname))
            except Exception as e:
                print(f"  WARN: could not copy translation {fname}: {e}", flush=True)
            translation_works.append({
                "date": fname[:10],
                "title": title,
                "domain": domain,
                "source_url": src,
                "language": lang,
                "file": fname,
                "content_file": f"translations/{fname}",
                "excerpt": body.strip()[:220],
            })
    # Count pages ONLY for the newest revision of each distinct work — old
    # revision files are readable but must not inflate the page total.
    if os.path.isdir(translations_outdir):
        for tw in translation_works:
            pub = os.path.join(translations_outdir, tw["file"])
            if not os.path.isfile(pub):
                continue
            translation_files += 1
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
    feed["latest_translations"] = translation_works
    feed["library"]["translations"] = len(translation_works)
    feed["library"]["translation_files"] = translation_files
    feed["library"]["pages_translated"] = pages_translated

    # --- 2b. Bilingual bridges — the same idea across languages ---
    # Phase 3: translations whose TITLES share significant tokens while their
    # source languages differ — the same theory reconstructed independently in
    # different linguistic silos (torsion in RU+DE, scalar field in FR+EN,
    # vortex in DE+ES). Metadata domains are too sparse to group by, so group
    # by normalized title tokens; require ≥2 shared tokens + different langs.
    BRIDGE_STOP = set(LANG_NAMES.keys()) | set(LANG_NAMES.values()) | {
        "translation", "theorie", "theory", "theories", "study", "studies",
        "complete", "full", "part", "vol", "volume", "toward", "towards",
        "matter", "gravity", "energy", "field", "research", "physics",
        "physics:", "scientific", "sciences", "science", "new", "newton",
        "present", "day", "newton", "based", "using", "their", "its",
        "with", "from", "into", "under", "over", "about",
    }
    def norm_lang(s):
        s = (s or "").lower().strip()
        return re.sub(r"\s*\([a-z]{2}\)$", "", s).strip()

    def _title_tokens(title):
        toks = re.findall(r"[a-z0-9]{4,}", (title or "").lower())
        out = []
        for t in toks:
            if t in BRIDGE_STOP or t.isdigit():
                continue
            out.append(t)
        return set(out)

    def _lang_of(tw, meta_scan):
        l = norm_lang(tw.get("language") or "")
        if l:
            return l
        hay = (tw.get("title") or "") + " " + meta_scan
        m = re.search(r"\((?:FR|DE|RU|ES|IT|EL|PT|JA|ZH|PL|CS|SR|UK|AR|NL)\s*→", hay, re.I)
        if m:
            return m.group(1).lower()
        m = re.search(r"[_-](fr|de|ru|es|it|el|pt|pl|cs|sr|uk|ar|nl)$", tw.get("file") or "", re.I)
        if m:
            return m.group(1).lower()
        low = hay.lower()
        for c, n in LANG_NAMES.items():
            if n.lower() in low or c in low.split():
                return c
        return ""

    bridges = []
    # collect token sets + languages first (meta_scan = description/domain text)
    meta_of = {}
    for tw in translation_works:
        meta_of[tw["file"]] = " ".join([tw.get("domain") or "", tw.get("excerpt") or ""][:1])
    tok_of = {}
    for tw in translation_works:
        tok_of[tw["file"]] = _title_tokens(tw["title"])
    # union-find clusters over cross-language pairs with ≥2 shared tokens
    parent = {tw["file"]: tw["file"] for tw in translation_works}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    files = [tw["file"] for tw in translation_works]
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            a, b = files[i], files[j]
            la, lb = _lang_of(translation_works[i], ""), _lang_of(translation_works[j], "")
            if not la or not lb or la == lb:
                continue
            shared = tok_of[a] & tok_of[b]
            if len(shared) >= 2:
                union(a, b)
    clusters = {}
    for tw in translation_works:
        clusters.setdefault(find(tw["file"]), []).append(tw)
    for root, tws in clusters.items():
        if len(tws) < 2:
            continue
        langs = []
        for tw in tws:
            l = _lang_of(tw, meta_of.get(tw["file"], ""))
            # normalize full name -> code so chips are clean (fr, de, ru…)
            code = next((c for c, n in LANG_NAMES.items() if n.lower() == norm_lang(l)), l)
            if code and code not in langs:
                langs.append(code)
        if len(langs) < 2:
            continue
        # representative shared tokens → readable subject
        tok_sets = [tok_of[tw["file"]] for tw in tws]
        shared_toks = set.intersection(*tok_sets) if tok_sets else set()
        if not shared_toks:
            shared_toks = set.union(*tok_sets)
        subject = " ".join(sorted(shared_toks)[:3]).title() or tws[0].get("domain") or tws[0]["title"]
        bridges.append({
            "domain": subject,
            "langs": sorted(langs),
            "works": sorted(tws, key=lambda t: t["date"], reverse=True),
        })
    bridges.sort(key=lambda b: (-len(b["langs"]), b["domain"]))
    feed["bridges"] = bridges[:8]
    feed["library"]["bridges"] = len(bridges)
    # Warn on a large unexplained regression vs the previous feed (e.g. the
    # declassified / Book5 path issues above) so it is visible in the cron log.
    prev_pages = ((prev_feed or {}).get("library") or {}).get("pages_translated")
    if prev_pages and pages_translated < prev_pages * 0.6:
        print(f"  WARN: pages_translated dropped {prev_pages} -> {pages_translated}; check paths / counting before trusting this feed", flush=True)

    # --- 3. Latest finds (scout sources) ---
    # Scout reports arrive in several formats — polyglot scouts use numbered
    # "N. **Title** — desc" lines with a URL; Scooter's growth scouts use a
    # richer "### N. Title — desc" heading + "**Source URL:**" body. Parse
    # any of them robustly so every scout's finds render on the site.
    def parse_scout_finds(body):
        finds = []
        # 3a. Numbered bold-title lines: "12. **Title** — desc" (polyglot)
        for m in re.finditer(r"^(\d+)\.\s+\*\*(.+?)\*\*\s*(?:—|-)+\s*(.+?)$",
                             body, re.MULTILINE):
            t, desc = m.group(2).strip(), m.group(3).strip()
            u = re.search(r"(?:URLs?|Source URL|Link)s?:\s*(https?://\S+)",
                          body[m.end():m.end()+600])
            finds.append({"title": t, "description": desc,
                          "url": u.group(1) if u else ""})
        # 3b. Numbered headings: "### 13. Title — desc" + "**Source URL:**"
        for m in re.finditer(r"^#{1,4}\s*(\d+)\.\s+(.+?)\s*(?:—|-|:)+\s*(.+?)$",
                             body, re.MULTILINE):
            t, desc = m.group(2).strip(), m.group(3).strip()
            u = re.search(r"(?:URLs?|Source URL|Link)s?:\s*(https?://\S+)",
                          body[m.end():m.end()+800])
            finds.append({"title": t, "description": desc,
                          "url": u.group(1) if u else ""})
        # 3c. Bullet-title lines: "- **Title** — desc" or "- Title — desc"
        for m in re.finditer(r"^[-\*]\s+(?:\*\*)?(.+?)(?:\*\*)?\s*(?:—|-|:)+\s*(.+?)$",
                             body, re.MULTILINE):
            t, desc = m.group(1).strip(), m.group(2).strip()
            if t.lower().startswith(("title", "source", "url", "language", "gear", "run")):
                continue
            u = re.search(r"(?:URLs?|Source URL|Link)s?:\s*(https?://\S+)",
                          body[m.end():m.end()+600])
            finds.append({"title": t, "description": desc,
                          "url": u.group(1) if u else ""})
        # Dedupe by (title,url) keeping first occurrence
        seen, out = set(), []
        for f in finds:
            k = (f["title"].lower()[:60], f["url"])
            if k in seen:
                continue
            seen.add(k)
            out.append(f)
        return out

    scout_roots = []
    sdir = os.path.join(LL, "sources")
    if os.path.isdir(sdir):
        scout_roots.append(sdir)
    # Also scan the public repo's own sources/ — Scooter/Forge push reports and
    # translations there via GitHub (their shared-repo projections don't
    # converge with this org's, but the public repo is a common channel).
    repo_sources = os.path.join(AFLINKS, "sources")
    if repo_sources != sdir and os.path.isdir(repo_sources):
        scout_roots.append(repo_sources)

    for sdir in scout_roots:
        for path in sorted(glob.glob(os.path.join(sdir, "*.md")), reverse=True):
            meta, title, body = parse_md_frontmatter(path)
            languages = meta.get("languages", "")
            scout = meta.get("scout", "")
            finds = parse_scout_finds(body)
            # Only include a scout file if it actually parsed finds; empty
            # finds lists render as dead cards on the live site.
            if finds:
                feed["latest_finds"].append({
                    "date": os.path.basename(path)[:10],
                    "file": os.path.basename(path),
                    "scout": scout,
                    "languages": languages,
                    "finds": finds[:8],
                })

    # --- 4. Top researchers (by source/domain weight) ---
    def _src_count(rec):
        srcs = rec.get("sources")
        if isinstance(srcs, (list, tuple)):
            return len(srcs)
        return rec.get("source_count", 0) or 0

    def _display_name(name, rec):
        kn = rec.get("known_as")
        if isinstance(kn, (list, tuple)) and kn and isinstance(kn[0], str) and kn[0].strip():
            return kn[0]
        for k in ("romanized_name", "name"):
            v = rec.get(k)
            if isinstance(v, str) and v.strip():
                return v
        return name

    ranked = sorted(
        researchers_by_name.items(),
        key=lambda kv: (
            _src_count(kv[1]),
            len(kv[1].get("domains", [])) if isinstance(kv[1].get("domains"), (list, tuple)) else 0,
        ),
        reverse=True,
    )[:24]
    feed["top_researchers"] = [
        {
            "name": _display_name(name, rec),
            "domains": rec.get("domains", [])[:3],
            "sources": rec.get("sources", [])[:2],
            "source_count": _src_count(rec),
            "patents": len(rec.get("patents", [])) if isinstance(rec.get("patents"), (list, tuple)) else 0,
        }
        for name, rec in ranked
    ]

    # --- 5. Domains from concept map ---
    # Guard: only surface connections that actually exist as categories in the
    # live index (category normalization may have merged away old labels).
    live_cats = set()
    try:
        with open(os.path.join(AFLINKS, "index.json"), encoding="utf-8") as f:
            for _d in json.load(f):
                for _c in (_d.get("categories") or []):
                    live_cats.add(_c)
    except Exception:
        pass
    for dn, info in concept.get("domains", {}).items():
        occ = info.get("co_occur_categories", {}) or {}
        occ = {c: s for c, s in occ.items() if c in live_cats}
        # categories = top co-occurring sub-categories by strength
        top_cats = sorted(occ.items(), key=lambda kv: -kv[1])[:6]
        # connections = sorted neighbors (shared = co-occurrence strength)
        conns = [{"to": c, "shared": s} for c, s in top_cats]
        feed["domains"].append({
            "name": dn,
            "categories": [c for c, _ in top_cats],
            "connections": conns[:5],
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

    # Some members keep a self-contained status file INSIDE this repo so their
    # crons — which run outside the shared cron-coordination repo's push path —
    # can report reliably. The site merges it into the fleet card.
    STATUS_FILES = {
        "drunvalo": os.path.join(AFLINKS, "drunvalo", "status.json"),
        "cure-8er": os.path.join(AFLINKS, "synthesist", "status.json"),
        # Scooter + Forge report through the public repo (their shared-repo
        # projections don't converge with this org's ledger). Same pattern as
        # drunvalo: cron writes scout/status.json + forge/status.json here.
        "scout": os.path.join(AFLINKS, "scout", "status.json"),
        "translation-qc": os.path.join(AFLINKS, "forge", "status.json"),
    }
    status_overrides = {}
    for member, spath in STATUS_FILES.items():
        st = load_json(spath, {})
        if st:
            status_overrides[member] = st

    for a in AGENT_FLEET:
        rec = members.get(a["member"], {})
        # Self-contained status file overrides/supplements the shared ledger
        if a["member"] in status_overrides:
            rec = {**rec, **status_overrides[a["member"]]}
        # PRESERVE live dots: if this run has no last_run for a member who
        # already shows a dot in the previous feed (stale ledger / sandbox
        # without the shared repo), fall back to the previous feed's value
        # instead of blanking it. A rebuild must never regress a live dot just
        # because it ran against an out-of-date cron_ledger.json. Freshest
        # non-null value wins.
        prev_a = {}
        prev_agents = (prev_feed or {}).get("agents", [])
        if isinstance(prev_agents, list):
            for _a in prev_agents:
                if isinstance(_a, dict) and _a.get("member") == a["member"]:
                    prev_a = _a
                    break
        fleet.append({
            **a,
            "last_run": rec.get("last_run") or prev_a.get("last_run"),
            "last_status": rec.get("last_status") or prev_a.get("last_status"),
            "last_summary": rec.get("last_summary") or prev_a.get("last_summary", ""),
        })
    feed["agents"] = fleet
    feed["library"]["active_agents"] = sum(1 for a in fleet if a.get("last_run"))

    # Activity log: living library log PLUS per-agent activity files
    # (drunvalo/ACTIVITY.md, synthesist/ACTIVITY.md in this repo), so runs from
    # agents outside the shared repo appear in "what's new".
    feed["activity_log"] = parse_activity_log(os.path.join(LL, "ACTIVITY-LOG.md"))
    local_activity = parse_activity_log(os.path.join(AFLINKS, "drunvalo", "ACTIVITY.md"))
    local_activity += parse_activity_log(os.path.join(AFLINKS, "synthesist", "ACTIVITY.md"))
    local_activity += parse_activity_log(os.path.join(AFLINKS, "scout", "ACTIVITY.md"))
    local_activity += parse_activity_log(os.path.join(AFLINKS, "forge", "ACTIVITY.md"))
    if local_activity:
        # Merge dedupe: keep living-library entries, prepend local agent entries.
        merged = local_activity + [
            e for e in feed["activity_log"]
            if not any(d.get("date") == e.get("date") and d.get("time") == e.get("time")
                       and d.get("agent") == e.get("agent") for d in local_activity)
        ]
        merged.sort(key=lambda e: (e.get("date", ""), e.get("time", "")), reverse=True)
        feed["activity_log"] = merged[:60]

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

    # --- 9. News — the "only here" strip for the What's New HUD ---
    # News is what Chris asked for: freshly translated works, newly opened
    # records, milestones, and finds on hosts that could vanish. Only claims
    # things we can stand behind: "fresh from X", "newly opened", "host may
    # vanish". Never "first-ever in English" — that needs verification.
    news = []
    today = datetime.date.today().isoformat()
    if feed["library"].get("book5_complete"):
        news.append({
            "date": today,
            "kind": "milestone",
            "title": "Atsyukovsky Book 5 — complete in English",
            "excerpt": "All 220 chunks of 'Initial Etherdynamic Experiments and Technologies' translated and assembled — most of the 320-page Russian volume, now readable end to end.",
            "rarity": "milestone",
            "href": "./library.html#booksSection",
        })
    for t in feed.get("latest_translations", [])[:3]:
        ln = _lang_label(t.get("language"))
        news.append({
            "date": t["date"],
            "kind": "translation",
            "title": t["title"],
            "excerpt": (t.get("excerpt") or "")[:160],
            "rarity": ("fresh from " + ln) if ln else "fresh translation",
            "href": "./library.html#trans-" + t["file"],
            "source_url": t.get("source_url") or "",
        })
    for d in feed.get("declassified", [])[-2:]:
        news.append({
            "date": today,
            "kind": "declassified",
            "title": d.get("title"),
            "excerpt": (d.get("description") or "")[:160],
            "rarity": "newly opened",
            "href": "./library.html#declass-" + _declass_slug(d.get("file")),
        })
    frag = 0
    for s in feed.get("latest_finds", [])[:8]:
        for f in s.get("finds", [])[:5]:
            u = f.get("url") or ""
            if FRAGILE_HOSTS.search(u):
                news.append({
                    "date": s.get("date", ""),
                    "kind": "find",
                    "title": f.get("title"),
                    "excerpt": (f.get("description") or "")[:160],
                    "rarity": "host may vanish",
                    "href": u,
                    "source_url": u,
                })
                frag += 1
                if frag >= 2:
                    break
        if frag >= 2:
            break
    # Pattern signals from the paradigm fleet (kind=paradigm-signal) — the
    # human-interface position: the front-end wire exists, the builder never
    # emitted them. These are the archive's cross-domain pattern notes.
    synth_path = os.path.join(AFLINKS, "synthesis", "synthesis_index.json")
    synth = load_json(synth_path, [])
    pcount = 0
    for e in synth:
        if e.get("kind") == "paradigm-signal":
            news.append({
                "date": e.get("date", ""),
                "kind": "paradigm",
                "title": e.get("title"),
                "excerpt": (e.get("teaser") or e.get("description") or "")[:160],
                "rarity": "pattern signal",
                "href": "./synthesis.html#" + (e.get("slug") or e.get("file")),
            })
            pcount += 1
            if pcount >= 2:
                break
    news.sort(key=lambda n: n["date"], reverse=True)
    feed["news"] = news[:8]

    # --- 9b. Entity graph (the contract agents read) ---
    # Phase 1: archive-graph.json (nodes: person/work/translation/concept +
    # typed edges) + curated-core-bindings.json. Serve the graph with the site
    # and stamp its stats into the feed so the HUD can surface it.
    graph_path = os.path.join(AFLINKS, "archive-graph.json")
    g = load_json(graph_path)
    if g:
        feed["graph"] = {
            "url": "archive-graph.json",
            "generated_at": g.get("_meta", {}).get("generated_at", ""),
            "stats": g.get("stats", {}),
        }
        feed["library"]["graph_edges"] = g.get("stats", {}).get("edges", 0)
        feed["library"]["graph_nodes"] = sum(v for k, v in g.get("stats", {}).items() if k != "edges")

    # --- 9c. Retrieval-grounding rules — the citation contract for entities ---
    # Phase 2 (AI-entity position): agents and synthesists hallucinate archive
    # contents when there's no id+quote grounding rule on the record. This is
    # the difference between AI finding new science and AI inventing it.
    feed["retrieval_contract"] = {
        "version": 1,
        "canonical_id": "doc:<id>",
        "quote_format": "「exact quoted text」 — doc:<id> (title, host)",
        "rules": [
            "Every factual claim about archive content must cite doc:<id>.",
            "Quotes must be verbatim from the document, never paraphrased as quotes.",
            "A document's existence is not evidence its claims are true — patents are claims, not validations.",
            "Contradictory documents must be cited as contradictions, not resolved silently.",
            "Never fabricate links between documents; the archive-graph.json edges are the only sanctioned relationships.",
        ],
        "dereference": {"doc": "archive-graph.json nodes.work/translation -> index.json#id"},
    }

    # --- 9d. The Replication Yard — practical applications pavilion ---
    # Chris (2026-09-06): the main site needs practical applications with a
    # feedback loop — quest cards, replication dossiers, and incoming
    # validations visible publicly, with a submission path. Reads the
    # living-library synthesis folders; the site renders them.
    practical = {"quests": [], "dossiers": [], "validations": [], "queue_url": None}
    qdir = os.path.join(LL, "synthesis", "quest-queue")
    if os.path.isdir(qdir):
        for path in sorted(glob.glob(os.path.join(qdir, "*.md")), reverse=True):
            base = os.path.basename(path)
            if base.lower() == "readme.md":
                continue
            meta, title, body = parse_md_frontmatter(path)
            # pull a rough status from body for cheap front-end filtering
            status = "proposed"
            m = re.search(r"status:\s*\*{0,2}(proposed|approved|merged|rejected)", body)
            if m:
                status = m.group(1)
            practical["quests"].append({
                "file": f"synthesis/quest-queue/{base}",
                "date": base[:10],
                "title": title,
                "status": status,
                "excerpt": (body.strip()[:200] or ""),
            })
    rdir = os.path.join(LL, "synthesis", "replication")
    if os.path.isdir(rdir):
        for path in sorted(glob.glob(os.path.join(rdir, "*.md")), reverse=True):
            base = os.path.basename(path)
            meta, title, body = parse_md_frontmatter(path)
            status = "draft"
            m = re.search(r"Status:\s*\*{0,2}([\w\-]+)", body)
            if m:
                status = m.group(1)
            practical["dossiers"].append({
                "file": f"synthesis/replication/{base}",
                "date": base[:10],
                "title": title,
                "status": status,
                "excerpt": (body.strip()[:200] or ""),
            })
    vdir = os.path.join(LL, "synthesis", "validations")
    if os.path.isdir(vdir):
        for path in sorted(glob.glob(os.path.join(vdir, "*.md")), reverse=True):
            base = os.path.basename(path)
            if base.lower() == "readme.md":
                continue
            meta, title, body = parse_md_frontmatter(path)
            practical["validations"].append({
                "file": f"synthesis/validations/{base}",
                "date": base[:10],
                "title": title,
                "excerpt": (body.strip()[:200] or ""),
            })
    practical["queue_url"] = f"synthesis/quest-queue/"
    feed["practical"] = practical
    feed["library"]["practical_quests"] = len(practical["quests"])
    feed["library"]["replication_dossiers"] = len(practical["dossiers"])
    feed["library"]["validations"] = len(practical["validations"])

    out = os.path.join(AFLINKS, "library_feed.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(feed, f, ensure_ascii=False, indent=2)
    print(f"library_feed.json written: {len(translation_works)} translation works "
          f"({translation_files} files), {len(feed['news'])} news items, "
          f"{len(feed['latest_finds'])} scout reports, {len(feed['top_researchers'])} researchers, "
          f"{len(feed['domains'])} domains")
    print(f"DB: {feed['library']['researchers']} researchers, {feed['library']['patents']} patents, "
          f"{feed['library']['categories']} categories")

    _bake_live_stats()

def _bake_live_stats() -> None:
    """Stamp fresh counts + cache-busting versions into the site HTML.

    Ensures raw HTML always carries the current archive numbers, so bots and
    agents that never execute JS still see the truth. Called automatically at
    the end of every build — the cron prose checklist is not the only guard.
    """
    import subprocess
    import sys
    from pathlib import Path

    here = Path(__file__).resolve().parent
    subprocess.run(
        [sys.executable, str(here / "bake_stats.py")],
        cwd=here,
        check=True,
    )


if __name__ == "__main__":
    main()