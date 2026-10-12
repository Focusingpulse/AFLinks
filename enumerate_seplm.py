#!/usr/bin/env python3
"""Enumerate all seplm.ru section article URLs via pagination; diff vs filelist."""
import json, re, time, urllib.request, os, sys

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def fetch(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode('utf-8', errors='replace')
        except Exception as e:
            if i == tries - 1:
                print(f'  ERR {url}: {e}')
                return None
            time.sleep(2)

def enumerate_section(section):
    urls = set()
    pg = 1
    while True:
        url = f'http://lenr.seplm.ru/{section}/' if pg == 1 else f'http://lenr.seplm.ru/{section}/?pg={pg}'
        html = fetch(url)
        if not html:
            break
        found = set(re.findall(r'href="(http://lenr\.seplm\.ru/' + re.escape(section) + r'/[\w\-\.%%]+)"', html))
        new = found - urls
        if not new and pg > 1:
            # check if page has any section-relative links at all (dead end)
            anylinks = re.findall(r'href="(http://lenr\.seplm\.ru/' + re.escape(section) + r'/[\w\-\.%%]+)"', html)
            if not anylinks:
                break
            # if paginator present, keep going
        prev = len(urls)
        urls |= found
        # detect next page via paginator
        has_next = re.search(r'pg=%d' % (pg + 1), html)
        print(f'  {section} pg{pg}: +{len(urls)-prev} (total {len(urls)})')
        if not has_next:
            break
        pg += 1
        if pg > 300:
            break
    return urls

def main():
    sections = sys.argv[1:] or ['articles', 'novosti', 'seminary', 'konferentsii', 'memorial', 'galereya-slavy']
    all_urls = set()
    for s in sections:
        print('===', s)
        all_urls |= enumerate_section(s)
    print('Total enumerated:', len(all_urls))
    fl = json.load(open(os.path.join(SCRIPT_DIR, 'lenr_seplm_ru_filelist.json')))
    fl_urls = {e['url'] for e in fl}
    new = all_urls - fl_urls
    print('Filelist len:', len(fl_urls))
    print('Genuinely NEW vs filelist:', len(new))
    for u in sorted(new):
        print('NEW:', u)
    json.dump(sorted(all_urls), open('/tmp/seplm_all_urls.json', 'w'), ensure_ascii=False, indent=1)
    json.dump(sorted(new), open('/tmp/seplm_new_urls.json', 'w'), ensure_ascii=False, indent=1)

main()
