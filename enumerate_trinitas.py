#!/usr/bin/env python3
"""Enumerate trinitas.ru (Академия Тринитаризма) — Russian alt-physics journal.
Bounded same-host BFS from root; collects .htm article pages under /rus/doc/ as
{url, filename} -> trinitas_ru_filelist.json. Checkpoints to
trinitas_ru_crawl_state.json every 25 pages.
"""
import os, re, json, time, urllib.parse, urllib.request, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(SCRIPT_DIR, "trinitas_ru_crawl_state.json")
OUT = os.path.join(SCRIPT_DIR, "trinitas_ru_filelist.json")

SEEDS = ["https://trinitas.ru/rus/doc/0016/001h/00164738.htm",
         "https://www.trinitas.ru/rus/doc/0016/001k/00165960.htm",
         "https://trinitas.ru/rus/doc/0231/008a/02311142.htm"]
MAX_VISITED = 6000
MAX_DOCS = 5000

def fetch(url, timeout=20):
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except Exception as e:
        return None

def norm_url(url, base):
    absu = urllib.parse.urljoin(base, url)
    absu = absu.replace("&amp;", "&").split("#")[0]
    return absu

def is_doc(u):
    p = urllib.parse.urlparse(u)
    return p.path.lower().endswith(".htm") or p.path.lower().endswith(".html")

def normalize_trinitas(u):
    # The site's canonical path is /rus/doc/<section>/<sub>/<id>.htm
    p = urllib.parse.urlparse(u)
    path = p.path
    if path.startswith("/doc/"):
        path = "/rus" + path
    if path.startswith("/rus//"):
        path = path.replace("/rus//", "/rus/", 1)
    return urllib.parse.urlunparse(p._replace(path=path))

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
        visited = set(st["visited"]); pending = st["pending"]
        docs = st["docs"]; seen_urls = set(st["seen_urls"])
        print(f"Resumed: {len(visited)} visited, {len(docs)} docs, {len(pending)} pending", flush=True)
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
        text = data.decode("utf-8", errors="replace")
        links = re.findall(r'[Hh][Rr][Ee][Ff]=["\']([^"\'>]+)["\']', text)
        for raw in links:
            raw = raw.strip()
            if raw.startswith("javascript:") or raw.startswith("mailto:") or raw.startswith("#"):
                continue
            absu = norm_url(raw, url)
            absu = normalize_trinitas(absu)
            p = urllib.parse.urlparse(absu)
            if p.scheme not in ("http", "https"):
                continue
            if not p.hostname or not (p.hostname.endswith("trinitas.ru")):
                continue
            low = p.path.lower()
            if any(seg in low for seg in (".css", ".gif", ".jpg", ".jpeg", ".png", ".js")):
                continue
            if is_doc(absu):
                if absu not in doc_urls and absu not in seen_urls:
                    fname = urllib.parse.unquote(p.path.split("/")[-1]) or p.path
                    docs.append({"url": absu, "filename": fname})
                    doc_urls.add(absu)
                    # article pages carry cross-links — queue them too
                    if absu not in seen_urls and absu not in visited:
                        seen_urls.add(absu)
                        pending.append(absu)
            else:
                if absu not in seen_urls and absu not in visited:
                    seen_urls.add(absu)
                    pending.append(absu)
        if time.time() - last_ck > 25:
            save_state(visited, pending, docs, seen_urls)
            write_filelist(docs)
            print(f"  [ck] visited {len(visited)} docs {len(docs)} pending {len(pending)}", flush=True)
            last_ck = time.time()
        time.sleep(0.15)

    save_state(visited, pending, docs, seen_urls)
    write_filelist(docs)
    print(f"DONE: visited {len(visited)}, docs {len(docs)}, pending {len(pending)}", flush=True)

if __name__ == "__main__":
    main()