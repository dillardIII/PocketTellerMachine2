from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase13_avatar_voice_event_logger.py

import os
import json
from datetime import datetime

AVATAR_VOICE_EVENT_LOG_FILE = "data/avatar_voice_event_log.json"
os.makedirs("data", exist_ok=True)

def log_avatar_voice_event(event_type, avatar_name, mood, message):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "event_type": event_type,
        "avatar_name": avatar_name,
        "mood": mood,
        "message": message
    }
    if not os.path.exists(AVATAR_VOICE_EVENT_LOG_FILE):
        with open(AVATAR_VOICE_EVENT_LOG_FILE, "w") as f:
            json.dump([log_entry], f, indent=2)
    else:
        with open(AVATAR_VOICE_EVENT_LOG_FILE, "r") as f:
            logs = json.load(f)
        logs.append(log_entry)
        with open(AVATAR_VOICE_EVENT_LOG_FILE, "w") as f:
            json.dump(logs[-100:], f, indent=2)

def get_recent_voice_events(limit=20):
    if os.path.exists(AVATAR_VOICE_EVENT_LOG_FILE):
        with open(AVATAR_VOICE_EVENT_LOG_FILE, "r") as f:
            logs = json.load(f)
        return logs[-limit:]
    return []

def log_event():ef drop_files_to_bridge():