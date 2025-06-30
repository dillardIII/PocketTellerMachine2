# cole_persona_mood_visual_updater.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
VISUAL_PROFILE_FILE = "data/persona_visual_profiles.json"
MOOD_VISUAL_LOG_FILE = "data/mood_visual_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Mood to Visual Cue Map ===
MOOD_VISUAL_MAP = {
    "happy": {"avatar_color": "bright_yellow", "expression": "smiling"},
    "frustrated": {"avatar_color": "dark_red", "expression": "frowning"},
    "calm": {"avatar_color": "light_blue", "expression": "neutral"},
    "angry": {"avatar_color": "deep_red", "expression": "angry_face"}
}

# === Ensure data directory ===
os.makedirs("data", exist_ok=True)

# === Logging ===
def log_visual_updater_event(message):
    logs = []
    if os.path.exists(MOOD_VISUAL_LOG_FILE):
        try:
            with open(MOOD_VISUAL_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(MOOD_VISUAL_LOG_FILE, "w") as f:
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

# === Update persona visuals ===
def update_visual_profile(persona, mood):
    profile = MOOD_VISUAL_MAP.get(mood, {"avatar_color": "grey", "expression": "neutral"})
    log_visual_updater_event(f"[MOOD VISUAL]: {persona} mood '{mood}' updated visuals to color '{profile['avatar_color']}' and expression '{profile['expression']}'")
    return profile

def update_visual_profiles():
    mood_state = load_mood_state()
    updated_visuals = {}

    for persona, mood in mood_state.items():
        updated_visuals[persona] = update_visual_profile(persona, mood)

    with open(VISUAL_PROFILE_FILE, "w") as f:
        json.dump(updated_visuals, f, indent=2)

# === Main Daemon Loop ===
def persona_mood_visual_updater_loop():
    print("[MOOD VISUAL UPDATER]: Running...")
    while True:
        try:
            update_visual_profiles()
        except Exception as e:
            log_visual_updater_event(f"[MOOD VISUAL UPDATER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_mood_visual_updater_loop()