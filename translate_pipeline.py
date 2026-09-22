#!/usr/bin/env python3
"""
Translation Pipeline for the Aetherforce Living Library
=========================================================

Extracts text from source PDFs, splits into chunks, and tracks translation progress.
Designed to be called by cron-fired agent conversations.

Usage:
    python translate_pipeline.py status          # Show what needs translating
    python translate_pipeline.py extract <book>   # Extract text from a PDF book
    python translate_pipeline.py next <book>      # Get next chunk to translate
    python translate_pipeline.py done <book> <chunk>  # Mark chunk as translated

Books are identified by their directory name under books/ (e.g., 'atsyukovsky').
"""

import os
import sys
import json
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BOOKS_DIR = os.path.join(SCRIPT_DIR, "books")
SOURCES_DIR = os.path.join(SCRIPT_DIR, "sources")
TRANSLATIONS_DIR = os.path.join(SCRIPT_DIR, "translations")
PROGRESS_DIR = os.path.join(SCRIPT_DIR, "translation_progress")

# Chunk size in characters — small enough for LLM context, large enough for throughput
CHUNK_SIZE = 8000

def ensure_dirs():
    for d in [PROGRESS_DIR]:
        os.makedirs(d, exist_ok=True)

def get_books():
    """List all book directories with their PDF files."""
    books = {}
    if not os.path.exists(BOOKS_DIR):
        return books
    for dirname in os.listdir(BOOKS_DIR):
        dirpath = os.path.join(BOOKS_DIR, dirname)
        if not os.path.isdir(dirpath):
            continue
        pdfs = [f for f in os.listdir(dirpath) if f.endswith('.pdf')]
        if pdfs:
            books[dirname] = sorted(pdfs)
    return books

def get_source_files():
    """List extracted source files (already OCR'd text)."""
    sources = {}
    if not os.path.exists(SOURCES_DIR):
        return sources
    for dirname in os.listdir(SOURCES_DIR):
        dirpath = os.path.join(SOURCES_DIR, dirname)
        if not os.path.isdir(dirpath):
            continue
        mds = [f for f in os.listdir(dirpath) if f.endswith('.md')]
        if mds:
            sources[dirname] = sorted(mds)
    return sources

def get_existing_translations():
    """List existing translation files."""
    if not os.path.exists(TRANSLATIONS_DIR):
        return []
    return sorted([f for f in os.listdir(TRANSLATIONS_DIR) if f.endswith('.md')])

def get_progress_file(book_dir, pdf_name):
    """Get the progress file path for a specific book/PDF."""
    safe_name = pdf_name.replace('.pdf', '').replace(' ', '_')
    return os.path.join(PROGRESS_DIR, f"{book_dir}_{safe_name}.json")

def load_progress(book_dir, pdf_name):
    """Load translation progress for a specific PDF."""
    path = get_progress_file(book_dir, pdf_name)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"pdf": pdf_name, "book_dir": book_dir, "total_chunks": 0, "translated_chunks": 0, "chunks": []}

def save_progress(progress):
    """Save translation progress."""
    path = get_progress_file(progress["book_dir"], progress["pdf"])
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)

def extract_pdf(pdf_path, max_chars=None):
    """Extract text from a PDF using pypdfium2."""
    try:
        import pypdfium2 as pdfium
        pdf = pdfium.PdfDocument(pdf_path)
        parts = []
        for i in range(len(pdf)):
            page = pdf[i]
            tp = page.get_textpage()
            text = tp.get_text_range()
            parts.append(text)
            tp.close()
            page.close()
            if max_chars and sum(len(p) for p in parts) > max_chars:
                break
        pdf.close()
        full = '\n'.join(parts)
        return full
    except Exception as e:
        return f"ERROR: {e}"

def split_into_chunks(text, chunk_size=CHUNK_SIZE):
    """Split text into chunks at line/paragraph boundaries.

    PDF-extracted text often uses single newlines as line breaks, so we split on
    any newline rather than blank lines. Runs of whitespace are normalized so
    chunks hold clean prose.
    """
    # Normalize whitespace: collapse runs of blank lines/space to single newlines
    lines = [re.sub(r"\s+", " ", ln).strip() for ln in text.split("\n")]
    lines = [ln for ln in lines if ln]
    chunks = []
    current = ""
    for line in lines:
        if len(current) + len(line) + 1 > chunk_size and current:
            chunks.append(current.strip())
            current = line
        else:
            current = current + "\n" + line if current else line
    if current.strip():
        chunks.append(current.strip())
    return chunks

def cmd_status():
    """Show translation status across all books."""
    books = get_books()
    sources = get_source_files()
    translations = get_existing_translations()
    
    print("=== Aetherforce Living Library — Translation Status ===\n")
    
    print(f"Existing translations: {len(translations)} files")
    
    print(f"\nSource files (already extracted text):")
    for book_dir, files in sources.items():
        for f in files:
            print(f"  {book_dir}/{f}")
    
    print(f"\nBooks (PDFs needing translation):")
    for book_dir, pdfs in books.items():
        for pdf in pdfs:
            progress = load_progress(book_dir, pdf)
            if progress["total_chunks"] > 0:
                done = progress["translated_chunks"]
                total = progress["total_chunks"]
                pct = (done / total * 100) if total > 0 else 0
                print(f"  {book_dir}/{pdf} — {done}/{total} chunks ({pct:.0f}%)")
            else:
                # Check if source text exists
                source_exists = book_dir in sources
                print(f"  {book_dir}/{pdf} — {'text extracted, ready to chunk' if source_exists else 'NOT STARTED (PDF not extracted yet)'}")
    
    # Show what's ready to translate right now
    print(f"\nReady to translate now:")
    found = False
    for book_dir, pdfs in books.items():
        for pdf in pdfs:
            progress = load_progress(book_dir, pdf)
            if progress["total_chunks"] > 0 and progress["translated_chunks"] < progress["total_chunks"]:
                next_idx = progress["translated_chunks"]
                print(f"  {book_dir}/{pdf} — chunk {next_idx + 1}/{progress['total_chunks']}")
                found = True
    if not found:
        # Check for source files that haven't been chunked yet
        for book_dir, files in sources.items():
            for f in files:
                # Check if any PDF in this book dir has progress
                pdfs = books.get(book_dir, [])
                for pdf in pdfs:
                    progress = load_progress(book_dir, pdf)
                    if progress["total_chunks"] == 0:
                        print(f"  {book_dir}/{f} — ready to chunk and translate")
                        found = True
                        break
        if not found:
            print("  Nothing ready. Extract PDFs first.")
    
    return 0

def cmd_extract(book_dir):
    """Extract text from all PDFs in a book directory (idempotent)."""
    books = get_books()
    if book_dir not in books:
        print(f"Book directory '{book_dir}' not found. Available: {list(books.keys())}")
        return 1
    
    for pdf_name in books[book_dir]:
        source_dir = os.path.join(SOURCES_DIR, book_dir)
        os.makedirs(source_dir, exist_ok=True)
        source_file = pdf_name.replace('.pdf', '_extracted.md')
        source_path = os.path.join(source_dir, source_file)
        
        if os.path.exists(source_path):
            print(f"Using existing extraction: {source_path}")
            with open(source_path, 'r', encoding='utf-8') as f:
                text = f.read()
        else:
            pdf_path = os.path.join(BOOKS_DIR, book_dir, pdf_name)
            print(f"Extracting {pdf_name}...")
            text = extract_pdf(pdf_path)
            
            if text.startswith("ERROR:"):
                print(f"  FAILED: {text}")
                continue
            
            with open(source_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"  Extracted {len(text)} chars -> {source_path}")
        
        # Create chunks and initialize progress from the SAME text cmd_next will read
        chunks = split_into_chunks(text)
        progress = load_progress(book_dir, pdf_name)
        progress["total_chunks"] = len(chunks)
        progress["translated_chunks"] = 0
        progress["chunks"] = [{"index": i, "status": "pending", "char_count": len(c)} for i, c in enumerate(chunks)]
        save_progress(progress)
        print(f"  {len(chunks)} chunks created")
    
    return 0

def cmd_next(book_dir):
    """Get the next chunk to translate for a book directory.

    Writes the chunk to translation_progress/next_chunk.txt and prints a
    machine-readable header the agent can parse. Avoids console encoding
    issues with Cyrillic text and 8K-char stdout dumps.
    """
    books = get_books()
    if book_dir not in books:
        print(f"Book directory '{book_dir}' not found. Available: {list(books.keys())}")
        return 1

    for pdf_name in books[book_dir]:
        progress = load_progress(book_dir, pdf_name)
        if progress["total_chunks"] == 0:
            print(f"  {pdf_name}: not extracted yet. Run 'python translate_pipeline.py extract {book_dir}' first.")
            continue

        next_idx = progress["translated_chunks"]
        if next_idx >= progress["total_chunks"]:
            print(f"  {pdf_name}: fully translated!")
            continue

        # Read the source text and get the chunk
        source_file = pdf_name.replace('.pdf', '_extracted.md')
        source_path = os.path.join(SOURCES_DIR, book_dir, source_file)
        if not os.path.exists(source_path):
            print(f"  {pdf_name}: source file missing. Run extract first.")
            continue

        with open(source_path, 'r', encoding='utf-8') as f:
            text = f.read()

        chunks = split_into_chunks(text)
        if next_idx < len(chunks):
            chunk = chunks[next_idx]
            # Write chunk to file for reliable reading
            out_path = os.path.join(PROGRESS_DIR, "next_chunk.txt")
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(chunk)
            # Machine-readable header
            print(f"BOOK={book_dir}")
            print(f"PDF={pdf_name}")
            print(f"CHUNK={next_idx + 1}")
            print(f"TOTAL_CHUNKS={progress['total_chunks']}")
            print(f"CHARS={len(chunk)}")
            print(f"SOURCE={source_path}")
            print(f"CHUNK_FILE={out_path}")
            return 0

    return 1

def cmd_done(book_dir, chunk_num):
    """Mark a chunk as translated."""
    books = get_books()
    if book_dir not in books:
        print(f"Book directory '{book_dir}' not found.")
        return 1
    
    chunk_idx = int(chunk_num) - 1  # Convert 1-indexed to 0-indexed
    
    for pdf_name in books[book_dir]:
        progress = load_progress(book_dir, pdf_name)
        if chunk_idx < 0 or chunk_idx >= progress["total_chunks"]:
            continue
        if chunk_idx == progress["translated_chunks"]:
            progress["translated_chunks"] = chunk_idx + 1
            if chunk_idx < len(progress["chunks"]):
                progress["chunks"][chunk_idx]["status"] = "translated"
            save_progress(progress)
            print(f"Marked {pdf_name} chunk {chunk_num}/{progress['total_chunks']} as translated")
            if progress["translated_chunks"] >= progress["total_chunks"]:
                print(f"  {pdf_name} FULLY TRANSLATED!")
            return 0
    
    print(f"Could not find chunk {chunk_num} for {book_dir}")
    return 1

def main():
    ensure_dirs()
    
    if len(sys.argv) < 2:
        print(__doc__)
        return 0
    
    cmd = sys.argv[1]
    
    if cmd == "status":
        return cmd_status()
    elif cmd == "extract":
        if len(sys.argv) < 3:
            print("Usage: python translate_pipeline.py extract <book_dir>")
            return 1
        return cmd_extract(sys.argv[2])
    elif cmd == "next":
        if len(sys.argv) < 3:
            print("Usage: python translate_pipeline.py next <book_dir>")
            return 1
        return cmd_next(sys.argv[2])
    elif cmd == "done":
        if len(sys.argv) < 4:
            print("Usage: python translate_pipeline.py done <book_dir> <chunk_num>")
            return 1
        return cmd_done(sys.argv[2], sys.argv[3])
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        return 1

if __name__ == "__main__":
    sys.exit(main())
