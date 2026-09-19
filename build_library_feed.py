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
    # Canonical cloud-sandbox pattern (any agent id): the shared repos are
    # projected at <agents-root>/<agent>/memory/../living-library.
    try:
        agents_root = "/root/workspace/.letta/agents"
        if os.path.isdir(agents_root):
            for a in os.listdir(agents_root):
                cand = os.path.join(agents_root, a, "memory", "..", "living-library")
                if os.path.isdir(cand):
                    candidates.append(os.path.normpath(cand))
    except Exception:
        pass
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
    {"member": "navigator", "name": "The Navigator", "real_name": "Navigator (Field & Trajectory Reporter)",
     "mission": "Trail guide for the community — converts the fleet's findings into what a person can actually teach, build, scout, or preserve. Turns each scout find, translation, and synthesis into a discriminating test rather than a promise.",
     "schedule": "daily digest + gear monitor", "icon": "🧭"},
    {"member": "watchtower", "name": "The Watchtower", "real_name": "Watchtower (Fleet Watchdog & Cross-Repo Synthesis)",
     "mission": "Eyes on the whole fleet's blind spots — audits all five repos for silent breakage, orphaned work, and cross-repo connections nobody else is seeing; publishes weekly synthesis reports and tracks flagged issues until they're fixed.",
     "schedule": "weekly synthesis + daily quick-scan", "icon": "🗼"},
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


# ── Translation metadata quality guards (2026-09-16) ────────────────────────
# living-library/synthesis and translations/ frontmatter is normalized by a
# shared-memory schema pass ("Normalize all shared-memory md frontmatter to
# memfs schema", e81e4a8) which rewrites `name` to either a bare filename slug
# or "Translation: <title truncated with …>", and `description` to the literal
# string "Translation document.". A blind mirror of those copies degrades the
# published site's translation titles, and some translator output carries
# mis-encoded (mojibake) bodies. The published copy is what readers are served,
# so the builder must not clobber a good copy with a worse one — the same
# never-regress principle as the Yard and Book5 guards above.
_SLUG_NAME_RX = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9\-_]+$", re.I)
_SLUG_TITLE_RX = re.compile(r"^(19|20)\d{2}-\d{2}-\d{2}[-_][\w\-]+$")
_MOJIBAKE_SEQS = ("â€", "Ã¼", "Ã©", "Ã¶", "Ã¤", "Ã ", "Â ")


def _frontmatter_degraded(meta):
    """True when a translation's frontmatter looks machine-generated, not authored."""
    name = (meta.get("name") or "").strip()
    desc = (meta.get("description") or "").strip()
    if not name:
        return True
    if _SLUG_NAME_RX.match(name):
        return True
    if name.startswith("Translation:") and name.endswith("…"):
        return True
    if desc in ("", "Translation document."):
        return True
    return False


def _has_mojibake(text):
    """True when text carries classic double-encoded UTF-8 sequences."""
    return any(seq in (text or "") for seq in _MOJIBAKE_SEQS)


def _is_slug_title(title):
    """True when a title looks machine-generated (filename slug) rather than authored.

    Covers the shapes the shared-memory frontmatter normalizer produces: a bare
    date-prefixed filename slug (with or without hyphens), a name truncated with
    a trailing ellipsis, or a Title-Cased filename-derived phrase.
    """
    t = (title or "").strip()
    if not t:
        return True
    if t.endswith("…") or t.endswith("..."):
        return True
    if _SLUG_TITLE_RX.match(t):
        return True
    words = t.split()
    if (len(words) >= 3 and all(w[:1].isupper() for w in words)
            and not re.search(r"[,:;()—–]", t)):
        return True
    return False


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
    # strip parenthetical code suffixes: "French (fr)" -> "French"
    lang = re.sub(r"\s*\([a-z]{2}\)\s*$", "", lang, flags=re.I).strip()
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
        print("WARN: living-library not found; will only scan AFLinks/translations/ for orphans")
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
    # Cloud-safe: LL may be a projection without database/ (sources only).
    # Fall back to the previous feed's values so counts don't zero out.
    db_root = os.path.join(LL, "database") if LL else None
    if db_root and os.path.isdir(db_root):
        tax = load_json(os.path.join(db_root, "taxonomy/taxonomy.json"))
        researchers = load_json(os.path.join(db_root, "entities/researcher-index.json"))
        persons = load_json(os.path.join(db_root, "persons/person-index.json"))
        patents = load_json(os.path.join(db_root, "patents/patent-index.json"))
        concept = load_json(os.path.join(db_root, "taxonomy/concept-map.json"))
    else:
        tax = prev_feed.get("taxonomy", {})
        researchers = prev_feed.get("researchers", {})
        persons = prev_feed.get("persons", {})
        patents = prev_feed.get("patents", {})
        concept = prev_feed.get("concept_map", {})

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
    # in the master index (index_shards/ via index_io). This is the number the
    # site's stats band shows ("Researchers"): an honest, derived figure that
    # tracks the whole archive, where the cataloged table is the curated subset.
    researcher_count = researcher_count_cataloged
    try:
        import index_io
        idx = index_io.load()
        seen = set()
        for e in idx:
            p = (e.get("primary_person") or "").strip()
            if p and not re.match(r"^[\d\s]+$", p):
                seen.add(p)
        if seen:
            researcher_count = len(seen)
    except Exception as exc:
        print(f"WARN: could not scan master index for distinct authors: {exc}")
    # Prefer the archive count, but never regress below the cataloged table.
    researcher_count = max(researcher_count, researcher_count_cataloged)

    # Patent count: prefer living-library DB, fall back to site patents.json, then index.json
    patent_count = patents.get("total_patents", len(patents.get("patents", {})))
    if patent_count == 0:
        # Fall back to site patents.json (generated by build_patents_index.py)
        site_patents = load_json(os.path.join(AFLINKS, "patents.json"))
        if site_patents and site_patents.get("_meta", {}).get("count"):
            patent_count = site_patents["_meta"]["count"]
            print(f"  Patent count from patents.json: {patent_count}", flush=True)
        else:
            # Last resort: count from index.json directly
            idx_path = os.path.join(AFLINKS, "index.json")
            if os.path.isfile(idx_path):
                idx = load_json(idx_path)
                if isinstance(idx, list):
                    patent_count = sum(1 for d in idx if d.get("patent_numbers"))
                    print(f"  Patent count from index.json: {patent_count}", flush=True)

    feed["library"] = {
        "researchers": researcher_count,
        "researchers_cataloged": researcher_count_cataloged,
        "patents": patent_count,
        "categories": len(tax.get("categories", {})),
        "meta_categories": len(tax.get("meta_categories", {})),
        "aflinks_docs": tax.get("aflinks_total_docs"),
        "translations": 0,
        "pages_translated": 0,
        "declassified_finds": 0,
        "active_agents": 0,
    }

    # Never-regress guard: a degraded run (LL database not found) computes
    # zeros for these counts. The previous feed's published values are the
    # floor — a rebuild must never zero out a live counter (2026-09-15
    # incident: "zero meta-categories and zero categories" on the HUD).
    _prev_lib = prev_feed.get("library", {}) if isinstance(prev_feed, dict) else {}
    for _k in ("researchers", "researchers_cataloged", "patents", "categories",
               "meta_categories", "aflinks_docs"):
        _prev_v = _prev_lib.get(_k)
        if not feed["library"].get(_k) and _prev_v:
            print(f"WARN: library.{_k} computed empty; keeping previous value "
                  f"{_prev_v} (degraded run guard)", flush=True)
            feed["library"][_k] = _prev_v

    # Degraded-run consistency: the guard above can restore
    # researchers_cataloged (e.g. 1138) while "researchers" was computed from
    # the archive scan alone (e.g. 999) — publishing researchers <
    # researchers_cataloged is incoherent. Re-apply the same floor the live
    # path uses: researchers is never below researchers_cataloged.
    if feed["library"].get("researchers_cataloged") and \
            feed["library"].get("researchers", 0) < feed["library"]["researchers_cataloged"]:
        print(f"WARN: library.researchers {feed['library']['researchers']} < "
              f"researchers_cataloged {feed['library']['researchers_cataloged']}; "
              f"raising researchers to the cataloged floor (degraded run guard)",
              flush=True)
        feed["library"]["researchers"] = feed["library"]["researchers_cataloged"]

    # --- 1b. Atsyukovsky book set (preserved PDFs + translation progress) ---
    books_dir = os.path.join(AFLINKS, "books", "atsyukovsky")
    ats_dir = os.path.join(LL, "sources", "atsyukovsky") if LL else None
    bookset = []
    book5_pages = 0
    if os.path.isdir(books_dir) and ats_dir and os.path.isdir(ats_dir):
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

    # --- 1c. Radiesthesia book set (scanned from disk; survives rebuilds) ---
    # 2026-09-14 (Drunvalo): radiesthesia_books used to be appended by hand to
    # library_feed.json and was silently wiped on every rebuild by this script.
    # Generate it from books/radiesthesia/** on disk instead. md5s are cached
    # in books/radiesthesia/.md5-cache.json so the rebuild stays fast.
    rad_root = os.path.join(AFLINKS, "books", "radiesthesia")
    rad_cache_path = os.path.join(rad_root, ".md5-cache.json")
    rad_cache = {}
    try:
        if os.path.isfile(rad_cache_path):
            with open(rad_cache_path, encoding="utf-8") as f:
                rad_cache = json.load(f)
    except Exception:
        rad_cache = {}
    rad_books = []
    prev_rad = (prev_feed or {}).get("radiesthesia_books", [])
    if not os.path.isdir(rad_root):
        # 2026-09-15: sparse-checkout sandbox excludes books/radiesthesia (2.7GB
        # of PDFs) to fit the 10GB disk. The files live in git + GitHub Pages;
        # preserve the previous feed's entries instead of zeroing the set.
        if prev_rad:
            print(f"  WARN: no books/radiesthesia/ dir on this machine (sparse checkout); preserving previous entries ({len(prev_rad)})", flush=True)
        rad_books = prev_rad
    else:
        rad_dirty = False
        for author_slug in sorted(os.listdir(rad_root)):
            adir = os.path.join(rad_root, author_slug)
            if not os.path.isdir(adir):
                continue
            for fname in sorted(os.listdir(adir)):
                p = os.path.join(adir, fname)
                if not os.path.isfile(p):
                    continue
                mtime = int(os.path.getmtime(p))
                size = os.path.getsize(p)
                key = f"{author_slug}/{fname}"
                cached = rad_cache.get(key)
                if cached and cached.get("mtime") == mtime and cached.get("size") == size:
                    h = cached["md5"]
                else:
                    import hashlib as _hl
                    with open(p, "rb") as fh:
                        h = _hl.md5(fh.read()).hexdigest()
                    rad_cache[key] = {"mtime": mtime, "size": size, "md5": h}
                    rad_dirty = True
                title = os.path.splitext(fname)[0].replace("_", " ").strip()
                rad_books.append({
                    "title": title,
                    "author": author_slug.replace("-", " ").title(),
                    "pdf": f"books/radiesthesia/{author_slug}/{fname}",
                    "size_mb": round(size / 1e6, 1),
                    "md5": h,
                    "provenance": "proton-drive-share-Physical-Radiesthesia (via Chris, 2026-09-14)",
                })
        if rad_dirty or not os.path.isfile(rad_cache_path):
            try:
                with open(rad_cache_path, "w", encoding="utf-8") as f:
                    json.dump(rad_cache, f)
            except Exception as e:
                print(f"  WARN: could not write radiesthesia md5 cache: {e}", flush=True)
    feed["radiesthesia_books"] = rad_books

    # --- 2. Latest translations (counted as distinct WORKS, not files) ---
    # Revision passes re-publish the same document under new dated filenames;
    # group by normalized title and keep the newest revision per work so the
    # counter and the list never claim more than is truly translated.
    tdir = os.path.join(LL, "translations") if LL else None
    translations_outdir = os.path.join(AFLINKS, "translations")
    translation_works = []
    translation_files = 0
    # Previously published titles keyed by filename — used to keep an authored
    # title when the shared frontmatter has been flattened to a slug (2026-09-16).
    prev_trans_titles = {}
    if isinstance(prev_feed, dict):
        for _t in prev_feed.get("latest_translations") or []:
            if isinstance(_t, dict) and _t.get("file"):
                prev_trans_titles[_t["file"]] = _t.get("title") or ""
    translations_skipped = 0
    pages_translated = book5_pages
    if tdir and os.path.isdir(tdir):
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
            # Fallback: derive language from filename suffix (-fr, -ru, etc.)
            if not lang:
                m = re.search(r"[_-](fr|de|ru|es|it|el|pt|pl|cs|sr|uk|ar|nl|ja|zh)\.md$", fname, re.I)
                if m:
                    lang = LANG_NAMES.get(m.group(1).lower(), m.group(1).upper())
            # Normalize to full names ("French", not "FR") so filters group cleanly
            lang = _lang_label(lang)
            # Target language: default English, override from frontmatter
            target_lang = meta.get("target_language") or meta.get("Target Language") or "English"
            target_lang = _lang_label(target_lang)
            # Title cleanup: if title looks like a filename or garbage, derive from filename
            garbage_patterns = [
                r"^\d{4}-\d{2}-\d{2}-",  # filename with date prefix
                r"^Skip to main",
                r"^Link to (Facebook|X|YouTube|Instagram)",
                r"^Link to ",
                r"^ACADEMY OF TRINITARIANISM",
                r"^Chercheurs Du Vrai",
                r"^WO\d+",
                r"^\d+\.\s+\*\*",  # numbered bold title from list
            ]
            title_clean = title
            if any(re.match(p, title or "") for p in garbage_patterns):
                # Derive from filename: strip date prefix and language suffix
                base = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", fname)
                base = re.sub(r"[_-](fr|de|ru|es|it|el|pt|pl|cs|sr|uk|ar|nl|ja|zh)\.md$", "", base, flags=re.I)
                base = re.sub(r"\.md$", "", base)
                base = re.sub(r"[\s_-]+(fr|de|ru|es|it|el|pt|pl|cs|sr|uk|ar|nl|ja|zh)$", "", base, flags=re.I)
                title_clean = re.sub(r"[-_]+", " ", base).strip().title()
            # Keep the previously published authored title when the shared
            # frontmatter has flattened this file's name into a bare filename
            # slug (the memfs-normalization pass). Never-regress, 2026-09-16.
            _prev_title = prev_trans_titles.get(fname) or ""
            if _is_slug_title(title_clean) and _prev_title \
                    and not _is_slug_title(_prev_title):
                title_clean = _prev_title
            # Copy the newest revision into the site repo so the page can serve it
            # — but never clobber an existing published copy with a worse source
            # (degraded frontmatter or a mojibake body). 2026-09-16.
            dst = os.path.join(translations_outdir, fname)
            try:
                if os.path.exists(dst) and (_frontmatter_degraded(meta)
                                            or _has_mojibake(body)):
                    translations_skipped += 1
                else:
                    import shutil
                    shutil.copy2(path, dst)
            except Exception as e:
                print(f"  WARN: could not copy translation {fname}: {e}", flush=True)
            translation_works.append({
                "date": fname[:10],
                "title": title_clean,
                "domain": domain,
                "source_url": src,
                "language": lang,
                "target_language": target_lang,
                "file": fname,
                "content_file": f"translations/{fname}",
                "excerpt": body.strip()[:220],
            })
    # --- 2a. Orphaned translations in AFLinks not yet in living-library ---
    # Files published directly to AFLinks/translations/ (by Forge, Sandra, Drunvalo)
    # bypass the living-library source and never enter the feed. Scan for orphans.
    if os.path.isdir(translations_outdir):
        feed_files = {tw["file"] for tw in translation_works}
        for path in sorted(glob.glob(os.path.join(translations_outdir, "*.md"))):
            fname = os.path.basename(path)
            if fname in feed_files:
                continue
            # Orphan found — parse and add to feed
            meta, title, body = parse_md_frontmatter(path)
            key = _norm_key(title or fname)
            domain = meta.get("Domain") or meta.get("domain") or ""
            src = meta.get("Source URL") or meta.get("source_url") or ""
            lang = meta.get("source_language") or meta.get("Language") or meta.get("language") or ""
            if not lang:
                m = re.search(r"[_-](fr|de|ru|es|it|el|pt|pl|cs|sr|uk|ar|nl|ja|zh)\.md$", fname, re.I)
                if m:
                    lang = LANG_NAMES.get(m.group(1).lower(), m.group(1).upper())
            lang = _lang_label(lang)
            target_lang = meta.get("target_language") or meta.get("Target Language") or "English"
            target_lang = _lang_label(target_lang)
            title_clean = title
            garbage_patterns = [
                r"^\d{4}-\d{2}-\d{2}-",
                r"^Skip to main",
                r"^Link to (Facebook|X|YouTube|Instagram)",
                r"^Link to ",
                r"^ACADEMY OF TRINITARIANISM",
                r"^Chercheurs Du Vrai",
                r"^WO\d+",
                r"^\d+\.\s+\*\*",
            ]
            if any(re.match(p, title or "") for p in garbage_patterns):
                base = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", fname)
                base = re.sub(r"[_-](fr|de|ru|es|it|el|pt|pl|cs|sr|uk|ar|nl|ja|zh)\.md$", "", base, flags=re.I)
                base = re.sub(r"\.md$", "", base)
                base = re.sub(r"[\s_-]+(fr|de|ru|es|it|el|pt|pl|cs|sr|uk|ar|nl|ja|zh)$", "", base, flags=re.I)
                title_clean = re.sub(r"[-_]+", " ", base).strip().title()
            translation_works.append({
                "date": fname[:10],
                "title": title_clean,
                "domain": domain,
                "source_url": src,
                "language": lang,
                "target_language": target_lang,
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
    # ALSO: use a multilingual concept dictionary to catch cross-language
    # matches that title-token matching misses (e.g., "ondes de forme" vs "form waves").
    CONCEPT_KEYWORDS = {
        "Schauberger / Vortex": [
            "schauberger", "vortex", "wirbel", "tourbillon", "remolino", "tromba",
            "implosion", "negentropy", "negentropic", "wasserwirbler", "hydroelectric",
            "suction turbine", "jet turbine", "dynamic hydroelectric",
        ],
        "Torsion Fields": [
            "torsion", "torsion", "torsion", "shipov", "akimov",
            "spinor", "торсион", "torsionsfeld", "champ de torsion",
        ],
        "Scalar Field / Potential": [
            "scalar", "scalaire", "skalar", "скаляр", "potential field",
            "longitudinal wave", "non-hertzian",
        ],
        "Ether / Aether": [
            "ether", "aether", "äther", "éther", "эфир", "eter", "eter",
            "etherodynamics", "эфиродинамика", "étherodynamique",
        ],
        "LENR / Cold Fusion": [
            "lenr", "cold fusion", "fusion froide", "kalte fusion",
            "холодный синтез", "low-energy nuclear",
        ],
        "Form Waves / Morphic Fields": [
            "form wave", "ondes de forme", "onde di forma", "ondas de forma",
            "morphic", "morphique", "morphisch", "formative", "formative field",
        ],
        "Sacred Geometry": [
            "sacred geometry", "geometria sacra", "géométrie sacrée",
            "geometría sagrada", "heilige geometrie", "geometric",
        ],
        "Goethean Science": [
            "goethe", "goethean", "goethéen", "goetheano", "goetheanisch",
            "phenomenological science", "qualitative science",
        ],
        "Water Structure / Memory": [
            "water memory", "eau mémoire", "wasser gedächtnis", "agua memoria",
            "pollack", "fourth phase", "ez water", "exclusion zone",
            "del giudice", "acqua viva",
        ],
        "Gravity / Ether Gravity": [
            "gravity", "gravité", "schwerkraft", "gravedad", "гравитация",
            "magnitsky", "compressible ether",
        ],
    }
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
        m = re.search(r"\((FR|DE|RU|ES|IT|EL|PT|JA|ZH|PL|CS|SR|UK|AR|NL)\s*→", hay, re.I)
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
    # Helper: get source language code for a translation work
    def _src_lang(tw):
        l = norm_lang(tw.get("language") or "")
        if l:
            # map full name to code
            return next((c for c, n in LANG_NAMES.items() if n.lower() == l.lower()), l.lower()[:2])
        # fallback: derive from filename suffix
        m = re.search(r"[_-](fr|de|ru|es|it|el|pt|pl|cs|sr|uk|ar|nl|ja|zh)\.md$", tw.get("file") or "", re.I)
        if m:
            return m.group(1).lower()
        return ""

    # Step 1: concept-based clustering
    concept_of = {}  # file -> set of canonical concepts
    for tw in translation_works:
        hay = ((tw.get("title") or "") + " " + (tw.get("excerpt") or "") + " " + (tw.get("domain") or "")).lower()
        concepts = set()
        for canon, kws in CONCEPT_KEYWORDS.items():
            for kw in kws:
                if kw.lower() in hay:
                    concepts.add(canon)
                    break
        concept_of[tw["file"]] = concepts

    # Group works by concept, then by different source languages
    concept_groups = {}  # concept -> list of works
    for tw in translation_works:
        for c in concept_of.get(tw["file"], []):
            concept_groups.setdefault(c, []).append(tw)

    # For each concept with ≥2 different source languages, create a bridge
    seen_bridge_domains = set()
    for concept_name, tws in concept_groups.items():
        langs = set(_src_lang(tw) for tw in tws if _src_lang(tw))
        if len(langs) < 2:
            continue
        # Use concept name as domain
        domain = concept_name
        if domain in seen_bridge_domains:
            continue
        seen_bridge_domains.add(domain)
        bridges.append({
            "domain": domain,
            "langs": sorted(langs),
            "works": sorted(tws, key=lambda t: t["date"], reverse=True),
        })

    # Step 2: token-based clustering (fallback for works not caught by concepts)
    meta_of = {}
    for tw in translation_works:
        meta_of[tw["file"]] = " ".join([tw.get("domain") or "", tw.get("excerpt") or ""][:1])
    tok_of = {}
    for tw in translation_works:
        tok_of[tw["file"]] = _title_tokens(tw["title"])
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
            code = next((c for c, n in LANG_NAMES.items() if n.lower() == norm_lang(l)), l)
            if code and code not in langs:
                langs.append(code)
        if len(langs) < 2:
            continue
        tok_sets = [tok_of[tw["file"]] for tw in tws]
        shared_toks = set.intersection(*tok_sets) if tok_sets else set()
        if not shared_toks:
            shared_toks = set.union(*tok_sets)
        subject = " ".join(sorted(shared_toks)[:3]).title() or tws[0].get("domain") or tws[0]["title"]
        # Skip if already covered by concept bridge (exact or substring match)
        if subject in seen_bridge_domains or any(
            subject.lower() in d.lower() or d.lower() in subject.lower()
            for d in seen_bridge_domains
        ):
            continue
        seen_bridge_domains.add(subject)
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
    sdir = os.path.join(LL, "sources") if LL else None
    if sdir and os.path.isdir(sdir):
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
    docs = []
    try:
        with open(os.path.join(AFLINKS, "index.json"), encoding="utf-8") as f:
            docs = json.load(f)
    except Exception:
        # index.json may be absent on sparse clones; the shard loader sees
        # the same catalog (bake_stats already uses it).
        try:
            import index_io
            docs = index_io.load()
        except Exception as exc:
            print(f"  WARN: no index for archive count: {exc}", flush=True)
    if docs:
        feed["library"]["archive_entries"] = len(docs)
        mc = {}
        for d in docs:
            for m in (d.get("meta_categories") or []):
                if m:
                    mc[m] = mc.get(m, 0) + 1
        feed["library"]["meta_counts"] = mc
    else:
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
        # Navigator reports through the public repo too — same pattern.
        "navigator": os.path.join(AFLINKS, "navigator", "status.json"),
        # Watchtower reports through the public repo too — same pattern.
        "watchtower": os.path.join(AFLINKS, "watchtower", "status.json"),
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
    feed["activity_log"] = parse_activity_log(os.path.join(LL, "ACTIVITY-LOG.md")) if LL else []
    local_activity = parse_activity_log(os.path.join(AFLINKS, "drunvalo", "ACTIVITY.md"))
    local_activity += parse_activity_log(os.path.join(AFLINKS, "synthesist", "ACTIVITY.md"))
    local_activity += parse_activity_log(os.path.join(AFLINKS, "scout", "ACTIVITY.md"))
    local_activity += parse_activity_log(os.path.join(AFLINKS, "forge", "ACTIVITY.md"))
    local_activity += parse_activity_log(os.path.join(AFLINKS, "navigator", "ACTIVITY.md"))
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
    d_roots = ([LL] if LL else []) + [os.path.join(AFLINKS, "sources"), AFLINKS]
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
            "href": "./library.html#translationsSection",
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

    # --- 9c. Daily drawers — the rotating strip beside Today's Salvage --------
    # Chris: "one pic from each category — one of the Declassified things, one
    # of the translated things, one of the newly found things, one of the rare
    # items, and something random. Something that rotates daily."
    # Seeded by the date so it is stable all day and turns over at midnight
    # even with no rebuild (the page re-picks client-side too).
    import hashlib
    seed = int(hashlib.sha256(today.encode("utf-8")).hexdigest()[:12], 16)

    def _pick(seq):
        return seq[seed % len(seq)] if seq else None

    def _flat(s, n=170):
        """First real prose from a markdown-ish excerpt.

        Harvested translation records carry the raw head of the file: a
        front-matter block, a "Link to Facebook / X / YouTube" chrome line, and
        a metadata bullet list, all before any prose. Showing that as the teaser
        reads like a database dump, so drop those and keep the first sentence.
        """
        s = s or ""
        s = re.sub(r"^\s*---\s*\n.*?\n---\s*\n", "", s, flags=re.S)
        keep = []
        for ln in s.split("\n"):
            t = ln.strip()
            if not t or t in ("---", "***", "___"):
                continue
            if re.match(r"^[-*]?\s*\*\*[a-z_]+\*\*\s*:", t, re.I):
                continue                      # - **date:** ...
            if re.match(r"^(link to |share |follow us|tweet|pin it|subscribe)", t, re.I):
                continue                      # social chrome
            if len(t) < 25:
                continue                      # nav fragments
            keep.append(t)
        s = " ".join(keep)
        s = re.sub(r"^[#>\-*\s]+", "", s)
        return re.sub(r"\s+", " ", s).strip()[:n]

    # Skip previews that are still site navigation. The preview cleaner is
    # working through the archive; until it finishes, a random draw can land on
    # a page whose text is still a menu, which reads as a broken card.
    try:
        import content_extract as _ce

        def _readable(t):
            return bool(t) and _ce.chrome_score(t) < 2
    except Exception:
        def _readable(t):
            return bool(t)

    def _doc_href(x):
        return "./pages/%08d.html" % int(x["id"]) if x.get("id") is not None else ""

    drawers = []

    # 1. Declassified — a newly opened record
    d = _pick(feed.get("declassified") or [])
    if d:
        drawers.append({
            "drawer": "declassified", "label": "Declassified",
            "title": d.get("title") or "", "excerpt": _flat(d.get("description")),
            "meta": (d.get("country") or "").title(), "rarity": "newly opened",
            "href": "./library.html#declass-" + _declass_slug(d.get("file")),
        })

    # 2. Translated — a work brought into English
    t = _pick(feed.get("latest_translations") or [])
    if t:
        ln = _lang_label(t.get("language"))
        drawers.append({
            "drawer": "translated", "label": "Translated",
            "title": t.get("title") or "", "excerpt": _flat(t.get("excerpt")),
            "meta": ln or "translation",
            "rarity": ("fresh from " + ln) if ln else "fresh translation",
            "href": "./library.html#trans-" + (t.get("file") or ""),
        })

    # 3. Newly found — a scout find
    # only finds that carry a description — a card with an empty teaser reads
    # as broken, and some scout records are title-only
    finds = [(f, s.get("date", "")) for s in (feed.get("latest_finds") or [])
             for f in (s.get("finds") or []) if (f.get("description") or "").strip()]
    f, fdate = (_pick(finds) or (None, ""))
    if f:
        drawers.append({
            "drawer": "found", "label": "Newly found",
            "title": f.get("title") or "", "excerpt": _flat(f.get("description")),
            "meta": fdate or "recent", "rarity": "scout find",
            "href": f.get("url") or "./library.html",
        })

    # 4. Rare — a document from one of the rarest source archives in the
    #    collection. "Rare" is a checkable claim about the collection, not a
    #    value judgement: the host contributed almost nothing else.
    #    (sargoytchev_zenodo 1 doc, merlib.lackluster.org 1, iscmns_org 2.)
    if docs:
        _counts = {}
        for x in docs:
            _s = x.get("source_site") or ""
            if _s:
                _counts[_s] = _counts.get(_s, 0) + 1
        _rarest = sorted(_counts, key=lambda k: _counts[k])[:12]
        _rare_pool = [x for x in docs
                      if x.get("source_site") in _rarest and _readable(x.get("content_preview"))]
        r = _pick(_rare_pool)
        if r:
            _host = r.get("source_site") or ""
            drawers.append({
                "drawer": "rare", "label": "Rare",
                "title": r.get("title") or r.get("filename") or "",
                "excerpt": _flat(r.get("content_preview")),
                "meta": _host.replace("_", "."),
                "rarity": "1 of %d from this host" % _counts.get(_host, 1),
                "href": _doc_href(r),
            })

    # 5. Random — anything with a readable preview
    _pool = [x for x in docs
             if _readable(x.get("content_preview")) and (x.get("title") or x.get("filename"))]
    q = _pick(_pool)
    if q:
        drawers.append({
            "drawer": "random", "label": "Random",
            "title": q.get("title") or q.get("filename") or "",
            "excerpt": _flat(q.get("content_preview")),
            "meta": (q.get("source_site") or "").replace("_", "."),
            "rarity": "drawn at random", "href": _doc_href(q),
        })

    feed["daily_drawers"] = {"as_of": today, "seed": seed, "drawers": drawers}

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
    yard_outdir = os.path.join(AFLINKS, "synthesis")

    def _yard_dir(sub):
        """Find a Replication Yard folder, preferring the shared living-library
        copy and falling back to this repo's own copy.

        Why the fallback exists: the Yard used to be read ONLY from
        living-library. When that shared repo is not attached to the machine
        running the build (a sandbox, a fresh clone, a worker agent), every
        folder lookup returned None and the Yard silently emptied — quests,
        dossiers and validations went to [] even though the files sit right
        here in AFLinks. A rebuild must never regress the Yard to empty just
        because a shared projection is missing. Returns (path, from_shared).

        2026-09-16: the shared folder being *present* is not enough — it can
        exist while carrying no records (e.g. living-library/synthesis/
        validations/ holds only README.md + quarantine/ after submissions were
        routed to human review, while the published Replication Watch records
        live in this repo). Preferring an empty shared folder blanked the
        published Yard. So prefer shared only when it actually has a non-README
        .md record; otherwise fall back to this repo's copy.
        """
        def _has_records(d):
            if not os.path.isdir(d):
                return False
            return any(os.path.basename(p).lower() != "readme.md"
                       for p in glob.glob(os.path.join(d, "*.md")))

        if LL:
            shared = os.path.join(LL, "synthesis", sub)
            if _has_records(shared):
                return shared, True
        return os.path.join(yard_outdir, sub), False

    qdir, q_shared = _yard_dir("quest-queue")
    if os.path.isdir(qdir):
        os.makedirs(os.path.join(yard_outdir, "quest-queue"), exist_ok=True)
        for path in sorted(glob.glob(os.path.join(qdir, "*.md")), reverse=True):
            base = os.path.basename(path)
            if base.lower() == "readme.md":
                continue
            # Copy to the site repo so the read button works. Skip when the
            # source IS the destination (guards shutil SameFileError).
            if q_shared:
                try:
                    import shutil
                    shutil.copy2(path, os.path.join(yard_outdir, "quest-queue", base))
                except Exception as e:
                    print(f"  WARN: could not copy quest {base}: {e}", flush=True)
            meta, title, body = parse_md_frontmatter(path)
            # pull a rough status from body for cheap front-end filtering
            status = "proposed"
            # Quest cards write "**Status:** proposed" — the old regex required
            # no space after the bold marker, so it never matched and every
            # quest silently rendered as "proposed". See 2026-09-19 note.
            m = re.search(r"[Ss]tatus:[ \t]*\*{0,2}[ \t]*(proposed|approved|merged|rejected)", body)
            if m:
                status = m.group(1)
            practical["quests"].append({
                "file": f"synthesis/quest-queue/{base}",
                "date": base[:10],
                "title": title,
                "status": status,
                "excerpt": (body.strip()[:200] or ""),
            })
    rdir, r_shared = _yard_dir("replication")
    if os.path.isdir(rdir):
        os.makedirs(os.path.join(yard_outdir, "replication"), exist_ok=True)
        for path in sorted(glob.glob(os.path.join(rdir, "*.md")), reverse=True):
            base = os.path.basename(path)
            # Copy to the site repo (skipped when source == destination)
            if r_shared:
                try:
                    import shutil
                    shutil.copy2(path, os.path.join(yard_outdir, "replication", base))
                except Exception as e:
                    print(f"  WARN: could not copy dossier {base}: {e}", flush=True)
            meta, title, body = parse_md_frontmatter(path)
            status = "draft"
            # Dossiers write "**Status:** protocol" (space before the value);
            # the old regex demanded a word char immediately after the bold
            # marker, so all 28 dossiers rendered as "draft". Fixed 2026-09-19.
            m = re.search(r"Status:[ \t]*\*{0,2}[ \t]*([\w\-]+)", body)
            if m:
                status = m.group(1)
            practical["dossiers"].append({
                "file": f"synthesis/replication/{base}",
                "date": base[:10],
                "title": title,
                "status": status,
                "excerpt": (body.strip()[:200] or ""),
            })
    vdir, v_shared = _yard_dir("validations")
    if os.path.isdir(vdir):
        os.makedirs(os.path.join(yard_outdir, "validations"), exist_ok=True)
        for path in sorted(glob.glob(os.path.join(vdir, "*.md")), reverse=True):
            base = os.path.basename(path)
            if base.lower() == "readme.md":
                continue
            # Copy to the site repo (skipped when source == destination)
            if v_shared:
                try:
                    import shutil
                    shutil.copy2(path, os.path.join(yard_outdir, "validations", base))
                except Exception as e:
                    print(f"  WARN: could not copy validation {base}: {e}", flush=True)
            meta, title, body = parse_md_frontmatter(path)
            practical["validations"].append({
                "file": f"synthesis/validations/{base}",
                "date": base[:10],
                "title": title,
                "excerpt": (body.strip()[:200] or ""),
            })
    practical["queue_url"] = f"synthesis/quest-queue/"
    # Never-regress guard: if every source folder was missing this run
    # (fresh clone, detached shared memory), inherit the previous feed's
    # Yard instead of publishing an empty pavilion.
    _prev_prac = prev_feed.get("practical") if isinstance(prev_feed, dict) else None
    if _prev_prac and not (practical["quests"] or practical["dossiers"]
                           or practical["validations"]):
        if _prev_prac.get("quests") or _prev_prac.get("dossiers") \
                or _prev_prac.get("validations"):
            print("WARN: Replication Yard computed empty; keeping previous "
                  "feed's Yard (degraded run guard)", flush=True)
            practical = _prev_prac
    feed["practical"] = practical
    feed["library"]["practical_quests"] = len(practical["quests"])
    feed["library"]["replication_dossiers"] = len(practical["dossiers"])
    feed["library"]["validations"] = len(practical["validations"])

    # --- 8. Daily deltas (24h HUD) ---
    # Maintain daily_counts.json: a per-build snapshot of the totals that
    # matter to visitors. The HUD compares today's snapshot against the
    # most recent snapshot that is >= 24h old, so "last 24 hours" stays
    # honest even when builds run more often than daily (or skip days).
    daily_path = os.path.join(AFLINKS, "daily_counts.json")
    lib_now = feed.get("library", {})
    snapshot = {
        "ts": feed.get("generated_at") or "",
        "docs": lib_now.get("archive_entries"),
        "translations": lib_now.get("translations"),
        "pages_translated": lib_now.get("pages_translated"),
        "declassified": lib_now.get("declassified_finds"),
        "researchers": lib_now.get("researchers"),
        "patents": lib_now.get("patents"),
    }
    history = []
    try:
        with open(daily_path, encoding="utf-8") as f:
            history = json.load(f)
        if not isinstance(history, list):
            history = []
    except Exception:
        history = []
    try:
        from datetime import timedelta

        def _ts(entry):
            try:
                return datetime.fromisoformat(str(entry.get("ts", "")))
            except Exception:
                return None

        now_dt = _ts(snapshot)
        # Keep the history small: last 30 snapshots.
        history = [h for h in history if isinstance(h, dict) and h.get("ts")]
        # Replace any snapshot from the same calendar day, then append.
        day_key = str(snapshot.get("ts", ""))[:10]
        history = [h for h in history if str(h.get("ts", ""))[:10] != day_key]
        history.append(snapshot)
        history = history[-30:]
        # Baseline: newest snapshot at least 24h old; if history is younger
        # than that (fresh machine, new history file), fall back to the
        # oldest snapshot so the strip still shows real growth — the
        # frontend labels the window honestly from the baseline ts.
        baseline = None
        if now_dt:
            cutoff = now_dt - timedelta(hours=24)
            for h in reversed(history[:-1]):
                h_dt = _ts(h)
                if h_dt and h_dt <= cutoff:
                    baseline = h
                    break
        if baseline is None and len(history) > 1:
            baseline = history[0]
        deltas = {}
        if baseline:
            for k in ("docs", "translations", "pages_translated", "declassified", "researchers", "patents"):
                a, b = snapshot.get(k), baseline.get(k)
                if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                    deltas[k] = max(0, int(a) - int(b))
        feed["daily"] = {
            "as_of": snapshot.get("ts"),
            "baseline": baseline.get("ts") if baseline else None,
            "deltas": deltas,
        }
        with open(daily_path, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    except Exception as exc:
        print(f"  WARN: daily deltas skipped: {exc}", flush=True)
        feed["daily"] = {"as_of": None, "baseline": None, "deltas": {}}

    # Never-regress guards for list sections: these are all read from the shared
    # living-library projection (or other machine-local sources). On a machine
    # where that projection is missing — a fresh clone, a sandbox, a worker
    # agent — they compute *shorter* lists, which silently shrinks live sections
    # of the page (the same bug class as the Replication Yard emptying). A
    # degraded run must never publish a smaller list than the previous feed:
    # inherit the previous published value whenever the new one is empty OR
    # shorter. (2026-09-16: Navigator saw latest_finds shrink 125 -> 64 on a
    # sandbox rebuild with no living-library attached.)
    if isinstance(prev_feed, dict):
        for _k in ("latest_finds", "domains", "top_researchers",
                   "declassified", "agents", "activity_log"):
            _old = prev_feed.get(_k)
            _new = feed.get(_k)
            if _old and (not _new or len(_new) < len(_old)):
                why = "empty" if not _new else f"shrank {len(_new)} < {len(_old)}"
                print(f"WARN: feed.{_k} computed {why}; keeping previous "
                      f"({len(_old)} items, degraded run guard)", flush=True)
                feed[_k] = _old

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