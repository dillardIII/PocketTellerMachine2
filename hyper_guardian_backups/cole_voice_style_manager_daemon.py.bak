# cole_voice_style_manager_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
VOICE_STYLE_FILE = "data/voice_style_settings.json"
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_LOG_FILE = "data/voice_style_manager_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Logging ===
def log_event(message):
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

# === Load Voice Styles ===
def load_voice_styles():
    if os.path.exists(VOICE_STYLE_FILE):
        try:
            with open(VOICE_STYLE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Load Mood States ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Adjust Voice Style Based on Mood ===
def adjust_voice_styles():
    styles = load_voice_styles()
    moods = load_mood_state()

    for persona, current_mood in moods.items():
        if persona in styles:
            styles[persona]["current_style"] = mood_to_style(current_mood)
            log_event(f"[VOICE STYLE]: {persona} style adjusted to {styles[persona]['current_style']} based on mood {current_mood}")
        else:
            styles[persona] = {"current_style": mood_to_style(current_mood)}
            log_event(f"[VOICE STYLE]: {persona} style initialized to {styles[persona]['current_style']}")

    with open(VOICE_STYLE_FILE, "w") as f:
        json.dump(styles, f, indent=2)

def mood_to_style(mood):
    if mood == "happy":
        return "uplifting"
    elif mood == "frustrated":
        return "firm"
    elif mood == "calm":
        return "soothing"
    else:
        return "neutral"

# === Main Daemon Loop ===
def voice_style_manager_loop():
    print("[VOICE STYLE MANAGER]: Running voice style manager daemon...")
    while True:
        try:
            adjust_voice_styles()
        except Exception as e:
            log_event(f"[VOICE STYLE MANAGER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    voice_style_manager_loop()