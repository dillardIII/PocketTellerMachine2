from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: log_strategy_logger.py ===

import json
import os
from datetime import datetime

LOG_FILE = "data/strategy_reason_log.json"

def log_strategy_reason(strategy_name, reason):
    os.makedirs("data", exist_ok=True)
    try:
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w") as f:
                json.dump([], f)

        with open(LOG_FILE, "r") as f:
            logs = json.load(f)

        logs.append({
            "timestamp": datetime.now().isoformat(),
            "strategy": strategy_name,
            "reason": reason
        })

        with open(LOG_FILE, "w") as f:
            json.dump(logs, f, indent=2)

        print(f"[Cole Brain] Strategy reason logged: {strategy_name} — {reason}")

    except Exception as e:
        print(f"[Cole Brain] Failed to log strategy reason: {e}")

def log_event():ef drop_files_to_bridge():