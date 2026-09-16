#!/usr/bin/env python3
"""
build_doc_pages.py — generate static per-document pages for the vault.

Every document that carries a content_preview gets a stable, shareable URL:

    /pages/00005643.html

Each page is a tiny self-contained HTML file (~1-1.5KB) with shared CSS in
pages/style.css, baked title/description meta, the full preview, source link,
categories, back-links (vault home + a same-category search), and — since
Phase 2 of the Master Directive — JSON-LD structured data (ScholarlyArticle)
plus lineage/contradiction links seeded from wrong-turn death certificates.

Docs without previews get NO page yet — when previews land (weekly merges),
the page appears automatically on the next build.

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
DC_DIR = ROOT / "synthesis" / "death-certificates"  # copied from living-library by build_library_feed.py
RG_FILE = ROOT / "synthesis" / "replication-guides.json"  # Open Lab replication guides [prescribed: Directive C]
IPFS_FILE = ROOT / "synthesis" / "ipfs-manifest.json"  # Phase 4 pinning manifest [prescribed: Directive B]
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
/* Share row [prescribed: virtual center component] */
.share{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:24px}
/* Lineage / death-certificate section [aesthetic: mirrors .preview styling] */
.lineage{background:#16131a;border:1px solid #3a2f40;border-left:3px solid #b06a9e;padding:16px 18px;border-radius:6px;font-size:.9rem;color:#cfc3d8;margin-bottom:24px}
.lineage h2{font-size:1rem;color:#e0b4d4;margin:0 0 8px}
.lineage .ev{margin:6px 0;padding-left:14px;border-left:2px solid #4a3a55}
.lineage .ev .d{color:#9e86b0;font-size:.8rem}
.lineage .st{display:inline-block;padding:2px 10px;border-radius:12px;font-size:.75rem;font-weight:bold;margin-bottom:8px}
.lineage .st.died{background:#3a1a24;color:#e08a8a}.lineage .st.suppressed{background:#2a1a3a;color:#b08ad0}
.lineage .st.continued{background:#1a2a1a;color:#8ad08a}.lineage .st.resurfaced{background:#2a2a1a;color:#d0c08a}
/* Open Lab [prescribed: Directive C] */
.openlab{background:#0f1a1c;border:1px solid #2a4a44;border-left:3px solid #6fc9b4;border-radius:6px;padding:16px 18px;margin-bottom:24px;font-size:.92rem;color:#cfded9}
.ol-tabs{display:flex;gap:8px;margin-bottom:12px;flex-wrap:wrap}
.ol-tab{background:#16262a;color:#9fc4b8;border:1px solid #2a4a44;padding:5px 14px;border-radius:20px;font-size:.8rem;cursor:pointer}
.ol-tab.on{background:#1c3a34;color:#8be0c8;border-color:#4a7a66}
.ol-meta{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:10px;align-items:center}
.ol-chip{background:#16262a;color:#9fc4b8;border:1px solid #2a4a44;padding:2px 10px;border-radius:12px;font-size:.75rem}
.rg-status{display:inline-block;padding:2px 10px;border-radius:12px;font-size:.75rem;font-weight:bold}
.rg-protocol{background:#1a2a3a;color:#8ab0d0}.rg-underway{background:#2a2a1a;color:#d0c08a}
.rg-replicated{background:#1a2a1a;color:#8ad08a}.rg-refuted{background:#3a1a24;color:#e08a8a}.rg-inconclusive{background:#2a2a1a;color:#c0b07a}
.rg-claim{font-size:.95rem;background:#0b1517;border:1px solid #1f3a36;padding:10px 12px;border-radius:4px;margin:0 0 12px}
.ol-subhead{font-size:.72rem;letter-spacing:1px;text-transform:uppercase;color:#7fa89c;margin:12px 0 6px;font-weight:700}
.rg-vars{display:flex;flex-direction:column;gap:5px}
.rg-row{display:flex;justify-content:space-between;gap:12px;padding:5px 8px;background:#0b1517;border:1px solid #1f3a36;border-radius:4px;font-size:.85rem}
.rg-var{color:#cfded9}.rg-mod{color:#6fc9b4;text-align:right;font-size:.8rem}
.rg-safety{font-size:.85rem;color:#b7c9c3}
.ol-log{margin-top:14px;padding-top:10px;border-top:1px solid #2a4a44}
.ol-log-label{color:#8be0c8;font-weight:bold;font-size:.9rem}
.ol-log-note{font-size:.8rem;color:#9fc4b8;margin:4px 0 8px}
/* Permanently Archived badge [prescribed: Directive B] */
.archived{display:flex;flex-wrap:wrap;gap:6px;align-items:center;background:#0e1a12;border:1px solid #2e4a34;border-left:3px solid #6fd08a;border-radius:6px;padding:8px 12px;margin-bottom:16px;font-size:.82rem;color:#cfe8d6}
.arch-badge{background:#1c3a24;color:#8be0a0;border:1px solid #3a5a44;padding:2px 10px;border-radius:12px;font-weight:bold;font-size:.78rem}
.arch-hash code{background:#0b1510;color:#8ad0a0;padding:1px 6px;border-radius:4px;font-size:.75rem}
.arch-cid a{color:#6fd08a}
.arch-gw{margin-left:auto;color:#6fd08a;font-size:.78rem}
"""


def esc(s):
    return htmlmod.escape(str(s), quote=True)


def load_index():
    import index_io
    return index_io.load()


def doc_url(doc_id):
    return f"/AFLinks/pages/{int(doc_id):08d}.html"


def load_death_certificates():
    """Load wrong-turn death certificates and build a doc_id -> lineage map.
    [prescribed: Master Directive B — contradiction links seeded from death certificates]"""
    dc_map = {}  # doc_id (int) -> list of certificate dicts
    if not DC_DIR.is_dir():
        return dc_map
    for p in sorted(DC_DIR.glob("*.json")):
        try:
            with open(p, encoding="utf-8") as f:
                cert = json.load(f)
        except Exception:
            continue
        if cert.get("schema") != "wrong-turn-death-certificate-v1":
            continue
        # map every archive doc in this lineage to this certificate
        for did in cert.get("archive_docs", []):
            try:
                dc_map.setdefault(int(did), []).append(cert)
            except (TypeError, ValueError):
                continue
        # also map numeric doc_ids appearing in lineage events
        for ev in cert.get("lineage", []):
            did = ev.get("doc_id")
            if did is None:
                continue
            m = re.search(r"(\d+)", str(did))
            if m:
                dc_map.setdefault(int(m.group(1)), []).append(cert)
    return dc_map


def load_replication_guides():
    """Load Open Lab replication guides, keyed by doc_id.
    [prescribed: Master Directive C — Modern Replication Guide tabs on flagship docs]"""
    guides = {}
    if not RG_FILE.is_file():
        return guides
    try:
        with open(RG_FILE, encoding="utf-8") as f:
            data = json.load(f)
        for did, g in data.get("guides", {}).items():
            try:
                guides[int(did)] = g
            except (TypeError, ValueError):
                continue
    except Exception:
        pass
    return guides


def load_ipfs_manifest():
    """Load the IPFS pinning manifest, keyed by doc_id.
    [prescribed: Master Directive B — anti-fragile archiving pilot]"""
    pins = {}
    if not IPFS_FILE.is_file():
        return pins
    try:
        with open(IPFS_FILE, encoding="utf-8") as f:
            data = json.load(f)
        for did, pin in data.get("docs", {}).items():
            try:
                pins[int(did)] = pin
            except (TypeError, ValueError):
                continue
    except Exception:
        pass
    return pins


def render_archival_badge(pin):
    """Render the 'Permanently Archived' badge with SHA-256 + IPFS CID.
    [prescribed: Master Directive B — display hash, link to gateway]"""
    sha = pin.get("sha256", "")
    cid = pin.get("cid", "")
    gw = f"https://ipfs.io/ipfs/{cid}"
    short_sha = sha[:16] + "…"
    return f"""<div class="archived" data-bg-tier="prescribed" data-bg-source="IPFS pin + SHA-256 (Directive B — anti-fragile archiving)">
  <span class="arch-badge">✅ Permanently Archived</span>
  <span class="arch-hash">SHA-256 <code>{esc(short_sha)}</code></span>
  <span class="arch-cid">IPFS <a href="{esc(gw)}" target="_blank" rel="noopener">{esc(cid[:24])}…</a></span>
  <a class="arch-gw" href="{esc(gw)}" target="_blank" rel="noopener">Fetch from IPFS →</a>
</div>"""


def render_open_lab(guide):
    """Render the Open Lab section (replication guide + why-now + log-an-attempt)
    for a flagship doc that has a guide.
    [prescribed: Master Directive C — vicarious learning engine]"""
    status = guide.get("status", "protocol")
    rc = guide.get("replicability", "home")
    cost = guide.get("cost", "?")
    claim = guide.get("claim", "")
    vars_rows = "".join(
        f'<div class="rg-row"><span class="rg-var">{esc(v[0])}</span>'
        f'<span class="rg-mod">{esc(v[1])}</span></div>'
        for v in guide.get("variables", [])
    )
    why = guide.get("why_now", "")
    refs = "".join(f'<li>{esc(r)}</li>' for r in guide.get("modern_refs", []))
    status_cls = {"protocol": "rg-protocol", "underway": "rg-underway",
                  "replicated": "rg-replicated", "refuted": "rg-refuted",
                  "inconclusive": "rg-inconclusive"}.get(status, "rg-protocol")
    return f"""<div class="openlab" data-bg-tier="aesthetic" data-bg-source="Open Lab replication guide (Directive C)">
  <div class="ol-tabs"><span class="ol-tab on">Modern Replication Guide</span><span class="ol-tab">Why This Matters Now</span></div>
  <div class="ol-panel">
    <div class="ol-meta"><span class="rg-status {status_cls}">{esc(status)}</span>
      <span class="ol-chip">replicability: {esc(rc)}</span><span class="ol-chip">cost: {esc(cost)}</span></div>
    <p class="rg-claim"><strong>Core hypothesis (quoted):</strong> {esc(claim)}</p>
    <p class="ol-subhead">Variable checklist — with modern affordable equivalents</p>
    <div class="rg-vars">{vars_rows}</div>
    <p class="ol-subhead">Safety &amp; calibration</p>
    <p class="rg-safety">{esc(guide.get('safety', ''))}</p>
  </div>
  <div class="ol-panel" style="display:none">
    <p class="rg-why">{esc(why)}</p>
    <p class="ol-subhead">Modern bridges</p>
    <ul class="rg-refs">{refs}</ul>
  </div>
  <div class="ol-log">
    <span class="ol-log-label">⚗ Log an Attempt</span>
    <p class="ol-log-note">Built it? Log photos, data, and notes. Submissions go to quarantine first, then human review — nothing publishes automatically.</p>
    <a class="btn ghost" href="mailto:?subject=Open Lab attempt — {esc(guide.get('title',''))}">Submit an attempt →</a>
  </div>
</div>"""


def jsonld_for_doc(doc, dc_map):
    """Emit Schema.org JSON-LD for a document page.
    [prescribed: Master Directive B — JSON-LD layer, not a graph DB]"""
    did = int(doc["id"])
    title = (doc.get("title") or doc.get("filename") or "Untitled").strip()
    person = doc.get("primary_person") or ""
    cats = doc.get("categories") or []
    metas = doc.get("meta_categories") or []
    src = doc.get("source_url") or ""
    preview = doc.get("content_preview") or ""
    date = doc.get("steiner_date") or ""
    patents = doc.get("patent_numbers") or []
    base = "https://focusingpulse.github.io"

    node = {
        "@context": "https://schema.org",
        "@type": "ScholarlyArticle",
        "name": title,
        "url": base + doc_url(did),
        "isPartOf": {"@type": "Collection", "name": "Aetherforce Knowledge Vault", "url": base + "/AFLinks/"},
        "publisher": {"@type": "Organization", "name": "Aetherforce Knowledge Vault"},
        "description": (preview[:400] or title).replace("\n", " "),
    }
    if person:
        node["author"] = {"@type": "Person", "name": person}
    if date:
        node["datePublished"] = date
    if src:
        node["sameAs"] = src
    if patents:
        node["identifier"] = [{"@type": "PropertyValue", "name": "patent", "value": p} for p in patents[:3]]
    about = [{"@type": "Thing", "name": c} for c in (metas + cats)[:8]]
    if about:
        node["about"] = about

    # Contradiction / lineage relationships from death certificates
    # [prescribed: Master Directive B — 'contradicts' is the missing half of synaptic links]
    certs = dc_map.get(did, [])
    if certs:
        rel = []
        for cert in certs:
            ev_ids = [int(re.search(r"(\d+)", str(e.get("doc_id"))).group(1))
                      for e in cert.get("lineage", [])
                      if e.get("doc_id") and re.search(r"(\d+)", str(e.get("doc_id")))]
            others = [base + doc_url(i) for i in ev_ids if i != did]
            if others:
                rel.append({
                    "@type": "Statement",
                    "name": f"Part of the {cert.get('claim', 'wrong-turn lineage')}",
                    "description": f"Lineage status: {cert.get('status', 'unknown')}. "
                                   f"The archive preserves claims; it does not certify them.",
                    "subjectOf": others,
                })
        if rel:
            node["subjectOf"] = rel

    return '<script type="application/ld+json">' + json.dumps(node, ensure_ascii=False) + "</script>"


def render_lineage_html(certs):
    """Visible lineage section for docs that appear in a death certificate.
    [prescribed: Master Directive B — synaptic links footer]"""
    if not certs:
        return ""
    parts = []
    for cert in certs:
        status = cert.get("status", "unknown")
        claim = cert.get("claim", "")
        events = []
        for ev in cert.get("lineage", []):
            m = re.search(r"(\d+)", str(ev.get("doc_id") or ""))
            link = (f' <a href="/AFLinks/pages/{int(m.group(1)):08d}.html">→</a>' if m else "")
            events.append(f'<div class="ev"><span class="d">{esc(ev.get("date", ""))}</span> — '
                          f'{esc(ev.get("event", ""))}{link}</div>')
        parts.append(f"""<div class="lineage">
  <h2>⚠ Wrong-Turn Lineage — {esc(claim)}</h2>
  <span class="st {esc(status)}">{esc(status)}</span>
  {''.join(events)}
  <div style="font-size:.78rem;color:#8a7a95;margin-top:8px">This document is one point in a documented
  lineage of a research line that died or was suppressed. The archive preserves the claim; it does not
  certify it. <a href="/AFLinks/methodology.html">Methodology</a></div>
</div>""")
    return "".join(parts)


def render_page(doc, has_preview, dc_map, rg_guides, ipfs_pins):
    did = int(doc["id"])
    title = (doc.get("title") or doc.get("filename") or "Untitled").strip()
    preview = doc.get("content_preview") or ""
    cats = doc.get("categories") or []
    metas = doc.get("meta_categories") or []
    src = doc.get("source_url") or ""
    person = doc.get("primary_person") or ""
    patents = doc.get("patent_numbers") or []
    date = doc.get("steiner_date") or ""
    ipfs_badge = render_archival_badge(ipfs_pins[did]) if did in ipfs_pins else ""

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

    # Virtual-center share row [prescribed: Karim virtual center — semi-circle +
    # two radiating lines — anchoring share/publish actions to the BG3 center]
    page_url = f"https://focusingpulse.github.io/AFLinks/pages/{did:08d}.html"
    vc_svg = ('<svg viewBox="0 0 100 30" width="34" height="20" aria-hidden="true" style="vertical-align:-3px;color:#c99a58">'
              '<path d="M 42 20 A 8 8 0 0 1 58 20" fill="none" stroke="currentColor" stroke-width="1.5" '
              'data-bg-tier="prescribed" data-bg-source="Karim virtual center, semi-circle + two radiating lines"/>'
              '<line x1="50" y1="20" x2="50" y2="5" stroke="currentColor" stroke-width="1.2" data-bg-tier="prescribed"/>'
              '<line x1="50" y1="20" x2="35" y2="20" stroke="currentColor" stroke-width="1.2" data-bg-tier="prescribed"/>'
              '</svg>')
    share_row = f"""<div class="share" data-bg-tier="prescribed" data-bg-source="Karim virtual center component for share/publish actions">
  {vc_svg}
  <button class="btn ghost" onclick="navigator.clipboard.writeText('{page_url}').then(()=>this.textContent='✓ Link copied')" title="Copy this document's permanent link">Share this document</button>
  <a class="btn ghost" href="mailto:?subject={esc(title)}&body={esc('From the Aetherforce Knowledge Vault: ' + page_url)}">Email →</a>
</div>"""

    # JSON-LD [prescribed: Master Directive B]
    ld = jsonld_for_doc(doc, dc_map)
    # Lineage section [prescribed: Master Directive B]
    lineage_html = render_lineage_html(dc_map.get(did, []))
    # Open Lab replication guide [prescribed: Master Directive C]
    open_lab_html = render_open_lab(rg_guides[did]) if did in rg_guides else ""

    # Open Lab tab-switch JS (kept out of the f-string to avoid brace escaping)
    ol_js = """
<script>
document.querySelectorAll('.openlab .ol-tab').forEach(function(tab){
  tab.addEventListener('click', function(){
    var box = this.closest('.openlab');
    box.querySelectorAll('.ol-tab').forEach(function(t){t.classList.remove('on')});
    this.classList.add('on');
    var i = Array.prototype.indexOf.call(box.querySelectorAll('.ol-tab'), this);
    box.querySelectorAll('.ol-panel').forEach(function(p, pi){p.style.display = (pi===i)?'':'none'});
  });
});
</script>
"""
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
{ld}
</head>
<body>
<div class="wrap">
  <div class="top">⚓ <a href="/AFLinks/">Aetherforce Knowledge Vault</a> · document #{did}</div>
  <h1>{esc(title)}</h1>
  <div class="meta">{('👤 ' + esc(person) + ' · ') if person else ''}{('📅 ' + esc(date)) if date else ''} · archived # {did:,}</div>
  {ipfs_badge}
  {lineage_html}<div class="preview">{esc(preview)}</div>
  {open_lab_html}
  <div class="actions">{src_line} {pat_line} <a class="btn ghost" href="/AFLinks/?q={esc(cat_query)}">Related documents →</a></div>
  {share_row}
  <div class="tags">{tags}</div>
  <div class="ppl">The archive preserves claims; it does not certify them. Category/meta tags describe content, not truth. <a href="/AFLinks/methodology.html">Methodology</a></div>
</div>
{ol_js}
</body>
</html>
"""
    return page


def write_css():
    (DOCS_DIR / "style.css").write_text(STYLE, encoding="utf-8")


def main():
    docs = load_index()
    dc_map = load_death_certificates()
    rg_guides = load_replication_guides()
    ipfs_pins = load_ipfs_manifest()
    if dc_map:
        print(f"  loaded {sum(len(v) for v in dc_map.values())} lineage links from death certificates")
    if rg_guides:
        print(f"  loaded {len(rg_guides)} Open Lab replication guides")
    if ipfs_pins:
        print(f"  loaded {len(ipfs_pins)} IPFS pins")
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
        out.write_text(render_page(doc, bool(pid), dc_map, rg_guides, ipfs_pins), encoding="utf-8")
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