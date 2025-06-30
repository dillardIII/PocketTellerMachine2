from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_voice_style_preset_manager.py

import os
import json
from datetime import datetime

# === Configurations ===
VOICE_STYLE_PRESETS_FILE = "data/voice_style_presets.json"
LOG_FILE = "data/voice_style_preset_log.json"

# === Ensure folders ===
os.makedirs("data", exist_ok=True)

# === Default Presets ===
DEFAULT_PRESETS = {
    "Professional": {"tone": "neutral", "pace": "medium", "emotion": "calm"},
    "Laid-back": {"tone": "soft", "pace": "slow", "emotion": "chill"},
    "Intense": {"tone": "sharp", "pace": "fast", "emotion": "serious"},
    "Smooth": {"tone": "melodic", "pace": "medium", "emotion": "soothing"},
    "Hype Mode": {"tone": "energetic", "pace": "fast", "emotion": "excited"},
    "Whisper Mode": {"tone": "whisper", "pace": "slow", "emotion": "mysterious"},
    "Classic AI": {"tone": "robotic", "pace": "medium", "emotion": "neutral"},
    "Human Cloned": {"tone": "realistic", "pace": "user_defined", "emotion": "user_defined"}
}

# === Load Presets ===
def load_presets():
    if os.path.exists(VOICE_STYLE_PRESETS_FILE):
        try:
            with open(VOICE_STYLE_PRESETS_FILE, "r") as f:
                return json.load(f)
        except:
            return DEFAULT_PRESETS
    return DEFAULT_PRESETS

# === Save Presets ===
def save_presets(presets):
    with open(VOICE_STYLE_PRESETS_FILE, "w") as f:
        json.dump(presets, f, indent=2)

# === Log Event ===
def log_event(message):
    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Add or Update Preset ===
def add_or_update_preset(name, config):
    presets = load_presets()
    presets[name] = config
    save_presets(presets)
    log_event(f"[VOICE STYLE]: Updated preset {name}")

# === Get All Presets ===
def get_all_presets():
    return load_presets()

# Example Usage (testable)
if __name__ == "__main__":
    add_or_update_preset("TestStyle", {"tone": "deep", "pace": "medium", "emotion": "intense"})
    print(get_all_presets())