#!/usr/bin/env python3
"""Enumerate borderlands.de tree (net_pdf/, Links/, infos.files.php3, misc) -> diff vs filelist."""
import json, re, time, urllib.request, urllib.parse, os
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0'
def fetch(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode('latin-1', 'replace')
        except Exception as e:
            if i == tries - 1:
                print('  ERR', url, str(e)[:80]); return None
            time.sleep(1.5)
def pdfs_on(html, base):
    out = set()
    for m in re.findall(r'(?:href|src)="([^"]+)"', html or ''):
        if not m or m.startswith('#') or m.startswith('mailto'): continue
        low = m.lower()
        if low.endswith('.pdf'):
            out.add(urllib.parse.urljoin(base, m))
        elif low.endswith('.php3') or low.endswith('.htm') or low.endswith('.html'):
            pass
    return out
# start with the directory-list pages
starts = ['http://www.borderlands.de/', 'http://www.borderlands.de/infos.files.php3',
          'http://www.borderlands.de/Links/', 'http://www.borderlands.de/net_pdf/',
          'http://www.borderlands.de/Links/net.shtml']
all_pdfs = set()
visited = set()
queue = list(starts)
while queue:
    u = queue.pop(0)
    if u in visited: continue
    visited.add(u)
    html = fetch(u)
    if html is None: continue
    new_pdf = pdfs_on(html, u) - all_pdfs
    if new_pdf:
        all_pdfs |= new_pdf
        print(f'+{len(new_pdf)} pdfs (total {len(all_pdfs)}) @ {u}')
    # follow Links/ subsections one level
    for m in re.findall(r'href="([^"]+\.(?:htm|html|php3))"', html):
        full = urllib.parse.urljoin(u, m)
        if 'borderlands.de/Links' in full and full not in visited:
            queue.append(full)
print('TOTAL pdfs found:', len(all_pdfs))
fl = json.load(open('borderlands_de_filelist.json'))
fl_urls = set()
for e in fl:
    u = e.get('url','')
    fl_urls.add(u if u.startswith('http') else 'http://www.borderlands.de/' + u)
# normalize
norm = lambda u: urllib.parse.unquote(u).replace('http://www.borderlands.de','http://www.borderlands.de')
new = {norm(u) for u in all_pdfs} - fl_urls
new2 = {u for u in new if u not in fl_urls and norm(u) not in fl_urls}
print('filelist len:', len(fl_urls))
print('GENUINELY NEW vs filelist:', len(new2))
for u in sorted(new2): print('  NEW:', u)
json.dump(sorted(all_pdfs), open('/tmp/borderlands_all_pdfs.json','w'), indent=1)
json.dump(sorted(new2), open('/tmp/borderlands_new_pdfs.json','w'), ensure_ascii=False, indent=1)
