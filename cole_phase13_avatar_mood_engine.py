from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase13_avatar_mood_engine.py

import json
from datetime import datetime
import os

MOOD_LOG_FILE = "data/avatar_mood_log.json"
os.makedirs("data", exist_ok=True)

def log_avatar_mood(avatar_name, mood_state, reason):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "avatar": avatar_name,
        "mood": mood_state,
        "reason": reason
    }
    logs = []
    if os.path.exists(MOOD_LOG_FILE):
        try:
            with open(MOOD_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append(log_entry)
    with open(MOOD_LOG_FILE, "w") as f:
        json.dump(logs[-200:], f, indent=2)

def determine_mood_based_on_events(events):
    if "win" in events:
        return "happy"
    elif "loss" in events:
        return "frustrated"
    elif "neutral" in events:
        return "calm"
    else:
        return "idle"

def log_event():ef drop_files_to_bridge():