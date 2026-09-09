#!/usr/bin/env python3
"""
build_doc_pages.py — generate static per-document pages for the vault.

Every document that carries a content_preview gets a stable, shareable URL:

    /docs/00005643.html

Each page is a tiny self-contained HTML file (~1-1.5KB) with shared CSS in
pages/style.css, baked title/description meta, the full preview, source link,
categories, and back-links (vault home + a same-category search). Docs without
previews get NO page yet — when previews land (weekly merges), the page
appears automatically on the next build.

Also writes:
  sitemap.xml  — all doc pages + main pages
  robots.txt   — allow all, sitemap pointer

Usage: python3 build_doc_pages.py [--all]
  --all  also emit pages for preview-less docs (thin catalog pages).
"""

import json
import os
import re
import sys
import html as htmlmod
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS_DIR = ROOT / "pages"
STYLE = """
body{background:#0b0f14;color:#d8d3c8;font-family:Georgia,'Times New Roman',serif;margin:0;padding:0;line-height:1.55}
.wrap{max-width:760px;margin:0 auto;padding:32px 20px 60px}
a{color:#ffd166;text-decoration:none}a:hover{text-decoration:underline}
.top{font-size:.85rem;color:#8a97a5;margin-bottom:26px}.top a{color:#ffd166}
h1{font-size:1.45rem;color:#ffd166;line-height:1.35;margin:0 0 10px}
.meta{font-size:.85rem;color:#8a97a5;margin-bottom:22px}
.preview{background:#131a22;border:1px solid #2a3440;border-left:3px solid #c99a58;padding:16px 18px;border-radius:6px;font-size:.98rem;color:#ded9ce;margin-bottom:24px;white-space:pre-wrap}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:24px}
.tag{background:#1d2731;color:#9db4c7;border:1px solid #2a3440;padding:3px 10px;border-radius:20px;font-size:.78rem}
.actions{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:28px}
.btn{background:#c99a58;color:#0b0f14;font-weight:bold;padding:9px 18px;border-radius:6px;font-size:.9rem}
.btn.ghost{background:transparent;color:#ffd166;border:1px solid #c99a58}
.ppl{font-size:.9rem;color:#aab6c2;margin-top:26px;border-top:1px solid #232e38;padding-top:16px}
"""


def esc(s):
    return htmlmod.escape(str(s), quote=True)


def load_index():
    with open(ROOT / "index.json", encoding="utf-8") as f:
        idx = json.load(f)
    return idx if isinstance(idx, list) else idx.get("entries", [])


def doc_url(doc_id):
    return f"/AFLinks/docs/{int(doc_id):08d}.html"


def render_page(doc, has_preview):
    did = int(doc["id"])
    title = (doc.get("title") or doc.get("filename") or "Untitled").strip()
    preview = doc.get("content_preview") or ""
    cats = doc.get("categories") or []
    metas = doc.get("meta_categories") or []
    src = doc.get("source_url") or ""
    person = doc.get("primary_person") or ""
    patents = doc.get("patent_numbers") or []
    date = doc.get("steiner_date") or ""

    if not preview:
        preview = "This document is cataloged but the full-text preview has not arrived yet — the harvest fleet is working through the archive."
    desc = preview[:300].replace("\n", " ") or title

    meta_tags = ""
    if person:
        meta_tags += f'<meta name="author" content="{esc(person)}">\n'
    if date:
        meta_tags += f'<meta name="citation_date" content="{esc(date)}">\n'
    for d in sorted(set(metas) | set(cats)):
        meta_tags += f'<meta name="keywords" content="{esc(d)}">\n'

    tags = "".join(f'<a class="tag" href="/AFLinks/?cat={esc(t)}">{esc(t)}</a>' for t in (metas + cats)[:8])
    cat_query = "+".join(re.sub(r"[^a-zA-Z0-9]", "+", c) for c in cats[:2]) or "Alternative+Physics"

    pat_line = f'<a href="https://patents.google.com/patent/{esc(patents[0])}" class="btn ghost">Patent {esc(patents[0])} →</a>' if patents else ""

    src_line = f'<a class="btn" href="{esc(src)}" target="_blank" rel="noopener">Open source →</a>' if src else ""

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} — Aetherforce Knowledge Vault</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc[:200])}">
<meta property="og:type" content="article">
<meta property="og:image" content="https://focusingpulse.github.io/AFLinks/og-image.png">
<meta name="robots" content="index,follow">
{meta_tags}<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="wrap">
  <div class="top">⚓ <a href="/AFLinks/">Aetherforce Knowledge Vault</a> · document #{did}</div>
  <h1>{esc(title)}</h1>
  <div class="meta">{('👤 ' + esc(person) + ' · ') if person else ''}{('📅 ' + esc(date)) if date else ''} · archived # {did:,}</div>
  <div class="preview">{esc(preview)}</div>
  <div class="actions">{src_line} {pat_line} <a class="btn ghost" href="/AFLinks/?q={esc(cat_query)}">Related documents →</a></div>
  <div class="tags">{tags}</div>
  <div class="ppl">The archive preserves claims; it does not certify them. Category/meta tags describe content, not truth. <a href="/AFLinks/methodology.html">Methodology</a></div>
</div>
</body>
</html>
"""
    return page


def write_css():
    (DOCS_DIR / "style.css").write_text(STYLE, encoding="utf-8")


def main():
    docs = load_index()
    all_flag = "--all" in sys.argv
    DOCS_DIR.mkdir(exist_ok=True)
    write_css()

    n = 0
    urls = []
    for doc in docs:
        pid = doc.get("content_preview")
        if not all_flag and not pid:
            continue
        out = DOCS_DIR / f"{int(doc['id']):08d}.html"
        out.write_text(render_page(doc, bool(pid)), encoding="utf-8")
        urls.append("https://focusingpulse.github.io" + doc_url(doc["id"]))
        n += 1
        if n % 5000 == 0:
            print(f"  {n} pages...")

    # sitemap.xml
    main_urls = [
        "https://focusingpulse.github.io/AFLinks/",
        "https://focusingpulse.github.io/AFLinks/library.html",
        "https://focusingpulse.github.io/AFLinks/translations.html",
        "https://focusingpulse.github.io/AFLinks/lens.html",
        "https://focusingpulse.github.io/AFLinks/synthesis.html",
        "https://focusingpulse.github.io/AFLinks/vault.html",
        "https://focusingpulse.github.io/AFLinks/stats.json",
    ]
    with open(ROOT / "sitemap.xml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u in main_urls + urls:
            f.write(f"  <url><loc>{esc(u)}</loc></url>\n")
        f.write("</urlset>\n")

    # robots.txt
    with open(ROOT / "robots.txt", "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\nSitemap: https://focusingpulse.github.io/AFLinks/sitemap.xml\n")

    print(f"done: {n} doc pages, {len(urls)} URLs in sitemap")


if __name__ == "__main__":
    main()