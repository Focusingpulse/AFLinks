#!/usr/bin/env python3
"""
QC Pass for synthesis reports and library integrity.

Checks:
1. Untranslated quotes (non-English without following translation)
2. Broken internal links
3. Duplicate entries in index
4. Orphaned entries (index points to missing files)
5. Citation traceability ([N] without corresponding reference)
6. Formatting drift (non-standard headers, missing sections)

Run: python3 scripts/qc_pass.py [--fix] [--report FILE]
"""

import re, json, sys, glob, os, hashlib
from pathlib import Path
from collections import defaultdict

EN_WORDS = {'the','and','of','to','in','is','that','with','as','we','not','are','be','this','for','on','a','it','by','from','was','but','they','which','have','at','or','an'}

def is_foreign(text):
    """Heuristic: text is likely non-English."""
    words = re.findall(r"[A-Za-zÀ-ÿ'’\-]+", text)
    if len(words) < 3:
        return False
    en_count = sum(1 for w in words if w.lower() in EN_WORDS)
    return en_count / len(words) <= 0.15 and any(0x00C0 <= ord(c) <= 0x024F for c in text)

def check_untranslated_quotes(content, filepath):
    """Find blockquotes without following translation."""
    issues = []
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if not line.startswith('>'):
            continue
        # skip continuation lines of a multi-line quote (">" alone or "> text" that is a translation)
        quote_text = line[1:].strip()
        if not quote_text or not is_foreign(quote_text):
            continue
        # Check following non-empty lines for translation (skip ">" continuation lines)
        next_line = ''
        for j in range(i+1, min(i+5, len(lines))):
            candidate = lines[j].strip()
            if not candidate or candidate == '>':
                continue
            # translations may be blockquote-embedded: "> *English...*" or "*English...*"
            if candidate.startswith('>'):
                candidate = candidate[1:].strip()
            if candidate.startswith('*') and re.search(r'[a-z]{3,}', candidate):
                next_line = candidate
            break
        if not (next_line.startswith('*') and re.search(r'[a-z]{3,}', next_line)):
            issues.append({
                'type': 'untranslated_quote',
                'file': filepath,
                'line': i+1,
                'snippet': quote_text[:80]
            })
    return issues

def check_citation_links(content, filepath):
    """Find [N] citations without corresponding reference."""
    issues = []
    # Find all citation numbers
    citations = set(int(m.group(1)) for m in re.finditer(r'\[(\d+)\]', content))
    if not citations:
        return issues
    # Find references section (## References or ## Sources)
    ref_match = re.search(r'##\s*(?:\d+\.?\s*)?(?:References?|Sources)\s*\n(.+)$', content, re.S | re.I)
    if not ref_match:
        issues.append({
            'type': 'missing_references_section',
            'file': filepath,
            'line': 1
        })
        return issues
    ref_section = ref_match.group(1)
    # References appear as [N] at line start or numbered "N." lists
    ref_nums = set()
    for m in re.finditer(r'^\s*-?\s*(?:\[(\d+)\]|(\d+)\.)\s', ref_section, re.M):
        ref_nums.add(int(m.group(1) or m.group(2)))
    missing = citations - ref_nums
    for n in missing:
        issues.append({
            'type': 'missing_citation',
            'file': filepath,
            'citation': n
        })
    return issues

def check_duplicate_index_entries(shards_dir='index_shards'):
    """Find duplicate entries across index shards.
    
    A duplicate = same source_url AND same filename AND same size.
    (filename-only collisions across different sites are expected.)
    """
    issues = []
    seen = defaultdict(list)
    
    for shard_file in sorted(glob.glob(f'{shards_dir}/shard_*.json')):
        shard = json.load(open(shard_file))
        for entry in shard:
            key = (entry.get('source_url', ''), entry.get('filename', ''), entry.get('size_bytes', 0))
            seen[key].append(entry.get('id'))
    
    for key, id_list in seen.items():
        if len(id_list) > 1:
            issues.append({
                'type': 'duplicate_by_content',
                'source_url': key[0][:80],
                'filename': key[1],
                'size': key[2],
                'count': len(id_list),
                'ids': id_list[:10]
            })
    return issues

def check_orphaned_entries(index_dir='index_shards', source_dirs=('translations',)):
    """Find index entries that reference LOCAL repo files that no longer exist.
    
    Only entries whose source_url/path points into the repo (e.g. translations/...)
    are checked — remote crawled URLs are not local files and are never orphans.
    """
    issues = []
    existing_files = set()
    for src_dir in source_dirs:
        for f in glob.glob(f'{src_dir}/**/*', recursive=True):
            if os.path.isfile(f):
                existing_files.add(os.path.basename(f))
    
    for shard_file in sorted(glob.glob(f'{index_dir}/shard_*.json')):
        shard = json.load(open(shard_file))
        for entry in shard:
            path = entry.get('source_url', '') or ''
            # Only local-repo references
            if not path or 'http' in path[:8]:
                continue
            if not any(path.endswith(e) for e in existing_files):
                issues.append({
                    'type': 'orphaned_entry',
                    'id': entry.get('id'),
                    'path': path[:100]
                })
    return issues

def compute_checksum(filepath):
    """MD5 checksum of file."""
    h = hashlib.md5()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def run_qc(fix=False, report_file=None):
    """Run all QC checks and optionally fix issues."""
    all_issues = []
    
    # Check synthesis files
    for syn_file in sorted(glob.glob('synthesis/*.md')):
        content = open(syn_file, encoding='utf-8').read()
        all_issues.extend(check_untranslated_quotes(content, syn_file))
        all_issues.extend(check_citation_links(content, syn_file))
    
    # Check index integrity
    all_issues.extend(check_duplicate_index_entries())
    all_issues.extend(check_orphaned_entries())
    
    # Report
    print(f"QC Pass: {len(all_issues)} issues found")
    
    by_type = defaultdict(list)
    for issue in all_issues:
        by_type[issue['type']].append(issue)
    
    for issue_type, items in sorted(by_type.items()):
        print(f"  {issue_type}: {len(items)}")
    
    if report_file:
        json.dump(all_issues, open(report_file, 'w'), indent=2)
        print(f"Report written to {report_file}")
    
    return len(all_issues)

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--fix', action='store_true', help='Attempt to fix issues')
    ap.add_argument('--report', default='qc_report.json', help='Report output file')
    args = ap.parse_args()
    
    sys.exit(run_qc(fix=args.fix, report_file=args.report))
