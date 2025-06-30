# cole_avatar_persona_sync_daemon.py

import os
import json
import time
from datetime import datetime
import pytz

CENTRAL_TZ = pytz.timezone("US/Central")

def get_local_time():
    return datetime.now(CENTRAL_TZ)
import pytz

CENTRAL_TZ = pytz.timezone("US/Central")

def get_local_time():
    return datetime.now(CENTRAL_TZ)

# === Configurations ===
AVATAR_FILE = "data/assistant_avatars.json"
PERSONA_FILE = "data/voice_persona_profiles.json"
SYNC_LOG_FILE = "data/avatar_persona_sync_log.json"
CHECK_INTERVAL = 1800  # Every 30 minutes

os.makedirs("data", exist_ok=True)

# === Load avatar data ===
def load_avatar_data():
    if os.path.exists(AVATAR_FILE):
        try:
            with open(AVATAR_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Load persona data ===
def load_persona_data():
    if os.path.exists(PERSONA_FILE):
        try:
            with open(PERSONA_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Sync avatars with personas ===
def sync_avatar_to_persona(avatars, personas):
    for name in avatars.keys():
        persona = personas.get(name)
        if persona:
            avatars[name]["mood"] = persona.get("mood_balance", "neutral")
            avatars[name]["clarity"] = persona.get("clarity", 80)
            avatars[name]["last_synced"] = datetime.now().isoformat()
            log_event(f"[SYNC]: {name} avatar updated with persona mood and clarity.")
    with open(AVATAR_FILE, "w") as f:
        json.dump(avatars, f, indent=2)

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(SYNC_LOG_FILE):
        try:
            with open(SYNC_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(SYNC_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def avatar_persona_sync_loop():
    print("[AVATAR-PERSONA SYNC DAEMON]: Running...")
    while True:
        try:
            avatars = load_avatar_data()
            personas = load_persona_data()
            if avatars and personas:
                sync_avatar_to_persona(avatars, personas)
        except Exception as e:
            log_event(f"[SYNC ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    avatar_persona_sync_loop()