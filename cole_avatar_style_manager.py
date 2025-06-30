from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_avatar_style_manager.py

import os
import json
from datetime import datetime

# === Configurations ===
AVATAR_STYLE_FILE = "data/avatar_style_profiles.json"
AVATAR_STYLE_LOG_FILE = "data/avatar_style_log.json"

# === Ensure folders ===
os.makedirs("data", exist_ok=True)

# === Default Avatar Styles ===
AVATAR_STYLE_PROFILES = {
    "Mo Cash": {"style": "urban", "colors": ["gold", "black"], "extras": "bling"},
    "Mentor": {"style": "professional", "colors": ["blue", "gray"], "extras": "glasses"},
    "Drill Instructor": {"style": "military", "colors": ["camouflage", "green"], "extras": "hat"},
    "Optimist": {"style": "vibrant", "colors": ["yellow", "orange"], "extras": "smile"},
    "Chill Trader": {"style": "casual", "colors": ["light blue", "white"], "extras": "surfboard"},
    "Strategist": {"style": "classic", "colors": ["black", "white"], "extras": "notepad"},
    "OG": {"style": "retro", "colors": ["brown", "gold"], "extras": "chain"},
    "Shadow": {"style": "dark", "colors": ["black", "purple"], "extras": "mask"}
}

# === Save avatar profiles ===
def save_avatar_styles():
    with open(AVATAR_STYLE_FILE, "w") as f:
        json.dump(AVATAR_STYLE_PROFILES, f, indent=2)
    log_event("[AVATAR STYLE MANAGER]: Avatar styles saved.")

# === Logging helper ===
def log_event(message):
    logs = []
    if os.path.exists(AVATAR_STYLE_LOG_FILE):
        try:
            with open(AVATAR_STYLE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(AVATAR_STYLE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Example usage ===
if __name__ == "__main__":
    save_avatar_styles()
    print("[AVATAR STYLE MANAGER]: Avatar profiles initialized.")