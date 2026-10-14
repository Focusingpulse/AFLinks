#!/usr/bin/env python3
"""Repair empty-preview coldfusioncommunity entries (burst-throttle recovery).

Re-fetches entries whose content_preview is empty (size_bytes==0 = fetch failed
during the burst-throttled processor run), re-extracts text via pdftotext, and
updates the entry in place. Polite pacing + retries to avoid re-triggering the
server's burst throttle.
"""
import json, re, os, time, subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

# Import helpers from process_generic_cloud by loading it as a module WITHOUT running main
import importlib.util
spec = importlib.util.spec_from_file_location('procmod', os.path.join(SCRIPT_DIR, 'process_generic_cloud.py'))
procmod = importlib.util.module_from_spec(spec)
src = open(os.path.join(SCRIPT_DIR, 'process_generic_cloud.py'), encoding='utf-8').read()
defs = src.split('def main():')[0]
ns = {'__file__': os.path.join(SCRIPT_DIR, 'process_generic_cloud.py'), '__name__': 'procdefs'}
exec(compile(defs, 'process_generic_cloud_defs', 'exec'), ns)
categorize = ns['categorize']
extract_patents = ns['extract_patents']
extract_persons = ns['extract_persons']


def fetch_pdf(url, timeout=50):
    try:
        r = subprocess.run(['curl', '-s', '-L', '--max-time', str(timeout), '-A', UA, url],
                           capture_output=True, timeout=65)
        return r.stdout
    except Exception as e:
        print(f'  CURL-ERR {e}')
        return None


def extract_pdftotext(pdf_bytes, max_chars=2000):
    if not pdf_bytes:
        return ''
    try:
        with open('/tmp/_repair.pdf', 'wb') as f:
            f.write(pdf_bytes)
        r = subprocess.run(['pdftotext', '/tmp/_repair.pdf', '-'], capture_output=True, timeout=60)
        full = re.sub(r'\s+', ' ', r.stdout.decode('utf-8', errors='replace')).strip()
        return full[:max_chars]
    except Exception:
        return ''


def main():
    progress_path = os.path.join(SCRIPT_DIR, 'coldfusioncommunity_net_progress.json')
    entries_path = os.path.join(SCRIPT_DIR, 'coldfusioncommunity_net_entries.json')
    p = json.load(open(progress_path, encoding='utf-8'))
    entries = p['entries']
    empty_idx = [i for i, e in enumerate(entries) if not (e.get('content_preview', '') or '').strip()]
    print('total entries:', len(entries), '| empty to repair:', len(empty_idx))

    repaired = 0
    still_fail = 0
    for i in empty_idx:
        e = entries[i]
        url = e.get('source_url')
        fn = e.get('filename', '')
        data = None
        for attempt in range(3):
            data = fetch_pdf(url)
            if data:
                break
            time.sleep(3)
        preview = ''
        size = 0
        if data:
            preview = extract_pdftotext(data)
            size = len(data)
        if preview.strip():
            e['content_preview'] = preview
            if size:
                e['size_bytes'] = size
            title = os.path.splitext(fn)[0].replace('_', ' ').strip()
            cats, metas = categorize(fn, title, preview, 'coldfusioncommunity.net')
            e['categories'] = cats
            e['meta_categories'] = metas
            persons = extract_persons(fn, title)
            e['primary_person'] = persons[0] if persons else ''
            e['patent_numbers'] = extract_patents(preview)
            e['last_modified'] = time.strftime('%Y-%m-%d %H:%M:%S')
            repaired += 1
        else:
            still_fail += 1
        time.sleep(0.5)
        if repaired and repaired % 20 == 0:
            json.dump(p, open(progress_path, 'w', encoding='utf-8'), ensure_ascii=False)
            json.dump(entries, open(entries_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
            print(f'  ...{repaired} repaired, {still_fail} fail so far', flush=True)

    json.dump(p, open(progress_path, 'w', encoding='utf-8'), ensure_ascii=False)
    json.dump(entries, open(entries_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('DONE repaired:', repaired, 'still fail:', still_fail)


if __name__ == '__main__':
    main()
