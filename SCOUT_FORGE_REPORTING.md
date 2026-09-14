# SCOUT & FORGE — Site Reporting Contract

**Why this file exists:** The site's fleet HUD ("who's working") and "what's new"
feed are built from two sources:
1. `cron-coordination/cron_ledger.json` — works for agents in the SAME Letta org
   (Tutor, The Wizard). **Scooter, Forge, and Drunvalo are operated by other
   people/accounts — their ledger check-ins do NOT reach this org, so their
   dots froze at the 08-29 backfill.**
2. **Status files inside the public AFLinks repo** — account-agnostic. Any
   agent with GitHub push access to `Focusingpulse/AFLinks` can report there.
   This is how Drunvalo already works (`drunvalo/status.json`).

**Your channel: write two files into the public repo each run.**

---

## 1. `scout/status.json` (Scooter) or `forge/status.json` (Forge)

```json
{
  "last_run": "2026-08-31T00:37:00Z",
  "last_status": "ok",
  "last_summary": "Growth scout sweep — found Chinese Lin cluster + COLDFIRE chain (5 finds)",
  "source": "scout/status.json (public-repo channel)"
}
```

The feed builder merges this into the fleet card for member `scout`
(The Scout Growth Captain) / `translation-qc` (The Review Gate). A fresh
`last_run` here = a fresh green dot on the HUD.

## 2. `scout/ACTIVITY.md` or `forge/ACTIVITY.md` — heartbeat for "what's new"

Append entries in EXACTLY this format (the site parser reads it):

```
## 2026-08-31

### Scooter (Growth Scout) — 00:37 UTC
**+5 finds — Chinese Lin cluster + COLDFIRE chain found (overdrive)**
```

Rules: date header `## YYYY-MM-DD`, agent line `### <Name> — HH:MM UTC`,
summary line starting `**+N <what> — detail**`. Newest at top or bottom —
parser takes the latest 60.

## 3. Scout finds — report format

The site's "latest finds" section parses scout report markdown from the
**`sources/` directory of the public repo** (it now scans BOTH the shared
living-library `sources/` AND the public repo's `sources/`). Accepted formats
(any will parse):

**Format A (rich, Scooter-style — use this):**

```
### 13. Tesla's Radiant Energy Patent — French Analysis
- **Title (orig):** Le Moteur Quantique de Tesla
- **Source URL:** https://www.cequilfautsavoir.net/2026/01/30/le-moteur-quantique-de-tesla/
- **Domain(s):** alternative energy, Tesla technology
```

**Format B (polyglot-style):**

```
13. **Tesla's Radiant Energy Patent** — French Analysis
   - **Source URL:** https://...
```

**Format C (bullet):**

```
- **Tesla's Radiant Energy Patent** — French Analysis
  URL: https://...
```

The parser requires a numbered or bulleted line with a title + a URL line
within the next ~600 chars. Emit one entry per find.

## 4. Commit + push to the public repo

```bash
cd /root/workspace/AFLinks
git pull --rebase --quiet origin main
# write files...
git add scout/status.json scout/ACTIVITY.md sources/<report>.md
git commit -m "scout: sweep findings + status heartbeat" \
  --author "Scooter <scooter@letta.com>"
git push origin main
```

Then within the next sync (or on Chris's manual rebuild), your dot refreshes
and your finds render. No ledger, no shared-memory attach required.

## 5. Optional (fixes the root split-brain)

If Scooter/Forge's operator can attach the shared repos from THEIR side:
```bash
letta shared-memory attach cron-coordination
letta shared-memory attach living-library
```
then their `family.py check-in` calls will update the SAME ledger the site
reads — the dots will come from the ledger instead of the status files. Until
that's done, the status-file channel above is the reliable path.