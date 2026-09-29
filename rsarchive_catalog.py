#!/usr/bin/env python3
"""
rsarchive_catalog.py — correct GA catalog builder for rsarchive.org.

Replaces crawl_rsarchive.py's do_catalog(), which had two defects:

  1. It matched only `href="/Lectures/GA053/"` (trailing slash required).
     On the real listing pages, most GA volumes appear as the slash-less
     number-cell link `href="/Lectures/GA053"`, so 186 volumes were never
     listed and therefore never harvested.

  2. It rebuilt the catalog from scratch each run, so newly-published
     volumes were only visible if someone happened to re-run it — and there
     was no record of WHAT changed.

This script parses the /Lectures/, /Books/ and /Articles/ tables row by row,
collects every GA reference in any href form, and records the per-row cycle
directories (the exact edition paths, e.g. /Lectures/GA051/English/UNK1970/).
Those cycle dirs are a better crawl seed than walking directories, because
the crawler's walk_index() has a depth limit of 2 that deeper nesting can
exceed.

Output (written into CWD, i.e. the AFLinks clone root):
  rsarchive_catalog.json       — superset; keeps the legacy `gas` shape so
                                 crawl_rsarchive.py keeps working, plus
                                 `cycles` and `sections` detail.
  rsarchive_catalog_delta.json — what changed vs the previous catalog:
                                 new GAs, newly gone GAs, new cycle dirs.
                                 This is the "are they still publishing?"
                                 watch.

Usage (from the AFLinks repo root):
  python3 rsarchive_catalog.py            # fetch + write catalog + delta
  python3 rsarchive_catalog.py --local    # parse saved copies instead of fetching

Politeness: rsarchive.org is a charity project. robots.txt asks
Crawl-delay: 1. This script fetches 3 listing pages, with 1s between them.
"""

import html
import json
import os
import re
import sys
import time
import urllib.request

BASE = "https://rsarchive.org"
SECTIONS = (("lectures", "/Lectures/"), ("books", "/Books/"), ("articles", "/Articles/"))
CATALOG = "rsarchive_catalog.json"
DELTA = "rsarchive_catalog_delta.json"
CRAWL_DELAY = 1.0
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

GA_RE = re.compile(r"^/(Lectures|Books|Articles)/(GA[0-9]+[a-zA-Z_]*)(?:/|$)")


def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*;q=0.8"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="ignore")


def strip_html(raw):
    body = re.sub(r"<script.*?</script>|<style.*?</style>", "", raw, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", body)
    return html.unescape(re.sub(r"\s+", " ", text)).strip()


def parse_listing(raw, section):
    """Return (gas_seen, cycles). One row = one lecture cycle / book edition."""
    gas_seen = set()
    cycles = []
    for row in re.findall(r"<tr[^>]*>(.*?)</tr>", raw, re.S):
        hrefs = re.findall(r'href="([^"]+)"', row)
        row_gas = set()
        deepest = None
        for h in hrefs:
            path = h
            if h.startswith("http"):
                # normalise absolute rsarchive links back to paths
                path = re.sub(r"^https?://(www\.)?rsarchive\.org", "", h)
            if not path.startswith("/"):
                continue
            m = GA_RE.match(path)
            if not m:
                continue
            ga = m.group(2)
            row_gas.add(ga)
            if len(path) > len(deepest or ""):
                deepest = path
        if not row_gas:
            continue
        gas_seen |= row_gas
        # row metadata: the text cells (title / year / count)
        cells = [strip_html(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)]
        cells = [c for c in cells if c]
        title = ""
        year = ""
        count = ""
        if len(cells) >= 2:
            # first cell is usually the GA number; the title is the longest text cell
            title = max(cells[1:3], key=len) if len(cells) >= 3 else cells[1]
        for c in cells:
            if re.fullmatch(r"(1[6-9]\d\d|20\d\d)([–-]\d{2,4})?", c):
                year = c
            elif c.isdigit():
                count = c
        if deepest:
            # normalise directory seeds to a trailing slash; keep .html links as-is
            seed = deepest if deepest.endswith(".html") else deepest.rstrip("/") + "/"
            cycles.append({
                "section": section,
                "ga": sorted(row_gas)[0],
                "url": BASE + seed,
                "title": title,
                "year": year,
                "lectures": count,
            })
    return gas_seen, cycles


def build(local=False):
    gas = {}          # legacy shape the existing crawler reads: ga -> {books, lectures, articles}
    sections = {}     # new: ga -> [sections]
    cycles = []
    live = {}
    for section, path in SECTIONS:
        try:
            if local:
                fn = f"listing_{section}.html"
                raw = open(fn, encoding="utf-8", errors="ignore").read()
            else:
                raw = fetch(BASE + path)
                with open(f"listing_{section}.html", "w", encoding="utf-8") as f:
                    f.write(raw)
                time.sleep(CRAWL_DELAY)
        except Exception as e:
            print(f"  {section}: fetch failed ({e})")
            continue
        seen, cyc = parse_listing(raw, section)
        live[section] = len(seen)
        print(f"  {section}: {len(seen)} GA volumes, {len(cyc)} cycle dirs")
        for ga in seen:
            gas.setdefault(ga, {})
            gas[ga][section] = gas[ga].get(section, 0) + 1
            sections.setdefault(ga, [])
            if section not in sections[ga]:
                sections[ga].append(section)
        cycles.extend(cyc)

    catalog = {
        "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source": BASE,
        "gas": gas,                     # legacy-compatible
        "sections": sections,           # new
        "cycles": cycles,               # new: authoritative crawl seed
        "counts": {"ga_total": len(gas), "cycles": len(cycles), "by_section": live},
    }
    return catalog


def diff(old, new):
    old_gas = set((old or {}).get("gas", {}).keys())
    new_gas = set(new["gas"].keys())
    old_cyc = {c["url"] for c in (old or {}).get("cycles", [])}
    new_cyc = {c["url"] for c in new.get("cycles", [])}
    return {
        "checked": new["generated"],
        "previous_catalog": (old or {}).get("generated"),
        "new_ga_volumes": sorted(new_gas - old_gas),
        "ga_volumes_no_longer_listed": sorted(old_gas - new_gas),
        "new_cycle_dirs": sorted(new_cyc - old_cyc),
        "total_ga": len(new_gas),
        "total_cycles": len(new_cyc),
    }


def main():
    local = "--local" in sys.argv
    old = None
    if os.path.exists(CATALOG):
        try:
            old = json.load(open(CATALOG, encoding="utf-8"))
        except Exception:
            old = None
    catalog = build(local=local)
    d = diff(old, catalog)
    with open(CATALOG, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=1)
    with open(DELTA, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)

    print(f"\ncatalog: {d['total_ga']} GA volumes, {d['total_cycles']} cycle dirs "
          f"-> {CATALOG}")
    if old is None:
        print("delta: no previous catalog (first run) -> " f"{DELTA}")
    else:
        print(f"delta vs {d['previous_catalog']}: "
              f"+{len(d['new_ga_volumes'])} new GA volumes, "
              f"+{len(d['new_cycle_dirs'])} new cycle dirs -> {DELTA}")
        if d["new_ga_volumes"]:
            print("  NEW VOLUMES: " + ", ".join(d["new_ga_volumes"]))
        if d["ga_volumes_no_longer_listed"]:
            print("  GONE FROM LISTING: " + ", ".join(d["ga_volumes_no_longer_listed"]))


if __name__ == "__main__":
    main()
