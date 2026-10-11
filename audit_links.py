#!/usr/bin/env python3
"""audit_links.py — Link integrity layer for AFLinks.

Scans all site pages for outbound links (Aetherforce, Rex Research,
Google Patents, other) and in-site asset references, verifies each with
a live HTTP check, and writes a report:

  - link_audit_report.json   (machine-readable)
  - link_audit_report.md     (human-readable, in the repo)

Usage:
  python3 audit_links.py [--check-remote] [--limit N]

--check-remote actually hits the network (default: only in-site assets are
checked, outbound URLs are classified by pattern). Use --check-remote for
a full pass; it is rate-limited and takes a while.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = ["index.html", "library.html", "lens.html", "vault.html"]

AF = "aetherforce.energy"
REX = "rexresearch.com"
GPL = "patents.google.com"

UA = "Mozilla/5.0 (AFLinks link-audit; research archive health check)"


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []  # (tag, attr, url)

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        for attr in ("href", "src"):
            if d.get(attr):
                self.links.append((tag, attr, d[attr]))


def extract_js_urls(text, page):
    """Pull URL string literals from inline JS (AF_* constants, template URLs)."""
    urls = set()
    # "https://..." literals
    for m in re.finditer(r"['\"](https?://[^'\"]+)['\"]", text):
        urls.add(m.group(1))
    # AF_BASE + "/path/" patterns
    for m in re.finditer(r"AF_BASE\s*\+\s*['\"]([^'\"]+)['\"]", text):
        urls.add("https://www.aetherforce.energy" + m.group(1))
    for m in re.finditer(r"AF_LINKS\s*\+\s*['\"]([^'\"]+)['\"]", text):
        urls.add("https://www.aetherforce.energy/resources/links/" + m.group(1))
    for m in re.finditer(r"AF_SHOP\s*\+\s*['\"]([^'\"]+)['\"]", text):
        urls.add("https://www.aetherforce.energy/shop-2/" + m.group(1))
    return urls


def classify(url):
    if url.startswith("#"):
        return "anchor"
    if url.startswith("javascript:"):
        return "js"
    if AF in url:
        return "aetherforce"
    if REX in url:
        return "rexresearch"
    if GPL in url:
        return "patents"
    if url.startswith("./") or url.startswith("../") or url.startswith("/") or url.startswith("data:"):
        return "in_site"
    if re.match(r"^https?://", url):
        return "external"
    return "other"


def http_status(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return None  # unreachable/timeout


def check_in_site(path, base):
    full = os.path.join(base, path.lstrip("./"))
    if os.path.isfile(full):
        return 200
    return 404


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-remote", action="store_true", help="hit the network for outbound URLs")
    ap.add_argument("--limit", type=int, default=0, help="cap remote checks (0 = all)")
    args = ap.parse_args()

    report = {"generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
              "pages": {}, "assets": {}, "summary": {}}
    outbound = {}  # url -> category (from markup)
    js_urls = set()

    for page in PAGES:
        path = os.path.join(HERE, page)
        if not os.path.isfile(path):
            report["pages"][page] = {"error": "missing"}
            continue
        text = open(path, encoding="utf-8", errors="replace").read()
        p = LinkParser()
        p.feed(text)
        plinks = []
        for tag, attr, url in p.links:
            if url.startswith("mailto:") or url.startswith("tel:"):
                continue
            cat = classify(url)
            plinks.append({"url": url, "tag": tag, "cat": cat})
            if cat in ("aetherforce", "rexresearch", "patents", "external") and url.startswith("http"):
                outbound.setdefault(url, cat)
        jurls = extract_js_urls(text, page)
        for u in jurls:
            cat = classify(u)
            outbound.setdefault(u, cat)
            plinks.append({"url": u, "tag": "js", "cat": cat})
        report["pages"][page] = {"links": plinks}
        js_urls |= jurls

    # In-site asset resolution
    asset_hits = set()
    for page in PAGES:
        for link in report["pages"].get(page, {}).get("links", []):
            u = link["url"]
            if link["cat"] == "in_site":
                asset_hits.add(u)
    asset_state = {}
    for u in sorted(asset_hits):
        asset_state[u] = check_in_site(u, HERE)

    # Remote checks (optional)
    remote_state = {}
    if args.check_remote:
        urls = sorted(u for u, cat in outbound.items() if cat != "in_site")
        if args.limit:
            urls = urls[: args.limit]
        print(f"Checking {len(urls)} remote URLs (concurrency 6)...", file=sys.stderr)
        with ThreadPoolExecutor(max_workers=6) as ex:
            futs = {ex.submit(http_status, u): u for u in urls}
            done = 0
            for fut in as_completed(futs):
                u = futs[fut]
                remote_state[u] = fut.result()
                done += 1
                if done % 25 == 0:
                    print(f"  {done}/{len(urls)}", file=sys.stderr)

    # Summarize
    cats = Counter()
    for page in PAGES:
        for link in report["pages"].get(page, {}).get("links", []):
            cats[link["cat"]] += 1
    report["summary"]["link_categories"] = dict(cats)
    report["summary"]["js_urls"] = sorted(js_urls)

    broken_remote = []
    if remote_state:
        for u, code in sorted(remote_state.items()):
            if code is None or code >= 400:
                broken_remote.append({"url": u, "status": code, "cat": outbound.get(u)})
        report["summary"]["remote_checked"] = len(remote_state)
        report["summary"]["remote_broken"] = len(broken_remote)
        report["summary"]["broken_remote"] = broken_remote

    broken_assets = [{"url": u, "status": c} for u, c in sorted(asset_state.items()) if c != 200]
    report["summary"]["assets_checked"] = len(asset_state)
    report["summary"]["assets_broken"] = len(broken_assets)
    report["summary"]["broken_assets"] = broken_assets

    with open(os.path.join(HERE, "link_audit_report.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, indent=1)

    # --- Markdown report ---
    md = ["# Link Audit Report", "",
          f"Generated: {report['generated']}", "",
          "## Summary", "",
          f"- Links by category: {report['summary']['link_categories']}",
          f"- In-site assets checked: {report['summary']['assets_checked']}, broken: {report['summary']['assets_broken']}",
          ]
    if remote_state:
        md += [f"- Remote URLs checked: {report['summary']['remote_checked']}, broken: {report['summary']['remote_broken']}", ""]
        md += ["### Broken remote links", ""]
        for b in broken_remote:
            md += [f"- `{b['status']}` {b['cat']}: {b['url']}"]
    else:
        md += ["- Remote check skipped (run with --check-remote)", ""]
    md += ["", "### Broken in-site assets", ""]
    for b in broken_assets:
        md += [f"- `{b['status']}` {b['url']}"]
    md += ["", "### Per-page", ""]
    for page in PAGES:
        links = report["pages"].get(page, {}).get("links", [])
        md += [f"- **{page}**: {len(links)} link refs"]
    md += ["", "### JS hardcoded outbound URLs", ""]
    for u in sorted(js_urls):
        md += [f"- {u}"]
    with open(os.path.join(HERE, "link_audit_report.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    print(json.dumps(report["summary"], indent=1))


if __name__ == "__main__":
    main()