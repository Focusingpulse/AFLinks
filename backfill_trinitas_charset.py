#!/usr/bin/env python3
"""
backfill_trinitas_charset.py — re-decode trinitas.ru entries with charset sniffing.

trinitas.ru serves windows-1251; the generic processor decodes as utf-8, so all
Cyrillic titles/previews are replacement-char mojibake. Re-fetch each URL,
sniff charset from <meta charset>, and rewrite title/preview in place.
Resumable: rewrites trinitas_ru_progress.json checkpoint every 50 entries.
"""
import json, os, re, time, urllib.request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BUDGET = int(os.environ.get('PROCESS_BUDGET', '3300'))
MAX_PREVIEW = int(os.environ.get('MAX_PREVIEW', '2000'))
SITE = "trinitas_ru"


def _decode(data):
    """Charset-sniff decode: meta tag first, then utf-8, then cp1251 fallback."""
    head = data[:4096].decode('ascii', errors='ignore').lower()
    m = re.search(r'charset\s*=\s*["\']?\s*([\w\-]+)', head)
    if m:
        enc = m.group(1)
        aliases = {'windows-1251': 'cp1251', 'win-1251': 'cp1251',
                   'windows-1252': 'cp1252', 'iso-8859-1': 'cp1252',
                   'koi8-r': 'koi8-r', 'utf8': 'utf-8', 'ascii': 'ascii'}
        enc = aliases.get(enc.lower(), enc)
        try:
            return data.decode(enc)
        except (LookupError, UnicodeDecodeError):
            pass
    try:
        return data.decode('utf-8')
    except UnicodeDecodeError:
        pass
    for enc in ('cp1251', 'latin-1'):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            continue
    return data.decode('utf-8', errors='replace')


def fetch_html(url, timeout=30):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except Exception as e:
        print(f"  ERR {url[:60]}: {e}", flush=True)
        return None


def clean_text(text):
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', text)
    for pat, rep in [('&amp;', '&'), ('&lt;', '<'), ('&gt;', '>'), ('&quot;', '"'),
                     ('&nbsp;', ' '), (r'&#\d+;', '')]:
        text = re.sub(pat, rep, text)
    return re.sub(r'\s+', ' ', text).strip()


def _save(progress, progress_path, entries_path):
    with open(progress_path, 'w', encoding='utf-8') as f:
        json.dump(progress, f, ensure_ascii=False)
    with open(entries_path, 'w', encoding='utf-8') as f:
        json.dump(progress["entries"], f, ensure_ascii=False, indent=2)


def main():
    entries_path = os.path.join(SCRIPT_DIR, f"{SITE}_entries.json")
    progress_path = os.path.join(SCRIPT_DIR, f"{SITE}_progress.json")

    progress = {"last_processed": -1, "entries": []}
    if os.path.exists(progress_path):
        with open(progress_path, encoding='utf-8') as f:
            prog = json.load(f)
        if prog.get("entries"):
            progress = prog
    if not progress["entries"]:
        with open(entries_path, encoding='utf-8') as f:
            progress["entries"] = json.load(f)

    total = len(progress["entries"])
    start = time.time()
    fixed = 0
    for i, e in enumerate(progress["entries"]):
        if time.time() - start > BUDGET:
            print(f"\nTime budget exceeded, stopping at {i}/{total}", flush=True)
            break
        url = e["source_url"]
        data = fetch_html(url)
        if data is None:
            pass  # keep old entry; resume later
        else:
            text = _decode(data)
            m = re.search(r'<title[^>]*>(.*?)</title>', text, re.I | re.DOTALL)
            if m:
                t = re.sub(r'&amp;', '&', m.group(1))
                e["title"] = re.sub(r'\s+', ' ', t).strip()
            e["content_preview"] = clean_text(text)[:MAX_PREVIEW]
            fixed += 1
        progress["last_processed"] = i
        if (i + 1) % 50 == 0:
            _save(progress, progress_path, entries_path)
            print(f"  [checkpoint {i+1}/{total}, fixed {fixed}]", flush=True)
        time.sleep(0.2)
    _save(progress, progress_path, entries_path)
    print(f"\nDone: rewrote {fixed}/{total} entries, progress {progress['last_processed']+1}/{total}")


if __name__ == "__main__":
    main()