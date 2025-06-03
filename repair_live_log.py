# === FILE: repair_live_log.py ===
# Live repair log tracker and display stream

import json
import os
import time

REPAIR_LOG_FILE = "logs/repair_log.json"
seen_entries = set()

def load_repair_log():
    if not os.path.exists(REPAIR_LOG_FILE):
        return []

    try:
        with open(REPAIR_LOG_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("[LogViewer] ⚠️ Malformed repair log.")
        return []

def stream_live_repair_log(interval=2):
    print("[LogViewer] 🛰️ Monitoring live repair activity...\n")
    while True:
        log = load_repair_log()
        for entry in log:
            key = entry.get("timestamp", "") + str(entry.get("requests_handled"))
            if key not in seen_entries:
                seen_entries.add(key)
                print(f"[{entry['timestamp']}] ➤ {entry['requests_handled']}")
        time.sleep(interval)

if __name__ == "__main__":
    stream_live_repair_log()