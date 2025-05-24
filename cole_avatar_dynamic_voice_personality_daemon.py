# cole_avatar_dynamic_voice_personality_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_STYLE_FILE = "data/avatar_voice_styles.json"
VOICE_LOG_FILE = "data/avatar_voice_personality_log.json"
CHECK_INTERVAL = 300  # Every 5 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Voice Style Mapping by Mood ===
MOOD_VOICE_MAP = {
    "happy": "cheerful_bright",
    "frustrated": "harsh_sharp",
    "calm": "soft_smooth",
    "neutral": "balanced_neutral"
}

# === Load Mood State ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Save Updated Voice Styles ===
def save_voice_styles(styles):
    with open(VOICE_STYLE_FILE, "w") as f:
        json.dump(styles, f, indent=2)

# === Core Logic ===
def update_voice_styles():
    mood_state = load_mood_state()
    updated_styles = {}

    for persona, mood in mood_state.items():
        voice_style = MOOD_VOICE_MAP.get(mood, "balanced_neutral")
        updated_styles[persona] = voice_style
        log_event(f"[VOICE PERSONALITY]: {persona} voice changed to {voice_style} due to mood {mood}")

    save_voice_styles(updated_styles)

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

# === Main Daemon Loop ===
def dynamic_voice_personality_loop():
    print("[VOICE PERSONALITY DAEMON]: Running dynamic voice adjuster...")
    while True:
        try:
            update_voice_styles()
        except Exception as e:
            log_event(f"[VOICE PERSONALITY ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    dynamic_voice_personality_loop()