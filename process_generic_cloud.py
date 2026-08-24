#!/usr/bin/env python3
"""
Generic batch processor for any site's file list.
Downloads files, extracts text, builds index entries, saves progress.
Time-budgeted: runs for ~480 seconds, saves progress, exits.
Usage: python process_generic_cloud.py <site_name>
"""
import os, re, json, time, tempfile, subprocess, urllib.parse, urllib.request, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BUDGET = 1500  # seconds - ~510 files per run (raised for economy: fewer wakes, more work)

def get_paths(site_name):
    """Get file list and progress paths for a site."""
    safe_name = site_name.replace('.', '_').replace('/', '_')
    return {
        "filelist": os.path.join(SCRIPT_DIR, f"{safe_name}_filelist.json"),
        "progress": os.path.join(SCRIPT_DIR, f"{safe_name}_progress.json"),
        "entries": os.path.join(SCRIPT_DIR, f"{safe_name}_entries.json"),
        "complete": os.path.join(SCRIPT_DIR, f"{safe_name}_complete.txt"),
    }

def load_progress(progress_path):
    if os.path.exists(progress_path):
        with open(progress_path, 'r') as f:
            return json.load(f)
    return {"last_processed": -1, "entries": []}

def save_progress(progress, progress_path, entries_path):
    with open(progress_path, 'w', encoding='utf-8') as f:
        json.dump(progress, f, ensure_ascii=False)
    with open(entries_path, 'w', encoding='utf-8') as f:
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
    except:
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

# Category keywords (same as tuks processor)
CAT_KW = {
    'Energy': ['energy', 'electric', 'power', 'fuel', 'generator', 'battery', 'capacitor',
               'transformer', 'circuit', 'voltage', 'current', 'resonance', 'coil', 'magnetic',
               'bedini', 'gray', 'meyer', 'tesla', 'free energy', 'overunity', 'zero point',
               'aether', 'ether', 'vacuum', 'radiant', 'impulse', 'orgone', 'schauberger',
               'hydrogen', 'water fuel', 'electrolysis', 'plasma', 'arc', 'discharge',
               'stowe', 'dollard', 'steinmetz', 'heaviside', 'maxwell', 'faraday', 'kromrey',
               'mueller', 'brandt', 'moray', 'hendershot', 'kapanadze', 'donald smith',
               'magnetic amplifier', 'parametric', 'homopolar', 'depalma', 'n-machine',
               'electret', 'browns gas', 'hho', 'bob boyce', 'les banki', 'wfc', 'lenr',
               'cold fusion', 'low energy nuclear', 'fusion', 'nuclear', 'reactor',
               'palladium', 'deuterium', 'electrolysis cell', 'calorimetry', 'excess heat',
               'fleischmann', 'pons', 'mills', 'hydrino', 'caviton', 'energetics'],
    'Patents': ['patent', 'us patent', 'gb patent', 'de patent', 'fr patent', 'wo'],
    'Electromagnetism': ['electromagnetic', 'em wave', 'radio', 'wave', 'frequency',
                         'antenna', 'transmission', 'wireless', 'telluric', 'ground',
                         'telegraph', 'oscillating', 'inductance', 'capacitance', 'waveguide',
                         'impedance', 'standing wave', 'resonant', 'lc circuit', 'rlc'],
    'Quantum & Relativity': ['quantum', 'relativity', 'einstein', 'spacetime', 'gravity',
                             'photon', 'electron', 'particle', 'atomic', 'nuclear',
                             'fine structure', 'charge', 'superfluid', 'lorentz', 'maxwell',
                             'navier-stokes', 'helmholtz', 'schrödinger', 'bell inequality',
                             'aspect', 'epr', 'entanglement', 'bohm', 'de broglie'],
    'Alternative Physics': ['aether', 'ether', 'vortex', 'torsion', 'scalar', 'tachyon',
                           'zero point', 'vacuum energy', 'cold fusion', 'lenr',
                           'low energy nuclear', 'transmutation', 'monopole', 'antigravity',
                           'reactionless', 'free energy', 'overunity', 'perpetual',
                           'second law', 'thermodynamics', 'violations', 'magnetic',
                           'psi', 'psionic', 'radionics', 'orgone', 'tachyon', 'biofield',
                           'subtle energy', 'life force', 'prana', 'chi', 'qi', 'orgone'],
    'Conspiracy / Politics': ['bilderberg', 'cia', 'nazi', 'bush', 'loftus', 'nwo',
                              'conspiracy', 'government', 'fascism', 'synarchy', 'wall street',
                              'hitler', 'oss', 'odessa', 'skull', 'bones', 'illuminati',
                              'new world order', 'kissinger', 'genocide'],
    'Finance / Economics': ['bitcoin', 'currency', 'euro', 'economic', 'bank', 'gold',
                           'financial', 'money', 'keynesian', 'federal reserve'],
    'Water / Hydrogen': ['water', 'hydrogen', 'fuel cell', 'wfc', 'electrolysis',
                         'meyer', 'dingle', 'hho', 'browns gas', 'oxyhydrogen', 'boyce',
                         'banki', 'dry cell', 'wet cell'],
    'Biology / Health': ['gmo', 'genetic', 'dna', 'cell', 'health', 'medicine', 'cancer',
                         'disease', 'nutrition', 'vitamin', 'toxin', 'pesticide',
                         'organic', 'agriculture', 'food', 'crop', 'seed', 'soil',
                         'microbe', 'bacteria', 'virus', 'immune', 'gut', 'microbiome'],
    'Environment / Climate': ['climate', 'carbon', 'pollution', 'ecosystem', 'biodiversity',
                              'deforestation', 'ocean', 'atmosphere', 'weather', 'geoengineering',
                              'chemtrail', 'geoengineering', 'solar', 'wind', 'renewable'],
    'Music / Audio': ['audio', 'mp3', 'music', 'interview', 'sound', 'acoustic'],
    'Reference Material': ['datasheet', 'manual', 'specification', 'reference', 'databook',
                           'service manual', 'user manual', 'programmer manual'],
    'Tesla': ['tesla', 'nikola tesla', 'magnifying transmitter', 'wardenclyffe',
              'colorado springs', 'wireless power', 'telluric', 'n6kph', 'alexanderson'],
    'Dollard': ['dollard', 'eric dollard', 'bolinas', 'sbarc', 'n6kph', 'alexanderson antenna',
                'dielectric', 'displacement', 'counter-space'],
    'Steinmetz': ['steinmetz', 'transient', 'oscillation', 'alternating current'],
    'LENR / Cold Fusion': ['lenr', 'cold fusion', 'low energy nuclear', 'fleischmann',
                           'pons', 'mills', 'hydrino', 'calorimetry', 'excess heat',
                           'palladium', 'deuterium', 'nickel', 'hydrogen', 'transmutation',
                           'nuclear reaction', 'e-cat', 'rossi', 'focardi', 'celani'],
    'Psionics / Radionics': ['psionic', 'radionics', 'psionics', 'orgone', 'reich',
                            'de la warr', 'malcolm rae', 't galen hieronymus', 'ruth drown',
                            'george de la warr', 'scalar wave', 'biofield'],
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
    'Biology / Health': 'Biology, Health & Medicine',
    'Environment / Climate': 'Environment & Climate',
    'Music / Audio': 'Media & Interviews',
    'Reference Material': 'Reference & Technical Data',
    'Tesla': 'Electromagnetic Theory',
    'Dollard': 'Electromagnetic Theory',
    'Steinmetz': 'Electromagnetic Theory',
    'LENR / Cold Fusion': 'Alternative Energy Technologies',
    'Psionics / Radionics': 'Frontier Science',
}

def categorize(filename, title, preview, site_name=""):
    combined = (filename + ' ' + title + ' ' + preview + ' ' + site_name).lower()
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
        (r'(Tesla)', 'Nikola Tesla'), (r'(Eric Dollard)', 'Eric Dollard'),
        (r'(Stan Meyer|Stanley Meyer)', 'Stan Meyer'), (r'(John Bedini)', 'John Bedini'),
        (r'(Edwin Gray|E\.V\. Gray)', 'Edwin Gray'),
        (r'(Arend Lammertink)', 'Arend Lammertink'),
        (r'(Charles Proteus Steinmetz|CP Steinmetz|CP Steimetz)', 'Charles Proteus Steinmetz'),
        (r'(Oliver Heaviside)', 'Oliver Heaviside'),
        (r'(James Clerk Maxwell|James Maxwell)', 'James Clerk Maxwell'),
        (r'(Michael Faraday)', 'Michael Faraday'),
        (r'(Thomas Bearden)', 'Thomas Bearden'),
        (r'(John Loftus)', 'John Loftus'),
        (r'(Antony Sutton)', 'Antony Sutton'),
        (r'(Fleischmann)', 'Martin Fleischmann'),
        (r'(Stanley Pons|Pons)', 'Stanley Pons'),
        (r'(Randell Mills)', 'Randell Mills'),
        (r'(Andrea Rossi|A\. Rossi)', 'Andrea Rossi'),
        (r'(Sergio Focardi)', 'Sergio Focardi'),
        (r'(Francesco Celani)', 'Francesco Celani'),
        (r'(William Reich|Wilhelm Reich)', 'Wilhelm Reich'),
        (r'(T\. Galen Hieronymus|Hieronymus)', 'T. Galen Hieronymus'),
        (r'(Ruth Drown)', 'Ruth Drown'),
        (r'(George de la Warr|De La Warr)', 'George de la Warr'),
        (r'(Malcolm Rae)', 'Malcolm Rae'),
        (r'(Paul Stowe)', 'Paul Stowe'),
        (r'(T\.?\s*Henry Moray)', 'T. Henry Moray'),
        (r'(Viktor Schauberger)', 'Viktor Schauberger'),
        (r'(Ronald Hatch)', 'Ronald Hatch'),
        (r'(Bruce DePalma)', 'Bruce DePalma'),
        (r'(Konstantin Meyl)', 'Konstantin Meyl'),
        (r'(Veljko Milkovic)', 'Veljko Milkovic'),
        (r'(Raymond Kromrey)', 'Raymond Kromrey'),
        (r'(Bob Boyce)', 'Bob Boyce'),
        (r'(Les Banki)', 'Les Banki'),
        (r'(Donald L\.?\s*Smith)', 'Donald L. Smith'),
        (r'(Ernst Alexanderson)', 'Ernst Alexanderson'),
        (r'(Vladimir Utkin)', 'Vladimir Utkin'),
        (r'(Gary Vesperman)', 'Gary Vesperman'),
        (r'(Claus Turtur)', 'Claus Turtur'),
        (r'(Mae-Wan Ho|Mae Wan Ho)', 'Mae-Wan Ho'),
    ]
    combined = filename + ' ' + title
    for pattern, name in name_patterns:
        if re.search(pattern, combined, re.I):
            if name not in persons:
                persons.append(name)
    return persons

def main():
    if len(sys.argv) < 2:
        print("Usage: python process_generic_cloud.py <site_name>")
        sys.exit(1)
    
    site_name = sys.argv[1]
    paths = get_paths(site_name)
    start_time = time.time()
    
    # Load file list
    if not os.path.exists(paths["filelist"]):
        print(f"File list not found: {paths['filelist']}")
        print(f"Run crawl_generic.py {site_name} first")
        sys.exit(1)
    
    with open(paths["filelist"], 'r', encoding='utf-8') as f:
        filelist = json.load(f)
    print(f"File list: {len(filelist)} files")
    
    # Load progress
    progress = load_progress(paths["progress"])
    start_idx = progress["last_processed"] + 1
    entries = progress["entries"]
    print(f"Resuming from index {start_idx}, {len(entries)} entries already done")
    
    if start_idx >= len(filelist):
        print("ALL FILES PROCESSED!")
        with open(paths["complete"], 'w') as f:
            f.write(f"Complete: {len(entries)} entries at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        return
    
    # Load existing index for next ID
    index_path = os.path.join(SCRIPT_DIR, "index.json")
    with open(index_path, 'r', encoding='utf-8') as f:
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
        
        cats, metas = categorize(filename, title, preview, site_name)
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
            'source_site': site_name
        }
        entries.append(entry_out)
        next_id += 1
        processed += 1
        progress["last_processed"] = i
        progress["entries"] = entries
        
        if processed % 10 == 0:
            save_progress(progress, paths["progress"], paths["entries"])
            print(f"  [Saved {len(entries)} entries]", flush=True)
        
        time.sleep(0.3)
    
    save_progress(progress, paths["progress"], paths["entries"])
    print(f"\nProcessed {processed} files this run")
    print(f"Total entries: {len(entries)}")
    print(f"Progress: {progress['last_processed']+1}/{len(filelist)}")
    
    if progress['last_processed'] + 1 >= len(filelist):
        print("ALL FILES PROCESSED!")
        with open(paths["complete"], 'w') as f:
            f.write(f"Complete: {len(entries)} entries at {time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == '__main__':
    main()
