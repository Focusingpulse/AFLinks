#!/usr/bin/env python3
"""
Phase 1: Crawl tuks.nl open directories and wiki, save file list to JSON.
Fast - no downloads, just directory listing parsing.
"""
import re, json, time, urllib.parse, urllib.request, sys

BASE_URL = "http://www.tuks.nl"
OUTPUT = "D:/rex_archive/tuks_filelist.json"
visited = set()
all_files = []

def fetch(url, timeout=15):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except Exception as e:
        print(f"  ERR {url}: {e}")
        return None

def crawl_dir(url):
    if url in visited: return
    visited.add(url)
    print(f"DIR: {url}", flush=True)
    data = fetch(url)
    if data is None: return
    text = data.decode('utf-8', errors='replace')
    
    files = re.findall(r'<td class="file"><a href="([^"]+)">', text)
    dirs = re.findall(r'<td class="dir"><a href="([^"]+)">', text)
    
    for f in files:
        if f in ('.', '..') or f.startswith('index.html'): continue
        file_url = url.rstrip('/') + '/' + urllib.parse.quote(f)
        all_files.append({"url": file_url, "filename": f})
    
    for d in dirs:
        if d in ('.', '..'): continue
        dir_url = url.rstrip('/') + '/' + urllib.parse.quote(d, safe='') 
        if not dir_url.endswith('/'): dir_url += '/'
        time.sleep(0.2)
        crawl_dir(dir_url)

# Crawl directories
for d in [f"{BASE_URL}/pdf/", f"{BASE_URL}/docs/", f"{BASE_URL}/WFCProject/"]:
    crawl_dir(d)
    time.sleep(0.3)

# Crawl wiki
print("\n--- Wiki articles ---", flush=True)
wiki_data = fetch(f"{BASE_URL}/wiki/index.php/Main/HomePage")
if wiki_data:
    text = wiki_data.decode('utf-8', errors='replace')
    wiki_links = re.findall(r'href="(http://www\.tuks\.nl/wiki/index\.php/Main/[^"?]+)"', text)
    wiki_links = sorted(set(l for l in wiki_links if not l.endswith('HomePage') and 'action=' not in l))
    for wl in wiki_links:
        all_files.append({"url": wl, "filename": wl.split('/Main/')[-1] + '.html', "is_wiki": True})
    print(f"Found {len(wiki_links)} wiki articles")

# Save
with open(OUTPUT, 'w', encoding='utf-8') as f:
    json.dump(all_files, f, ensure_ascii=False, indent=2)

print(f"\nTotal files found: {len(all_files)}")
print(f"Saved to {OUTPUT}")
