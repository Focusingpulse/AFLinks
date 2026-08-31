#!/usr/bin/env python3
"""fix_previews.py — fill in missing content_previews for archived PDFs.

Downloads each preview-less PDF, extracts text (pymupdf), and falls back to
Tesseract OCR for scanned/image PDFs. Idempotent + stateful: entries that
fail (unreachable/no text) get a preview_state marker so later runs skip
them instead of re-hammering dead hosts.

Usage:
  python3 fix_previews.py --limit 300 --workers 4 [--host vixra.org]
  python3 fix_previews.py --retry-unreachable   # re-attempt marked entries
"""
import argparse, json, os, re, sys, threading, time, concurrent.futures
import urllib.request, urllib.error

try:
    import pymupdf
except Exception:
    pymupdf = None

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(HERE, "index.json")
UA = "Mozilla/5.0 (AFLinks preview-fixer; research archive)"
PREVIEW_CHARS = 1000
MIN_TEXT = 60
lock = threading.Lock()


def fetch(url, timeout=30):
    for attempt in (1, 2):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
                if data[:4] == b"%PDF" and len(data) > 100:
                    return data
                return None
        except Exception:
            if attempt == 2:
                return None
            time.sleep(1)
    return None


def extract_text(data):
    if pymupdf is None:
        return ""
    try:
        doc = pymupdf.open(stream=data, filetype="pdf")
        txt = "".join(p.get_text() for p in doc[:4])
        return (txt or "").strip()
    except Exception:
        return ""


def ocr_text(data, max_pages=2):
    """Render first pages + Tesseract OCR for scanned PDFs."""
    if pymupdf is None:
        return ""
    try:
        doc = pymupdf.open(stream=data, filetype="pdf")
        out = []
        for i in range(min(max_pages, len(doc))):
            pix = doc[i].get_pixmap(dpi=150)
            img = pix.tobytes("png")
            r = subprocess_run_tesseract(img)
            if r:
                out.append(r)
        return "\n".join(out).strip()
    except Exception:
        return ""


def subprocess_run_tesseract(png_bytes):
    import subprocess
    import tempfile
    try:
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
            f.write(png_bytes)
            path = f.name
        r = subprocess.run(["tesseract", path, "stdout", "--psm", "6"],
                           capture_output=True, timeout=120)
        os.unlink(path)
        return r.stdout.decode("utf-8", errors="replace").strip()
    except Exception:
        return ""


def process(e):
    url = e.get("source_url") or ""
    if not url:
        return e, "no_url"
    if e.get("preview_state") and e.get("preview_state") != "retry":
        return e, e["preview_state"]
    data = fetch(url)
    if data is None:
        e["preview_state"] = "unreachable"
        return e, "unreachable"
    txt = extract_text(data)
    if len(txt) < MIN_TEXT:
        txt = ocr_text(data)
    if txt:
        e["content_preview"] = txt[:PREVIEW_CHARS]
        e["preview_state"] = "ok"
        return e, "ok"
    e["preview_state"] = "no_text"
    return e, "no_text"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--host", default="", help="only process URLs containing this host")
    ap.add_argument("--retry-unreachable", action="store_true")
    ap.add_argument("--commit-every", type=int, default=20)
    args = ap.parse_args()

    with open(INDEX, encoding="utf-8") as f:
        data = json.load(f)

    targets = []
    for e in data:
        if (e.get("content_preview") or "").strip():
            continue
        url = e.get("source_url") or ""
        if not re.search(r"\.pdf$", url, re.I):
            continue
        if args.host and args.host not in url:
            continue
        if e.get("preview_state") == "unreachable" and not args.retry_unreachable:
            continue
        targets.append(e)
    if args.limit:
        targets = targets[: args.limit]

    print(f"targets: {len(targets)} (workers={args.workers}, host={args.host or 'all'})", flush=True)
    stats = {"ok": 0, "unreachable": 0, "no_text": 0}
    done = 0
    t0 = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(process, e): e for e in targets}
        for fut in concurrent.futures.as_completed(futs):
            e, status = fut.result()
            stats[status] = stats.get(status, 0) + 1
            done += 1
            if done % args.commit_every == 0:
                with open(INDEX, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False)
                print(f"  [{done}/{len(targets)}] saved checkpoint | "
                      f"ok={stats['ok']} unreachable={stats['unreachable']} no_text={stats['no_text']} | "
                      f"{time.time()-t0:.0f}s", flush=True)
    with open(INDEX, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    print(f"DONE in {time.time()-t0:.0f}s: {stats}", flush=True)


if __name__ == "__main__":
    main()