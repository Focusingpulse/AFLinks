#!/usr/bin/env python3
"""Progressive teslauniverse enumerator: saves filelist after each section, handles big paging."""
import json, re, subprocess, os, time, sys
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'teslauniverse_com_filelist.json')
DEADLINE = time.time() + 1500  # overall wall budget
def fetch(url):
    if time.time() > DEADLINE:
        return None
    try:
        out = subprocess.run(['curl','-sL','-A',UA,'--max-time','20',url],
                             capture_output=True, text=True, timeout=30).stdout
        return out
    except Exception:
        return ''
def real_items(html, sec):
    out = set()
    for u in re.findall(r'href="(/nikola-tesla/' + sec + r'/[^"?#]+)"', html or ''):
        seg = u.split('/')[-1]
        if seg == sec or u.rstrip('/').endswith(sec):
            continue
        out.add(u)
    return out
def pager_max(html):
    pages = re.findall(r'\?page=(\d+)', html or '')
    return max((int(p) for p in pages), default=0)
allu = set()
for sec in ['patents','documents','articles']:
    html = fetch(f'https://teslauniverse.com/nikola-tesla/{sec}')
    if html is None:
        print(f'{sec}: ABORT (deadline)'); break
    last = pager_max(html)
    cur = real_items(html, sec)
    done = 0
    for pg in range(1, last+1):
        if time.time() > DEADLINE:
            print(f'{sec}: deadline hit at pg {pg}/{last}'); break
        h = fetch(f'https://teslauniverse.com/nikola-tesla/{sec}?page={pg}')
        cur |= real_items(h, sec)
        done += 1
    allu |= cur
    print(f'{sec}: pages {done+1}/{last+1} items {len(cur)}', flush=True)
    # progressive save
    entries = [{'url': 'https://teslauniverse.com'+u, 'filename': u.strip('/').split('/')[-1]+'.html'} for u in sorted(allu)]
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=1)
    print(f'  filelist now {len(entries)}', flush=True)
print('FINAL:', len(allu), flush=True)
