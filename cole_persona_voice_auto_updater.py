from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_voice_auto_updater.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_SETTINGS_FILE = "data/persona_voice_settings.json"
VOICE_LOG_FILE = "data/voice_auto_update_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Ensure data directory ===
os.makedirs("data", exist_ok=True)

# === Voice Profiles Map ===
VOICE_PRESETS = {
    "happy": {"tone": "cheerful", "speed": "fast", "emotion": "positive"},
    "frustrated": {"tone": "stern", "speed": "normal", "emotion": "neutral"},
    "calm": {"tone": "soft", "speed": "slow", "emotion": "calm"}
}

# === Logging ===
def log_voice_update(message):
    logs = []
    if os.path.exists(VOICE_LOG_FILE):
        try:
            with open(VOICE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load current mood state ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Update persona voice settings based on mood ===
def update_persona_voices(mood_state):
    new_voice_settings = {}
    for persona, mood in mood_state.items():
        preset = VOICE_PRESETS.get(mood, VOICE_PRESETS["calm"])
        new_voice_settings[persona] = preset
        log_voice_update(f"[VOICE UPDATE]: {persona} voice updated to {preset} based on mood '{mood}'")

    with open(VOICE_SETTINGS_FILE, "w") as f:
        json.dump(new_voice_settings, f, indent=2)

# === Main Daemon Loop ===
def persona_voice_auto_update_loop():
    print("[VOICE AUTO UPDATER]: Running...")
    while True:
        try:
            mood_state = load_mood_state()
            if mood_state:
                update_persona_voices(mood_state)
            else:
                log_voice_update("[VOICE AUTO UPDATER]: No mood state found.")
        except Exception as e:
            log_voice_update(f"[VOICE AUTO UPDATER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_voice_auto_update_loop()

def log_event():ef drop_files_to_bridge():