# === FILE: repair_broadcaster.py ===
# Distributes repair events across active bot systems

import json
import os
import time

REPAIR_LOG_FILE = "logs/repair_log.json"
BOTS = ["FixOps", "GPTAssist", "BravoRecon", "StrategyMapper"]

sent_hashes = set()

def load_repairs():
    if not os.path.exists(REPAIR_LOG_FILE):
        return []
    try:
        with open(REPAIR_LOG_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def broadcast_to_bots(entry):
    for bot in BOTS:
        print(f"[Broadcast] 📡 Sending to {bot}: {entry['requests_handled']}")

def start_broadcast_loop(interval=10):
    print("[Broadcaster] 🌐 Starting repair broadcast loop...")
    while True:
        log = load_repairs()
        for entry in log:
            key = entry.get("timestamp", "") + str(entry.get("requests_handled"))
            if key not in sent_hashes:
                sent_hashes.add(key)
                broadcast_to_bots(entry)
        time.sleep(interval)

if __name__ == "__main__":
    start_broadcast_loop()