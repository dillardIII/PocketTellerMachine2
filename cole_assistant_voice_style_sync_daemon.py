# cole_assistant_voice_style_sync_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
AVATAR_FILE = "data/assistant_avatars.json"
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_STYLE_LOG_FILE = "data/voice_style_sync_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Ensure data directory exists ===
os.makedirs("data", exist_ok=True)

# === Load avatar profiles ===
def load_avatar_profiles():
    if os.path.exists(AVATAR_FILE):
        try:
            with open(AVATAR_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Load mood states ===
def load_mood_states():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Sync voice style based on mood ===
def sync_voice_style(avatars, moods):
    for name, avatar in avatars.items():
        mood = moods.get(name, "neutral")
        voice_style = mood_to_voice_style(mood)
        avatar["voice_style"] = voice_style
        avatar["voice_last_synced"] = datetime.now().isoformat()
        log_event(f"[VOICE SYNC]: {name} voice style synced to {voice_style} based on mood {mood}.")
    with open(AVATAR_FILE, "w") as f:
        json.dump(avatars, f, indent=2)

def mood_to_voice_style(mood):
    mapping = {
        "happy": "energetic",
        "frustrated": "serious",
        "calm": "soft",
        "angry": "firm",
        "sad": "gentle"
    }
    return mapping.get(mood, "neutral")

# === Logging Helper ===
def log_event(message):
    logs = []
    if os.path.exists(VOICE_STYLE_LOG_FILE):
        try:
            with open(VOICE_STYLE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_STYLE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def voice_style_sync_loop():
    print("[VOICE STYLE SYNC DAEMON]: Running...")
    while True:
        try:
            avatars = load_avatar_profiles()
            moods = load_mood_states()
            if avatars and moods:
                sync_voice_style(avatars, moods)
        except Exception as e:
            log_event(f"[VOICE STYLE SYNC ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    voice_style_sync_loop()