from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_brain_logger.py ===

import os
import json
from datetime import datetime

BRAIN_LOG_PATH = "data/cole_brain_log.json"

# Ensure the data directory exists
os.makedirs("data", exist_ok=True)

def log_strategy_reason(strategy="None", reason="No reason provided"):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "strategy": strategy,
        "reason": reason
    }

    try:
        if os.path.exists(BRAIN_LOG_PATH):
            with open(BRAIN_LOG_PATH, "r") as f:
                logs = json.load(f)
        else:
            logs = []

        logs.append(log_entry)

        with open(BRAIN_LOG_PATH, "w") as f:
            json.dump(logs, f, indent=2)

        print(f"[Cole Brain] Strategy reason logged: {strategy} — {reason}")

    except Exception as e:
        print(f"[Cole Brain] Failed to log: {e}")

def log_event():ef drop_files_to_bridge():