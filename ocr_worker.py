#!/usr/bin/env python3
"""
ocr_worker.py -- cloud OCR worker for the AFLinks archive (Scooter).

Scope (mirrors repo ocr_previews.py): rexresearch.com PDF entries whose
content_preview is empty. Downloads the PDF, renders page 1 @ 100 DPI via
pymupdf, runs Tesseract (--psm 6), writes the first 500 chars as
content_preview. Resumable; batched saves + git commit/push.

Usage:
  python3 ocr_worker.py --limit 200 --workers 2 --batch 100
  python3 ocr_worker.py --status          # print backlog/state without running
  python3 ocr_worker.py --no-push         # write locally, no git push
"""
import argparse
import concurrent.futures
import json
import os
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request

import pymupdf  # installed in /tmp/ocr-venv (or system)

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "ocr_worker_state.json")
LOG = os.path.join(HERE, "ocr_worker.log")

socket.setdefaulttimeout(30)
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}

AUTHOR = "Scooter <scooter@letta.com>"


def log(msg):
    line = f"{time.strftime('%Y-%m-%d %H:%M:%S')}Z {msg}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


# ---------------- state ----------------
def load_state():
    if os.path.isfile(STATE):
        try:
            return json.load(open(STATE, encoding="utf-8"))
        except Exception:
            return {"done": {}, "updated": 0}
    return {"done": {}, "updated": 0}


def save_state(s):
    tmp = STATE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(s, f, ensure_ascii=False, separators=(",", ":"))
    os.replace(tmp, STATE)


# ---------------- ocr ----------------
def download_pdf(url):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        if len(data) >= 100 and data[:4] == b"%PDF":
            return data
        return None
    except Exception:
        return None


def ocr_pdf(pdf_bytes, max_pages=1):
    try:
        doc = pymupdf.open(stream=pdf_bytes, filetype="pdf")
        parts = []
        for i in range(min(max_pages, len(doc))):
            pix = doc[i].get_pixmap(dpi=100)
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
                f.write(pix.tobytes("png"))
                path = f.name
            try:
                r = subprocess.run(
                    ["tesseract", path, "stdout", "--psm", "6"],
                    capture_output=True, text=True, timeout=60,
                )
                if r.stdout and r.stdout.strip():
                    parts.append(r.stdout.strip())
            except Exception:
                pass
            finally:
                try:
                    os.unlink(path)
                except OSError:
                    pass
        doc.close()
        if parts:
            c = " ".join(" ".join(parts).split())
            return c[:500] if len(c) > 20 else None
        return None
    except Exception:
        return None


def process_one(url):
    """Returns (reason, text): reason in {'ok','dl','ocr'} — dl = dead link
    (download/HTTP failed), ocr = downloaded but produced no usable text."""
    pdf = download_pdf(url)
    if pdf is None:
        return ("dl", None)
    text = ocr_pdf(pdf)
    if text is None:
        return ("ocr", None)
    return ("ok", text)


# ---------------- git ----------------
def git(cmd):
    r = subprocess.run(["git"] + cmd, capture_output=True, text=True, cwd=HERE)
    return r.returncode, r.stdout, r.stderr


def commit_push(batch_size, updated_batch):
    msg = f"ocr worker: +{updated_batch} scanned-PDF previews (batch {batch_size})"
    git(["add", "index_shards"])
    git(["commit", "-m", msg, "--author", AUTHOR])
    rc, out, err = git(["pull", "--rebase", "origin", "main"])
    if rc != 0:
        log(f"  WARN rebase failed ({err.strip()[:120]}); retrying once")
        git(["rebase", "--abort"])
        r2, o2, e2 = git(["pull", "origin", "main"])
        if r2 != 0:
            log(f"  PUSH SKIPPED this batch: {e2.strip()[:160]}")
            return False
    rc, out, err = git(["push", "origin", "main"])
    if rc != 0:
        log(f"  PUSH FAILED: {err.strip()[:160]}")
        return False
    head = git(["rev-parse", "HEAD"])[1].strip()
    log(f"  pushed {head}")
    return True


# ---------------- main ----------------
def build_backlog(docs):
    """(url, doc) pairs needing OCR, not yet attempted."""
    state = load_state()
    done = state["done"]
    backlog = []
    for d in docs:
        u = d.get("source_url") or ""
        if "rexresearch.com/" not in u or not u.endswith(".pdf"):
            continue
        if len(d.get("content_preview") or "") >= 20:
            continue
        if u in done:
            continue
        backlog.append((u, d))
    return backlog, state


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=1000)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--batch", type=int, default=100)
    ap.add_argument("--no-push", action="store_true")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()

    # freshen local copy first
    git(["pull", "--rebase", "origin", "main"])

    import index_io
    docs = index_io.load()
    log(f"index loaded: {len(docs)} docs")

    backlog, state = build_backlog(docs)
    log(f"OCR backlog (rexresearch PDFs w/o preview, not attempted): {len(backlog)}")
    if args.status:
        # also report already-done + overall preview coverage
        done_ok = sum(1 for u, s in state["done"].items() if s == "ok")
        print(json.dumps({
            "backlog": len(backlog),
            "state_done": len(state["done"]),
            "state_ok": done_ok,
        }, indent=2))
        return
    if not backlog:
        log("backlog empty -- nothing to do")
        return

    jobs = [u for u, _ in backlog[: args.limit]]
    log(f"running up to {len(jobs)} PDFs with {args.workers} workers, batch {args.batch}")

    updated_total = state.get("updated", 0)
    updated_batch = 0
    failed = 0
    dead_links = {}
    started = time.time()
    last_save = 0

    # map url -> doc index
    idx = {d.get("source_url"): i for i, d in enumerate(docs)}

    def handle(future, u):
        nonlocal updated_total, updated_batch, failed
        try:
            reason, text = future.result()
        except Exception:
            reason, text = "err", None
        if text:
            docs[idx[u]]["content_preview"] = text
            state["done"][u] = "ok"
            updated_total += 1
            updated_batch += 1
        else:
            state["done"][u] = reason
            failed += 1
            if reason == "dl":
                dead_links[u] = (docs[idx[u]].get("title") or "")[:80]

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(process_one, u): u for u in jobs}
        completed = 0
        for fut in concurrent.futures.as_completed(futs):
            handle(fut, futs[fut])
            completed += 1
            if completed % 10 == 0:
                el = time.time() - started
                rate = completed / el if el else 0
                remain = (len(jobs) - completed) / rate if rate else 0
                log(f"  [{completed}/{len(jobs)}] updated_batch={updated_batch} "
                    f"failed={failed} | {rate:.1f}/s | eta {remain:.0f}s")
            # periodic save + push
            if completed - last_save >= args.batch:
                last_save = completed
                state["updated"] = updated_total
                save_state(state)
                index_io.save(docs)
                log(f"  saved@ {completed} (updated_total {updated_total})")
                if not args.no_push:
                    git(["pull", "--rebase", "origin", "main"])
                    commit_push(completed, updated_batch)

    state["updated"] = updated_total
    save_state(state)
    index_io.save(docs)
    # dump dead-link report (worker-area only, not committed to repo)
    if dead_links:
        with open(os.path.join(HERE, "ocr_dead_links.json"), "w", encoding="utf-8") as f:
            json.dump(dead_links, f, ensure_ascii=False, indent=1)
        log(f"dead-link report: {len(dead_links)} urls -> ocr_dead_links.json")
    log(f"final save: updated_total={updated_total}, failed={failed}")
    if not args.no_push and updated_batch > 0:
        commit_push(completed, updated_batch)

    elapsed = time.time() - started
    log(f"done in {elapsed:.0f}s | +{updated_batch} this run | {failed} failed")


if __name__ == "__main__":
    main()
