from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bridge_status_scanner.py ===
# Monitors bridge_sync.json and reports system sync stats

import json
import os
from datetime import datetime

BRIDGE_SYNC_FILE = "bridge_sync.json"

def read_bridge_status():
    """
    Reads and returns the current sync status.
    """
    if not os.path.exists(BRIDGE_SYNC_FILE):
        return {
            "status": "missing",
            "message": "No bridge sync file found"
        }

    try:
        with open(BRIDGE_SYNC_FILE, "r") as f:
            data = json.load(f)
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to read sync file: {str(e)}"
        }

    return {
        "status": "ok",
        "last_sync": data.get("timestamp"),
        "success_count": data.get("success_count", 0),
        "fail_count": data.get("fail_count", 0),
        "last_error": data.get("last_error", "None")
    }

def print_bridge_status():
    """
    Prints bridge sync stats for terminal viewing.
    """
    status = read_bridge_status()
    print("[BridgeStatus] 🔄 Bridge Sync Summary")
    for key, value in status.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    print_bridge_status()

def log_event():ef drop_files_to_bridge():