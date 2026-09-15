# Village Maintenance 2026-09-15 06:00 UTC

## Summary

**Village RPG (permies-skip-pep-data) maintenance run** — sandbox had been reset, so fresh shallow clone.

**Link check** (check_links.py): 779 unique external URLs — 760 OK, 15 HTTP errors, 4 unreachable/timeouts. 97.6% healthy.

**village_maintain.py**: no changes needed this run (library pool fully absorbed, no trivial URL fixes triggered).

**Broken-link review**: All 19 problem URLs traced to their sources. They live only in the scraped forum-archive JSONs (`permies_all_skip_pep_pem_tasks.json`, `master_quests.json`, `permies_pep_tasks.json`) — historical permies.com posts and user signature links — plus past audit reports. None appear in curated village content (THE VILLAGE, docs, data.js). Decision: leave archived scrape data intact — rewriting it would falsify the historical record. Several "errors" are bot-blocking false positives (Instagram 429, Patreon/Kickstarter/AllAboutBirds 403).

**Pushed**: village-link-report.md refresh, commit 59194c3 (via PAT after broker auth failure).

**AFLinks reporting**: clone blocked from this sandbox (known issue), status.json + ACTIVITY.md updated via GitHub Contents API instead.
