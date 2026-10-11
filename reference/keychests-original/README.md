# KeyChests.com — original design reference (rescued from the Wayback Machine)

Fetched 2026-08-31. These are the actual visual assets of the ORIGINAL KeyChests.com
(dead since ~May 2013), pulled from the Internet Archive. Use them as the frame of
reference for the vault's chest/key interface work.

## Wayback captures

- Homepage (cleanest): https://web.archive.org/web/20130410071014/http://keychests.com/
- Homepage (earliest good): https://web.archive.org/web/20130404030905/http://keychests.com/
- Example chest page ("Banned Books of Truth", live files): https://web.archive.org/web/20130805223109/http://keychests.com/?c=159&r=75

## What the site actually was

Tagline: **"KeyChests — Don't just share your stuff, Sell it."**

Not a category/unlock navigation site. It was a crowd-funding + file-sharing marketplace
built on a literal chest-and-key metaphor:

- **Chests** = user-created file bundles, each with a numeric id (?c=159), creator + profile
  pic, optional vanity URL, file count + total size ("34 files — 281.37 MB"), view count
  ("748 Views"), dates, and a masonry grid of files with type icons (pdf/mp3/zip/jpg/video).
- **Keys** = secret access URLs (?ck=<hash>). "Success! You now have the key to this chest.
  With the key you can download everything here anytime." One chest, one key — that was the
  whole unlock mechanic.
- **Homepage structure** (April 2013):
  1. Header: logo + "login join"
  2. Pitch: "Great for 1. Selling Crowd Funding Perks After the Campaign is Done
     2. Getting Donations for Your Stuff 3. Sharing Files Easily"
  3. "Scan & Sell" grid of content types: EBooks · Songs/Podcasts · Source Code & Apps ·
     Photos/Art/Comics · Video Tutorials & Clips · College Exams & Papers
  4. Member perks: "Earn Cash & Get Paid · Have more than one chest · Customize Link URL"
  5. "my chest" — upload, share, get paid. Upload Files → get your chest key.
  6. File-type icons, masonry layout, jQuery, lightbox, SoundManager audio.

## Asset inventory (this folder)

| file | what it is |
|---|---|
| `icons_chest.png` | CLOSED wooden chest, 300×300, metal straps + padlock |
| `icons_chestopen.png` | OPEN chest, 300×300, lid up, gold/treasure glow |
| `anim_icons_key.gif` | Animated golden key, 100×100 |
| `icons_lock.png` | Padlock, 100×100 |
| `icons_link.png` | Link/chain icon, 32×32 |
| `logo.png` | KeyChests wordmark, 94×60 |
| `pdf.png` / `mp3.png` | File-type icons, 200×200 / 256×256 |

Not archived: `anim_chest.gif` (animated chest bounce) and the jpg/zip/video file icons
returned 404/redirect from the Archive; they can be recreated as SVG/CSS equivalents.

## Design lessons to carry into the new interface

- Chest = a curated collection with visible stats (files/size/views/creator) — the stat
  strip did real work.
- Key = the unlock flourish. The "you now have the key" moment is the emotional peak.
- Open/closed chest states are THE interaction feedback: closed = locked + blurred/dark,
  open = gold glow + lid up.
- The old site's categories were file types, flat. Our 44 subjects + 23 meta-categories
  are a richer dial than anything the original had — the chest/key language is the frame,
  our taxonomy is the content.