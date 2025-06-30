from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: service_status.py ===

import os
import json
from datetime import datetime

STATUS_FILE = "data/service_status.json"

def update_service_status(name, status, note=""):
    os.makedirs("data", exist_ok=True)
    now = datetime.utcnow().isoformat()
    
    try:
        if os.path.exists(STATUS_FILE):
            with open(STATUS_FILE, "r") as f:
                data = json.load(f)
        else:
            data = {}

        data[name] = {
            "status": status,
            "note": note,
            "updated": now
        }

        with open(STATUS_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"[StatusTracker] Failed to update status for {name}: {e}")

def get_all_statuses():
    try:
        if os.path.exists(STATUS_FILE):
            with open(STATUS_FILE, "r") as f:
                return json.load(f)
        return {}
    except:
        return {}

def log_event():ef drop_files_to_bridge():