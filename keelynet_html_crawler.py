#!/usr/bin/env python3
"""keelynet_html_crawler.py — harvest keelynet.com HTML pages via Wayback CDX.

Keelynet (dead domain) was a huge free-energy / gravity-control / alternative-
science research site. Its PDFs were harvested by wayback_scavenger.py (46 done);
the HTML article + news surfaces were never captured. This crawler pulls the
text/html captures from the Wayback CDX API, fetches each page's raw bytes via
the id_ endpoint, extracts text, and queues entries for the AFLinks index.

State is kept in the same wayback_keelynet_com.json dict (new "html" key, so
the PDF scavenger's done/skipped keys are untouched). Entries accumulate in
wayback_keelynet_html_entries.json and are mirrored into
wayback_keelynet_html_progress.json (merge_all_progress.py-compatible).

Usage:
  python3 keelynet_html_crawler.py --scope articles --limit 0 --workers 5
  python3 keelynet_html_crawler.py --scope news --limit 1500 --workers 5
"""
import argparse, json, os, re, sys, time, urllib.request, concurrent.futures, threading

HERE = os.path.dirname(os.path.abspath(__file__))
STATE_PATH = os.path.join(HERE, "wayback_keelynet_com.json")
ENTRIES_PATH = os.path.join(HERE, "wayback_keelynet_html_entries.json")
PROGRESS_PATH = os.path.join(HERE, "wayback_keelynet_html_progress.json")

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (AFLinks archive; research)"
CDX = "http://web.archive.org/cdx/search/cdx"
ARC = "https://web.archive.org/web/{ts}id_/{url}"

JUNK_DIRS = {"cgi-sys", "ezoic", "chat", "humor", "mexistim", "confer", "viewitem",
             "images", "img", "css", "js", "icons", "%5fvtI_cnf", "_vti_cnf",
             "spider", "water.htm", "vsrtnews"}
lock = threading.Lock()
RECOVER = False  # when True, process() re-emits done-state items (for --recover)


def norm_url(u):
    """Normalize an original keelynet URL to http://www.keelynet.com/<path>."""
    u = re.sub(r"^[a-z]+://", "", u, flags=re.I)
    host, _, path = u.partition("/")
    host = re.sub(r":\d+$", "", host)
    host = re.sub(r"^www\.", "", host, flags=re.I).lower()
    return f"http://www.{host}/{path}"


def classify(url):
    ul = url.lower()
    if "?" in url:
        return "junk"
    if "/news/" in ul:
        # /news/xxx.htm = "Energy & Freedom" news archive (a content lane of its own)
        return "news"
    if "/interact/" in ul:
        return "interact"
    for j in JUNK_DIRS:
        if "/" + j + "/" in ul or ul.endswith("/" + j):
            return "junk"
    return "articles"


def load_state():
    if os.path.isfile(STATE_PATH):
        with open(STATE_PATH, encoding="utf-8") as f:
            st = json.load(f)
        st.setdefault("html", {})
        return st
    return {"domain": "keelynet.com", "done": {}, "skipped": {}, "html": {}}


def save_state(st):
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(st, f, indent=1)


def load_entries():
    if os.path.isfile(ENTRIES_PATH):
        with open(ENTRIES_PATH, encoding="utf-8") as f:
            return json.load(f)
    return []


def save_entries(entries):
    with open(ENTRIES_PATH, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False)
    # mirror into progress file for merge_all_progress.py compatibility
    with open(PROGRESS_PATH, "w", encoding="utf-8") as f:
        json.dump({"last_processed": len(entries), "entries": entries}, f, ensure_ascii=False)


def cdx_rows():
    url = (f"{CDX}?url=keelynet.com&matchType=domain&output=json&collapse=urlkey"
           f"&fl=timestamp,original&filter=statuscode:200&filter=mimetype:text/html")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        rows = json.load(r)
    return rows[1:]  # drop header


def fetch(url, timeout=45):
    """Fetch via curl subprocess. web.archive IP-rate-gates bursts, so keep to
    ~1 request/sec and back off hard on 5xx. Returns (data, status)."""
    import subprocess
    time.sleep(1.0)
    for attempt, wait in ((1, 6.0), (2, 15.0), (3, 25.0)):
        try:
            r = subprocess.run(
                ["curl", "-s", "-L", "--max-redirs", "5", "--max-time", str(timeout),
                 "-A", UA, "-w", "\n%{http_code}", url],
                capture_output=True, timeout=timeout + 15)
            body, _, code_b = r.stdout.rpartition(b"\n")
            code = code_b.decode("utf-8", "replace").strip()
            if r.returncode != 0:
                time.sleep(wait)
                continue
            if code in ("404", "451", "403"):
                return None, "dead"
            if code.startswith(("5", "429")) or not body:
                time.sleep(wait)  # cooldown for the IP rate gate
                continue
            return body, "ok"
        except Exception:
            time.sleep(wait)
    return None, "retry"


def strip_html(h):
    h = re.sub(r"<script.*?</script>|<style.*?</style>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<!--.*?-->", " ", h, flags=re.S)
    h = re.sub(r"<[^>]+>", " ", h)
    h = re.sub(r"\s+", " ", h).strip()
    return h


def extract_title(h):
    m = re.search(r"<title>(.*?)</title>", h, re.S | re.I)
    if m:
        t = m.group(1).strip()
        if t:
            return t[:200]
    return ""


def process(item, st, scope_slug, existing_norm):
    ts, orig = item
    key = f"{ts}_{orig}"
    stx = st["html"].setdefault(scope_slug, {"done": {}, "skip": {}})
    if not RECOVER:
        if key in stx["done"]:
            return None
        if key in stx["skip"] and stx["skip"][key] != "unreachable":
            return None
    norm = norm_url(orig)
    if norm in existing_norm:
        with lock:
            stx["skip"][key] = "already_indexed"
            save_state(st)
        return None
    raw, status = fetch(ARC.format(ts=ts, url=orig))
    if status == "retry":
        with lock:
            stx["skip"][key] = "unreachable"  # transient — retried next run
            save_state(st)
        return None
    if raw is None:
        # status == "dead" (404/403/451) — permanent; no point retrying
        with lock:
            stx["skip"][key] = "dead"
            save_state(st)
        return None
    body = raw.decode("utf-8", errors="replace")
    if not re.search(r"<html|<title", body[:800], re.I):
        with lock:
            stx["skip"][key] = "not_html"
            save_state(st)
        return None
    txt = strip_html(body)
    if len(txt) < 60:
        with lock:
            stx["skip"][key] = "no_text"
            save_state(st)
        return None
    title = extract_title(body) or re.sub(r"[_\-]+", " ", os.path.basename(orig.split("?")[0])).strip()
    entry = {
        "id": None,
        "filename": os.path.basename(orig.split("?")[0]) or orig,
        "title": title,
        "type": "document",
        "extension": ".html",
        "size_bytes": len(raw),
        "source_url": norm,
        "source_site": "wayback:keelynet.com",
        "categories": ["Borderland Research"],
        "meta_categories": [],
        "patent_numbers": [],
        "primary_person": "",
        "content_preview": txt[:2000],
        "preview_state": "ok",
        "archive_ts": ts,
        "concepts": [],
        "last_modified": time.strftime("%Y-%m-%d"),
    }
    with lock:
        stx["done"][key] = {"ts": ts, "orig": orig, "preview_chars": len(txt)}
        save_state(st)
    return entry


def entry_key(e):
    """Rebuild the (ts_orig) state key from a persisted entry."""
    return f"{e.get('archive_ts','')}_{e.get('source_url','')}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scope", choices=["articles", "news", "interact", "all"], default="articles")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=5)
    ap.add_argument("--recover", action="store_true",
                    help="re-fetch done-state items whose entry was lost on a killed run")
    args = ap.parse_args()
    global RECOVER
    RECOVER = args.recover

    print("CDX query keelynet.com (text/html)...", flush=True)
    rows = cdx_rows()
    print(f"  {len(rows)} unique text/html URLs", flush=True)

    st = load_state()
    entries = load_entries()

    # pre-existing URL normalization set from the master index (dedupe)
    # load via index_io to avoid re-reading shards ad hoc
    try:
        import index_io
        exset = index_io.url_set()
    except Exception:
        exset = set()
    existing_norm = {norm_url(u) for u in exset if u}
    existing_norm |= {norm_url(u) for u in exset}
    print(f"  {len(existing_norm)} existing indexed URLs (normalized) in dedupe set", flush=True)

    scope = args.scope
    items = [(ts, o) for ts, o in rows if scope == "all" or classify(o) == scope]
    if args.recover:
        # add done-state items whose entry is missing from the persisted entries file
        from_entries = {(e.get("archive_ts", ""), e.get("source_url", "")) for e in entries}
        stx = st["html"].setdefault(scope, {"done": {}, "skip": {}})
        for key, rec in stx.get("done", {}).items():
            ts, orig = key.split("_", 1)
            if (ts, norm_url(orig)) not in from_entries:
                items.append((ts, orig))
        print(f"  recover: {len(items) - len([1 for _t, o in rows if scope == 'all' or classify(o) == scope])} lost entries queued for rebuild", flush=True)
    if args.limit:
        items = items[:args.limit]
    print(f"  scope={scope}: {len(items)} targets", flush=True)

    new = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = [ex.submit(process, it, st, scope, existing_norm) for it in items]
        done_n = 0
        for fut in concurrent.futures.as_completed(futs):
            e = fut.result()
            done_n += 1
            if e:
                new.append(e)
                entries.append(e)
                save_entries(entries)  # write-through: no loss if killed
            if done_n % 100 == 0:
                print(f"  ... {done_n}/{len(items)} checked, {len(new)} new", flush=True)
    save_entries(entries)
    print(f"done: {len(new)} new entries harvested (total cumulative {len(entries)})", flush=True)


if __name__ == "__main__":
    main()
