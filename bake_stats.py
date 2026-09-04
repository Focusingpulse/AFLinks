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
import re
import sys
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
        "researchers": researchers,
        "researchers_cataloged": lib.get("researchers_cataloged", researchers),
        "patents": patents,
        "categories": categories,
        "translations": translations,
        "pages_translated": pages_translated,
        "generated_at": generated_at,
        "note": "Derived from index.json + library_feed.json by bake_stats.py. Raw HTML carries these numbers too. 'researchers' = distinct named authors in the archive; 'researchers_cataloged' = curated researcher records.",
    }
    (ROOT / "stats.json").write_text(
        json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"stats.json -> {docs} docs, {translations} translations, {pages_translated} pages")

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
            new_html, n = pat.subn(
                lambda m: m.group(1) + format(int(value), ",") + m.group(2), html
            )
            return new_html, n

        for span_id, value in [
            ("heroDocCount", docs),
            ("heroTransCount", translations),
            ("heroPagesCount", pages_translated),
            ("statTotal", docs),
            ("noscriptCount", docs),
        ]:
            html, n = bake_span(html, span_id, value)
            if n:
                print(f"{page}: baked #{span_id} = {int(value):,}")

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

    if not changed:
        print("No HTML changes needed (already baked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())