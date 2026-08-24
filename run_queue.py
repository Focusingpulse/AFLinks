#!/usr/bin/env python3
"""
Master orchestrator: checks site_queue.json, crawls and processes the next pending site.
Called by the cloud cron. Does incremental merge after each site's batch.

Flow:
1. Check queue for next action
2. If a site needs crawling -> crawl it
3. If a site has a file list but isn't fully processed -> process a batch
4. After each batch -> incremental merge into index.json
5. If all sites are done -> clean up and signal completion
"""
import json, os, sys, subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
QUEUE_PATH = os.path.join(SCRIPT_DIR, "site_queue.json")

def get_safe_name(site_name):
    return site_name.replace('.', '_').replace('/', '_')

def get_paths(site_name):
    safe = get_safe_name(site_name)
    return {
        "filelist": os.path.join(SCRIPT_DIR, f"{safe}_filelist.json"),
        "progress": os.path.join(SCRIPT_DIR, f"{safe}_progress.json"),
        "entries": os.path.join(SCRIPT_DIR, f"{safe}_entries.json"),
        "complete": os.path.join(SCRIPT_DIR, f"{safe}_complete.txt"),
    }

def main():
    with open(QUEUE_PATH, 'r', encoding='utf-8') as f:
        queue = json.load(f)
    
    print("=== Site Queue Status ===")
    for s in queue["sites"]:
        paths = get_paths(s["name"])
        status = s["status"]
        if os.path.exists(paths["complete"]):
            status = "complete"
            s["status"] = "complete"
        
        file_count = s.get("file_count", "?")
        if os.path.exists(paths["progress"]):
            with open(paths["progress"], 'r') as pf:
                prog = json.load(pf)
                done = prog["last_processed"] + 1
                total = file_count if isinstance(file_count, int) else "?"
                status = f"in_progress ({done}/{total})"
        elif os.path.exists(paths["filelist"]):
            with open(paths["filelist"], 'r') as ff:
                fl = json.load(ff)
                status = f"crawled ({len(fl)} files, not started)"
                s["file_count"] = len(fl)
        
        print(f"  {s['name']}: {status}")
    
    # Save updated queue
    with open(QUEUE_PATH, 'w', encoding='utf-8') as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)
    
    # Find next site to process
    # Priority: 1) in_progress sites with file lists, 2) crawled but not started, 3) pending sites to crawl
    site_to_process = None
    site_to_crawl = None
    
    for s in queue["sites"]:
        paths = get_paths(s["name"])
        
        # Skip complete or down sites
        if os.path.exists(paths["complete"]) or s["status"] in ("complete", "site_down"):
            continue
        
        # Check if tuks.nl is done (special case - it was started separately)
        if s["name"] == "tuks.nl":
            tuks_progress = os.path.join(SCRIPT_DIR, "tuks_progress.json")
            if os.path.exists(tuks_progress):
                with open(tuks_progress, 'r') as f:
                    prog = json.load(f)
                if prog["last_processed"] + 1 >= 1718:
                    s["status"] = "complete"
                    continue
                # tuks.nl uses its own processor
                site_to_process = s
                break
        
        # If site has a file list but not complete -> process it
        if os.path.exists(paths["filelist"]):
            if os.path.exists(paths["progress"]):
                with open(paths["progress"], 'r') as f:
                    prog = json.load(f)
                with open(paths["filelist"], 'r') as f:
                    fl = json.load(f)
                if prog["last_processed"] + 1 < len(fl):
                    site_to_process = s
                    break
            else:
                site_to_process = s
                break
        
        # If site is pending and hasn't been crawled -> crawl it
        if s["status"] == "pending" and not os.path.exists(paths["filelist"]):
            if site_to_crawl is None:
                site_to_crawl = s
    
    # Action 1: Process a site that has a file list
    if site_to_process:
        name = site_to_process["name"]
        print(f"\n=== Processing: {name} ===")
        
        if name == "tuks.nl":
            # Use the tuks-specific processor
            script = os.path.join(SCRIPT_DIR, "process_tuks_cloud.py")
        else:
            script = os.path.join(SCRIPT_DIR, "process_generic_cloud.py")
            # Run generic processor with site name argument
            result = subprocess.run([sys.executable, script, name], capture_output=False)
            # After processing, do incremental merge
            print("\n--- Incremental merge ---")
            merge_script = os.path.join(SCRIPT_DIR, "merge_incremental.py")
            # For generic sites, we need to merge from their progress file
            # merge_incremental.py reads tuks_progress.json by default, so we need a generic version
            merge_generic(SCRIPT_DIR, name)
            return
        
        result = subprocess.run([sys.executable, script], capture_output=False)
        
        # After processing, do incremental merge
        print("\n--- Incremental merge ---")
        merge_script = os.path.join(SCRIPT_DIR, "merge_incremental.py")
        subprocess.run([sys.executable, merge_script], capture_output=False)
        return
    
    # Action 2: Crawl a new site
    if site_to_crawl:
        name = site_to_crawl["name"]
        print(f"\n=== Crawling new site: {name} ===")
        print(f"  Type: {site_to_crawl['crawl_type']}")
        print(f"  Notes: {site_to_crawl.get('notes', '')}")
        
        script = os.path.join(SCRIPT_DIR, "crawl_generic.py")
        result = subprocess.run([sys.executable, script, name], capture_output=False)
        
        # Check if crawl produced a file list
        paths = get_paths(name)
        if os.path.exists(paths["filelist"]):
            with open(paths["filelist"], 'r') as f:
                fl = json.load(f)
            print(f"\n  Crawl complete: {len(fl)} files found")
            site_to_crawl["status"] = "crawled"
            site_to_crawl["file_count"] = len(fl)
            with open(QUEUE_PATH, 'w', encoding='utf-8') as f:
                json.dump(queue, f, ensure_ascii=False, indent=2)
        else:
            print(f"\n  Crawl failed or found no files")
            site_to_crawl["status"] = "crawl_failed"
            with open(QUEUE_PATH, 'w', encoding='utf-8') as f:
                json.dump(queue, f, ensure_ascii=False, indent=2)
        return
    
    # Action 3: All sites done
    all_done = True
    for s in queue["sites"]:
        paths = get_paths(s["name"])
        if not os.path.exists(paths["complete"]) and s["status"] != "complete":
            all_done = False
            break
    
    if all_done:
        print("\n=== ALL SITES COMPLETE ===")
        # Create a completion marker
        with open(os.path.join(SCRIPT_DIR, "ALL_SITES_COMPLETE.txt"), 'w') as f:
            f.write(f"All sites complete at {__import__('time').strftime('%Y-%m-%d %H:%M:%S')}")
        print("Created ALL_SITES_COMPLETE.txt")
        print("The cron should be deleted manually or will self-detect this file.")
    else:
        print("\nNo actionable site found in this run. Will check again next cycle.")

def merge_generic(script_dir, site_name):
    """Merge entries from a generic site's progress file into index.json."""
    safe = site_name.replace('.', '_').replace('/', '_')
    progress_path = os.path.join(script_dir, f"{safe}_progress.json")
    index_path = os.path.join(script_dir, "index.json")
    
    if not os.path.exists(progress_path):
        print(f"  No progress file for {site_name}")
        return
    
    with open(index_path, 'r', encoding='utf-8') as f:
        existing = json.load(f)
    
    existing_urls = set(e.get('source_url', '') for e in existing)
    
    with open(progress_path, 'r') as f:
        progress = json.load(f)
    
    new_entries = progress.get("entries", [])
    added = 0
    for entry in new_entries:
        url = entry.get('source_url', '')
        if url and url not in existing_urls:
            entry['id'] = max(e['id'] for e in existing) + 1 + added
            existing.append(entry)
            existing_urls.add(url)
            added += 1
    
    print(f"  Existing: {len(existing) - added}, New: {added}, Total: {len(existing)}")
    
    if added > 0:
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(existing, f, ensure_ascii=False, indent=2)
        print(f"  Saved updated index.json")
    else:
        print(f"  No new entries to merge")

if __name__ == '__main__':
    main()
