from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_avatar_voice_tone_changer_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_TONE_STATE_FILE = "data/avatar_voice_tone_state.json"
VOICE_TONE_LOG_FILE = "data/avatar_voice_tone_changer_log.json"
CHECK_INTERVAL = 300  # Every 5 minutes

os.makedirs("data", exist_ok=True)

# === Load current mood state ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Load current voice tone state ===
def load_voice_tone_state():
    if os.path.exists(VOICE_TONE_STATE_FILE):
        try:
            with open(VOICE_TONE_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Save voice tone state ===
def save_voice_tone_state(state):
    with open(VOICE_TONE_STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

# === Change voice tone based on mood ===
def update_voice_tone():
    mood_state = load_mood_state()
    voice_state = load_voice_tone_state()

    for persona, mood in mood_state.items():
        tone = map_mood_to_tone(mood)
        voice_state[persona] = tone
        log_event(f"[VOICE TONE CHANGER]: {persona} voice tone set to {tone} based on mood {mood}")

    save_voice_tone_state(voice_state)

def map_mood_to_tone(mood):
    mapping = {
        "happy": "energetic",
        "frustrated": "serious",
        "calm": "soft"
    }
    return mapping.get(mood, "neutral")

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(VOICE_TONE_LOG_FILE):
        try:
            with open(VOICE_TONE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_TONE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main daemon loop ===
def voice_tone_changer_loop():
    print("[VOICE TONE CHANGER]: Running...")
    while True:
        try:
            update_voice_tone()
        except Exception as e:
            log_event(f"[VOICE TONE CHANGER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    voice_tone_changer_loop()