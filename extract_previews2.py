#!/usr/bin/env python3
"""
Download PDFs from rexresearch.com in parallel, extract text, update index.json.
Saves progress every 200 files.
"""

import json
import os
import sys
import time
import urllib.request
import urllib.error
import socket
import concurrent.futures
import threading

import pymupdf  # use pymupdf directly, not fitz

INPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.json')
OUTPUT_FILE = INPUT_FILE

socket.setdefaulttimeout(30)

# Thread-safe lock for writing
write_lock = threading.Lock()
data = []
save_counter = 0

def download_and_extract(url, timeout=20):
    """Download a PDF from URL and extract first 3 pages of text."""
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            pdf_bytes = resp.read()
            if len(pdf_bytes) < 100 or pdf_bytes[:4] != b'%PDF':
                return None
        # Extract text
        doc = pymupdf.open(stream=pdf_bytes, filetype='pdf')
        text_parts = []
        for i in range(min(3, len(doc))):
            page = doc[i]
            text = page.get_text()
            if text.strip():
                text_parts.append(text.strip())
        doc.close()
        if text_parts:
            combined = ' '.join(text_parts)
            combined = ' '.join(combined.split())
            return combined[:500]
        return None
    except Exception:
        return None

def fetch_html(url, timeout=15):
    """Fetch an HTML page and extract readable text."""
    try:
        import re
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
            html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
            text = re.sub(r'<[^>]+>', ' ', html)
            text = ' '.join(text.split())
            return text[:500] if len(text) > 20 else None
    except Exception:
        return None

def process_entry(args):
    """Process a single entry: download, extract text, return (index, preview or None)."""
    idx, url, entry = args
    
    # Skip images and media
    if url.endswith(('.gif', '.jpg', '.jpeg', '.png', '.bmp', '.mp4', '.mp3', '.avi', '.mov', '.wav')):
        return (idx, None, 'skip')
    
    # PDFs
    if url.endswith('.pdf'):
        text = download_and_extract(url)
        return (idx, text, 'pdf')
    
    # HTML pages
    if url.endswith(('.html', '.htm')):
        text = fetch_html(url)
        return (idx, text, 'html')
    
    # Other: try HTML first, then PDF
    text = fetch_html(url)
    if text:
        return (idx, text, 'html')
    text = download_and_extract(url)
    return (idx, text, 'pdf')

def main():
    global data
    
    print("Loading index.json...", flush=True)
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Find entries to process
    to_process = []
    for i, entry in enumerate(data):
        if len(entry.get('content_preview', '')) < 20 and entry.get('source_url'):
            url = entry['source_url']
            if 'rexresearch.com/' in url:
                to_process.append((i, url, entry))
    
    total = len(to_process)
    pdfs = sum(1 for _,u,_ in to_process if u.endswith('.pdf'))
    images = sum(1 for _,u,_ in to_process if u.endswith(('.gif','.jpg','.jpeg','.png','.bmp')))
    media = sum(1 for _,u,_ in to_process if u.endswith(('.mp4','.mp3','.avi','.mov','.wav')))
    other = total - pdfs - images - media
    
    print(f"Processing {total} entries: {pdfs} PDFs, {images} images, {media} media, {other} other", flush=True)
    
    updated = 0
    failed = 0
    skipped = 0
    start_time = time.time()
    last_save = 0
    
    # Process with 10 parallel threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(process_entry, item): item for item in to_process}
        
        for future in concurrent.futures.as_completed(futures):
            idx, url, entry = futures[future]
            try:
                result_idx, text, source_type = future.result()
                if text:
                    data[result_idx]['content_preview'] = text
                    updated += 1
                elif source_type == 'skip':
                    skipped += 1
                else:
                    failed += 1
            except Exception:
                failed += 1
            
            done = updated + failed + skipped
            if done % 100 == 0:
                elapsed = time.time() - start_time
                rate = done / elapsed if elapsed > 0 else 0
                remaining = (total - done) / rate if rate > 0 else 0
                print(f"  [{done}/{total}] {updated} updated, {failed} failed, {skipped} skipped | "
                      f"{rate:.1f}/s | ETA: {remaining:.0f}s", flush=True)
                
                # Save every 200 files
                if done - last_save >= 200:
                    last_save = done
                    with write_lock:
                        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                            json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
                        print(f"  [saved at {done}]", flush=True)
    
    elapsed = time.time() - start_time
    print(f"\nDone in {elapsed:.0f}s", flush=True)
    print(f"  Updated: {updated}", flush=True)
    print(f"  Failed: {failed}", flush=True)
    print(f"  Skipped (images/media): {skipped}", flush=True)
    
    # Final save
    print("Saving index.json...", flush=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
    
    with_preview = sum(1 for e in data if len(e.get('content_preview', '')) >= 20)
    print(f"\nFinal: {with_preview}/{len(data)} ({with_preview/len(data)*100:.1f}%) have content previews", flush=True)

if __name__ == '__main__':
    main()
