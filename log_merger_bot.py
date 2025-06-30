from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: log_merger_bot.py ===
# Daemonized Merger Bot for PTM – Combines logs into self_commands_log.json every 30 seconds
# Supports manual merge and live status check

import os
import json
import time
from datetime import datetime
from threading import Thread

LOG_DIR = "logs/"
MERGED_FILE = os.path.join(LOG_DIR, "self_commands_log.json")
MERGE_TIMESTAMP_FILE = os.path.join(LOG_DIR, "last_merge_time.txt")

SOURCE_LOGS = [
    "cole_tasks.json",
    "strategy_reason_log.json",
    "intel_log.json",
    "bridge_sync.json"
]

# Store status of last merge for external access
last_merge_info = {
    "merged_at": None,
    "entry_count": 0,
    "source_file_count": len(SOURCE_LOGS)
}

def load_json_lines(filepath):
    entries = []
    if not os.path.exists(filepath):
        print(f"⛔ {filepath} does not exist.")
        return entries

    try:
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                    entries.append(entry)
                except json.JSONDecodeError:
                    print(f"❌ Skipped malformed line in {filepath}")
    except Exception as e:
        print(f"❌ Failed to read {filepath}: {e}")
    return entries

def merge_logs():
    global last_merge_info

    merged_entries = []

    print(f"🔍 Scanning {len(SOURCE_LOGS)} source logs...")
    for filename in SOURCE_LOGS:
        path = os.path.join(LOG_DIR, filename)
        entries = load_json_lines(path)
        print(f"✅ Loaded {len(entries)} from {filename}")
        merged_entries.extend(entries)

    # Timestamp the merge
    timestamp = datetime.utcnow().isoformat() + "Z"
    merged_log = {
        "merged_at": timestamp,
        "entry_count": len(merged_entries),
        "logs": merged_entries
    }

    try:
        with open(MERGED_FILE, "w") as f:
            json.dump(merged_log, f, indent=2)
        with open(MERGE_TIMESTAMP_FILE, "w") as t:
            t.write(timestamp)

        last_merge_info = {
            "merged_at": timestamp,
            "entry_count": len(merged_entries),
            "source_file_count": len(SOURCE_LOGS)
        }

        print(f"✅ Merge complete → {MERGED_FILE}")
    except Exception as e:
        print(f"❌ Failed to write merged log: {e}")

def run_merger():
    print("🧩 [Merger Bot] Manual log merge triggered...")
    merge_logs()

def run_merger_loop():
    print("🧩 [MergerBot] Daemon running in background every 30 seconds...")
    while True:
        merge_logs()
        time.sleep(30)

def start_merger_bot():
    Thread(target=run_merger_loop, daemon=True).start()

def manual_merge():
    merge_logs()
    return last_merge_info

def get_merger_status():
    return last_merge_info

if __name__ == "__main__":
    run_merger()

def log_event():ef drop_files_to_bridge():