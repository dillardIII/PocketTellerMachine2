from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bot_status.py ===
# 🛰️ Bot Status Tracker – Provides live status updates for UI and logs

import json
import os
from datetime import datetime

STATUS_FILE = "logs/bot_status.json"
os.makedirs("logs", exist_ok=True)

def update_bot_status(status):
    """
    Saves the current status of the bot to a JSON file.

    Args:
        status (str): Description of bot's current state.
    """
    timestamp = datetime.utcnow().isoformat() + "Z"
    data = {
        "status": status,
        "timestamp": timestamp
    }

    with open(STATUS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"[BOT STATUS] 📡 {status} @ {timestamp}")

def get_bot_status():
    """
    Returns the most recent bot status entry.

    Returns:
        dict: Bot status and timestamp.
    """
    if not os.path.exists(STATUS_FILE):
        return {"status": "Unknown", "timestamp": "N/A"}

    with open(STATUS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def log_event():ef drop_files_to_bridge():