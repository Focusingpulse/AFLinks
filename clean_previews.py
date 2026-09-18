#!/usr/bin/env python3
"""clean_previews.py — strip navigation chrome out of already-harvested previews.

WHY: the first-generation harvest flattened every page with a whole-document
tag strip, so site chrome ("Jump to content / Main menu / Random page / Recent
changes / Log in / Contents / Toggle the table of contents") landed in
content_preview as if it were prose. Because previews are cut at ~2000 chars,
on the worst sites the chrome IS the document. Measured 2026-09-18:
8,313 of 49,470 previews (16.8%) carry >=2 nav markers; the worst hosts are
wiki.naturalphilosophy.org (100% of pages) and energeticforum.com (29%).

This tool re-fetches those pages, extracts the real document with
content_extract.extract_content(), and writes cleaner text back — into the
master index AND into every per-site *_entries.json that holds the same URL, so
a later merge cannot re-introduce the chrome.

Safe by construction:
  * only HTML-ish URLs are touched (PDF text never had chrome)
  * a replacement is kept only if it LOWERS the chrome score and keeps a
    minimum of real text — otherwise the original preview is left alone
  * every fetch is cached in clean_cache.json, so the index and the entries
    files are repaired from one fetch, and re-runs cost nothing
  * stateful, resumable, time-budgeted, threaded

Usage:
    python3 clean_previews.py --scan                 # report contamination only
    python3 clean_previews.py --limit 400 --budget 1200 --workers 4
    python3 clean_previews.py --host wiki.naturalphilosophy.org --limit 2000
    python3 clean_previews.py --apply                # write cache back, no fetching
    python3 clean_previews.py --retry-failed
"""
import argparse
import concurrent.futures
import glob
import json
import os
import re
import threading
import time
import urllib.request

import content_extract as ce

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH = os.path.join(SCRIPT_DIR, "clean_cache.json")
STATE_PATH = os.path.join(SCRIPT_DIR, "clean_previews_state.json")
UA = "Mozilla/5.0 (AFLinks preview-cleaner; research archive)"
MIN_TEXT = 200          # a replacement must hold at least this much real text
CLEAN_SCORE = 1         # below this, the preview counts as chrome-free
HTML_EXT = ("html", "htm", "php", "asp", "aspx", "shtml", "")
_lock = threading.Lock()


# ---------------------------------------------------------------- helpers
def is_html_url(url):
    """True if this URL is worth HTML-extracting.

    Query strings and fragments must be stripped before looking at the
    extension: `index.php?title=Keely` and `tiki-index.php?page=X` end in an
    extension that is not the last dot-segment, so a naive split drops exactly
    the wiki pages that need cleaning most. Extension-less paths (`/Keely`)
    are HTML too. PDFs and media never had chrome and are skipped.
    """
    path = url.split("#", 1)[0].split("?", 1)[0]
    tail = path.rsplit("/", 1)[-1]
    if "." not in tail:
        return True          # clean URL, e.g. svpwiki.com/Keely
    ext = tail.rsplit(".", 1)[-1].lower()
    return ext in HTML_EXT


def fetch_html(url, timeout=25):
    for attempt in (1, 2):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": UA,
                "Accept": "text/html,application/xhtml+xml,*/*"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                ctype = (r.headers.get("Content-Type") or "").lower()
                data = r.read()
            if "pdf" in ctype or "image" in ctype or "octet-stream" in ctype:
                return None, "not-html"
            return data.decode("utf-8", errors="replace"), None
        except Exception as e:
            if attempt == 2:
                return None, str(e)[:120]
            time.sleep(0.8)
    return None, "unreachable"


def load_json(path, default):
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return default


def save_json(path, obj, indent=2):
    """Write JSON matching the file's existing style.

    The *_entries.json progress files are written with indent=2 by
    process_generic_cloud.save_progress(). Rewriting them compact would show a
    148k-line diff for a 300-line change and break the repo's file consistency.
    """
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=indent)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def contaminated(entry):
    p = entry.get("content_preview") or ""
    return bool(p) and ce.chrome_score(p) >= 2


# ---------------------------------------------------------------- scan
def host_of(url):
    return re.sub(r"^https?://", "", url).split("/")[0]


def order_targets(urls):
    """Worst host first.

    A run is budget-limited, so the order it fetches in decides what actually
    gets fixed. Sorting by how many contaminated URLs a host has means the run
    finishes wiki.naturalphilosophy.org (5k pages of pure menu) before it
    touches a host with a handful.
    """
    from collections import Counter
    counts = Counter(host_of(u) for u in urls)
    return dict(sorted(urls.items(), key=lambda kv: -counts[host_of(kv[0])]))


def collect_targets(mode="all"):
    """Return {url: {'where': [...], 'preview': str}} across index + entries."""
    urls = {}
    try:
        import index_io
        for e in index_io.iter_docs():
            u = e.get("source_url") or ""
            if not u or not is_html_url(u) or not contaminated(e):
                continue
            urls.setdefault(u, {"where": set(), "preview": e["content_preview"]})
            urls[u]["where"].add("index")
    except Exception as ex:
        print(f"  (index read skipped: {ex})")

    if mode in ("all", "entries"):
        for f in sorted(glob.glob(os.path.join(SCRIPT_DIR, "*_entries.json"))):
            try:
                with open(f, encoding="utf-8") as fh:
                    data = json.load(fh)
            except Exception:
                continue
            if not isinstance(data, list):
                continue
            n = 0
            for e in data:
                if not isinstance(e, dict) or not contaminated(e):
                    continue
                u = e.get("source_url") or ""
                if not u or not is_html_url(u):
                    continue
                urls.setdefault(u, {"where": set(), "preview": e["content_preview"]})
                urls[u]["where"].add(os.path.basename(f))
                n += 1
            if n:
                print(f"  {os.path.basename(f)}: {n} contaminated")
    return urls


# ---------------------------------------------------------------- clean
RETRY_AFTER = 3 * 86400   # re-attempt a failed URL after 3 days


def should_retry(u, state, force=False):
    """Has this URL earned another attempt?

    A transient network error must not blacklist a page forever, but a URL that
    is genuinely unfetchable should not be hammered every run either. Failures
    are stored with a timestamp and become eligible again after RETRY_AFTER.
    """
    if force:
        return True
    if u not in state["failed"]:
        return True
    rec = state["failed"][u]
    if isinstance(rec, dict):
        return (time.time() - rec.get("ts", 0)) > RETRY_AFTER
    return True  # legacy bare-string record: treat as eligible


def clean_batch(urls, cache, state, limit, budget, workers):
    todo = []
    for u in urls:
        if u in cache:
            continue
        if not should_retry(u, state, state.get("retry_failed")):
            continue
        todo.append(u)
    print(f"to fetch: {len(todo)} (cached {len(cache)}, known-failed {len(state['failed'])})")
    todo = todo[:limit]
    start = time.time()
    done = [0]

    def work(u):
        if time.time() - start > budget:
            return
        html, err = fetch_html(u)
        if html is None:
            with _lock:
                state["failed"][u] = {"reason": err or "fetch-failed", "ts": int(time.time())}
            return
        title, text = ce.extract_content(html, u, max_chars=2000)
        score = ce.chrome_score(text)
        with _lock:
            if len(text) >= MIN_TEXT and score <= CLEAN_SCORE:
                cache[u] = {"kind": "text", "text": text, "title": title,
                            "ts": int(time.time())}
                state["failed"].pop(u, None)
                done[0] += 1
                if done[0] % 20 == 0:
                    print(f"  cleaned {done[0]}...", flush=True)
            elif len(text) < MIN_TEXT or score >= 3:
                # The page carries no readable document — it was only ever a
                # menu. Record that honestly instead of shipping the menu.
                cache[u] = {"kind": "stub", "text": "",
                            "title": title, "ts": int(time.time())}
                state["failed"].pop(u, None)
                done[0] += 1
            else:
                state["failed"][u] = {"reason": "ambiguous", "ts": int(time.time())}

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        list(ex.map(work, todo))
    print(f"fetched clean text for {done[0]} pages this run")
    return done[0]


def improved(old, new):
    """Should `new` replace `old`?

    Two conditions, both required:
      * the new text must be meaningfully cleaner (chrome score drops), and
      * it must actually be clean (score <= CHROME_FLOOR), not merely less bad.

    Without the second condition a nav-only stub page could "improve" from 17
    chrome hits to 4 and still ship a menu to the reader.
    """
    if not new or len(new) < MIN_TEXT:
        return False
    so, sn = ce.chrome_score(old), ce.chrome_score(new)
    if sn >= so:
        return False
    return sn <= CLEAN_SCORE


def stub_replacement(old):
    """For a page that has no readable content at all, the honest outcome is an
    explicit note rather than a menu. Kept deliberately short so the doc page's
    own 'preview pending' path still reads as the primary explanation."""
    return ce.STUB_MARKER if ce.chrome_score(old) >= 2 else None


def apply_entry(e, c):
    """Apply one cache record to one index/entries record. True if changed."""
    if not c:
        return False
    old = e.get("content_preview") or ""
    kind = c.get("kind", "text")
    if kind == "text":
        if improved(old, c["text"]):
            e["content_preview"] = c["text"]
            if c.get("title") and len(c["title"]) > 2:
                e["title"] = c["title"]
            return True
    elif kind == "stub":
        st = stub_replacement(old)
        if st and old != st:
            e["content_preview"] = st
            return True
    return False


def apply_cache(cache):
    """Write cached clean text into the index and every matching entries file."""
    changed = 0
    # --- index
    try:
        import index_io
        docs = index_io.load()
        n = sum(1 for e in docs if apply_entry(e, cache.get(e.get("source_url") or "")))
        if n:
            index_io.save(docs)
        print(f"index: {n} previews replaced")
        changed += n
    except Exception as ex:
        print(f"index write failed: {ex}")

    # --- per-site entries files
    for f in sorted(glob.glob(os.path.join(SCRIPT_DIR, "*_entries.json"))):
        try:
            with open(f, encoding="utf-8") as fh:
                data = json.load(fh)
        except Exception:
            continue
        if not isinstance(data, list):
            continue
        n = 0
        for e in data:
            if not isinstance(e, dict):
                continue
            c = cache.get(e.get("source_url") or "")
            if c and apply_entry(e, c):
                n += 1
        if n:
            save_json(f, data)
            print(f"  {os.path.basename(f)}: {n} replaced")
            changed += n
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan", action="store_true", help="report contamination, change nothing")
    ap.add_argument("--apply", action="store_true", help="write cache back, fetch nothing")
    ap.add_argument("--limit", type=int, default=400)
    ap.add_argument("--budget", type=int, default=900)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--host", default="", help="restrict to one host")
    ap.add_argument("--retry-failed", action="store_true")
    ap.add_argument("--mode", choices=["all", "entries", "index"], default="all")
    a = ap.parse_args()

    cache = load_json(CACHE_PATH, {})
    state = load_json(STATE_PATH, {"failed": {}})
    state.setdefault("failed", {})
    state["retry_failed"] = a.retry_failed

    urls = collect_targets(a.mode)
    if a.host:
        urls = {u: v for u, v in urls.items() if a.host in u}
    urls = order_targets(urls)
    print(f"contaminated HTML previews: {len(urls)}")

    if a.scan:
        from collections import Counter
        c = Counter(host_of(u) for u in urls)
        for host, n in c.most_common(20):
            print(f"  {n:6d}  {host}")
        print(f"already cached: {len(cache)}")
        print("fetch order (worst host first):")
        seen = []
        for u in urls:
            h = host_of(u)
            if h not in seen:
                seen.append(h)
                print(f"  {len(seen):2d}. {h}")
            if len(seen) >= 8:
                break
        return

    if not a.apply:
        clean_batch(urls, cache, state, a.limit, a.budget, a.workers)
        save_json(CACHE_PATH, cache)
        save_json(STATE_PATH, {"failed": state["failed"]})

    n = apply_cache(cache)
    print(f"total previews replaced: {n}")


if __name__ == "__main__":
    main()