from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 🌐 GhostNet Tracker – Logs every active AI, its mission, and updates system status dashboard

import os
import json
import time
from utils.logger import log_event

AI_STATUS_DIR = "data/ai_status"
TRACKER_LOG = "logs/ghostnet_tracker.json"
UPDATE_INTERVAL = 30  # seconds

os.makedirs(AI_STATUS_DIR, exist_ok=True)
os.makedirs(os.path.dirname(TRACKER_LOG), exist_ok=True)

def scan_ai_status():
    status_map = {}

    for filename in os.listdir(AI_STATUS_DIR):
        if filename.endswith(".json"):
            try:
                with open(os.path.join(AI_STATUS_DIR, filename), "r") as f:
                    status = json.load(f)
                    bot_name = status.get("name", filename.replace(".json", ""))
                    status_map[bot_name] = status
            except Exception as e:
                log_event("GhostNetTracker", {"error": str(e), "file": filename})

    return status_map

def save_tracker_log(status_map):
    try:
        with open(TRACKER_LOG, "w") as f:
            json.dump(status_map, f, indent=2)
        log_event("GhostNetTracker", {"status": "Updated tracker log", "bots": len(status_map)})
    except Exception as e:
        log_event("GhostNetTracker", {"error": str(e)})

def track_ghostnet():
    print("[GhostNet] 🛰️ Scanning active AI...")
    while True:
        try:
            status_map = scan_ai_status()
            save_tracker_log(status_map)
        except Exception as e:
            log_event("GhostNetTracker", {"error": str(e)})

        time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    track_ghostnet()