#!/usr/bin/env python3
"""
build_af_focus.py — the founding group's focus map.

Reads af_catalog.json (all 534 Aetherforce posts with dates, from the
founding group's own publishing history) and scores each of the vault's
24 meta-lenses + 44 subjects by how central it is to what Aetherforce
actually publishes. Writes af_focus.json consumed by index.html to:
  - order the Key Chest dial by founding-group focus (not raw doc count)
  - light gold stars on the lanes the founding group actually publishes in
  - add a "Founders' Focus" spin button (top focus lane)

Method: title + category keyword matching. Each lens/subject has a
vocabulary of terms drawn from the vault's own seam data + AF's own
category names. Count = number of AF posts (of 534) whose title or
categories match. Transparent, data-driven, rebuildable.
"""
import json, re, os
from collections import Counter

ROOT = os.path.dirname(os.path.abspath(__file__))

catalog = json.load(open(os.path.join(ROOT, "af_catalog.json")))

# --- vault taxonomy (24 lenses, from the feed seam) ---
feed = json.load(open(os.path.join(ROOT, "library_feed.json")))
lenses = list(feed["seam"]["category_index"].keys())
seam = feed["seam"]

# lens vocabularies: lens -> list of sub-category names
lens_vocab = {}
for lens in lenses:
    lens_vocab[lens] = seam.get("meta_cats", {}).get(lens, [])
# also add AF category names as lens vocabulary where they match subject names
# (AF uses the same language: Aether Physics, Goethe, Radionics, Geometry, Light, Magnetism, Tesla, Harmonics, Water, Biology...)

# --- AF category names —---
cats = {}
try:
    import urllib.request
    for page in (1, 2):
        url = f"https://www.aetherforce.energy/wp-json/wp/v2/categories?per_page=100&page={page}&_fields=id,name,count"
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'}), timeout=30) as r:
            for c in json.load(r):
                cats[c['id']] = c['name']
except Exception as e:
    print("warn: could not fetch AF categories:", e)

cat_name = lambda cid: cats.get(cid, '')

# case-insensitive term sets per lens: subject names + key AF category names
def norm(s):
    return re.sub(r'[^a-z]+', ' ', s.lower()).strip()

lens_terms = {}
for lens in lenses:
    terms = set()
    for sub in lens_vocab.get(lens, []):
        for w in norm(sub).split():
            terms.add(w)
    lens_terms[lens] = terms

# extra lens wisdom from AF's own categories
AF_CAT_TO_LENS = {
    "Aether Physics": ["Aether, Light & Electricity"],
    "Ethers": ["Aether, Light & Electricity"],
    "Counterspace": ["Aether, Light & Electricity", "Energy & Transportation"],
    "Radiant Energy": ["Energy & Transportation", "Aether, Light & Electricity"],
    "Goethe": ["Goethean & Anthroposophical Science"],
    "Goethean Morphology": ["Goethean & Anthroposophical Science", "Biological & Morphogenetic Science"],
    "Formative Forces": ["Goethean & Anthroposophical Science", "Biological & Morphogenetic Science"],
    "Anthroposophy": ["Goethean & Anthroposophical Science"],
    "Radionics": ["Radionics, Radiesthesia & Shape Power"],
    "Radiesthesia": ["Radionics, Radiesthesia & Shape Power"],
    "Shape Power": ["Radionics, Radiesthesia & Shape Power"],
    "Psychotronics": ["Radionics, Radiesthesia & Shape Power", "Transhumanism & Psychotronic Warfare"],
    "Borderland Research": ["Challenges to the Standard Model"],
    "Fallacies of Standard Model": ["Challenges to the Standard Model"],
    "Geometry": ["Sacred & Projective Geometry"],
    "Projective Geometry": ["Sacred & Projective Geometry"],
    "Consciousness": ["Biological & Morphogenetic Science"],
    "Life Force": ["Biological & Morphogenetic Science", "Aether, Light & Electricity"],
    "Light": ["Optics & Colour Therapy", "Aether, Light & Electricity"],
    "Magnetism": ["Aether, Light & Electricity", "Energy & Transportation"],
    "Tesla": ["Energy & Transportation", "Aether, Light & Electricity"],
    "Electric Universe": ["Plasma, Torsion & Cosmology", "Challenges to the Standard Model"],
    "Alchemy - Transmutation": ["Material Sciences & Alchemy"],
    "Vortex Science": ["Water Structure & Memory", "Plasma, Torsion & Cosmology"],
    "Harmonics": ["Harmonics, Rhythms & Cycles"],
    "Water": ["Water Structure & Memory"],
    "Biology": ["Biological & Morphogenetic Science"],
    "Electrobiology": ["Biological & Morphogenetic Science", "Aether, Light & Electricity"],
    "Walter Russell": ["Aether, Light & Electricity", "Sacred & Projective Geometry"],
    "Gerry Vassilatos": ["Aether, Light & Electricity"],
    "Michael Theroux": ["Aether, Light & Electricity", "Challenges to the Standard Model"],
}
for afcat, lenslist in AF_CAT_TO_LENS.items():
    for w in norm(afcat).split():
        for lens in lenslist:
            lens_terms.setdefault(lens, set()).add(w)

# --- score per lens ---
def title_cat_text(post):
    t = norm(post["title"])
    c = " ".join(norm(cat_name(cid)) for cid in post.get("cats", []))
    return t + " " + c

post_texts = [title_cat_text(p) for p in catalog]

lens_scores = {}
for lens in lenses:
    terms = lens_terms.get(lens, set())
    if not terms:
        lens_scores[lens] = 0
        continue
    cnt = 0
    for txt in post_texts:
        if any(t in txt for t in terms if len(t) > 2):
            cnt += 1
    lens_scores[lens] = cnt

# --- score per subject (sub-category) ---
sub_scores = Counter()
for post in catalog:
    c = " ".join(norm(cat_name(cid)) for cid in post.get("cats", []))
    t = norm(post["title"])
    txt = t + " " + c
    # match against all subject names in seam
for lens in lenses:
    for sub in lens_vocab.get(lens, []):
        words = [w for w in norm(sub).split() if len(w) > 2]
        if not words:
            continue
        cnt = sum(1 for txt2 in post_texts if any(w in txt2 for w in words))
        sub_scores[sub] += cnt

# --- output ---
focus = {
    "generated_at": "2026-09-02T16:10:00Z",
    "source": "af_catalog.json (534 Aetherforce posts, 2013-2024, incl. dates from founders' own archive)",
    "total_af_posts": len(catalog),
    "lenses": {l: lens_scores.get(l, 0) for l in sorted(lens_scores, key=lambda x: -lens_scores[x])},
    "subjects": {k: v for k, v in sub_scores.most_common()},
    "top_af_categories": [],
}
try:
    focus["top_af_categories"] = [{"name": n, "posts": c} for n, c in Counter(cat_name(cid) for p in catalog for cid in p.get("cats", []) if cid in cats).most_common(20)]
except Exception:
    pass

json.dump(focus, open(os.path.join(ROOT, "af_focus.json"), "w"), indent=1)
print("af_focus.json written")
print("\n=== LENS FOCUS (AF founding group's publishing focus) ===")
for lens, cnt in sorted(lens_scores.items(), key=lambda x: -x[1])[:24]:
    bar = "#" * (cnt // 8)
    print(f"  {cnt:3d} {bar:7s} {lens}")
print("\n=== TOP SUBJECTS ===")
for sub, cnt in sub_scores.most_common(20):
    print(f"  {cnt:3d}  {sub}")
