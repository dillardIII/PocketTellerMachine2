# cole_visual_voice_persona_sync_daemon.py

import os
import json
import time
from datetime import datetime
import pytz

CENTRAL_TZ = pytz.timezone("US/Central")

def get_local_time():
    return datetime.now(CENTRAL_TZ)

# === Configurations ===
PERSONA_FILE = "data/voice_persona_profiles.json"
AVATAR_FILE = "data/assistant_avatars.json"
SYNC_LOG_FILE = "data/visual_voice_persona_sync_log.json"
CHECK_INTERVAL = 1200  # Every 20 minutes

# === Ensure data directory exists ===
os.makedirs("data", exist_ok=True)

# === Load persona data ===
def load_persona_profiles():
    if os.path.exists(PERSONA_FILE):
        try:
            with open(PERSONA_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Load avatar data ===
def load_avatar_data():
    if os.path.exists(AVATAR_FILE):
        try:
            with open(AVATAR_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Synchronize visual and voice persona settings ===
def synchronize_visual_voice(personas, avatars):
    for name, persona in personas.items():
        avatar = avatars.get(name, {})
        avatar["voice_style"] = persona.get("voice_style", "default")
        avatar["expression"] = persona.get("preferred_expression", "neutral")
        avatar["mood"] = persona.get("current_emotion", "neutral")
        avatar["last_synced"] = datetime.now().isoformat()
        avatars[name] = avatar
        log_event(f"[SYNC]: Synced avatar for {name} with voice persona settings.")
    with open(AVATAR_FILE, "w") as f:
        json.dump(avatars, f, indent=2)

# === Logging helper ===
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
def visual_voice_persona_sync_loop():
    print("[VISUAL VOICE PERSONA SYNC DAEMON]: Running...")
    while True:
        try:
            personas = load_persona_profiles()
            avatars = load_avatar_data()
            if personas:
                synchronize_visual_voice(personas, avatars)
        except Exception as e:
            log_event(f"[SYNC ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    visual_voice_persona_sync_loop()