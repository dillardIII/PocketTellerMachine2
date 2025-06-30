from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_voice_mood_reflector_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_PROFILE_FILE = "data/voice_persona_profiles.json"
MOOD_VOICE_LOG_FILE = "data/mood_voice_reflector_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Mood to Voice Preset Mapping ===
MOOD_VOICE_MAP = {
    "happy": "upbeat_clear",
    "frustrated": "low_firm",
    "calm": "soft_balanced",
    "angry": "stern_commanding"
}

# === Ensure data directory ===
os.makedirs("data", exist_ok=True)

# === Logging ===
def log_voice_reflector_event(message):
    logs = []
    if os.path.exists(MOOD_VOICE_LOG_FILE):
        try:
            with open(MOOD_VOICE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(MOOD_VOICE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load current mood state ===
def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Adjust voice profiles based on mood ===
def adjust_voice_profiles():
    mood_state = load_current_mood_state()
    new_voice_profiles = {}

    for persona, mood in mood_state.items():
        voice_preset = MOOD_VOICE_MAP.get(mood, "neutral_clear")
        new_voice_profiles[persona] = {"mood": mood, "voice_preset": voice_preset}
        log_voice_reflector_event(f"[MOOD VOICE REFLECTOR]: {persona} mood '{mood}' → voice preset set to '{voice_preset}'.")

    with open(VOICE_PROFILE_FILE, "w") as f:
        json.dump(new_voice_profiles, f, indent=2)

# === Main Daemon Loop ===
def mood_voice_reflector_loop():
    print("[MOOD VOICE REFLECTOR]: Running mood voice reflector...")
    while True:
        try:
            adjust_voice_profiles()
        except Exception as e:
            log_voice_reflector_event(f"[MOOD VOICE REFLECTOR ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    mood_voice_reflector_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():