from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: status_overlay.py ===
# 🛰 PTM Status Overlay – Updates a visible UI or dashboard overlay in real-time

import time
import json
import os
from self_rebuilder import get_rebuilder_status

OVERLAY_PATH = "ui/status_overlay.json"

def update_overlay_loop():
    print("[OVERLAY] 🧩 Starting status overlay updater...")

    while True:
        try:
            status = get_rebuilder_status()
            os.makedirs(os.path.dirname(OVERLAY_PATH), exist_ok=True)

            with open(OVERLAY_PATH, "w", encoding="utf-8") as f:
                json.dump(status, f, indent=2)

            print(f"[OVERLAY] ✅ Updated overlay: {OVERLAY_PATH}")
        except Exception as e:
            print(f"[OVERLAY ERROR] ❌ {e}")

        time.sleep(30)  # Update every 30 seconds

def log_event():ef drop_files_to_bridge():