#!/usr/bin/env python3
"""wayback_scavenger.py — harvest PDFs from DEAD archives via Wayback CDX.

The rarest fringe-science content lives on dead domains (personal sites,
forums, expired hosts). The Wayback Machine has archived copies. This
scavenger queries the CDX API for every archived PDF under a target domain,
downloads a batch through web.archive.org, extracts text, and merges the
entries into the AFLinks index with provenance (original URL + archive
timestamp).

Usage:
  python3 wayback_scavenger.py --domain keelynet.com --limit 5 --workers 3
  python3 wayback_scavenger.py --domain keelynet.com --dry-run   # just count

State:
  wayback_<domain>.json  — per-domain crawl state (filelist + progress)
"""
import argparse, json, os, re, sys, time, threading, urllib.request
import concurrent.futures

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(HERE, "index.json")
UA = "Mozilla/5.0 (AFLinks wayback-scavenger; research archive)"
CDX = "http://web.archive.org/cdx/search/cdx"
ARC = "http://web.archive.org/web/{ts}id_/{url}"   # id_ = original bytes
# NOTE: http (not https) — the sandbox gets IP-blocked on web.archive.org:443
# after bursts, while port 80 keeps serving. urllib follows the 302 redirect
# (which may land on a different snapshot ts) and returns the original bytes.
ACCEPTED_EXTS = (".pdf", ".txt", ".htm", ".html")
lock = threading.Lock()

try:
    import pymupdf
except Exception:
    pymupdf = None


def cdx_list(domain, limit=0, exts=("pdf",), mimetype=None, urlfilter=None):
    """Return [(timestamp, original_url)] for archived files under domain.

    exts limits which extensions are harvested (default: pdf only, the
    historical behaviour). Pass e.g. ("txt", "html", "htm") for text archives
    like filestore.orgfree.com, where the valuable content is plain text.
    """
    alt = "|".join(re.escape(str(e).lstrip(".")) for e in exts)
    url = (f"{CDX}?url={domain}&matchType=domain&output=json&collapse=digest"
           f"&fl=timestamp,original")
    if mimetype:
        # mimetype mode: for extensionless CMS pages (Omeka, Drupal, wikis)
        # where the URL never carries a file extension.
        url += f"&filter=mimetype:{mimetype}"
    else:
        url += f"&filter=original:.*\\.({alt})$"
    url += "&filter=statuscode:200"
    if urlfilter:
        url += f"&filter=original:{urlfilter}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        rows = json.load(r)
    # dedupe by original URL, keeping the LATEST capture of each page
    # (collapse=digest still yields multiple snapshots of one URL)
    latest = {}
    for t, o in rows[1:]:  # drop header row
        if o not in latest or t > latest[o][0]:
            latest[o] = (t, o)
    out = list(latest.values())
    if limit:
        out = out[:limit]
    return out


def state_path(domain):
    safe = domain.replace(".", "_").replace("/", "_")
    return os.path.join(HERE, f"wayback_{safe}.json")


def load_state(domain):
    p = state_path(domain)
    if os.path.isfile(p):
        with open(p, encoding="utf-8") as f:
            st = json.load(f)
            # 'unreachable' is often a Wayback throttle burst (429/conn-refused),
            # not a dead capture — make it non-permanent so later runs retry it.
            st["skipped"] = {k: v for k, v in st.get("skipped", {}).items()
                             if v != "unreachable"}
            return st
    return {"domain": domain, "done": {}, "skipped": {}}


def save_state(st):
    # atomic write: two threads saving concurrently must never leave a
    # truncated/partial JSON file behind (observed losing done-entries).
    p = state_path(st["domain"])
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(st, f, indent=1)
    os.replace(tmp, p)


def acquire_run_lock(domain):
    """Prevent two scavenger processes from sweeping the same domain at once.
    Today's incident: a restart raced the old process and both clobbered
    each other's state saves. Returns an open fd to hold, or exits."""
    lock_path = state_path(domain) + ".runlock"
    try:
        fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        # stale lock? if older than 2h, break it
        try:
            age = time.time() - os.path.getmtime(lock_path)
        except OSError:
            age = 999
        if age > 7200:
            os.unlink(lock_path)
            fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        else:
            print(f"another scavenger is running on {domain} "
                  f"(lock {lock_path}, age {int(age)}s) — exiting.", flush=True)
            sys.exit(1)
    os.write(fd, str(os.getpid()).encode())
    return fd


pace_lock = threading.Lock()
_pace_last = [0.0]
PACE = 0.7  # min seconds between fetches, ~1.4 req/s across all workers


def _pace():
    with pace_lock:
        delta = time.time() - _pace_last[0]
        wait = PACE - delta
        if wait > 0:
            time.sleep(wait)
        _pace_last[0] = time.time()


def fetch(url, timeout=60, require_pdf=True):
    for attempt in range(1, 6):
        try:
            _pace()
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
                if len(data) > 100 and data[:4] == b"%PDF":
                    return data
                return None if require_pdf else (data if len(data) > 100 else None)
        except Exception:
            if attempt == 5:
                return None
            time.sleep(min(2 ** attempt, 30))  # 2,4,8,16s backoff — Wayback throttles hard
    return None


def extract(data, ext="pdf"):
    ext = (ext or "pdf").lower().lstrip(".")
    if ext == "pdf":
        if pymupdf is None:
            return ""
        try:
            doc = pymupdf.open(stream=data, filetype="pdf")
            return "".join(p.get_text() for p in doc[:4]).strip()
        except Exception:
            return ""
    # text-ish formats: decode, strip markup, collapse whitespace
    try:
        txt = data.decode("utf-8", "replace")
    except Exception:
        return ""
    if ext in ("html", "htm", "xhtml"):
        txt = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", txt)
        txt = re.sub(r"(?is)<(br|/p|/div|/tr)[^>]*>", "\n", txt)
        txt = re.sub(r"(?s)<[^>]+>", " ", txt)
    txt = (txt.replace("&nbsp;", " ").replace("&amp;", "&")
              .replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"'))
    return " ".join(txt.split()).strip()


def process(item, st):
    ts, orig = item
    key = f"{ts}_{orig}"
    if key in st["done"] or key in st["skipped"]:
        return None
    url_ext = os.path.splitext(orig.split("?")[0])[1].lstrip(".").lower()
    pending_url = ARC.format(ts=ts, url=orig)
    with lock:
        t0 = time.time()
    data = fetch(pending_url, require_pdf=(url_ext == "pdf"))
    if data is None:
        with lock:
            st["skipped"][key] = "unreachable"
            save_state(st)
        return None
    ext = url_ext
    if not ext:
        # extensionless CMS page: infer from magic bytes / content
        if data[:4] == b"%PDF":
            ext = "pdf"
        elif data[:1] in (b"{", b"[") or data.lstrip()[:1] in (b"{", b"["):
            ext = "json"
        else:
            ext = "html"
    txt = extract(data, ext)
    if not txt or len(txt) < 60:
        with lock:
            st["skipped"][key] = "no_text"
            save_state(st)
        return None
    entry = {
        "id": None,  # merged by merge_all_progress style below
        "filename": os.path.basename(orig) or orig,
        "title": title_for(data, ext, orig),
        "type": "document",
        "extension": f".{ext}",
        "size_bytes": 0,
        "source_url": orig,
        "source_site": f"wayback:{st['domain']}",
        "categories": ["Borderland Research"],
        "meta_categories": [],
        "patent_numbers": [],
        "primary_person": "",
        "content_preview": txt[:1000],
        "preview_state": "ok",
        "archive_ts": ts,
        "concepts": [],
        "last_modified": time.strftime("%Y-%m-%d"),
    }
    with lock:
        st["done"][key] = {"ts": ts, "orig": orig, "preview_chars": len(txt)}
        save_state(st)
    return entry


def title_for(data, ext, orig):
    """Prefer the page <title> for CMS/HTML pages; fall back to basename."""
    if ext in ("html", "htm", "xhtml"):
        try:
            raw = data.decode("utf-8", "replace")
            m = re.search(r"(?is)<title[^>]*>(.*?)</title>", raw)
            if m:
                t = " ".join(m.group(1).split()).strip()
                if t and len(t) >= 3:
                    return t[:200]
        except Exception:
            pass
    return (os.path.basename(orig).replace(".pdf", "")
            .replace("_", " ").replace("-", " ") or orig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", required=True)
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--exts", default="pdf",
                    help="comma-separated extensions to harvest (default: pdf). "
                         "e.g. --exts txt,html for text archives")
    ap.add_argument("--mimetype", default=None,
                    help="harvest by CDX mimetype instead of URL extension, "
                         "for extensionless CMS pages (e.g. text/html)")
    ap.add_argument("--urlfilter", default=None,
                    help="extra CDX regex on original URL (e.g. "
                         "'.*/items/show/.*' to take only item pages)")
    args = ap.parse_args()

    print(f"CDX query: {args.domain} (limit {args.limit})...", flush=True)
    exts = tuple(e.strip().lstrip(".").lower()
                 for e in args.exts.split(",") if e.strip())
    items = cdx_list(args.domain, args.limit, exts,
                     mimetype=args.mimetype, urlfilter=args.urlfilter)
    print(f"  archived files found ({'/'.join(exts)}): {len(items)}", flush=True)
    if args.dry_run:
        for ts, u in items[:10]:
            print(f"    {ts[:8]} {u}")
        return

    lock_fd = acquire_run_lock(args.domain)

    st = load_state(args.domain)
    new = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(process, it, st): it for it in items}
        for fut in concurrent.futures.as_completed(futs):
            e = fut.result()
            if e:
                new.append(e)
                print(f"  + {e['title'][:60]} ({e['archive_ts'][:8]})", flush=True)
    print(f"harvested: {len(new)}", flush=True)

    if not new:
        return
    # merge into index.json (dedupe by source_url)
    import index_io
    idx = index_io.load()
    existing = {e.get("source_url") for e in idx if e.get("source_url")}
    added = 0
    next_id = index_io.next_id()
    for e in new:
        if e["source_url"] in existing:
            continue
        e["id"] = next_id
        next_id += 1
        idx.append(e)
        existing.add(e["source_url"])
        added += 1
    index_io.save(idx)
    print(f"merged {added} new entries -> master index ({len(idx)} total)")
    os.close(lock_fd)
    try:
        os.unlink(state_path(args.domain) + ".runlock")
    except OSError:
        pass


if __name__ == "__main__":
    main()
