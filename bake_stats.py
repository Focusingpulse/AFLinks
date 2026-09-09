#!/usr/bin/env python3
"""
bake_stats.py — bake live archive stats into static HTML so the raw page
source carries the truth (no JS, no 16MB download needed).

What it does:
1. Reads index.json + library_feed.json (single source of truth).
2. Writes stats.json — a tiny agent/bot-friendly endpoint (~1KB).
3. Rewrites hardcoded counters in index.html / vault.html / lens.html
   (heroDocCount, heroTransCount, heroPagesCount, statTotal, noscriptCount).
4. Version-stamps the big data fetches (?v=<generated_at>) so browsers
   cache them long-term and any rebuild busts the cache. Also drops the
   `cache: 'no-store'` on versioned fetches (would defeat caching).

Idempotent: safe to re-run; only touches known patterns. Run it AFTER
build_library_feed.py + build_slim_index.py, BEFORE commit:
    python3 bake_stats.py
"""

import json
import random
import re
import sys
import html as html_mod
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# The big derived-data files that change on every merge — version these.
VERSIONED = [
    "./search_index.json",
    "./library_feed.json",
    "./full_manifest.json",
    "./synthesis/synthesis_index.json",
]

# Pages whose hero/stat counters get baked (also versioned-fetch + meta counts).
PAGES = ["index.html", "vault.html", "lens.html", "library.html", "synthesis.html"]


def load_json(name: str):
    with open(ROOT / name, encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    index = load_json("index.json")
    feed = load_json("library_feed.json")

    docs = len(index)
    docs_with_previews = sum(1 for d in index if d.get("content_preview"))
    lib = feed.get("library", {})
    translations = lib.get("translations", 0)
    pages_translated = lib.get("pages_translated", 0)
    researchers = lib.get("researchers", 0)
    patents = lib.get("patents", 0)
    categories = lib.get("categories", 0)
    generated_at = feed.get("generated_at", "")

    # URL-safe version stamp from the feed build timestamp.
    ver = re.sub(r"\D", "", str(generated_at))[:14] or "0"
    if len(ver) < 14:
        ver = ver.ljust(14, "0")

    stats = {
        "docs": docs,
        "docs_with_previews": docs_with_previews,
        "researchers": researchers,
        "researchers_cataloged": lib.get("researchers_cataloged", researchers),
        "patents": patents,
        "categories": categories,
        "translations": translations,
        "pages_translated": pages_translated,
        "generated_at": generated_at,
        "note": "Derived from index.json + library_feed.json by bake_stats.py. Raw HTML carries these numbers too. 'docs' = cataloged entries; 'docs_with_previews' = those carrying full-text content previews (the honest 'searchable' figure). 'researchers' = distinct named authors in the archive; 'researchers_cataloged' = curated researcher records.",
    }
    (ROOT / "stats.json").write_text(
        json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"stats.json -> {docs} docs ({docs_with_previews} with previews), {translations} translations, {pages_translated} pages")

    changed = False
    for page in PAGES:
        path = ROOT / page
        html = path.read_text(encoding="utf-8")
        orig = html

        # 1) Counter spans (exact ids only — never touch JS numbers).
        def bake_span(html, span_id, value):
            pat = re.compile(
                r"(<span\s+id=\"" + re.escape(span_id) + r"\">)[^<]*(</span>)"
            )

            def _sub(m):
                label = format(int(value), ",") if isinstance(value, (int, float)) and not isinstance(value, bool) else str(value)
                return m.group(1) + label + m.group(2)

            new_html, n = pat.subn(_sub, html)
            return new_html, n

        for span_id, value in [
            ("heroDocCount", docs),
            ("heroPreviewCount", docs_with_previews),
            ("heroTransCount", translations),
            ("heroPagesCount", pages_translated),
            ("statTotal", docs),
            ("noscriptCount", docs),
            ("lastUpdated", str(generated_at)[:10]),
        ]:
            html, n = bake_span(html, span_id, value)
            if n:
                print(f"{page}: baked #{span_id} = {value}")

        # 1b) Doc counts inside meta description / og:description content.
        for phrase in ("primary-source", "searchable primary-source"):
            html, n = re.subn(
                r'(content=")[0-9][0-9,]*( ' + re.escape(phrase) + r')',
                lambda m: m.group(1) + f"{docs:,}" + m.group(2),
                html,
            )
            if n:
                print(f"{page}: baked {n} meta count(s) for '{phrase}'")

        # 2) Versioned fetches + drop no-store on the big files.
        url_alt = "|".join(re.escape(u) for u in VERSIONED)
        # Already versioned? Re-stamp the value.
        html, n = re.subn(
            r"(?P<q>['\"])(" + url_alt + r")\?v=[0-9]+(?P=q)",
            lambda m: m.group("q") + m.group(2) + "?v=" + ver + m.group("q"),
            html,
        )
        if n:
            print(f"{page}: re-stamped {n} versioned fetch(es) -> v{ver}")
        # Fresh: append ?v=VER
        html, n = re.subn(
            r"(?P<q>['\"])(" + url_alt + r")(?P=q)",
            lambda m: m.group("q") + m.group(2) + "?v=" + ver + m.group("q"),
            html,
        )
        if n:
            print(f"{page}: versioned {n} fetch(es) -> v{ver}")
        # Drop `{ cache: 'no-store' }` from those fetches now that URLs are unique.
        html, n = re.subn(
            r"fetch\(\s*(['\"])((?:\./)(?:search_index|library_feed|full_manifest|synthesis/synthesis_index)\.json\?v=[0-9]+)\1\s*,\s*\{\s*cache:\s*'no-store'\s*\}\s*\)",
            r"fetch(\1\2\1)",
            html,
        )
        if n:
            print(f"{page}: dropped no-store on {n} versioned fetch(es)")

        if html != orig:
            path.write_text(html, encoding="utf-8")
            changed = True


    # 3) Today's Salvage — bake one random artifact card (seeded by date so it's
    #    stable per build day but rotates daily).
    day_seed = int(re.sub(r"\D", "", str(generated_at)[:10]) or 0)
    rng = random.Random(day_seed)
    pool = [d for d in index if d.get("content_preview") and (d.get("title") or d.get("filename"))]
    if pool:
        d = rng.choice(pool)
        title = html_mod.escape(d.get("title") or d.get("filename"))
        person = html_mod.escape(d.get("primary_person") or "")
        prev = html_mod.escape(d["content_preview"][:220])
        page = f"/AFLinks/pages/{int(d['id']):08d}.html"
        site = d.get("source_site") or ""
        site_label = "Rex Research" if site == "rexresearch_com" else (site.replace("_", ".") if site else "the archive")
        meta_cats = " · ".join(html_mod.escape(c) for c in (d.get("meta_categories") or [])[:2])
        card_html = f'''<a class="salvage-card" href="{page}">
    <span class="salvage-person">👤 {person}</span>
    <span class="salvage-doc-title">{title}</span>
    <span class="salvage-preview">{prev}…</span>
    <span class="salvage-meta">{site_label}{meta_cats and f" · {meta_cats}" or ""}</span>
</a>'''
        # Splice into index.html between markers
        idx_path = ROOT / "index.html"
        idx_html = idx_path.read_text(encoding="utf-8")
        marker_pat = re.compile(r"(<!--\s*SALVAGE:BEGIN\s*-->)(.*?)(<!--\s*SALVAGE:END\s*-->)", re.DOTALL)
        new_idx, n = marker_pat.subn(r"\1" + card_html + r"\3", idx_html)
        if n and new_idx != idx_html:
            idx_path.write_text(new_idx, encoding="utf-8")
            print(f"index.html: baked Today's Salvage -> {title[:50]}…")
        else:
            print("index.html: SALVAGE markers not found or no change.")
    else:
        print("No documents with previews — skipped salvage baking.")

    if not changed:
        print("No HTML changes needed (already baked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())