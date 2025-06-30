# cole_persona_voice_manager_daemon.py

import os
import json
import time
from datetime import datetime

# === Configuration ===
VOICE_CONFIG_FILE = "data/persona_voice_profiles.json"
VOICE_EVENT_LOG_FILE = "data/persona_voice_event_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Ensure data directory exists ===
os.makedirs("data", exist_ok=True)

# === Logging Helper ===
def log_voice_event(message):
    logs = []
    if os.path.exists(VOICE_EVENT_LOG_FILE):
        try:
            with open(VOICE_EVENT_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_EVENT_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load Voice Profiles ===
def load_voice_profiles():
    if not os.path.exists(VOICE_CONFIG_FILE):
        return []
    try:
        with open(VOICE_CONFIG_FILE, "r") as f:
            return json.load(f)
    except:
        return []

# === Dynamic Voice Adjustment Logic ===
def adjust_persona_voices():
    profiles = load_voice_profiles()
    updated_profiles = []
    for persona in profiles:
        current_style = persona.get("voice_style", "default")
        # Example style cycle logic
        if current_style == "default":
            persona["voice_style"] = "energetic"
        elif current_style == "energetic":
            persona["voice_style"] = "calm"
        elif current_style == "calm":
            persona["voice_style"] = "authoritative"
        else:
            persona["voice_style"] = "default"

        log_voice_event(f"[VOICE CYCLE]: {persona['name']} voice style changed to {persona['voice_style']}")
        updated_profiles.append(persona)
    
    # Save updated voice profiles
    with open(VOICE_CONFIG_FILE, "w") as f:
        json.dump(updated_profiles, f, indent=2)

# === Main Daemon Loop ===
def persona_voice_manager_loop():
    print("[PERSONA VOICE MANAGER DAEMON]: Running...")
    while True:
        try:
            adjust_persona_voices()
        except Exception as e:
            log_voice_event(f"[ERROR]: {e}")
            print(f"[VOICE MANAGER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run Daemon ===
if __name__ == "__main__":
    persona_voice_manager_loop()