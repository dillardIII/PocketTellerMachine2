# === FILE: core/memory_logger.py ===

import os
import json
from datetime import datetime

LOG_DIR = "ptm_memory_logs"
os.makedirs(LOG_DIR, exist_ok=True)

def log_game_action(game_name, action, source="Unknown"):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "type": "game_action",
        "game": game_name,
        "action": action,
        "source": source
    }
    save_log(log_entry)

def log_trade_event(ticker, event_type, details):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "type": "trade_event",
        "ticker": ticker,
        "event": event_type,
        "details": details
    }
    save_log(log_entry)

def log_system_update(message, level="INFO"):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "type": "system_update",
        "level": level,
        "message": message
    }
    save_log(log_entry)

def save_log(entry):
    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    filename = f"{LOG_DIR}/{date_str}.json"

    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)