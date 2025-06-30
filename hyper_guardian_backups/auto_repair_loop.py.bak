# === FILE: auto_repair_loop.py ===

# 🛠️ AutoRepair Loop – Scans core folders, detects damage, re-requests files

import os
from inspector_bot import inspect_directory
from ghostcore_state_manager import request_file_repair

WATCHED_DIRS = ["ptm_inbox", "ptm_bridge", "vault", "core"]

def start_auto_repair_loop():
    print("[AutoRepair] 🔧 Repair loop started.")
    while True:
        try:
            for folder in WATCHED_DIRS:
                missing = inspect_directory(folder)
                if missing:
                    for f in missing:
                        request_file_repair(f)
            time.sleep(10)
        except Exception as e:
            print(f"[AutoRepair] ❌ Loop error: {e}")