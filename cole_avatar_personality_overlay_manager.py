# cole_avatar_personality_overlay_manager.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
OVERLAY_LOG_FILE = "data/avatar_overlay_manager_log.json"
CHECK_INTERVAL = 300  # Every 5 minutes

# === Overlay presets based on mood or state ===
OVERLAY_MAP = {
    "happy": "Radiant Glow + Green Highlights",
    "frustrated": "Dark Cloud + Red Highlights",
    "calm": "Soft Blue Aura",
    "thinking": "Pulsing Light",
    "talking": "Waveform Animation"
}

# === Ensure data directory exists ===
os.makedirs("data", exist_ok=True)

def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def apply_overlay_adjustments():
    mood_state = load_current_mood_state()

    for persona, mood in mood_state.items():
        overlay = OVERLAY_MAP.get(mood, OVERLAY_MAP["calm"])
        log_event(f"[OVERLAY MANAGER]: {persona} avatar overlay set to '{overlay}' due to mood '{mood}'.")

def log_event(message):
    logs = []
    if os.path.exists(OVERLAY_LOG_FILE):
        try:
            with open(OVERLAY_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(OVERLAY_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

if __name__ == "__main__":
    print("[OVERLAY MANAGER]: Starting...")
    apply_overlay_adjustments()