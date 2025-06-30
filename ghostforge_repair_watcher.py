from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghostforge_repair_watcher.py ===

# 🔧 GhostForge Repair Watcher – Monitors repair requests and activates GhostForge recovery.

import os
import json
from datetime import datetime

REQUESTS_FILE = "requests/ghostforge_repair_requests.json"
REPAIR_LOG = "logs/ghostforge_repair_log.json"
REBUILD_PATH = "repair_queue/rebuild_targets.json"

def load_repair_requests():
    """Load all queued repair requests."""
    if not os.path.exists(REQUESTS_FILE):
        return []
    try:
        with open(REQUESTS_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[GhostForgeWatcher] ❌ Failed to load repair requests: {e}")
        return []

def log_repair_action(file_list, action="queued"):
    """Log which files are being repaired or sent to GhostForge."""
    os.makedirs(os.path.dirname(REPAIR_LOG), exist_ok=True)
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "action": action,
        "files": file_list
    }

    try:
        if os.path.exists(REPAIR_LOG):
            with open(REPAIR_LOG, "r") as f:
                logs = json.load(f)
        else:
            logs = []

        logs.append(entry)

        with open(REPAIR_LOG, "w") as f:
            json.dump(logs, f, indent=2)

        print(f"[GhostForgeWatcher] 🛠️ Logged repair action for {len(file_list)} file(s).")
    except Exception as e:
        print(f"[GhostForgeWatcher] ❌ Failed to log repair: {e}")

def push_to_rebuild_queue(file_list):
    """Push files into the rebuild queue for GhostForge to process."""
    os.makedirs(os.path.dirname(REBUILD_PATH), exist_ok=True)

    try:
        if os.path.exists(REBUILD_PATH):
            with open(REBUILD_PATH, "r") as f:
                current = json.load(f)
        else:
            current = []

        for file in file_list:
            if file not in current:
                current.append(file)

        with open(REBUILD_PATH, "w") as f:
            json.dump(current, f, indent=2)

        print(f"[GhostForgeWatcher] 🔄 Queued {len(file_list)} files for rebuild.")
    except Exception as e:
        print(f"[GhostForgeWatcher] ❌ Failed to queue rebuild: {e}")

def process_repair_requests():
    """Main function – handles queued repairs and preps for GhostForge."""
    print("[GhostForgeWatcher] 🚨 Checking for repair requests...")
    requests = load_repair_requests()
    if not requests:
        print("[GhostForgeWatcher] ✅ No active repair requests.")
        return

    files_to_fix = []
    for req in requests:
        if req.get("request_type") == "file_repair":
            files_to_fix.extend(req.get("files", []))

    unique_files = sorted(set(files_to_fix))

    if unique_files:
        log_repair_action(unique_files, action="queued")
        push_to_rebuild_queue(unique_files)
    else:
        print("[GhostForgeWatcher] 💤 No valid files to process.")

# === Boot trigger
if __name__ == "__main__":
    process_repair_requests()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():