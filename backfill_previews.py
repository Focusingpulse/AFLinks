#!/usr/bin/env python3
"""backfill_previews.py — fill missing content_preview values for HTML pages.

WHY: some site batches were catalogued with metadata only — the entry exists in
the master index but `content_preview` is empty, so the page is invisible to
content search. SVPwiki (Dale Pond's 15k-page Keely/SVP TikiWiki) is the worst
case: ~12k pages catalogued, almost none searchable by text.

This tool re-fetches those pages, extracts readable article text, and writes it
back into the master index. Idempotent and stateful: attempted URLs are
recorded so later runs skip them instead of re-hammering the host. Time-budgeted
so a cron turn can run a batch and exit cleanly.

Usage:
    python3 backfill_previews.py --host svpwiki.com --limit 400
    python3 backfill_previews.py --host svpwiki.com --budget 900 --workers 3
    python3 backfill_previews.py --host svpwiki.com --retry-failed
"""
import argparse
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
import concurrent.futures

import index_io

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (AFLinks preview-backfill; research archive)"
PREVIEW_CHARS = 1500
MIN_TEXT = 80
_lock = threading.Lock()


def fetch_html(url, timeout=25):
    for attempt in (1, 2):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                       "Accept": "text/html,application/xhtml+xml,*/*"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                ctype = (r.headers.get("Content-Type") or "").lower()
                data = r.read()
            if "html" not in ctype and "text" not in ctype:
                return None, None
            return data.decode("utf-8", errors="replace"), None
        except Exception as e:
            if attempt == 2:
                return None, str(e)[:120]
            time.sleep(1.0)
    return None, "unreachable"


def clean_text(s):
    for k, v in (("&nbsp;", " "), ("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"),
                 ("&quot;", '"'), ("&#39;", "'"), ("&raquo;", "»"), ("&laquo;", "«")):
        s = s.replace(k, v)
    s = re.sub(r"&#\d+;", "", s)
    return re.sub(r"\s+", " ", s).strip()


def extract(html):
    """Return (title, text). Prefer TikiWiki's <article id="top"> when present."""
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    title = clean_text(m.group(1)) if m else ""
    # strip the site prefix TikiWiki adds ("Sympathetic Vibratory Physics | X")
    if "|" in title:
        title = title.split("|")[-1].strip()
    body = None
    for pat in (r'<article[^>]*id="top"[^>]*>(.*?)</article>',
                r'<div[^>]*class="[^"]*wikitext[^"]*"[^>]*>(.*?)</div>',
                r'<main[^>]*>(.*?)</main>'):
        mm = re.search(pat, html, re.S | re.I)
        if mm:
            body = mm.group(1)
            break
    if not body:
        body = html
    body = re.sub(r"<script.*?</script>", " ", body, flags=re.S | re.I)
    body = re.sub(r"<style.*?</style>", " ", body, flags=re.S | re.I)
    body = re.sub(r"<[^>]+>", " ", body)
    return title, clean_text(body)[:PREVIEW_CHARS]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", required=True)
    ap.add_argument("--limit", type=int, default=400)
    ap.add_argument("--budget", type=int, default=900, help="seconds")
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--retry-failed", action="store_true")
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()

    state_path = os.path.join(SCRIPT_DIR, f"backfill_{a.host.replace('.', '_')}_state.json")
    state = {"filled": {}, "failed": {}}
    if os.path.exists(state_path):
        try:
            state = json.load(open(state_path))
        except Exception:
            pass
    state.setdefault("filled", {})
    state.setdefault("failed", {})

    docs = index_io.load()
    host = a.host
    cands = []
    for e in docs:
        u = e.get("source_url", "")
        if not u or not u.startswith("https://" + host) and not u.startswith("http://" + host):
            continue
        if e.get("content_preview"):
            continue
        if u in state["filled"]:
            continue
        if u in state["failed"] and not a.retry_failed:
            continue
        cands.append(e)

    print(f"{host}: {len(cands)} entries need a preview "
          f"({len(state['filled'])} filled, {len(state['failed'])} known-failed)")
    if not cands:
        return
    cands = cands[: a.limit]

    start = time.time()
    done = [0]

    def work(e):
        if time.time() - start > a.budget:
            return
        url = e["source_url"]
        html, err = fetch_html(url)
        if html is None:
            with _lock:
                state["failed"][url] = err or "fetch-failed"
            return
        title, text = extract(html)
        if len(text) < MIN_TEXT:
            with _lock:
                state["failed"][url] = "no-text"
                if title and not e.get("title"):
                    e["title"] = title
            return
        with _lock:
            e["content_preview"] = text
            if title and len(title) > 2:
                e["title"] = title
            state["filled"][url] = len(text)
            done[0] += 1
            if done[0] % 25 == 0:
                print(f"  filled {done[0]}...", flush=True)

    with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers) as ex:
        list(ex.map(work, cands))

    filled = len(state["filled"])
    failed = len(state["failed"])
    print(f"this run: +{done[0]} previews (state: {filled} filled / {failed} failed)")

    if a.dry:
        print("DRY RUN — index not written")
        return

    n = index_io.save(docs)
    json.dump(state, open(state_path, "w"))
    print(f"saved index: {n} shards, {len(docs)} entries; state -> {os.path.basename(state_path)}")


if __name__ == "__main__":
    main()