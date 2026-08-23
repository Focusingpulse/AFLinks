#!/usr/bin/env python3
"""
OCR extraction for scanned-image PDFs that had no text layer.
Downloads PDF, renders first 2 pages as images, runs Tesseract OCR.
Saves progress every 100 files.
"""

import json
import os
import sys
import time
import urllib.request
import socket
import subprocess
import tempfile
import concurrent.futures
import threading

import pymupdf

INPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.json')
OUTPUT_FILE = INPUT_FILE

socket.setdefaulttimeout(30)
write_lock = threading.Lock()

def download_pdf(url):
    """Download a PDF from URL, return bytes or None."""
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
            if len(data) < 100 or data[:4] != b'%PDF':
                return None
            return data
    except Exception:
        return None

def ocr_pdf(pdf_bytes, max_pages=1):
    """Render PDF pages as images and run Tesseract OCR."""
    try:
        doc = pymupdf.open(stream=pdf_bytes, filetype='pdf')
        text_parts = []
        for i in range(min(max_pages, len(doc))):
            page = doc[i]
            # Render at 100 DPI (fast enough for OCR, much faster than 150)
            pix = page.get_pixmap(dpi=100)
            img_data = pix.tobytes('png')
            
            # Write to temp file for Tesseract
            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as img_file:
                img_file.write(img_data)
                img_path = img_file.name
            
            try:
                # Run Tesseract OCR
                result = subprocess.run(
                    ['tesseract', img_path, 'stdout', '--psm', '6'],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                if result.stdout and result.stdout.strip():
                    text_parts.append(result.stdout.strip())
            except Exception:
                pass
            finally:
                os.unlink(img_path)
        
        doc.close()
        
        if text_parts:
            combined = ' '.join(text_parts)
            combined = ' '.join(combined.split())
            # Filter out very short or garbage text
            if len(combined) > 20:
                return combined[:500]
        return None
    except Exception:
        return None

def process_entry(args):
    """Process a single entry: download PDF, OCR it, return (index, text or None)."""
    idx, url = args
    pdf_bytes = download_pdf(url)
    if not pdf_bytes:
        return (idx, None)
    text = ocr_pdf(pdf_bytes)
    return (idx, text)

def main():
    print("Loading index.json...", flush=True)
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Find PDFs without content previews
    to_process = []
    for i, entry in enumerate(data):
        if len(entry.get('content_preview', '')) < 20 and entry.get('source_url'):
            url = entry['source_url']
            if 'rexresearch.com/' in url and url.endswith('.pdf'):
                to_process.append((i, url))
    
    total = len(to_process)
    print(f"OCR processing {total} scanned PDFs", flush=True)
    
    updated = 0
    failed = 0
    start_time = time.time()
    last_save = 0
    
    # Process with 2 parallel threads (Tesseract is CPU-bound, more threads cause timeouts)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        futures = {executor.submit(process_entry, item): item for item in to_process}
        
        for future in concurrent.futures.as_completed(futures):
            idx, url = futures[future]
            try:
                result_idx, text = future.result()
                if text:
                    data[result_idx]['content_preview'] = text
                    updated += 1
                else:
                    failed += 1
            except Exception:
                failed += 1
            
            done = updated + failed
            if done % 5 == 0:
                elapsed = time.time() - start_time
                rate = done / elapsed if elapsed > 0 else 0
                remaining = (total - done) / rate if rate > 0 else 0
                print(f"  [{done}/{total}] {updated} OCR'd, {failed} failed | "
                      f"{rate:.1f}/s | ETA: {remaining:.0f}s", flush=True)
                
                # Save every 10 files (frequent saves for short timeout windows)
                if done - last_save >= 5:
                    last_save = done
                    with write_lock:
                        tmp_file = OUTPUT_FILE + '.tmp'
                        with open(tmp_file, 'w', encoding='utf-8') as f:
                            json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
                            f.flush()
                            os.fsync(f.fileno())
                        os.rename(tmp_file, OUTPUT_FILE)
                        print(f"  [saved at {done}]", flush=True)
    
    elapsed = time.time() - start_time
    print(f"\nDone in {elapsed:.0f}s", flush=True)
    print(f"  OCR'd: {updated}", flush=True)
    print(f"  Failed: {failed}", flush=True)
    
    # Final save
    print("Saving index.json...", flush=True)
    tmp_file = OUTPUT_FILE + '.tmp'
    with open(tmp_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
        f.flush()
        os.fsync(f.fileno())
    os.rename(tmp_file, OUTPUT_FILE)
    
    with_preview = sum(1 for e in data if len(e.get('content_preview', '')) >= 20)
    print(f"\nFinal: {with_preview}/{len(data)} ({with_preview/len(data)*100:.1f}%) have content previews", flush=True)

if __name__ == '__main__':
    main()
