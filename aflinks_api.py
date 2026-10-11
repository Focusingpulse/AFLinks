#!/usr/bin/env python3
"""aflinks_api.py — write files into AFLinks (and sibling Focusingpulse repos)
through the GitHub Git Data API instead of `git push`.

WHY THIS EXISTS
---------------
AFLinks is ~3.9 GB. A `git push` from a sandbox clone fails with:

    error: RPC failed; HTTP 500
    send-pack: unexpected disconnect while reading sideband packet

That is a *transfer* failure, not a permissions failure — authentication
succeeds. Pack negotiation cannot complete at that repo size from a shallow /
blob-filtered clone.

Commits built server-side through the Git Data API move only the blobs that
actually changed, so repo size is irrelevant. Reads still work fine over git
(the standard sparse clone); use this only for writes.

USAGE
-----
  # one file
  python3 aflinks_api.py put --path database/foo.json --file ./foo.json \
      --message "rescue: add foo"

  # many files in ONE atomic commit (preferred for sweeps)
  python3 aflinks_api.py put --manifest ./changes.json \
      --message "rescue-sweep: +12 documents"

  # delete
  python3 aflinks_api.py rm --path old/file.md --message "chore: drop old file"

  # just read a file (works for private/large paths without cloning)
  python3 aflinks_api.py cat --path database/research-index.json

MANIFEST FORMAT (JSON object, repo-path -> source)
  {
    "database/foo.json":  {"file": "./local_foo.json"},
    "journal/bar.md":     {"text": "literal contents"},
    "index/baz.json":     {"data": {"any": "json object"}}
  }

TOKEN
-----
Resolved from $GUTHUBN / $GITHUB_TOKEN if present, otherwise fetched from the
Letta agent secrets API. Must carry contents:write. The first candidate is
probed; a read-only token is skipped rather than silently producing a 403.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

API = "https://api.github.com"
DEFAULT_REPO = "Focusingpulse/AFLinks"
UA = "aflinks-api-writer (+research archive)"


# --------------------------------------------------------------------------
# token resolution
# --------------------------------------------------------------------------

def _probe_write(token: str, repo: str) -> bool:
    """Zero-side-effect capability probe.

    DELETE a ref that does not exist:
      lacks contents:write -> 403
      has   contents:write -> 422 (reference does not exist)
    Nothing is created or destroyed.
    """
    url = f"{API}/repos/{repo}/git/refs/heads/__aflinks_probe_nonexistent"
    req = urllib.request.Request(url, method="DELETE")
    req.add_header("Authorization", f"token {token}")
    req.add_header("User-Agent", UA)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status not in (401, 403)
    except urllib.error.HTTPError as e:
        return e.code not in (401, 403)
    except Exception:
        return False


def _candidate_tokens() -> list[str]:
    cands: list[str] = []
    for key in ("GUTHUBN", "GITHUB_TOKEN", "GH_TOKEN"):
        v = os.environ.get(key)
        if v:
            cands.append(v)

    api_key = os.environ.get("LETTA_API_KEY")
    base = os.environ.get("LETTA_BASE_URL")
    agent = os.environ.get("LETTA_AGENT_ID") or os.environ.get("AGENT_ID")
    if api_key and base and agent:
        try:
            req = urllib.request.Request(
                f"{base}/v1/agents/{agent}/secrets",
                headers={"Authorization": f"Bearer {api_key}", "User-Agent": UA},
            )
            with urllib.request.urlopen(req, timeout=20) as r:
                secrets = json.load(r)
            for s in secrets if isinstance(secrets, list) else []:
                if not isinstance(s, dict):
                    continue
                v = s.get("value")
                if isinstance(v, str) and any(
                    v.startswith(p) for p in
                    ("github_pat_", "ghp_", "gho_", "ghs_", "ghu_")
                ):
                    cands.append(v)
        except Exception:
            pass

    seen: set[str] = set()
    out: list[str] = []
    for c in cands:
        if c and c not in seen:
            seen.add(c)
            out.append(c)
    return out


def resolve_token(repo: str = DEFAULT_REPO, verbose: bool = False) -> str:
    cands = _candidate_tokens()
    if not cands:
        sys.exit("aflinks_api: no GitHub token available (env or Letta secrets)")
    for t in cands:
        if _probe_write(t, repo):
            return t
    # Nothing probed writable — return the first so the caller gets a real
    # API error rather than a confusing local failure.
    if verbose:
        print("aflinks_api: warning — no candidate proved contents:write",
              file=sys.stderr)
    return cands[0]


# --------------------------------------------------------------------------
# github helpers
# --------------------------------------------------------------------------

def api(method: str, path: str, token: str, body: dict | None = None):
    url = path if path.startswith("http") else f"{API}{path}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", UA)
    if data:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:400]
        sys.exit(f"aflinks_api: {method} {path} -> HTTP {e.code}\n{detail}")


def try_api(method: str, path: str, token: str,
            body: dict | None = None) -> tuple[int, dict]:
    """Like api() but returns (status, payload) instead of exiting."""
    url = path if path.startswith("http") else f"{API}{path}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", UA)
    if data:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read()
            return r.status, (json.loads(raw) if raw else {})
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", "replace")
        try:
            return e.code, json.loads(raw)
        except Exception:
            return e.code, {"message": raw[:400]}
    except Exception as e:
        return 0, {"message": str(e)}


def get_head(repo: str, branch: str, token: str) -> tuple[str, str]:
    ref = api("GET", f"/repos/{repo}/git/ref/heads/{branch}", token)
    commit_sha = ref["object"]["sha"]
    commit = api("GET", f"/repos/{repo}/git/commits/{commit_sha}", token)
    return commit_sha, commit["tree"]["sha"]


def put_files(repo: str, branch: str, entries: list[dict], message: str,
              token: str, retries: int = 5) -> dict:
    """Create ONE commit containing every entry. Entries:
       {"path": str, "data": bytes|str, "mode": "100644"|"100755"}
    `mode` defaults to 100644. Paths are removed with data=None.

    RETRIES on non-fast-forward. Multiple agents push to main concurrently, so
    a ref update can lose a race between reading HEAD and patching it. Each
    retry re-reads HEAD and rebuilds blobs/tree/commit on top of the new tip,
    so the change is never silently dropped and nothing is force-pushed.
    """
    last_err = ""
    for attempt in range(1, retries + 1):
        parent_sha, base_tree = get_head(repo, branch, token)

        # Reuse blob SHAs across retries: content does not change, so re-uploading
        # on every attempt would be pure waste.
        tree: list[dict] = []
        for e in entries:
            if e.get("data") is None:
                tree.append({"path": e["path"], "mode": "100644", "type": "blob",
                             "sha": None})
                continue
            if e.get("_blob") is None:
                blob = api("POST", f"/repos/{repo}/git/blobs", token, {
                    "content": base64.b64encode(e["data"]).decode(),
                    "encoding": "base64",
                })
                e["_blob"] = blob["sha"]
            tree.append({"path": e["path"], "mode": e.get("mode", "100644"),
                         "type": "blob", "sha": e["_blob"]})

        new_tree = api("POST", f"/repos/{repo}/git/trees", token,
                       {"base_tree": base_tree, "tree": tree})
        commit = api("POST", f"/repos/{repo}/git/commits", token, {
            "message": message,
            "tree": new_tree["sha"],
            "parents": [parent_sha],
        })

        status, payload = try_api(
            "PATCH", f"/repos/{repo}/git/refs/heads/{branch}", token,
            {"sha": commit["sha"], "force": False})
        if status in (200, 201):
            return commit

        last_err = payload.get("message", f"HTTP {status}")
        if status == 422 and "fast forward" in last_err.lower():
            print(f"aflinks_api: {branch} moved during write "
                  f"(attempt {attempt}/{retries}) — re-reading HEAD and retrying",
                  file=sys.stderr)
            import time as _t
            _t.sleep(1.5 * attempt)
            continue
        sys.exit(f"aflinks_api: ref update failed -> HTTP {status}\n{last_err}")

    sys.exit(f"aflinks_api: could not update {branch} after {retries} attempts "
             f"(concurrent writers): {last_err}")


# --------------------------------------------------------------------------
# cli
# --------------------------------------------------------------------------

def _entries_from_manifest(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        manifest = json.load(f)
    out: list[dict] = []
    for repo_path, src in manifest.items():
        if "file" in src:
            with open(src["file"], "rb") as f:
                data = f.read()
        elif "data" in src:
            data = json.dumps(src["data"], indent=1).encode()
        elif "text" in src:
            data = src["text"].encode()
        else:
            raise SystemExit(f"manifest entry {repo_path!r} needs file/data/text")
        out.append({"path": repo_path, "data": data,
                    "mode": src.get("mode", "100644")})
    return out


def main() -> None:
    p = argparse.ArgumentParser(description="Write files to AFLinks via GitHub API")
    p.add_argument("--repo", default=DEFAULT_REPO)
    p.add_argument("--branch", default="main")
    sub = p.add_subparsers(dest="cmd", required=True)

    put = sub.add_parser("put", help="create one commit with one or more files")
    put.add_argument("--path")
    put.add_argument("--file")
    put.add_argument("--text")
    put.add_argument("--manifest")
    put.add_argument("--message", required=True)
    put.add_argument("--mode", default="100644")

    rm = sub.add_parser("rm", help="delete a path")
    rm.add_argument("--path", required=True)
    rm.add_argument("--message", required=True)

    cat = sub.add_parser("cat", help="print a file's contents")
    cat.add_argument("--path", required=True)

    args = p.parse_args()
    token = resolve_token(args.repo)

    if args.cmd == "cat":
        d = api("GET", f"/repos/{args.repo}/contents/{args.path}"
                       f"?ref={args.branch}", token)
        print(base64.b64decode(d["content"]).decode("utf-8", "replace"))
        return

    if args.cmd == "rm":
        head_sha, _ = get_head(args.repo, args.branch, token)
        current = api("GET", f"/repos/{args.repo}/contents/{args.path}"
                             f"?ref={args.branch}", token)
        api("DELETE", f"/repos/{args.repo}/contents/{args.path}", token, {
            "message": args.message,
            "sha": current["sha"],
            "branch": args.branch,
        })
        print(f"deleted {args.path}")
        return

    if args.manifest:
        entries = _entries_from_manifest(args.manifest)
    else:
        if not args.path:
            sys.exit("put: --path is required unless --manifest is used")
        if args.file:
            with open(args.file, "rb") as f:
                data = f.read()
        elif args.text is not None:
            data = args.text.encode()
        else:
            sys.exit("put: one of --file, --text or --manifest is required")
        entries = [{"path": args.path, "data": data, "mode": args.mode}]

    commit = put_files(args.repo, args.branch, entries, args.message, token)
    print(f"committed {len(entries)} file(s): {commit['sha'][:12]}")
    for e in entries:
        print(f"  {e['path']}")


if __name__ == "__main__":
    main()
