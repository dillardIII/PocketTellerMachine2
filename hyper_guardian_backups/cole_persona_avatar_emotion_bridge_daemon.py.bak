# cole_persona_avatar_emotion_bridge_daemon.py

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
EMOTION_BRIDGE_LOG = "data/persona_avatar_emotion_bridge_log.json"
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

# === Bridge persona emotions to avatar ===
def bridge_persona_emotions(avatars, personas):
    for name in avatars.keys():
        persona = personas.get(name)
        if persona:
            avatars[name]["emotional_state"] = persona.get("current_emotion", "neutral")
            avatars[name]["expression"] = persona.get("preferred_expression", "smile")
            avatars[name]["last_synced"] = datetime.now().isoformat()
            log_event(f"[EMOTION BRIDGE]: {name} avatar updated with persona emotion and expression.")
    with open(AVATAR_FILE, "w") as f:
        json.dump(avatars, f, indent=2)

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(EMOTION_BRIDGE_LOG):
        try:
            with open(EMOTION_BRIDGE_LOG, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(EMOTION_BRIDGE_LOG, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def persona_avatar_emotion_bridge_loop():
    print("[PERSONA-AVATAR EMOTION BRIDGE DAEMON]: Running...")
    while True:
        try:
            avatars = load_avatar_data()
            personas = load_persona_data()
            if avatars and personas:
                bridge_persona_emotions(avatars, personas)
        except Exception as e:
            log_event(f"[EMOTION BRIDGE ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_avatar_emotion_bridge_loop()