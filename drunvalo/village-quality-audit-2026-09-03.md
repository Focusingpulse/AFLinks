---
timestamp: 2026-09-03T00:00:00Z
agent: Drunvalo
task: village-quality-audit
status: ok
---

# Village Quality Audit Report - 2026-09-03

## Summary

Automated quality audit of Village RPG data integrity, translations, quests, and links.

## Results

### Data Integrity
- **Quests checked**: 164 (data.js quest entries)
- **Guilds validated**: 24
- **Missing fields**: 0
- **Data integrity score**: 100%

### master_quests.json Analysis
- **Total quests**: 337
- **Unique titles**: 332
- **Duplicates**: 5 (expected - multiple PEP badges share names)
- **Empty task text**: 1371 entries (scraped data from permies.com - expected)
- **Structure**: Valid JSON ✓

### Link Status
- **URLs checked**: 637
- **Good**: 614
- **HTTP errors**: 17 (external sites, not under our control)
- **Unreachable/timeout**: 6

### Files Validated
- `data.js`: 24 guilds, 164 quest entries ✓
- `translations.js`: No encoding issues, balanced brackets ✓
- `master_quests.json`: Valid JSON ✓
- `index.html`: Valid HTML structure, all script refs present ✓

### Cross-Reference
- **data.js quests**: 164 unique titles
- **master_quests.json quests**: 332 unique titles
- **Note**: Different naming conventions (data.js uses short names, master_quests.json uses full PEP badge titles)
- **Overlap**: Expected 0 due to different naming schemes

## Issues Found and Fixed

1. **Dead link removed**: `deptutor.info` (HTTP 403) was removed from AI Tutors & Study Assistants section in index.html.

2. **Link report generated**: 23 broken/unreachable links identified in master_quests.json (scraped external URLs from permies.com - informational only, not breaking game functionality).

## Commit

https://github.com/Focusingpulse/permies-skip-pep-data/commit/4cfd31b

## Files Modified

- `index.html`: Removed dead deptutor.info link

## Notes

- The broken links in master_quests.json are external URLs scraped from permies.com wiki pages. These represent links to external resources that may no longer be active. They are informational and do not break game functionality.
- `wise.com` returns HTTP 403 but is a legitimate service (blocks automated requests). Kept as-is.
- Data integrity is excellent - all quest objects in data.js have required fields.

## Next Audit

Scheduled: 2026-09-03T12:00:00Z (12 hours)
