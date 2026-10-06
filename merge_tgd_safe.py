#!/usr/bin/env python3
"""Id-safe merge for tgdtheory_fi: append ONLY genuinely-new entries (dedup by normalized source_url + basename), fresh ids above remote max, compact dump.
"""
import json, sys, urllib.parse

entries_path = sys.argv[1]
with open('index.json', encoding='utf-8') as f:
    idx = json.load(f)

with open(entries_path, encoding='utf-8') as f:
    entries = json.load(f)

def norm(u):
    # normalize host (www vs non-www) and unquote + lowercase basename
    un = u.replace('https://www.tgdtheory.fi', 'https://tgdtheory.fi')
    bn = urllib.parse.unquote(un.split('/')[-1]).lower()
    return bn

existing_bn = set()
for e in idx:
    su = e.get('source_url', '')
    if 'tgdtheory' in su:
        existing_bn.add(norm(su))

cur_max = max(e['id'] for e in idx)
fresh = []
nid = cur_max + 1
added = 0
skipped = 0
for e in entries:
    bn = norm(e.get('source_url', ''))
    if not bn or bn in existing_bn:
        skipped += 1
        continue
    e['id'] = nid
    nid += 1
    fresh.append(e)
    existing_bn.add(bn)
    added += 1

idx.extend(fresh)
with open('index.json', 'w', encoding='utf-8') as f:
    json.dump(idx, f, ensure_ascii=False, separators=(',', ':'))

print(f"merged {added} new entries (skipped {skipped} dups); index.json now has {len(idx)} entries; new max id {nid-1}")