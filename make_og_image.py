#!/usr/bin/env python3
"""make_og_image.py — regenerate og-image.png (1200x630 social share card).

WHY THIS EXISTS
---------------
The first card (2026-09-09) was built with a throwaway heredoc PIL script that
was never saved, so nothing could regenerate it. It froze at "52,676 documents
/ 35,989 with full-text previews" while the archive passed 106,000, and the
treasure-chest motif sat on top of the first line of body text.

This script is the durable replacement. Re-run it whenever the headline numbers
move enough to matter:

    python3 make_og_image.py            # writes og-image.png
    python3 make_og_image.py --check    # print live stats vs the labels below

NOTE: `*.png` is gitignored (.gitignore line 13). og-image.png is TRACKED, so
`git add -A` stages a modification normally — but a fresh copy would need
`git add -f`. Do not "fix" the gitignore.

DESIGN RULES
------------
* Wording is deliberately STABLE, not live: "100,000+" and a whole percent stay
  true for months, so the card does not need regenerating every day. Do not
  swap in an exact document count — that is what made the first card stale.
* `--check` is the guard: it prints the live numbers so a human can see whether
  the labels below have drifted out of honesty.
* Palette is sampled from the live site CSS (:root in index.html), not invented.
"""

import argparse
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

# --- headline labels (the only things that need editing) --------------------
DOCS_LABEL = "100,000+"          # stays true until 200,000
PREVIEW_PCT = "91%"              # whole percent; re-check when it moves 1pt

# --- palette (sampled from the live card + site :root) ----------------------
BG = (11, 15, 20)          # #0b0f14
HATCH = (22, 28, 36)       # #161c24
FRAME = (201, 154, 88)     # #c99a58
FRAME_INNER = (60, 48, 28)  # #3c301c
GOLD = (232, 182, 76)      # #e8b64c
GOLD_BRIGHT = (255, 209, 102)  # #ffd166
CREAM = (235, 225, 205)    # #ebe1cd
MUTED_GOLD = (201, 154, 88)  # #c99a58
DIM = (138, 155, 174)      # #8a9bae
FOOTER_DIM = (90, 107, 125)  # #5a6b7d
CHEST_FILL = (92, 64, 22)  # #5c4016

W, H = 1200, 630
FRAME_INSET = 24
FRAME_W = 3
INNER_INSET = 36
HATCH_STEP = 60
HATCH_PHASE = 59           # matches the original card's hatch alignment
HATCH_W = 3

FONT_DIR = os.environ.get("OG_FONT_DIR", "/tmp/fonts")
FONT = os.path.join(FONT_DIR, "Montserrat.ttf")
FONT_ITALIC = os.path.join(FONT_DIR, "Montserrat-Italic.ttf")

# Montserrat is OFL-licensed. Fetched on demand rather than vendored, so the
# repo carries no font binaries and a fresh sandbox can still rebuild the card.
FONT_URLS = {
    "Montserrat.ttf":
        "https://raw.githubusercontent.com/google/fonts/main/ofl/montserrat/Montserrat%5Bwght%5D.ttf",
    "Montserrat-Italic.ttf":
        "https://raw.githubusercontent.com/google/fonts/main/ofl/montserrat/Montserrat-Italic%5Bwght%5D.ttf",
}


def ensure_fonts():
    import urllib.request
    os.makedirs(FONT_DIR, exist_ok=True)
    for name, url in FONT_URLS.items():
        path = os.path.join(FONT_DIR, name)
        if not os.path.exists(path):
            print(f"fetching {name} ...")
            urllib.request.urlretrieve(url, path)


def font(size, weight="Regular", italic=False):
    path = FONT_ITALIC if italic else FONT
    if not os.path.exists(path):
        sys.exit(f"missing font {path} — set OG_FONT_DIR to a dir holding "
                 f"Montserrat.ttf / Montserrat-Italic.ttf")
    f = ImageFont.truetype(path, size)
    try:
        f.set_variation_by_name(weight)
    except Exception:
        pass  # static font: fall back to its default weight
    return f


def draw_hatch(d):
    """45-degree '/' lines: x + y = c, matching the original card."""
    for c in range(HATCH_PHASE, W + H, HATCH_STEP):
        # clip the segment to the canvas
        x0, y0 = max(0, c - H), min(H, c)
        x1, y1 = min(W, c), max(0, c - W)
        d.line([(x0, y0), (x1, y1)], fill=HATCH, width=HATCH_W)


def draw_frame(d):
    d.rectangle([FRAME_INSET, FRAME_INSET, W - 1 - FRAME_INSET, H - 1 - FRAME_INSET],
                outline=FRAME, width=FRAME_W)
    d.rectangle([INNER_INSET, INNER_INSET, W - 1 - INNER_INSET, H - 1 - INNER_INSET],
                outline=FRAME_INNER, width=1)


def draw_plus(d, cx, cy, arm, color, w=2):
    d.line([(cx - arm, cy), (cx + arm, cy)], fill=color, width=w)
    d.line([(cx, cy - arm), (cx, cy + arm)], fill=color, width=w)


def draw_crosshair(d, cx, cy, r, color, w=2):
    """Surveyor's mark: a ring with four ticks crossing it."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=w)
    tick = int(r * 1.7)
    d.line([(cx - tick, cy), (cx + tick, cy)], fill=color, width=w)
    d.line([(cx, cy - tick), (cx, cy + tick)], fill=color, width=w)


def draw_chest(d, cx, cy, w, h):
    """Treasure chest: domed lid, gold outline, lid seam and latch. Brand motif.

    Pillow 9.4 has no per-corner radii, so the lid and body are two rounded
    rectangles overlapped to hide the join, then the seam is redrawn on top.
    """
    x0, y0, x1, y1 = cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2
    lid_h = int(h * 0.44)
    seam = y0 + lid_h
    # lid first, then the body overlaps its lower edge
    d.rounded_rectangle([x0, y0, x1, seam], radius=lid_h // 2,
                        fill=CHEST_FILL, outline=GOLD, width=5)
    d.rounded_rectangle([x0, seam - 16, x1, y1], radius=10,
                        fill=CHEST_FILL, outline=GOLD, width=5)
    # lid seam + latch straddling it
    d.line([(x0 + 4, seam), (x1 - 4, seam)], fill=GOLD, width=4)
    lw, lh = int(w * 0.17), int(h * 0.26)
    d.rounded_rectangle([cx - lw // 2, seam - lh // 2, cx + lw // 2, seam + lh // 2],
                        radius=4, fill=GOLD)
    d.ellipse([cx - 5, seam - 3, cx + 5, seam + 7], fill=CHEST_FILL)


def build(out_path):
    ensure_fonts()
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    draw_hatch(d)

    # --- decorative marks (kept clear of every text baseline) ---------------
    draw_plus(d, 430, 92, 13, GOLD)
    draw_plus(d, 726, 158, 13, GOLD)
    draw_crosshair(d, 1010, 372, 15, GOLD)
    draw_plus(d, 872, 486, 11, GOLD)
    draw_plus(d, 1128, 500, 11, GOLD)

    # --- treasure chest, top right (the first card had this over the text) --
    draw_chest(d, 1042, 150, 150, 124)

    # --- title --------------------------------------------------------------
    f_title = font(74, "ExtraBold")
    d.text((90, 160), "AETHERFORCE", font=f_title, fill=GOLD_BRIGHT, anchor="ls")
    d.text((90, 242), "TREASURE VAULT", font=f_title, fill=GOLD_BRIGHT, anchor="ls")

    # --- headline stats: big gold number + smaller cream label --------------
    f_num = font(46, "ExtraBold")
    f_lab = font(28, "Medium")
    for baseline, num, label in ((330, DOCS_LABEL, " primary-source documents"),
                                 (382, PREVIEW_PCT, " with full-text previews")):
        d.text((90, baseline), num, font=f_num, fill=GOLD_BRIGHT, anchor="ls")
        nw = d.textlength(num, font=f_num)
        d.text((90 + nw + 14, baseline), label, font=f_lab, fill=CREAM, anchor="ls")

    # --- caption / tagline / url / footer -----------------------------------
    d.text((90, 428), "Cross-linked to Aetherforce — search, browse, translate.",
           font=font(24), fill=DIM, anchor="ls")
    d.text((90, 490), "The archive is the map; the treasure is the people.",
           font=font(27, "Medium", italic=True), fill=MUTED_GOLD, anchor="ls")
    d.text((90, 548), "focusingpulse.github.io/AFLinks",
           font=font(30, "Bold"), fill=GOLD_BRIGHT, anchor="ls")
    d.text((90, 582), "Living Library · translations · paradigm lenses",
           font=font(19), fill=FOOTER_DIM, anchor="ls")

    draw_frame(d)

    img.save(out_path, "PNG", optimize=True)
    return out_path


def stamp_version(png_path, html_name="index.html"):
    """Point og:image / twitter:image at og-image.png?v=<image content hash>.

    Social platforms cache a share card by URL, so replacing the PNG alone can
    leave the old card showing for days. The version is the image's own hash, so
    it changes exactly when the image changes — never on a rebuild that did not
    touch it, and never needs bumping by hand.
    """
    import hashlib
    import re

    digest = hashlib.sha256(open(png_path, "rb").read()).hexdigest()[:8]
    url = "https://focusingpulse.github.io/AFLinks/og-image.png"
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), html_name)
    if not os.path.exists(path):
        return None
    html = open(path, encoding="utf-8").read()
    new = re.sub(re.escape(url) + r"(\?v=[0-9a-f]+)?", url + "?v=" + digest, html)
    if new != html:
        open(path, "w", encoding="utf-8").write(new)
    return digest


def check():
    """Print live stats next to the labels, so drift is visible."""
    here = os.path.dirname(os.path.abspath(__file__))
    for cand in (os.path.join(here, "stats.json"),
                 os.path.join(here, "..", "stats.json")):
        if os.path.exists(cand):
            s = json.load(open(cand, encoding="utf-8"))
            docs, prev = s.get("docs"), s.get("docs_with_previews")
            pct = round(100 * prev / docs) if docs and prev else None
            print(f"live stats.json : {docs:,} docs, {prev:,} previews ({pct}%)")
            print(f"card labels     : {DOCS_LABEL} docs, {PREVIEW_PCT} previews")
            if docs and docs < 100_000:
                print("WARN: DOCS_LABEL overstates the archive")
            if pct is not None and abs(pct - int(PREVIEW_PCT.rstrip('%'))) > 1:
                print("WARN: PREVIEW_PCT is more than 1 point off — update it")
            return
    print("no stats.json found next to this script; labels not verified")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "og-image.png"))
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--no-stamp", action="store_true",
                    help="skip rewriting the ?v= hash into index.html")
    a = ap.parse_args()
    if a.check:
        check()
    else:
        print("wrote", build(a.out))
        if not a.no_stamp:
            v = stamp_version(a.out)
            if v:
                print(f"stamped og:image ?v={v} in index.html")
        check()
