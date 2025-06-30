from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: voice_recap_logger.py ===

import os
import json
from datetime import datetime

LOG_FILE = "logs/voice_recap_log.json"

def log_voice_recap(prompt, voice="Unknown", mood="default"):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "voice": voice,
        "mood": mood
    }

    os.makedirs("logs", exist_ok=True)
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs[-200:], f, indent=2)

def log_event():ef drop_files_to_bridge():