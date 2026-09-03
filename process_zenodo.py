#!/usr/bin/env python3
"""
process_zenodo.py — batch-process the zenodo-rh filelist into index entries.

Downloads each PDF, extracts text (pypdfium2 -> pdftotext -> abstract snippet),
builds entries in the archive's standard schema, and saves progress so each run
advances from where the last one stopped. Safe to run on every cron cycle.

Usage:
    python3 process_zenodo.py            # process up to MAX_PER_RUN records
    python3 process_zenodo.py --max 80   # override batch size
"""
import json, os, re, sys, time, tempfile, subprocess, urllib.request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE = "zenodo-rh"
FILELIST = os.path.join(SCRIPT_DIR, f"{SITE}_filelist.json")
PROGRESS = os.path.join(SCRIPT_DIR, f"{SITE}_progress.json")
ENTRIES = os.path.join(SCRIPT_DIR, f"{SITE}_entries.json")

MAX_PER_RUN = 40          # default batch (quota-friendly); override with --max
BUDGET = 600              # seconds; stop early if exceeded
UA = "Mozilla/5.0 (research archive harvesting; contact via GitHub Focusingpulse)"

from process_generic_cloud import categorize, extract_patents, extract_persons


def get_paths():
    return FILELIST, PROGRESS, ENTRIES


def load_progress(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"last_processed": -1, "entries": []}


def save_progress(progress, progress_path, entries_path):
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False)
    with open(entries_path, "w", encoding="utf-8") as f:
        json.dump(progress["entries"], f, ensure_ascii=False, indent=2)


def fetch(url, timeout=60):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except Exception as e:
        print(f"  ERR download: {e}")
        return None


def extract_pdf_text(pdf_path, max_chars=2000):
    # pypdfium2 first
    try:
        import pypdfium2 as pdfium
        pdf = pdfium.PdfDocument(pdf_path)
        parts = []
        for i in range(min(len(pdf), 10)):
            page = pdf[i]
            tp = page.get_textpage()
            parts.append(tp.get_text_range() or "")
            tp.close()
            page.close()
        pdf.close()
        full = re.sub(r"\s+", " ", " ".join(parts)).strip()
        if full:
            return full[:max_chars]
    except Exception:
        pass
    # poppler fallback
    try:
        out = subprocess.run(
            ["pdftotext", pdf_path, "-"],
            capture_output=True, timeout=30,
        ).stdout.decode("utf-8", errors="replace")
        full = re.sub(r"\s+", " ", out).strip()
        if full:
            return full[:max_chars]
    except Exception:
        pass
    return ""


def clean_title(t):
    t = (t or "").strip()
    t = " ".join(t.split())
    t = t.rstrip(".")
    return t


def build_entry(rec, preview):
    title = clean_title(rec.get("title")) or os.path.splitext(rec.get("filename", ""))[0]
    authors = rec.get("authors", [])
    primary_person = ""
    for a in authors:
        # Zenodo 1234-format: "Kulik, Dean" -> "Dean Kulik".
        if "," in a:
            fam, _, given = a.partition(",")
            fam, given = fam.strip(), given.strip()
            if given.lower().endswith(" " + fam.lower()) or given.lower() == fam.lower():
                name = given  # given name already carries the surname
            else:
                name = given + " " + fam
            name = " ".join(w[:1].upper() + w[1:] for w in name.split() if w)
        else:
            name = a.strip()
        if name:
            primary_person = name
            break

    combined = (rec.get("filename", "") + " " + title + " " + (rec.get("abstract") or "") + " " + primary_person).lower()
    cats, metas = categorize(rec.get("filename", ""), title, rec.get("abstract") or "", SITE)
    # Fallback refinement: pure harmonic/consciousness/aether theory shouldn't
    # default to Borderland Research alone.
    if cats == ["Borderland Research"]:
        if any(k in combined for k in ("harmonic", "codex", "nexus", "quaternion", "consciousness")):
            cats = ["Alternative Physics"]
            metas = ["Challenges to the Standard Model"]

    doi = rec.get("doi", "")
    source_url = f"https://doi.org/{doi}" if doi else rec.get("landing_url", "")

    return {
        "filename": rec.get("filename", ""),
        "title": title,
        "type": "document",
        "extension": os.path.splitext(rec.get("filename", ""))[1] or ".pdf",
        "size_bytes": 0,
        "source_url": source_url,
        "categories": cats,
        "meta_categories": metas,
        "patent_numbers": extract_patents(preview),
        "primary_person": primary_person,
        "content_preview": preview or (rec.get("abstract") or "")[:2000],
        "last_modified": rec.get("publication_date", ""),
        "source_site": SITE,
        "doi": doi,
        "zenodo_record": rec.get("record_id"),
    }


def main():
    max_run = MAX_PER_RUN
    if "--max" in sys.argv:
        try:
            max_run = int(sys.argv[sys.argv.index("--max") + 1])
        except (ValueError, IndexError):
            pass

    filelist_path, progress_path, entries_path = get_paths()
    if not os.path.exists(filelist_path):
        print(f"filelist not found: {filelist_path} — run crawl_zenodo.py first")
        sys.exit(1)

    with open(filelist_path, "r", encoding="utf-8") as f:
        filelist = json.load(f)
    progress = load_progress(progress_path)

    # Idempotency across filelist regenerations: skip DOIs already in the
    # current index.json AND DOIs this progress file has already ingested.
    skip = set()
    try:
        with open(os.path.join(SCRIPT_DIR, "index.json"), "r", encoding="utf-8") as f:
            for e in json.load(f):
                u = e.get("source_url", "")
                if u.startswith("https://doi.org/"):
                    skip.add(u.split("doi.org/")[-1].lower())
    except Exception:
        pass
    for e in progress.get("entries", []):
        u = e.get("source_url", "")
        if u.startswith("https://doi.org/"):
            skip.add(u.split("doi.org/")[-1].lower())

    start = time.time()
    done = 0
    last_idx = progress["last_processed"]

    for i, rec in enumerate(filelist):
        if done >= max_run or (time.time() - start) > BUDGET:
            break
        doi = (rec.get("doi") or "").lower()
        if rec.get("record_id") in {e.get("zenodo_record") for e in progress["entries"]}:
            last_idx = i
            continue
        if doi and doi in skip:
            last_idx = i
            continue
        preview = ""
        data = fetch(rec["url"])
        if data:
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tf:
                tf.write(data)
                tmp = tf.name
            try:
                preview = extract_pdf_text(tmp)
            finally:
                os.unlink(tmp)
        entry = build_entry(rec, preview)
        progress["entries"].append(entry)
        skip.add(doi)
        progress["last_processed"] = i
        last_idx = i
        done += 1
        if done % 5 == 0 or done == max_run:
            save_progress(progress, progress_path, entries_path)
            print(f"  {done}/{max_run} (record {i+1}/{len(filelist)}): {entry['title'][:60]}")
        time.sleep(0.3)

    if last_idx > progress["last_processed"]:
        progress["last_processed"] = last_idx
    save_progress(progress, progress_path, entries_path)
    print(f"zenodo-rh: processed {done} this run; {len(progress['entries'])} total ingested; "
          f"{sum(1 for r in filelist if (r.get('doi') or '').lower() not in skip)} uningested in list")


if __name__ == "__main__":
    main()