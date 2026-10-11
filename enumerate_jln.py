#!/usr/bin/env python3
"""Enumerate JLN Labs (jnaudin.free.fr + jlnlabs.online.fr + bingofuel.online.fr).
Bounded same-family BFS: collects document URLs (.pdf/.htm/.html/.doc/.txt) as
{url, filename} entries -> jnaudin_free_fr_filelist.json. Checkpoints to
jnaudin_free_fr_crawl_state.json every 30 pages.
"""
import os, re, json, time, urllib.parse, urllib.request, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(SCRIPT_DIR, "jnaudin_free_fr_crawl_state.json")
OUT = os.path.join(SCRIPT_DIR, "jnaudin_free_fr_filelist.json")

SEEDS = [
    "http://jnaudin.free.fr/",
    "http://jlnlabs.online.fr/",
    "http://bingofuel.online.fr/bingofuel/index.htm",
    "http://www.jlnlab.com/",
]
# Allow these host families
ALLOW_HOSTS = ("jnaudin.free.fr", "jlnlabs.online.fr", "bingofuel.online.fr", "www.jlnlab.com", "jlnlab.com")
DOC_EXT = (".pdf", ".htm", ".html", ".doc", ".txt", ".rtf", ".php")
MAX_VISITED = 8000
MAX_DOCS = 6000

def fetch(url, timeout=20):
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except Exception as e:
        print(f"  ERR: {url}: {e}", flush=True)
        return None

def norm_url(url, base):
    absu = urllib.parse.urljoin(base, url)
    absu = absu.replace("&amp;", "&")
    # strip fragments, trailing junk
    absu = absu.split("#")[0]
    return absu

def is_doc(u):
    p = urllib.parse.urlparse(u)
    path = p.path.lower()
    return path.endswith(DOC_EXT)

def save_state(visited, pending, docs, seen_urls):
    st = {"visited": sorted(visited), "pending": pending, "docs": docs, "seen_urls": sorted(seen_urls)}
    tmp = STATE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(st, f, ensure_ascii=False)
    os.replace(tmp, STATE)

def write_filelist(docs):
    with open(OUT + ".tmp", "w", encoding="utf-8") as f:
        json.dump(docs, f, ensure_ascii=False, indent=1)
    os.replace(OUT + ".tmp", OUT)

def main():
    visited, pending, docs, seen_urls = set(), [], [], set()
    if os.path.exists(STATE):
        st = json.load(open(STATE, encoding="utf-8"))
        visited = set(st["visited"])
        pending = st["pending"]
        docs = st["docs"]
        seen_urls = set(st["seen_urls"])
        print(f"Resumed: {len(visited)} visited, {len(docs)} docs, {len(pending)} pending")
    else:
        pending = list(SEEDS)

    doc_urls = {d["url"] for d in docs}
    last_ck = time.time()

    while pending and len(visited) < MAX_VISITED and len(docs) < MAX_DOCS:
        url = pending.pop(0)
        if url in visited:
            continue
        visited.add(url)
        data = fetch(url)
        if data is None:
            continue
        if is_doc(url):
            # document page itself — may contain more links too, try both
            pass
        text = data.decode("utf-8", errors="replace")
        links = re.findall(r'href=["\']([^"\']+)["\']', text, re.I)
        new_docs = 0
        for raw in links:
            raw = raw.strip()
            if raw.startswith("javascript:") or raw.startswith("mailto:") or raw.startswith("#"):
                continue
            absu = norm_url(raw, url)
            p = urllib.parse.urlparse(absu)
            if p.scheme not in ("http", "https"):
                continue
            if not p.hostname or not any(p.hostname == h or p.hostname.endswith("." + h) for h in ALLOW_HOSTS):
                continue
            # skip search engines / external cgi
            if "freefind" in p.hostname or "webring" in p.hostname:
                continue
            low = p.path.lower()
            if any(seg in low for seg in ("/images/", "/img/", "/gif/", "/photos/")) and not low.endswith(DOC_EXT):
                continue
            if is_doc(absu):
                if absu not in doc_urls and absu not in seen_urls:
                    fname = urllib.parse.unquote(p.path.split("/")[-1]) or p.path
                    if not fname or fname in (".", "/"):
                        fname = absu
                    docs.append({"url": absu, "filename": fname})
                    doc_urls.add(absu)
                    new_docs += 1
                # HTML doc pages still carry cross-links — queue for BFS too
                if p.path.lower().endswith((".htm", ".html", ".php")) and absu not in seen_urls and absu not in visited:
                    seen_urls.add(absu)
                    pending.append(absu)
            else:
                if absu not in seen_urls and absu not in visited:
                    seen_urls.add(absu)
                    pending.append(absu)
        if time.time() - last_ck > 20:
            save_state(visited, pending, docs, seen_urls)
            write_filelist(docs)
            print(f"  [ck] visited {len(visited)} docs {len(docs)} pending {len(pending)}", flush=True)
            last_ck = time.time()
        time.sleep(0.25)

    save_state(visited, pending, docs, seen_urls)
    write_filelist(docs)
    print(f"DONE: visited {len(visited)}, docs {len(docs)}, pending {len(pending)}")

if __name__ == "__main__":
    main()