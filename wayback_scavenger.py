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
ARC = "https://web.archive.org/web/{ts}id_/{url}"   # id_ = original bytes
ACCEPTED_EXTS = (".pdf", ".txt", ".htm", ".html")
lock = threading.Lock()

try:
    import pymupdf
except Exception:
    pymupdf = None


def cdx_list(domain, limit=0):
    """Return [(timestamp, original_url)] for archived PDFs under domain."""
    url = (f"{CDX}?url={domain}&matchType=domain&output=json&collapse=digest"
           f"&fl=timestamp,original&filter=original:.*\\.pdf$&filter=statuscode:200")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        rows = json.load(r)
    out = [(t, o) for t, o in rows[1:]]  # drop header row
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
            return json.load(f)
    return {"domain": domain, "done": {}, "skipped": {}}


def save_state(st):
    with open(state_path(st["domain"]), "w", encoding="utf-8") as f:
        json.dump(st, f, indent=1)


def fetch(url, timeout=60):
    for attempt in (1, 2):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
                if len(data) > 100 and data[:4] == b"%PDF":
                    return data
                return None
        except Exception:
            if attempt == 2:
                return None
            time.sleep(2)
    return None


def extract(data):
    if pymupdf is None:
        return ""
    try:
        doc = pymupdf.open(stream=data, filetype="pdf")
        return "".join(p.get_text() for p in doc[:4]).strip()
    except Exception:
        return ""


def process(item, st):
    ts, orig = item
    key = f"{ts}_{orig}"
    if key in st["done"] or key in st["skipped"]:
        return None
    pending_url = ARC.format(ts=ts, url=orig)
    with lock:
        t0 = time.time()
    data = fetch(pending_url)
    if data is None:
        with lock:
            st["skipped"][key] = "unreachable"
            save_state(st)
        return None
    txt = extract(data)
    if not txt or len(txt) < 60:
        with lock:
            st["skipped"][key] = "no_text"
            save_state(st)
        return None
    entry = {
        "id": None,  # merged by merge_all_progress style below
        "filename": os.path.basename(orig) or orig,
        "title": os.path.basename(orig).replace(".pdf", "").replace("_", " ").replace("-", " ") or orig,
        "type": "document",
        "extension": ".pdf",
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", required=True)
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print(f"CDX query: {args.domain} (limit {args.limit})...", flush=True)
    items = cdx_list(args.domain, args.limit)
    print(f"  archived PDFs found: {len(items)}", flush=True)
    if args.dry_run:
        for ts, u in items[:10]:
            print(f"    {ts[:8]} {u}")
        return

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
    with open(INDEX, encoding="utf-8") as f:
        idx = json.load(f)
    existing = {e.get("source_url") for e in idx if e.get("source_url")}
    added = 0
    for e in new:
        if e["source_url"] in existing:
            continue
        e["id"] = max((x.get("id", 0) for x in idx), default=0) + 1
        idx.append(e)
        existing.add(e["source_url"])
        added += 1
    with open(INDEX, "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False)
    print(f"merged {added} new entries -> index.json ({len(idx)} total)")


if __name__ == "__main__":
    main()