#!/usr/bin/env python3
"""
Database refresh script for AetherForce Links.
Scans translations/ and updates person-index.json and research-index.json.
"""

import json
import os
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

BASE_DIR = Path("/root/workspace/aflinks")
TRANSLATIONS_DIR = BASE_DIR / "translations"
PERSON_INDEX = BASE_DIR / "database" / "person-index.json"
RESEARCH_INDEX = BASE_DIR / "database" / "research-index.json"

# Known researcher name variations
RESEARCHER_ALIASES = {
    "shipov": ["shipov", "g.i. shipov", "g. shipov", "shipov g.i."],
    "akimov": ["akimov", "a.e. akimov", "akimov a.e."],
    "magnitsky": ["magnitsky", "n.a. magnitsky", "magnitsky n.a.", "magnitskii"],
    "atsyukovsky": ["atsyukovsky", "v.a. atsyukovsky", "atsyukovsky v.a."],
    "cartan": ["cartan", "élie cartan", "e. cartan"],
    "sheldrake": ["sheldrake", "rupert sheldrake", "r. sheldrake"],
    "tesla": ["tesla", "nikola tesla", "n. tesla"],
    "schauberger": ["schauberger", "viktor schauberger", "v. schauberger"],
    "del giudice": ["del giudice", "giuliano del giudice"],
    "pollack": ["pollack", "gerald pollack", "g. pollack"],
    "enel": ["enel", "r. enel"],
    "tuo": ["tuo"],
    "deba": ["deba", "deba debailleul"],
}

# Domain keywords for classification
DOMAIN_KEYWORDS = {
    "torsion": ["torsion", "torsion field", "torsion physics"],
    "aether": ["aether", "ether", "physical vacuum", "phyton"],
    "gravity": ["gravity", "gravitation", "gravitational"],
    "scalar": ["scalar", "scalar field", "scalar energy"],
    "electrogravitics": ["electrogravitics", "biefeld-brown"],
    "lenr": ["lenr", "low energy nuclear", "cold fusion"],
    "water": ["ez water", "fourth phase", "exclusion zone"],
    "morphic": ["morphic resonance", "morphogenetic"],
    "sacred_geometry": ["sacred geometry", "bioGeometry", "biosignatures"],
}

def load_json(path):
    """Load JSON file."""
    if path.exists():
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_json(path, data):
    """Save JSON file."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def extract_metadata(filepath):
    """Extract metadata from a translation file."""
    metadata = {
        "filename": filepath.name,
        "language": None,
        "authors": [],
        "title": None,
        "date": None,
        "source_url": None,
    }
    
    # Extract language from filename (e.g., -ru.md, -fr.md, -en.md)
    lang_match = re.search(r'-(ru|fr|en|de|it|es|pt|el|pt)\.md$', filepath.name, re.I)
    if lang_match:
        metadata["language"] = lang_match.group(1).lower()
    
    # Extract date from filename
    date_match = re.match(r'(\d{4}-\d{2}-\d{2})', filepath.name)
    if date_match:
        metadata["date"] = date_match.group(1)
    
    # Read file content
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return metadata
    
    # Extract title from first heading or frontmatter description
    lines = content.split('\n')
    
    # Look for title in first non-empty, non-frontmatter line
    in_frontmatter = False
    for line in lines:
        line = line.strip()
        if line == '---':
            in_frontmatter = not in_frontmatter
            continue
        if in_frontmatter:
            if line.startswith('description:'):
                desc = line.split(':', 1)[1].strip().strip('"')
                if desc and not metadata["title"]:
                    metadata["title"] = desc
            continue
        if line.startswith('#'):
            title = line.lstrip('#').strip()
            if title and not metadata["title"]:
                metadata["title"] = title
                break
        elif line and not metadata["title"]:
            # First substantial line might be title
            if len(line) > 10 and len(line) < 200:
                metadata["title"] = line
                break
    
    # Extract authors from known patterns
    content_lower = content.lower()
    for researcher_id, aliases in RESEARCHER_ALIASES.items():
        for alias in aliases:
            if alias.lower() in content_lower:
                # More specific check - look for author line
                if re.search(rf'\b{re.escape(alias)}\b', content, re.I):
                    if researcher_id not in metadata["authors"]:
                        metadata["authors"].append(researcher_id)
                    break
    
    # Look for explicit author lines
    author_patterns = [
        r'[Aa]uthors?[:\s]+([A-Z][a-z]+(?:\s+[A-Z]\.?\s*)?[A-Z][a-z]+)',
        r'([A-Z]\.\s*[A-Z]\.\s*[A-Z][a-z]+)',
        r'([A-Z][a-z]+\s+[A-Z]\.\s*[A-Z][a-z]+)',
    ]
    
    for pattern in author_patterns:
        matches = re.findall(pattern, content)
        for match in matches:
            # Try to match to known researchers
            match_lower = match.lower()
            for researcher_id, aliases in RESEARCHER_ALIASES.items():
                if any(alias in match_lower for alias in aliases):
                    if researcher_id not in metadata["authors"]:
                        metadata["authors"].append(researcher_id)
    
    return metadata

def detect_domains(content):
    """Detect research domains from content."""
    domains = []
    content_lower = content.lower()
    
    for domain, keywords in DOMAIN_KEYWORDS.items():
        for keyword in keywords:
            if keyword in content_lower:
                if domain not in domains:
                    domains.append(domain)
                break
    
    return domains

def scan_translations():
    """Scan all translation files and extract metadata."""
    translations = []
    
    if not TRANSLATIONS_DIR.exists():
        print(f"Translations directory not found: {TRANSLATIONS_DIR}")
        return translations
    
    for filepath in TRANSLATIONS_DIR.glob("*.md"):
        metadata = extract_metadata(filepath)
        
        # Read content for domain detection
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            metadata["domains"] = detect_domains(content)
        except:
            metadata["domains"] = []
        
        translations.append(metadata)
        print(f"Scanned: {filepath.name}")
    
    return translations

def update_person_index(translations, person_index):
    """Update person-index.json with new researchers."""
    if "persons" not in person_index:
        person_index["persons"] = []
    
    existing_ids = {p.get("id") for p in person_index["persons"]}
    
    # Collect all authors from translations
    author_works = defaultdict(list)
    author_domains = defaultdict(set)
    
    for t in translations:
        for author in t.get("authors", []):
            author_works[author].append(t["filename"])
            for domain in t.get("domains", []):
                author_domains[author].add(domain)
    
    # Update existing persons or add new ones
    for author_id, works in author_works.items():
        if author_id in existing_ids:
            # Update existing entry
            for person in person_index["persons"]:
                if person.get("id") == author_id:
                    existing_works = set(person.get("works_in_collection", []))
                    new_works = existing_works.union(set(works))
                    person["works_in_collection"] = sorted(list(new_works))
                    person["domains"] = sorted(list(author_domains[author_id]))
                    person["last_updated"] = datetime.now().strftime("%Y-%m-%d")
                    break
        else:
            # Add new person entry
            new_person = {
                "id": author_id,
                "name": author_id.replace("_", " ").title(),
                "role": "researcher",
                "works_in_collection": sorted(works),
                "domains": sorted(list(author_domains[author_id])),
                "cited_by": [],
                "notes": "Auto-detected from translations",
                "last_updated": datetime.now().strftime("%Y-%m-%d")
            }
            person_index["persons"].append(new_person)
            print(f"Added new person: {author_id}")
    
    # Update metadata
    if "_about" not in person_index:
        person_index["_about"] = {}
    person_index["_about"]["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    
    return person_index

def update_research_index(translations, research_index):
    """Update research-index.json with new works."""
    if "works" not in research_index:
        research_index["works"] = []
    
    existing_files = {w.get("file") for w in research_index["works"]}
    
    new_works = 0
    for t in translations:
        if t["filename"] not in existing_files:
            # Create work entry
            work_id = re.sub(r'\.md$', '', t["filename"])
            work_id = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', work_id)
            
            work_entry = {
                "id": work_id,
                "title": t.get("title", work_id),
                "authors": t.get("authors", []),
                "date": t.get("date", "unknown"),
                "language": t.get("language", "unknown"),
                "translated": True,
                "file": t["filename"],
                "themes": [],
                "concepts": t.get("domains", []),
                "key_claims": [],
                "cross_references": [],
                "status": "translated"
            }
            
            research_index["works"].append(work_entry)
            new_works += 1
            print(f"Added new work: {t['filename']}")
    
    # Update metadata
    if "_about" not in research_index:
        research_index["_about"] = {}
    research_index["_about"]["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    
    print(f"Added {new_works} new works to research index")
    return research_index

def generate_health_report(translations, person_index, research_index):
    """Generate health report for the database."""
    report = {
        "timestamp": datetime.now().isoformat(),
        "total_translations": len(translations),
        "total_researchers": len(person_index.get("persons", [])),
        "total_works": len(research_index.get("works", [])),
        "languages": defaultdict(int),
        "domains": defaultdict(int),
        "new_since_last_refresh": 0,
    }
    
    for t in translations:
        if t.get("language"):
            report["languages"][t["language"]] += 1
        for domain in t.get("domains", []):
            report["domains"][domain] += 1
    
    # Convert defaultdicts to regular dicts for JSON
    report["languages"] = dict(report["languages"])
    report["domains"] = dict(report["domains"])
    
    return report

def main():
    print("=" * 60)
    print("AetherForce Database Refresh")
    print("=" * 60)
    
    # Load existing indices
    print("\nLoading existing indices...")
    person_index = load_json(PERSON_INDEX)
    research_index = load_json(RESEARCH_INDEX)
    
    # Scan translations
    print("\nScanning translations...")
    translations = scan_translations()
    print(f"Found {len(translations)} translation files")
    
    # Update indices
    print("\nUpdating person index...")
    person_index = update_person_index(translations, person_index)
    
    print("\nUpdating research index...")
    research_index = update_research_index(translations, research_index)
    
    # Save indices
    print("\nSaving indices...")
    save_json(PERSON_INDEX, person_index)
    save_json(RESEARCH_INDEX, research_index)
    
    # Generate health report
    print("\nGenerating health report...")
    health_report = generate_health_report(translations, person_index, research_index)
    
    print("\n" + "=" * 60)
    print("HEALTH REPORT")
    print("=" * 60)
    print(f"Total Translations: {health_report['total_translations']}")
    print(f"Total Researchers: {health_report['total_researchers']}")
    print(f"Total Works: {health_report['total_works']}")
    print(f"\nLanguages: {health_report['languages']}")
    print(f"Domains: {health_report['domains']}")
    
    # Save health report
    health_report_path = BASE_DIR / "database" / "health-report.json"
    save_json(health_report_path, health_report)
    
    print("\n" + "=" * 60)
    print("Database refresh complete!")
    print("=" * 60)
    
    return health_report

if __name__ == "__main__":
    main()
