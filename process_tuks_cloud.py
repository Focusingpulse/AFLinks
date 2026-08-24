#!/usr/bin/env python3
"""
Cloud version of tuks.nl batch processor.
Uses relative paths (repo root) instead of Windows D: drive paths.
No Tesseract OCR (cloud may not have it) - uses pypdfium2 text extraction only.
Time-budgeted: runs for ~100 seconds, saves progress, exits.
"""
import os, re, json, time, tempfile, subprocess, urllib.parse, urllib.request, sys

# Use repo-relative paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILELIST = os.path.join(SCRIPT_DIR, "tuks_filelist.json")
OUTPUT = os.path.join(SCRIPT_DIR, "tuks_entries.json")
PROGRESS = os.path.join(SCRIPT_DIR, "tuks_progress.json")
INDEX_PATH = os.path.join(SCRIPT_DIR, "index.json")
BUDGET = 100  # seconds

def load_progress():
    if os.path.exists(PROGRESS):
        with open(PROGRESS, 'r') as f:
            return json.load(f)
    return {"last_processed": -1, "entries": []}

def save_progress(progress):
    with open(PROGRESS, 'w', encoding='utf-8') as f:
        json.dump(progress, f, ensure_ascii=False)
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(progress["entries"], f, ensure_ascii=False, indent=2)

def fetch_url(url, timeout=30):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except Exception as e:
        print(f"  ERR: {e}")
        return None

def extract_pdf_text(pdf_path, max_chars=2000):
    try:
        import pypdfium2 as pdfium
        pdf = pdfium.PdfDocument(pdf_path)
        parts = []
        for i in range(min(len(pdf), 10)):
            page = pdf[i]
            tp = page.get_textpage()
            text = tp.get_text_range()
            parts.append(text)
            tp.close()
            page.close()
        pdf.close()
        full = ' '.join(parts)
        full = re.sub(r'\s+', ' ', full).strip()
        return full[:max_chars]
    except Exception as e:
        return ""

def fetch_html_text(url, max_chars=2000):
    data = fetch_url(url, timeout=15)
    if data is None: return ""
    text = data.decode('utf-8', errors='replace')
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'&amp;', '&', text)
    text = re.sub(r'&lt;', '<', text)
    text = re.sub(r'&gt;', '>', text)
    text = re.sub(r'&quot;', '"', text)
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'&#\d+;', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:max_chars]

# Category keywords
CAT_KW = {
    'Energy': ['energy', 'electric', 'power', 'fuel', 'generator', 'battery', 'capacitor',
               'transformer', 'circuit', 'voltage', 'current', 'resonance', 'coil', 'magnetic',
               'bedini', 'gray', 'meyer', 'tesla', 'free energy', 'overunity', 'zero point',
               'aether', 'ether', 'vacuum', 'radiant', 'impulse', 'orgone', 'schauberger',
               'hydrogen', 'water fuel', 'electrolysis', 'plasma', 'arc', 'discharge',
               'stowe', 'dollard', 'steinmetz', 'heaviside', 'maxwell', 'faraday', 'kromrey',
               'mueller', 'brandt', 'moray', 'hendershot', 'kapanadze', 'donald smith',
               'magnetic amplifier', 'parametric', 'homopolar', 'depalma', 'n-machine',
               'electret', 'browns gas', 'hho', 'bob boyce', 'les banki', 'wfc'],
    'Patents': ['patent', 'us patent', 'gb patent', 'de patent', 'fr patent', 'wo'],
    'Electromagnetism': ['electromagnetic', 'em wave', 'radio', 'wave', 'frequency',
                         'antenna', 'transmission', 'wireless', 'telluric', 'ground',
                         'telegraph', 'oscillating', 'inductance', 'capacitance', 'waveguide',
                         'impedance', 'standing wave', 'resonant', 'lc circuit', 'rlc'],
    'Quantum & Relativity': ['quantum', 'relativity', 'einstein', 'spacetime', 'gravity',
                             'photon', 'electron', 'particle', 'atomic', 'nuclear',
                             'fine structure', 'charge', 'superfluid', 'lorentz', 'maxwell',
                             'navier-stokes', 'helmholtz', 'schrödinger', 'bell inequality',
                             'aspect', 'epr', 'entanglement'],
    'Alternative Physics': ['aether', 'ether', 'vortex', 'torsion', 'scalar', 'tachyon',
                           'zero point', 'vacuum energy', 'cold fusion', 'lenr',
                           'low energy nuclear', 'transmutation', 'monopole', 'antigravity',
                           'reactionless', 'free energy', 'overunity', 'perpetual',
                           'second law', 'thermodynamics', 'violations'],
    'Conspiracy / Politics': ['bilderberg', 'cia', 'nazi', 'bush', 'loftus', 'nwo',
                              'conspiracy', 'government', 'fascism', 'synarchy', 'wall street',
                              'hitler', 'oss', 'odessa', 'skull', 'bones', 'illuminati',
                              'new world order', 'kissinger', 'genocide', 'pabst',
                              'prins bernhard', 'klinkenberg', 'bilderberg'],
    'Finance / Economics': ['bitcoin', 'currency', 'euro', 'economic', 'bank', 'gold',
                           'financial', 'money', 'keynesian', 'federal reserve', 'lisbon treaty'],
    'Water / Hydrogen': ['water', 'hydrogen', 'fuel cell', 'wfc', 'electrolysis',
                         'meyer', 'dingle', 'hho', 'browns gas', 'oxyhydrogen', 'boyce',
                         'banki', 'dry cell', 'wet cell'],
    'Music / Audio': ['audio', 'mp3', 'music', 'interview', 'sound', 'acoustic', 'loftus'],
    'Reference Material': ['datasheet', 'manual', 'specification', 'reference', 'databook',
                           'tektronix', 'service manual', 'user manual', 'programmer manual'],
    'Tesla': ['tesla', 'nikola tesla', 'magnifying transmitter', 'wardenclyffe',
              'colorado springs', 'wireless power', 'telluric', 'n6kph', 'alexanderson'],
    'Dollard': ['dollard', 'eric dollard', 'bolinas', 'sbarc', 'n6kph', 'alexanderson antenna',
                'dielectric', 'displacement', 'counter-space'],
    'Steinmetz': ['steinmetz', 'steinmetz', 'transient', 'oscillation', 'alternating current'],
}

META_MAP = {
    'Energy': 'Alternative Energy Technologies',
    'Patents': 'Patents & Inventions',
    'Electromagnetism': 'Electromagnetic Theory',
    'Quantum & Relativity': 'Challenges to the Standard Model',
    'Alternative Physics': 'Challenges to the Standard Model',
    'Conspiracy / Politics': 'Geopolitics & Hidden History',
    'Finance / Economics': 'Geopolitics & Hidden History',
    'Water / Hydrogen': 'Alternative Energy Technologies',
    'Music / Audio': 'Media & Interviews',
    'Reference Material': 'Reference & Technical Data',
    'Tesla': 'Electromagnetic Theory',
    'Dollard': 'Electromagnetic Theory',
    'Steinmetz': 'Electromagnetic Theory',
}

def categorize(filename, title, preview):
    combined = (filename + ' ' + title + ' ' + preview).lower()
    cats = []
    metas = []
    for cat, keywords in CAT_KW.items():
        for kw in keywords:
            if kw in combined:
                if cat not in cats:
                    cats.append(cat)
                    meta = META_MAP.get(cat)
                    if meta and meta not in metas:
                        metas.append(meta)
                break
    if not cats:
        cats = ['Borderland Research']
        metas = ['Challenges to the Standard Model']
    return cats, metas

def extract_patents(text):
    patents = []
    for m in re.finditer(r'\bUS\s*#?(\d{6,8})\b', text, re.I):
        patents.append(f"US{m.group(1)}")
    for m in re.finditer(r'\bpatent\s*#?\s*(\d{6,8})\b', text, re.I):
        p = m.group(1)
        if f"US{p}" not in patents:
            patents.append(p)
    for m in re.finditer(r'\bUS(\d{7})\b', text):
        p = f"US{m.group(1)}"
        if p not in patents:
            patents.append(p)
    return list(set(patents))[:10]

def extract_persons(filename, title):
    persons = []
    name_patterns = [
        (r'(Tesla)', 'Nikola Tesla'),
        (r'(Eric Dollard)', 'Eric Dollard'),
        (r'(Stan Meyer|Stanley Meyer)', 'Stan Meyer'),
        (r'(John Bedini)', 'John Bedini'),
        (r'(Edwin Gray|E\.V\. Gray)', 'Edwin Gray'),
        (r'(Arend Lammertink)', 'Arend Lammertink'),
        (r'(Charles Proteus Steinmetz|CP Steinmetz|CP Steimetz|CP Steimnetz)', 'Charles Proteus Steinmetz'),
        (r'(Oliver Heaviside)', 'Oliver Heaviside'),
        (r'(James Maxwell|James Clerk Maxwell)', 'James Clerk Maxwell'),
        (r'(Michael Faraday)', 'Michael Faraday'),
        (r'(Thomas Bearden)', 'Thomas Bearden'),
        (r'(John Loftus)', 'John Loftus'),
        (r'(Antony Sutton)', 'Antony Sutton'),
        (r'(David Wilcock)', 'David Wilcock'),
        (r'(William Stowe|Paul Stowe)', 'Paul Stowe'),
        (r'(T\.?\s*Henry Moray|T\.?\s*H\.?\s*Moray)', 'T. Henry Moray'),
        (r'(Viktor Schauberger)', 'Viktor Schauberger'),
        (r'(Ronald Hatch|Ron Hatch)', 'Ronald Hatch'),
        (r'(Bruce DePalma)', 'Bruce DePalma'),
        (r'(Konstantin Meyl)', 'Konstantin Meyl'),
        (r'(Veljko Milkovic)', 'Veljko Milkovic'),
        (r'(Raymond Kromrey)', 'Raymond Kromrey'),
        (r'(Bob Boyce)', 'Bob Boyce'),
        (r'(Les Banki)', 'Les Banki'),
        (r'(Donald L\.?\s*Smith)', 'Donald L. Smith'),
        (r'(Nikola Alexanderson|Ernst Alexanderson)', 'Ernst Alexanderson'),
        (r'(J\.R\.?\s*Tolman)', 'J.R. Tolman'),
        (r'(Vladimir Utkin)', 'Vladimir Utkin'),
        (r'(Gary Vesperman)', 'Gary Vesperman'),
        (r'(Claus Turtur)', 'Claus Turtur'),
        (r'(Mandelstam|Papalexi)', 'Mandelstam & Papalexi'),
        (r'(Minorsky)', 'Minorsky'),
        (r'(Pollack)', 'Gerald Pollack'),
        (r'(Lakhovski)', 'Georges Lakhovsky'),
    ]
    combined = filename + ' ' + title
    for pattern, name in name_patterns:
        if re.search(pattern, combined, re.I):
            if name not in persons:
                persons.append(name)
    return persons

def main():
    start_time = time.time()

    with open(FILELIST, 'r', encoding='utf-8') as f:
        filelist = json.load(f)
    print(f"File list: {len(filelist)} files")

    progress = load_progress()
    start_idx = progress["last_processed"] + 1
    entries = progress["entries"]
    print(f"Resuming from index {start_idx}, {len(entries)} entries already done")

    if start_idx >= len(filelist):
        print("ALL FILES PROCESSED!")
        # Signal completion
        with open(os.path.join(SCRIPT_DIR, "tuks_complete.txt"), 'w') as f:
            f.write(f"Complete: {len(entries)} entries at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        return

    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        existing = json.load(f)
    next_id = max(e['id'] for e in existing) + 1 + len(entries)

    processed = 0
    for i in range(start_idx, len(filelist)):
        elapsed = time.time() - start_time
        if elapsed > BUDGET:
            print(f"\nTime budget exceeded ({elapsed:.0f}s), stopping")
            break

        entry = filelist[i]
        url = entry["url"]
        filename = urllib.parse.unquote(entry["filename"])

        print(f"[{i+1}/{len(filelist)}] {filename[:60]}", flush=True)

        ext = os.path.splitext(filename)[1].lower()
        if ext in ('.pdf', '.html', '.htm', '.rtf', '.doc', '.txt', '.md', '.php'):
            ftype = 'document'
        elif ext in ('.mp3', '.mp4', '.avi', '.wav', '.ogg', '.webm', '.torrent'):
            ftype = 'media'
        elif ext in ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.zip'):
            ftype = 'media'
        else:
            ftype = 'document'

        title = os.path.splitext(filename)[0].replace('_', ' ').strip()
        preview = ""

        if ext == '.pdf':
            pdf_data = fetch_url(url, timeout=30)
            if pdf_data:
                with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
                    tmp.write(pdf_data)
                    tmp_path = tmp.name
                preview = extract_pdf_text(tmp_path)
                os.unlink(tmp_path)
        elif ext in ('.html', '.htm', '.php'):
            preview = fetch_html_text(url)
        elif ext == '.txt':
            txt_data = fetch_url(url, timeout=15)
            if txt_data:
                preview = txt_data.decode('utf-8', errors='replace')[:2000]
                preview = re.sub(r'\s+', ' ', preview).strip()

        cats, metas = categorize(filename, title, preview)
        patents = extract_patents(filename + ' ' + preview)
        persons = extract_persons(filename, title)

        entry_out = {
            'id': next_id,
            'filename': filename,
            'title': title,
            'type': ftype,
            'extension': ext,
            'size_bytes': 0,
            'source_url': url,
            'categories': cats,
            'meta_categories': metas,
            'patent_numbers': patents,
            'primary_person': persons[0] if persons else "",
            'content_preview': preview,
            'last_modified': time.strftime('%Y-%m-%d'),
            'source_site': 'tuks.nl'
        }
        entries.append(entry_out)
        next_id += 1
        processed += 1
        progress["last_processed"] = i
        progress["entries"] = entries

        if processed % 5 == 0:
            save_progress(progress)
            print(f"  [Saved {len(entries)} entries]", flush=True)

        time.sleep(0.3)

    save_progress(progress)
    print(f"\nProcessed {processed} files this run")
    print(f"Total entries: {len(entries)}")
    print(f"Progress: {progress['last_processed']+1}/{len(filelist)}")

    if progress['last_processed'] + 1 >= len(filelist):
        print("ALL FILES PROCESSED!")
        with open(os.path.join(SCRIPT_DIR, "tuks_complete.txt"), 'w') as f:
            f.write(f"Complete: {len(entries)} entries at {time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == '__main__':
    main()
