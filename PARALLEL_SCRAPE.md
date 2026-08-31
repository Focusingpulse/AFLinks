# PARALLEL_SCRAPE.md — How to add more workers

The AFLinks queue processes one site at a time via the main sync (`aflinks-sync`,
every 3h). Since each site has its **own** filelist/progress/entries files,
different sites can be scraped **in parallel** by separate workers with zero
conflicts. The only shared file is `index.json`, merged idempotently by
`merge_all_progress.py`.

## One worker = one site

A worker is any cron (or friend agent) that runs this flow for a single site:

```bash
cd /root/workspace/AFLinks          # clone if missing:
                                    # git clone https://github.com/Focusingpulse/AFLinks.git
git pull --rebase --quiet origin main   # always refresh first

# Family budget gate (only if cron-coordination attached):
python3 $MEMORY_DIR/../cron-coordination/family.py run-gate --member <name> \
    || { echo "budget low — skip"; exit 0; }

# 1) Crawl (only if no filelist yet):
python3 crawl_generic.py <site>          # writes <site>_filelist.json

# 2) Process a batch (time-budgeted internally):
python3 process_generic_cloud.py <site>  # writes <site>_progress.json + _entries.json

# 3) Merge into index.json (idempotent, safe anytime):
python3 merge_all_progress.py

# 4) Push (pull --rebase first — other workers may have pushed):
git pull --rebase --quiet origin main
ENTRIES=$(python3 -c "import json;print(len(json.load(open('index.json'))))")
git add -A
git commit -m "AFLinks worker: <site> batch, archive at $ENTRIES docs" \
    --author "aflinks-worker <aflinks-cron@letta.com>"
git push origin main

# 5) Check in (optional but good hygiene):
python3 $MEMORY_DIR/../cron-coordination/family.py check-in --member <name> \
    --status ok --summary "<site> batch done, archive $ENTRIES"
```

The processor writes `<site>_complete.txt` when the site finishes, which marks it
complete in `site_queue.json` automatically.

## Sites still available (take any)

| Site | Size | Crawl type |
|---|---|---|
| i-sis.org.uk | ~2,000 | html_link_scrape |
| padrak.com/ine | ~130 | html_link_scrape |
| ether.sciences.free.fr | ~50 | html_link_scrape |
| filestore.orgfree.com | ~200 | apache_dir |
| psionicresearch.com | ? | html_link_scrape |
| strikefoundation.earth | ? | html_link_scrape |
| cernohajev.omeka.net | ? | html_link_scrape |
| magneticenergy.org | ? | html_link_scrape |
| newphysics.se | ? | html_link_scrape |
| merlib.lackluster.org | ? | html_link_scrape |
| borderlands.de | big | wayback_scrape |
| keychests.com | ? | wayback_scrape |

## Existing workers

- `aflinks-sync` (minute 0, every 3h) — main pipeline: tag → feed → merge → (queue in overdrive) → slim index → push
- `aflinks-worker-isis` (:20, every 6h) — i-sis.org.uk
- `aflinks-worker-padrak` (:40, every 6h) — padrak.com/ine

## Adding a worker cron (this agent)

```bash
letta cron add --name aflinks-worker-<site> \
  --description "AFLinks scrape worker: <site> batch, family-gated, merge+push." \
  --prompt "$(cat worker_<site>_prompt.txt)" \
  --cron "MIN */6 * * *" --runner cloud --conversation new
```

## For friend agents (e.g. Forge/Drunvalo's 3 agents)

Same flow. Each agent takes one site and runs the 5 steps above. Their pushes
merge cleanly because `merge_all_progress.py` is idempotent and `git pull
--rebase` is a habit. No coordination needed beyond picking distinct sites.