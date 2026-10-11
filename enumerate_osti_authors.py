#!/usr/bin/env python3
"""
enumerate_osti_authors.py — OSTI.gov author-query + phrase expansion for the
scout growth engine. Complements the 20:15Z first harvest (4 on-lane title
queries -> 46 records) with author-name queries (LENR scientists' DOE
footprints) and fresh phrase queries, paginated deeper.

Output: appends {"url", "filename"} entries to osti_gov_filelist.json
(only genuinely new, on-lane, fulltext-bearing records).
"""
import json, os, re, sys, time, urllib.request, urllib.parse, html as html_module

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILELIST = os.path.join(SCRIPT_DIR, "osti_gov_filelist.json")
OUT = os.path.join(SCRIPT_DIR, "osti_enum_candidates.json")

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
API = "https://www.osti.gov/api/v1/records"

AUTHORS = [
    "Edmund Storms", "Michael McKubre", "Peter Hagelstein", "Martin Fleischmann",
    "Stanley Pons", "Steven Jones", "Thomas Claytor", "Melvin Miles",
    "Pamela Mosier-Boss", "Xing Li", "Yasuhiro Iwamura", "Tadahiko Mizuno",
    "Akito Takahashi", "Francesco Celani", "Yoshiaki Arata", "George Miley",
    "Mahadeva Srinivasan", "John Dash", "David Nagel", "Mitchell Swartz",
    "Dennis Cravens", "Antonella De Ninno", "Vittorio Violante", "Frank Gordon",
    "Robert Bush", "Graham Hubler", "Lawrence Forsley", "John Bockris",
    "Jan Marwan", "Stanley Szpak", "Irving Dardik", "Scott Chubb",
    "Allan Widom", "Lewis Larsen", "Joseph Zawodny", "William Tuszynski",
]
PHRASES = [
    '"excess heat" deuterium', '"anomalous heat" palladium',
    '"deuterated palladium"', '"palladium deuterium"',
    '"metal deuterides"', '"lattice confinement fusion"',
    '"tritium" "deuterated metals"', '"electrochemically loaded" palladium',
    '"nuclear reactions in condensed matter"', '"cold fusion"',
    '"low energy nuclear reactions"', '"condensed matter nuclear science"',
    '"D2O" electrolysis heat', '"hydrogen loading" nickel heat',
]

STRONG = [
    "cold fusion", "low energy nuclear", "lenr", "l-enr", "l enr",
    "excess heat", "excess power", "anomalous heat", "anomalous power",
    "anomalous energy", "anomalous effect", "condensed matter nuclear",
    "lattice confinement", "deuterated", "deuteride", "tritium",
    "fleischmann", "mckubre", "hagelstein", "iwamura", "mizuno", "miley",
    "szpak", "mosier", "claytor", "letts", "dardik", "swartz", "arata",
]
WEAK = [
    "palladium", "deuterium", "electrolysis", "electrolytic", "d2o",
    "deuteron", "nickel-hydrogen", "transmutation", "hydrogen loading",
    "deuterium loading",
]
NEG = [
    "heavy-ion", "superheavy", "super-heavy", "oganesson", "seaborgium",
    "dubnium", "nihonium", "fission", "nuclear structure", "octupole",
    "scintillator", "radiotherapy", "radiopharm", "radioisotope",
    "isotope production", "isotope separation", "isotope exchange",
    "enrichment", "medical", "inertial confinement", "tokamak", "iter",
    "jet fusion", "stellarator", "laser fusion", "cross section",
    "nuclear data", "neutron scattering", "materials science",
    "radiation damage", "pairing dynamics", "battery", "electrolyte",
    "lithium-ion", "photovoltaic", "solar cell", "hurricane",
    "storm surge", "precipitation", "climate", "resilience", "fuel cell",
    "catalyst", "catalysis", "zeolite", "hydrogen storage",
    "hydrogen embrittlement", "hydride storage", "nuclear waste",
    "accelerator mass", "hadron", "quark", "gluon", "dark matter",
    "neutrino", "cosmology", "dosimetry", "therapy", "neutron generator",
    "magnetron", "klystron", "fuel cycle", "reactor physics", "criticality",
    "shielding", "dose", "plasma", "betavoltaic", "zircaloy", "getter",
    "fuel retention", "containment vessel", "superconductor",
    "elastic recoil", "differential scanning",
]


def clean(s):
    return re.sub(r"\s+", " ", html_module.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip().lower()


def fetch_page(q, per_page, page):
    url = API + "?" + urllib.parse.urlencode({"q": q, "per_page": per_page, "page": page})
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8", errors="replace"))
    except Exception as e:
        print(f"  API-ERR page {page}: {e}", flush=True)
        return None


def on_lane(record):
    title = clean(record.get("title", ""))
    desc = clean(record.get("description", ""))
    text = title + " " + desc
    # fulltext required
    ft = [l.get("href", "") for l in record.get("links", []) if l.get("rel") == "fulltext"]
    if not ft or "/servlets/purl/" not in ft[0]:
        return None
    # reject off-lane
    if any(n in text for n in NEG):
        return None
    # strong on-lane signal, OR two weak signals (e.g. palladium+electrolysis)
    hit = any(s in text for s in STRONG)
    if not hit:
        weak_hits = sum(1 for w in WEAK if w in text)
        if weak_hits < 2:
            return None
    return ft[0]


def main():
    fl = json.load(open(FILELIST, encoding="utf-8"))
    have = {e["url"] for e in fl}
    print(f"existing osti filelist: {len(fl)}", flush=True)

    # archive url set for dedupe
    sys.path.insert(0, SCRIPT_DIR)
    import index_io
    arch_urls = index_io.url_set()
    print(f"archive urls: {len(arch_urls)}", flush=True)

    cands, seen = [], set()
    queries = [(a, 0) for a in AUTHORS] + [(p, 1) for p in PHRASES]
    for q, is_phrase in queries:
        max_pages = 8 if is_phrase else 3
        for page in range(1, max_pages + 1):
            recs = fetch_page(q, 20, page)
            if not recs:
                break
            if len(recs) == 0:
                break
            got_any = True
            for r in recs:
                ft = on_lane(r)
                if not ft:
                    continue
                if ft in have or ft in seen:
                    continue
                if ft in arch_urls:
                    continue
                seen.add(ft)
                pid = ft.rstrip("/").split("/")[-1]
                cands.append({
                    "url": ft,
                    "filename": f"{pid}.pdf",
                    "title": clean(r.get("title", "")),
                    "product_type": r.get("product_type", ""),
                    "authors": (r.get("authors") or [""])[0][:60],
                    "pub_date": str(r.get("publication_date", ""))[:10],
                    "query": q,
                })
            # stop early if page returned fewer than per_page (last page)
            if len(recs) < 20:
                break
            time.sleep(0.4)
        print(f"  {q[:45]:45s} pages done, cum cands {len(cands)}", flush=True)
        time.sleep(0.5)

    print(f"\nTOTAL candidates: {len(cands)}", flush=True)
    json.dump(cands, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    # append to filelist
    n = 0
    for c in cands:
        fl.append({"url": c["url"], "filename": c["filename"]})
        n += 1
    json.dump(fl, open(FILELIST, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"appended {n} to {FILELIST} (now {len(fl)} entries)", flush=True)


if __name__ == "__main__":
    main()
