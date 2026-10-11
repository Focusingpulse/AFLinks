#!/usr/bin/env python3
"""
Dedicated crawler for lenr.com.cn — "冷聚变世界" (Cold Fusion World), a Chinese
LENR document library (文献下载, catid=13). Foreign-language lane.

The download flow is a two-hop signed dance:
  show page  ->  ?m=content&c=down&a_k=<signed>   (hop 1: a "check" page)
  hop 1 page -> ?m=content&c=down&a=download&a_k=<signed>  (hop 2: the actual file)
Signed tokens are EPHEMERAL (change per page fetch), so this crawler resolves
them live instead of storing stale signed URLs in a filelist.

The stable identity for dedupe / archive is the canonical show-page URL:
  http://www.lenr.com.cn/index.php?a=show&c=index&catid=13&id=<N>

Usage:
  python3 process_lenr_com_cn.py            # enumerate catid=13, process all docs
  python3 process_lenr_com_cn.py --dry      # enumerate + report only
Resumable: progress saved to lenr_com_cn_progress.json after each doc.
"""
import os, re, json, time, subprocess, tempfile, urllib.request, sys, html as html_module

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = "http://www.lenr.com.cn"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
MAX_PREVIEW = int(os.environ.get('MAX_PREVIEW', '2000'))
DRY = "--dry" in sys.argv

SITE_CODE = "lenr_com_cn"
PATHS = {
    "filelist": os.path.join(SCRIPT_DIR, f"{SITE_CODE}_filelist.json"),
    "progress": os.path.join(SCRIPT_DIR, f"{SITE_CODE}_progress.json"),
    "entries": os.path.join(SCRIPT_DIR, f"{SITE_CODE}_entries.json"),
    "complete": os.path.join(SCRIPT_DIR, f"{SITE_CODE}_complete.txt"),
}

def fetch(url, timeout=30, referer=BASE + "/"):
    """GBK site. Returns raw bytes or None."""
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Referer': referer})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except Exception as e:
        print(f"  FETCH-ERR {e}")
        return None

def dec_gbk(data):
    try:
        return data.decode('gbk', errors='replace')
    except Exception:
        return data.decode('utf-8', errors='replace')

def load_progress():
    if os.path.exists(PATHS["progress"]):
        with open(PATHS["progress"], encoding='utf-8') as f:
            return json.load(f)
    return {"last_processed": -1, "entries": []}

def save_progress(progress):
    with open(PATHS["progress"], 'w', encoding='utf-8') as f:
        json.dump(progress, f, ensure_ascii=False)
    with open(PATHS["entries"], 'w', encoding='utf-8') as f:
        json.dump(progress["entries"], f, ensure_ascii=False, indent=2)

def enumerate_docs():
    """Fetch catid=13 list pages (page=1..7), return sorted unique ids."""
    doc_ids = set()
    for page in range(1, 8):
        url = f"{BASE}/index.php?a=lists&c=index&catid=13&m=content&page={page}"
        data = fetch(url, timeout=25)
        if not data:
            continue
        html = dec_gbk(data)
        ids = set(int(m) for m in re.findall(r'a=show&catid=13&id=(\d+)', html))
        doc_ids |= ids
    return sorted(doc_ids)

def resolve_pdf(show_url):
    """Return (pdf_bytes, canonical_title) following the two-hop signed dance.

    show page -> hop1 (c=down&a_k=...) -> hop2 (a=download&a_k=...) -> file.
    """
    data = fetch(show_url)
    if not data:
        return None, ""
    html = dec_gbk(data)
    # title
    tm = re.search(r'<title>([^<]*)</title>', html)
    title = tm.group(1).strip() if tm else ""
    # strip the site suffix
    title = re.sub(r'\s*-\s*文献下载.*$', '', title).strip()
    title = re.sub(r'\s*-\s*冷聚变世界.*$', '', title).strip()
    # hop 1 link
    m1 = re.search(r'index\.php\?m=content&c=down&a_k=([^\s"\'&]+)', html)
    if not m1:
        m1 = re.search(r'(\?m=content&c=down&a_k=[^\s"\'&]+)', html)
    if not m1:
        return None, title
    hop1_url = BASE + "/index.php?m=content&c=down&a_k=" + m1.group(1)
    h1 = fetch(hop1_url)
    if not h1:
        return None, title
    h1html = dec_gbk(h1)
    m2 = re.search(r'\?m=content&c=down&a=download&a_k=([^\s"\'&]+)', h1html)
    if not m2:
        m2 = re.search(r'a=download&a_k=([^\s"\'&]+)', h1html)
    if not m2:
        return None, title
    hop2_url = BASE + "/?m=content&c=down&a=download&a_k=" + m2.group(1)
    # final fetch as curl with referer (urllib got PDF fine too, but curl is robust)
    try:
        r = subprocess.run(['curl', '-s', '-L', '--max-time', '60',
                            '-A', UA, '-e', BASE + '/', hop2_url],
                           capture_output=True, timeout=70)
        pdf = r.stdout
        if pdf and pdf[:4] == b'%PDF':
            return pdf, title
    except Exception as e:
        print(f"  CURL-ERR {e}")
    return None, title

def extract_pdf_text(pdf_path):
    try:
        r = subprocess.run(['pdftotext', pdf_path, '-'], capture_output=True, timeout=90)
        full = re.sub(r'\s+', ' ', r.stdout.decode('utf-8', errors='replace')).strip()
        return full[:MAX_PREVIEW]
    except Exception:
        return ""

def slugify(title, docid):
    s = re.sub(r'[^\w\u4e00-\u9fff]+', '_', title).strip('_')
    s = s[:40]
    return (s or f"doc{docid}") + ".pdf"

def main():
    doc_ids = enumerate_docs()
    print(f"Enumerated {len(doc_ids)} docs in catid=13", flush=True)
    if DRY:
        json.dump([{"id": i, "url": f"{BASE}/index.php?a=show&c=index&catid=13&id={i}"} for i in doc_ids],
                  open(PATHS["filelist"], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print("DRY — filelist seeded only")
        sys.exit(0)

    if not os.path.exists(PATHS["filelist"]):
        json.dump([{"id": i, "url": f"{BASE}/index.php?a=show&c=index&catid=13&id={i}"} for i in doc_ids],
                  open(PATHS["filelist"], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    filelist = json.load(open(PATHS["filelist"], encoding='utf-8'))
    print(f"Filelist: {len(filelist)} docs", flush=True)

    progress = load_progress()
    start_idx = progress["last_processed"] + 1
    entries = progress["entries"]
    print(f"Resuming from index {start_idx}, {len(entries)} entries already done", flush=True)

    processed = 0
    for i in range(start_idx, len(filelist)):
        doc = filelist[i]
        show_url = doc["url"]
        docid = doc["id"]
        filename = f"id{docid}_" + re.sub(r'[^\w\u4e00-\u9fff]+', '_', str(docid)) + ".pdf"
        prev = ""
        title = f"doc{docid}"
        stype = "document"

        pdf, page_title = resolve_pdf(show_url)
        if pdf:
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
                tmp.write(pdf)
                tmp_path = tmp.name
            prev = extract_pdf_text(tmp_path)
            os.unlink(tmp_path)
            if page_title:
                title = page_title
            filename = slugify(title, docid)
            # size
            size = len(pdf)
        else:
            # fallback: no fetchable PDF -> record an HTML entry for the show page
            data = fetch(show_url)
            if data:
                html = dec_gbk(data)
                tm = re.search(r'<title>([^<]*)</title>', html)
                if tm:
                    title = re.sub(r'\s*-\s*文献下载.*$', '', tm.group(1)).strip()
                # pull article content
                body = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
                body = re.sub(r'<style[^>]*>.*?</style>', '', body, flags=re.DOTALL)
                body = re.sub(r'<[^>]+>', ' ', body)
                body = html_module.unescape(body)
                body = re.sub(r'\s+', ' ', body).strip()
                prev = body[:MAX_PREVIEW]
                size = len(data)
                stype = "document"
                filename = slugify(title, docid)

        cats = ['LENR / Cold Fusion'] if any(k in (title + ' ' + prev).lower()
                for k in ['lenr', 'cold fusion', '冷聚变', '冷核', '凝聚态', 'fusion', 'nuclear',
                          'e-cat', 'rossi', 'focardi', 'palladium', '镍氢', '氘']) else ['Borderland Research']
        metas = ['Alternative Energy Technologies'] if 'LENR / Cold Fusion' in cats else ['Challenges to the Standard Model']

        entry_out = {
            'id': -1,
            'filename': filename,
            'title': title,
            'type': stype,
            'extension': '.pdf',
            'size_bytes': size if pdf else 0,
            'source_url': show_url,
            'categories': cats,
            'meta_categories': metas,
            'patent_numbers': [],
            'primary_person': "",
            'content_preview': prev,
            'last_modified': time.strftime('%Y-%m-%d'),
            'source_site': SITE_CODE,
        }
        entries.append(entry_out)
        processed += 1
        progress["last_processed"] = i
        progress["entries"] = entries
        print(f"[{i+1}/{len(filelist)}] id{docid} | {title[:50]} | {len(prev)}ch preview", flush=True)

        if processed % 10 == 0:
            save_progress(progress)
            print(f"  [Saved {len(entries)} entries]", flush=True)
        time.sleep(0.4)

    save_progress(progress)
    print(f"\nProcessed {processed} docs this run")
    print(f"Total entries: {len(entries)}")
    if progress["last_processed"] + 1 >= len(filelist):
        print("ALL DOCS PROCESSED!")
        with open(PATHS["complete"], 'w') as f:
            f.write(f"Complete: {len(entries)} entries at {time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == '__main__':
    main()
