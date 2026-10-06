#!/usr/bin/env python3
"""Build a fleet-wide report index from every agent's published reports.

The Aetherforce fleet publishes narrative reports into the AFLinks repo from
multiple agents, each with its own folder and authoring convention:

  synthesis/            Drunvalo       deep synthesis briefings (kind=synthesis)
  paradigm/             The Connector  Paradigm Signal Reports (kind=paradigm-signal)
  sources/*scout-finds* Scooter        scout field/finds reports (kind=scout-finds)

Each report is parsed for: frontmatter description (teaser), H1 or name
(title), date, and the author/agent who wrote it. Attribution is read from
each file's own conventions — never assumed from the folder. The output is a
single JSON array, newest first, consumed by the home-page strip and
synthesis.html.

Usage:  python3 build_synthesis_index.py
Output: synthesis/synthesis_index.json
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "synthesis" / "synthesis_index.json"

# ─── Polar Ring lane derivation ──────────────────────────────────────────────
# Every briefing gets a position on the two-ring widget: which Founder lane
# (content band) and which Paradigm (lens band) it lives at. Method A derives
# the position by keyword-matching the report against hue_lexicon.json (shared
# with the widget). Method B — optional frontmatter tags — overrides, and is
# read here too so tagging works the day an author starts using it.
# Derivation reads what the report's author chose to frame with: title, teaser,
# sources. Body text is deliberately NOT read — a briefing body mentions every
# lane in the archive, so matching it would assign a position to everything and
# mean nothing. No match is an honest answer: the briefing still lists under
# "All", it simply has no junction yet.
HEAD_WEIGHTS = {"title": 3.0, "teaser": 2.0, "sources": 1.5}
LANE_MIN_SCORE = 2.0          # founder lane: one title hit, or two softer ones
PARADIGM_MIN_SCORE = 3.0      # paradigm: a rarer claim, so a higher bar
# Aliases this generic would fire on every report (the fleet literally calls its
# weekly reports "Paradigm Signal Report"), so they never count as lane evidence.
STOP_TERMS = {"paradigm", "dogma", "forgotten", "ignored", "analog", "conspiracy"}
# House-style title prefixes the fleet uses on every report of a kind.
KIND_PREFIX_RE = re.compile(r"^(paradigm signal report|synthesis report|scout finds?|fleet briefing)\s*[:\-—]\s*", re.IGNORECASE)

_LEXICON_CACHE = None


def norm_text(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def lane_lexicon():
    """{name: {hue, quality, keywords}} for meta-categories and paradigms."""
    global _LEXICON_CACHE
    if _LEXICON_CACHE is not None:
        return _LEXICON_CACHE

    meta, para = {}, {}
    lex_path = ROOT / "hue_lexicon.json"
    if lex_path.exists():
        lex = json.loads(lex_path.read_text(encoding="utf-8"))
        for name, rec in (lex.get("meta_categories") or {}).items():
            meta[name] = {
                "hue": rec.get("hue"),
                "color": rec.get("color", ""),
                "quality": rec.get("quality", ""),
                "keywords": list(rec.get("keywords") or []),
            }
        for name, rec in (lex.get("paradigms") or {}).items():
            # The paradigm ring is the eye — it reads against the content band,
            # so the band hue is the complement of the paradigm's own base hue.
            para[name] = {
                "hue": rec.get("band_hue", rec.get("hue")),
                "color": rec.get("band_color", rec.get("color", "")),
                "quality": rec.get("quality", ""),
                "keywords": list(rec.get("keywords") or []),
            }
        # Enrich paradigms with the curated aliases already in the taxonomy.
        concepts_path = ROOT / "taxonomy" / "concepts.json"
        if concepts_path.exists():
            try:
                concepts = json.loads(concepts_path.read_text(encoding="utf-8"))
                by_id = {rec["concept"]: name for name, rec in (lex.get("paradigms") or {}).items()
                         if rec.get("concept")}
                for c in concepts.get("concepts", []):
                    name = by_id.get(c.get("id"))
                    if not name:
                        continue
                    for alias in c.get("aliases", []):
                        if len(alias) > 4 and alias.lower() not in [k.lower() for k in para[name]["keywords"]]:
                            para[name]["keywords"].append(alias.lower())
            except Exception:
                pass

    _LEXICON_CACHE = (meta, para)
    return _LEXICON_CACHE


def score_lanes(fields, lexicon, weights):
    """Weighted keyword score per lane. fields: {field: normalized text}."""
    scores = {}
    for name, rec in lexicon.items():
        total = 0.0
        for kw in rec["keywords"]:
            k = norm_text(kw)
            if len(k) < 4 or k in STOP_TERMS:
                continue
            phrase_bonus = 1.0 + 0.5 * k.count(" ")   # multi-word terms are stronger
            for field, weight in weights.items():
                hay = fields.get(field, "")
                if not hay:
                    continue
                hits = hay.count(k)
                if hits:
                    total += weight * min(hits, 3) * phrase_bonus
        if total > 0:
            scores[name] = round(total, 2)
    return scores


def pick_lane(scores, minimum):
    """Best-scoring lane above the bar, or an honest None."""
    if scores:
        best = max(scores, key=lambda n: scores[n])
        if scores[best] >= minimum:
            return best, scores[best]
    return None, 0


def derive_lanes(fm, title, teaser, sources, body):
    """Return the lane position for one report.

    Tagged wins (method B); otherwise derived (method A). Unknown = None, which
    is honest: the briefing still lists under All, it just has no junction.
    """
    meta, para = lane_lexicon()
    # The house-style prefix ("Paradigm Signal Report:") is a label, not content.
    head_title = KIND_PREFIX_RE.sub("", title or "")
    head = {
        "title": norm_text(head_title),
        "teaser": norm_text(teaser),
        "sources": norm_text(sources),
    }

    tagged = bool(fm.get("founder_lane") or fm.get("paradigm") or fm.get("lens"))

    if fm.get("founder_lane") in meta:
        founder_lane, founder_hue = fm["founder_lane"], meta[fm["founder_lane"]]["hue"]
    else:
        founder_lane, _ = pick_lane(score_lanes(head, meta, HEAD_WEIGHTS), LANE_MIN_SCORE)
        founder_hue = meta[founder_lane]["hue"] if founder_lane else None

    if fm.get("paradigm") in para:
        paradigm, paradigm_hue = fm["paradigm"], para[fm["paradigm"]]["hue"]
    else:
        paradigm, _ = pick_lane(score_lanes(head, para, HEAD_WEIGHTS), PARADIGM_MIN_SCORE)
        paradigm_hue = para[paradigm]["hue"] if paradigm else None

    return {
        "founder_lane": founder_lane,
        "founder_hue": founder_hue,
        "paradigm": paradigm,
        "paradigm_hue": paradigm_hue,
        "lanes": [n for n in (founder_lane, paradigm) if n],
        "lane_source": "tagged" if tagged else "derived",
    }

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
DATE_RE = re.compile(r"^(20\d{2}-\d{2}-\d{2})")

# Author conventions, tried in order per file:
#   1. frontmatter "author:" field
#   2. "*Synthesis created by X ...*" footer (Drunvalo's older briefings)
#   3. "*Synthesis by X — date*" footer (Drunvalo's newer briefings)
#   4. "*By X — date*" (The Connector's paradigm reports)
#   5. "**Scout:** X" body line (Scooter's finds reports)
AUTHOR_PATTERNS = [
    re.compile(r"^author:\s*(.+)$", re.MULTILINE),
    re.compile(r"Synthesis\s+created\s+by\s+([A-Za-z][A-Za-z .'()\-]*)", re.MULTILINE),
    re.compile(r"Synthesis\s+by\s+([A-Za-z][A-Za-z .'()\-]*)", re.MULTILINE),
    re.compile(r"^\*?By\s+([A-Za-z][A-Za-z .'()\-]*?)\s*[—–-]\s*\d{4}", re.MULTILINE),
    re.compile(r"\*\*Scout:\*\*\s*([A-Za-z][A-Za-z .'()\-]*?)(?=\s*[—–-]|\s*$)", re.MULTILINE),
]

# Footer style: "*Sources: 5 translations, ...*" (NOT inline "**Source:** `file`")
SOURCES_SUMMARY_RE = re.compile(r"^\*(?!\*)\s*Sources?:\s*(?!`)(.+?)\*?\s*$", re.MULTILINE)
# Inline style: "**Source:** `translations/xxx.md`, `translations/yyy.md`"
SOURCE_REF_RE = re.compile(r"\*\*Sources?:\*\*\s*([^\n]+)")

# File globs per report kind, with the fleet agent behind them
SOURCES = [
    ("synthesis",   "synthesis",            "*.md"),
    ("paradigm-signal", "paradigm",         "*.md"),
    ("scout-finds", "sources",              "*scout-finds*.md"),
]


def parse_frontmatter(text):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    fm = m.group(1)
    out = {}
    name = re.search(r"^name:\s*(.+)$", fm, re.MULTILINE)
    if name:
        out["name"] = name.group(1).strip().strip('"')
    desc = re.search(r"^description:\s*(.+)$", fm, re.MULTILINE)
    if desc:
        out["description"] = desc.group(1).strip().strip('"')
    author = re.search(r"^author:\s*(.+)$", fm, re.MULTILINE)
    if author:
        out["author"] = author.group(1).strip().strip('"')
    date = re.search(r"^date:\s*(.+)$", fm, re.MULTILINE)
    if date:
        out["date"] = date.group(1).strip().strip('"')
    # Method B — optional lane tags. A report that carries these keeps them
    # instead of the derived position.
    for key in ("lens", "founder_lane", "paradigm", "hue"):
        m = re.search(rf"^{key}:\s*(.+)$", fm, re.MULTILINE)
        if m:
            out[key] = m.group(1).strip().strip('"')
    return out


def parse_report(path: Path, kind: str):
    text = path.read_text(encoding="utf-8", errors="replace")
    fm = parse_frontmatter(text)

    teaser = fm.get("description", "")
    title = ""
    m = H1_RE.search(text)
    if m:
        title = m.group(1).strip()
    if not title:
        title = fm.get("name", "")

    date = ""
    m = DATE_RE.match(path.name)
    if m:
        date = m.group(1)
    if not date:
        date = fm.get("date", "")

    author = ""
    for pat in AUTHOR_PATTERNS:
        m = pat.search(text)
        if m:
            author = m.group(1).strip()
            if author:
                break

    # Scout finds frontmatter names often carry the scout attribution
    if not author and kind == "scout-finds":
        name = fm.get("name", "")
        ms = re.search(r"Scout\s*\(([A-Za-z][A-Za-z .'()\-]*)\)", name)
        if ms:
            author = ms.group(1).strip()
    if not author and kind == "scout-finds":
        # "**Agent**: Drunvalo" header block (AetherForce Scout Report style)
        m = re.search(r"\*\*Agent\*\*:\s*([A-Za-z][A-Za-z .'()\-]*?)(?=\s*\n|$)", text)
        if m:
            author = m.group(1).strip()
    if not author and kind == "scout-finds":
        # "Scout (Scooter) 04:00 round..." in frontmatter description
        desc = fm.get("description", "")
        m = re.search(r"Scout\s*\(([A-Za-z][A-Za-z .'()\-]*)\)", desc)
        if not m:
            # "Scooter scout round" in frontmatter description
            m = re.search(r"([A-Za-z][A-Za-z .'()\-]*?)\s+scout round", desc, re.IGNORECASE)
        if m:
            author = m.group(1).strip()
    if not author and kind == "scout-finds":
        # "(Scooter)" in the H1 title
        m = re.search(r"\(([A-Za-z][A-Za-z .'()\-]*)\)", title)
        if m:
            author = m.group(1).strip()
    # Trim any trailing role/institution text captured by greedy patterns
    # e.g. "Drunvalo for the AetherForce Living Library." → "Drunvalo"
    author = re.sub(r"\s+for\s+.*$", "", author).rstrip(".").strip()

    # Distilled sources line: footer summary when present, else count of
    # distinct linked archive files.
    sources_summary = ""
    m = SOURCES_SUMMARY_RE.search(text)
    if m:
        sources_summary = m.group(1).strip().strip("*").strip()
    linked = set(re.findall(r"`([^`]+)`", " ".join(SOURCE_REF_RE.findall(text))))
    sources_count = sum(1 for p in linked if not p.startswith("http"))
    sources = sources_summary
    if not sources and sources_count:
        sources = f"{sources_count} source files linked"

    entry = {
        "file": path.name,
        "path": str(path.relative_to(ROOT)),
        "slug": path.stem,
        "kind": kind,
        "date": date,
        "title": title,
        "teaser": teaser,
        "author": author or "Unknown agent",
        "sources": sources,
        "sources_count": sources_count,
    }
    entry.update(derive_lanes(fm, title, teaser, sources, text))
    return entry


def main():
    entries = []
    for kind, folder, pattern in SOURCES:
        dirpath = ROOT / folder
        if not dirpath.exists():
            continue
        for path in sorted(dirpath.glob(pattern)):
            if path.name == "synthesis_index.json":
                continue
            entries.append(parse_report(path, kind))

    # newest first; stable tie-break by kind then slug
    entries.sort(key=lambda e: (e["date"], e["kind"], e["slug"]), reverse=True)
    OUT.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"build_synthesis_index: {len(entries)} reports -> {OUT.relative_to(ROOT)}")
    for e in entries[:6]:
        print(f"  [{e['kind']:>16}] {e['date']}  {e['author']:>12}  {e['title'][:52]}")

    # Polar Ring lane coverage — how many briefings landed on each axis.
    lanes = sum(1 for e in entries if e.get("founder_lane"))
    paradigms = sum(1 for e in entries if e.get("paradigm"))
    tagged = sum(1 for e in entries if e.get("lane_source") == "tagged")
    print(f"\nlane derivation: {lanes}/{len(entries)} founder lanes · "
          f"{paradigms}/{len(entries)} paradigms · {tagged} tagged")
    for e in entries[:14]:
        fl, pa = e.get("founder_lane") or "—", e.get("paradigm") or "—"
        print(f"  {(e['date'] or '          ')[:10]}  {fl[:34]:34s} × {pa[:44]}")


if __name__ == "__main__":
    sys.exit(main())