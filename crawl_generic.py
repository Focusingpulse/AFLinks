#!/usr/bin/env python3
"""
Generic crawler for multiple site types:
- apache_dir: Apache directory listings (like tuks.nl)
- html_link_scrape: HTML pages with links to PDFs/docs
- api_listing: Structured listing pages (like viXra.org)
- wayback_scrape: Scrape archived pages from Wayback Machine (for dead sites)

Usage: python crawl_generic.py <site_name>
Reads site_queue.json for site config, outputs <site_name>_filelist.json
"""
import os, re, json, time, signal, urllib.parse, urllib.request, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
QUEUE_PATH = os.path.join(SCRIPT_DIR, "site_queue.json")

# --- Progressive checkpointing ----------------------------------------------
# Timeout-safe crawling: every N pages (or on SIGTERM) we save the visited set
# + accumulated file list to <site>_crawl_state.json, so a run killed by the
# cron's time budget resumes where it left off instead of losing everything.
CHECKPOINT_EVERY = 20          # pages
_last_checkpoint = [0.0]       # [timestamp]

def _site_slug(site_name):
    return site_name.replace('.', '_').replace('/', '_')

def _save_checkpoint(site_name, visited, files):
    """Write partial crawl state (visited urls + file list) to disk."""
    state_path = os.path.join(SCRIPT_DIR, f"{_site_slug(site_name)}_crawl_state.json")
    tmp = state_path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump({"visited": sorted(visited), "files": files}, f, ensure_ascii=False)
    os.replace(tmp, state_path)  # atomic

def _load_checkpoint(site_name):
    state_path = os.path.join(SCRIPT_DIR, f"{_site_slug(site_name)}_crawl_state.json")
    if not os.path.exists(state_path):
        return None
    try:
        with open(state_path, "r", encoding="utf-8") as f:
            state = json.load(f)
        return state
    except Exception:
        return None

def _maybe_checkpoint(site_name, visited, files, force=False):
    global _last_checkpoint
    now = time.time()
    if force or (now - _last_checkpoint[0]) >= CHECKPOINT_EVERY:
        try:
            _save_checkpoint(site_name, visited, files)
            _last_checkpoint[0] = now
        except Exception as e:
            print(f"  [checkpoint warn] {e}", flush=True)

def fetch_url(url, timeout=20):
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5'
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except Exception as e:
        print(f"  ERR: {url}: {e}")
        return None

def crawl_apache_dir(url, visited, files, base_url, depth=0, max_depth=10):
    """Crawl Apache-style directory listings."""
    if url in visited or depth > max_depth:
        return
    visited.add(url)
    print(f"  DIR: {url}", flush=True)
    
    data = fetch_url(url)
    if data is None:
        return
    
    text = data.decode('utf-8', errors='replace')
    
    # Apache directory listing patterns
    file_patterns = [
        r'<td class="file"><a href="([^"]+)">',  # tuks.nl style
        r'<a href="([^"]+\.(?:pdf|PDF|doc|DOC|rtf|RTF|txt|TXT|html|HTML|htm|HTM|mp3|MP3|mp4|MP4|zip|ZIP))"',  # generic
        r'href="([^"]+\.(?:pdf|PDF|doc|DOC|rtf|RTF|txt|TXT|html|HTML|htm|HTM|mp3|MP3|mp4|MP4|zip|ZIP))"',  # broader
    ]
    dir_patterns = [
        r'<td class="dir"><a href="([^"]+)">',
        r'href="([^"]+/)"',
    ]
    
    found_files = set()
    for pattern in file_patterns:
        for f in re.findall(pattern, text):
            if f in ('.', '..') or f.startswith('http://') or f.startswith('https://'):
                # Handle absolute URLs to same domain
                if f.startswith(base_url):
                    found_files.add(f)
                continue
            if f.startswith('index.html') or f.startswith('?'):
                continue
            file_url = url.rstrip('/') + '/' + urllib.parse.quote(f)
            found_files.add(file_url)
    
    found_dirs = set()
    for pattern in dir_patterns:
        for d in re.findall(pattern, text):
            if d in ('.', '..') or d.startswith('http') or d.startswith('?'):
                continue
            if d.endswith('/'):
                dir_url = url.rstrip('/') + '/' + urllib.parse.quote(d, safe='')
            else:
                dir_url = url.rstrip('/') + '/' + urllib.parse.quote(d, safe='') + '/'
            if dir_url.startswith(base_url) or dir_url.startswith(url):
                found_dirs.add(dir_url)
    
    for f in found_files:
        files.append({"url": f, "filename": urllib.parse.unquote(f.split('/')[-1])})
    
    for d in found_dirs:
        time.sleep(0.2)
        crawl_apache_dir(d, visited, files, base_url, depth + 1, max_depth)

def crawl_html_links(url, visited, files, base_url, depth=0, max_depth=3, site_name=""):
    """Scrape HTML pages for links to documents."""
    if url in visited or depth > max_depth:
        return
    visited.add(url)
    print(f"  PAGE: {url}", flush=True)
    
    data = fetch_url(url)
    if data is None:
        return
    
    text = data.decode('utf-8', errors='replace')
    
    # Find all links
    doc_extensions = r'\.(?:pdf|PDF|doc|DOC|rtf|RTF|txt|TXT|mp3|MP3|mp4|MP4|zip|ZIP|epub|EPUB)'
    
    # Document links
    for m in re.finditer(r'href=["\']([^"\']+' + doc_extensions + r')["\']', text, re.I):
        link = m.group(1)
        if link.startswith('http'):
            if base_url in link:
                files.append({"url": link, "filename": urllib.parse.unquote(link.split('/')[-1])})
        else:
            full_url = urllib.parse.urljoin(url, link)
            if base_url in full_url:
                files.append({"url": full_url, "filename": urllib.parse.unquote(link.split('/')[-1])})
    
    # Timeout-safe: save what we have so far
    if site_name:
        _maybe_checkpoint(site_name, visited, files)
    
    # Also look for HTML article pages (not just direct file links)
    if depth < max_depth:
        for m in re.finditer(r'href=["\']([^"\']+)["\']', text, re.I):
            link = m.group(1)
            # Skip external links, anchors, javascript, etc.
            if link.startswith('#') or link.startswith('javascript:') or link.startswith('mailto:'):
                continue
            if link.startswith('http') and base_url not in link:
                continue
            
            full_url = urllib.parse.urljoin(url, link)
            # Only follow links on same domain
            if base_url not in full_url:
                continue
            
            # Skip if already visited or if it's a file link
            if full_url in visited:
                continue
            if re.search(doc_extensions, full_url, re.I):
                continue
            
            # Follow the link
            time.sleep(0.3)
            crawl_html_links(full_url, visited, files, base_url, depth + 1, max_depth, site_name)

def crawl_vixra(url, visited, files, base_url, max_pages=50, max_months_per_cat=5):
    """Crawl viXra.org listing pages.
    
    viXra.org structure:
    - Main page (https://vixra.org/) has category links like href="hep", href="qgst"
    - Each category page (https://vixra.org/hep) has direct PDF links at /pdf/XXXX.XXXXv1.pdf
    - Category pages also have month archive links like href="0702", href="0802" (relative to category)
    - Month archives (https://vixra.org/hep/0702) also have direct PDF links
    
    To keep crawl time reasonable for hourly cron, we skip the "all" category
    (redundant - all papers appear in specific categories) and limit month archives
    per category. Subsequent runs can pick up more months via the progress file.
    """
    
    print(f"  Crawling viXra listings...", flush=True)
    
    # Start with the main page to find category links
    data = fetch_url(url)
    if data is None:
        return
    
    text = data.decode('utf-8', errors='replace')
    
    # viXra category names from the homepage (short codes like hep, qgst, astro, etc.)
    # They appear as href="hep", href="qgst", etc. - relative links
    # Skip "all" - it's redundant (every paper appears in its specific category)
    category_codes = [
        'hep', 'qgst', 'relcos', 'astro', 'quant', 'nucl', 'condmt', 'therm',
        'class', 'geop', 'clim', 'mathph', 'histph', 'setlog', 'numth', 'combgt',
        'alg', 'geom', 'top', 'anal', 'stat', 'math', 'dsp', 'dsalg', 'ai',
        'bioch', 'phbio', 'mind', 'qbio', 'chem', 'arch', 'ling', 'econ'
    ]
    
    # Verify which categories exist on the page
    found_cats = []
    for cat in category_codes:
        if f'href="{cat}"' in text:
            found_cats.append(cat)
    
    print(f"  Found {len(found_cats)} categories (excluding 'all')", flush=True)
    
    for cat in found_cats[:max_pages]:
        cat_url = f"{base_url.rstrip('/')}/{cat}"
        if cat_url in visited:
            continue
        visited.add(cat_url)
        
        print(f"  CAT: {cat_url}", flush=True)
        cat_data = fetch_url(cat_url)
        if cat_data is None:
            continue
        
        cat_text = cat_data.decode('utf-8', errors='replace')
        
        # Collect PDF links directly from the category page (current month)
        pdf_links = re.findall(r'href=["\'](/pdf/[^"\']+\.pdf)["\']', cat_text)
        for pdf_path in pdf_links:
            pdf_url = urllib.parse.urljoin(base_url, pdf_path)
            filename = pdf_url.split('/')[-1]
            files.append({"url": pdf_url, "filename": filename})
        
        # Find month archive links (like href="0702", href="0802", etc.)
        # These are relative to the category, so they resolve to /hep/0702
        month_links = re.findall(r'href=["\'](\d{4})["\']', cat_text)
        month_links = sorted(list(set(month_links)), reverse=True)  # newest first
        
        # Only crawl the most recent N months per category to keep runtime bounded
        for month in month_links[:max_months_per_cat]:
            month_url = f"{cat_url}/{month}"
            if month_url in visited:
                continue
            visited.add(month_url)
            
            print(f"    MONTH: {month_url}", flush=True)
            month_data = fetch_url(month_url)
            if month_data is None:
                continue
            
            month_text = month_data.decode('utf-8', errors='replace')
            
            # Collect PDF links from month archive
            month_pdfs = re.findall(r'href=["\'](/pdf/[^"\']+\.pdf)["\']', month_text)
            for pdf_path in month_pdfs:
                pdf_url = urllib.parse.urljoin(base_url, pdf_path)
                filename = pdf_url.split('/')[-1]
                files.append({"url": pdf_url, "filename": filename})
            
            time.sleep(0.3)
        
        time.sleep(0.5)

def crawl_wayback(url, visited, files, base_url, original_domain, depth=0, max_depth=4):
    """Scrape a dead site via Wayback Machine archives."""
    if url in visited or depth > max_depth:
        return
    visited.add(url)
    print(f"  WAYBACK: {url}", flush=True)
    
    data = fetch_url(url, timeout=20)
    if data is None:
        return
    
    text = data.decode('utf-8', errors='replace')
    
    # Remove Wayback Machine toolbar/rewriting to find original links
    # Wayback rewrites links like: /web/20180101/http://site.com/page
    # We want to find the original URLs and reconstruct them
    
    doc_extensions = r'\.(?:pdf|PDF|doc|DOC|rtf|RTF|txt|TXT|mp3|MP3|mp4|MP4|zip|ZIP|epub|EPUB)'
    
    # Find document links (PDFs, docs, etc.)
    # Wayback-rewritten links contain the original URL
    for m in re.finditer(r'href=["\'](?:https?://web\.archive\.org/web/\d+/)?(https?://[^"\']+)' + doc_extensions + r')["\']', text, re.I):
        full_url = m.group(1)
        # Strip wayback prefix if present
        if 'web.archive.org' in full_url:
            # Extract original URL from wayback format
            orig_match = re.search(r'web/\d+/(https?://.+)', full_url)
            if orig_match:
                full_url = orig_match.group(1)
        if original_domain in full_url:
            filename = full_url.split('/')[-1]
            # Clean wayback artifacts from filename
            filename = re.sub(r'\.html?$', '', filename)
            files.append({"url": full_url, "filename": filename, "wayback": True})
    
    # Also look for links to other pages on the same site (for recursive crawling)
    if depth < max_depth:
        for m in re.finditer(r'href=["\'](?:https?://web\.archive\.org/web/(\d+)/)?(https?://[^"\']+)["\']', text, re.I):
            link = m.group(2)
            # Only follow links to the original domain
            if original_domain not in link:
                continue
            # Skip external links, anchors, etc.
            if link.startswith('#') or link.startswith('javascript:'):
                continue
            
            # Reconstruct as a Wayback URL
            timestamp = m.group(1) or ''
            if timestamp:
                wayback_url = f"https://web.archive.org/web/{timestamp}/{link}"
            else:
                wayback_url = f"https://web.archive.org/web/2018/{link}"
            
            if wayback_url not in visited:
                time.sleep(0.3)
                crawl_wayback(wayback_url, visited, files, base_url, original_domain, depth + 1, max_depth)

def main():
    if len(sys.argv) < 2:
        print("Usage: python crawl_generic.py <site_name>")
        sys.exit(1)
    
    site_name = sys.argv[1]
    
    # Load queue
    with open(QUEUE_PATH, 'r', encoding='utf-8') as f:
        queue = json.load(f)
    
    # Find site config
    site = None
    for s in queue["sites"]:
        if s["name"] == site_name:
            site = s
            break
    
    if site is None:
        print(f"Site '{site_name}' not found in queue")
        sys.exit(1)
    
    base_url = site["base_url"]
    crawl_type = site["crawl_type"]
    crawl_paths = site["crawl_paths"]
    
    print(f"=== Crawling {site_name} ===")
    print(f"Type: {crawl_type}")
    print(f"Base URL: {base_url}")
    
    # Resume from a previous run's checkpoint if present (timeout-safe crawling)
    state = _load_checkpoint(site_name)
    if state:
        visited = set(state.get("visited", []))
        files = state.get("files", [])
        print(f"[resume] loaded {len(visited)} visited, {len(files)} files from checkpoint")
    else:
        visited = set()
        files = []
    
    # Save state on SIGTERM (the cron's timeout sends TERM — don't lose the run)
    def _term_handler(signum, frame):
        print(f"\n[signal] SIGTERM — saving checkpoint ({len(visited)} visited, {len(files)} files)", flush=True)
        try:
            _save_checkpoint(site_name, visited, files)
            # also write the partial filelist so processing can start now
            output_path = os.path.join(SCRIPT_DIR, f"{_site_slug(site_name)}_filelist.json")
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(files, f, ensure_ascii=False)
        except Exception as e:
            print(f"  [signal] checkpoint failed: {e}", flush=True)
        sys.exit(0)
    signal.signal(signal.SIGTERM, _term_handler)
    
    # For wayback scraping, extract the original domain
    original_domain = ""
    if crawl_type == "wayback_scrape":
        # base_url is like https://web.archive.org/web/2018/http://borderlands.de
        domain_match = re.search(r'web/\d+/(https?://(.+?))', base_url)
        if domain_match:
            original_domain = domain_match.group(2)
            print(f"Original domain: {original_domain}")
    
    for path in crawl_paths:
        url = base_url + path
        if crawl_type == "apache_dir":
            crawl_apache_dir(url, visited, files, base_url)
        elif crawl_type == "html_link_scrape":
            crawl_html_links(url, visited, files, base_url, site_name=site_name)
        elif crawl_type == "api_listing":
            crawl_vixra(url, visited, files, base_url)
        elif crawl_type == "wayback_scrape":
            crawl_wayback(url, visited, files, base_url, original_domain)
        time.sleep(0.3)
    
    # Deduplicate by URL
    seen_urls = set()
    unique_files = []
    for f in files:
        if f["url"] not in seen_urls:
            seen_urls.add(f["url"])
            unique_files.append(f)
    
    # Save file list
    output_path = os.path.join(SCRIPT_DIR, f"{_site_slug(site_name)}_filelist.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(unique_files, f, ensure_ascii=False, indent=2)
    
    print(f"\nTotal unique files found: {len(unique_files)}")
    print(f"Saved to {output_path}")
    
    # Clear checkpoint state on successful full completion
    state_path = os.path.join(SCRIPT_DIR, f"{_site_slug(site_name)}_crawl_state.json")
    if os.path.exists(state_path):
        os.remove(state_path)
        print(f"Checkpoint cleared (crawl completed)")
    
    # Update queue status
    site["status"] = "crawled"
    site["file_count"] = len(unique_files)
    with open(QUEUE_PATH, 'w', encoding='utf-8') as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
