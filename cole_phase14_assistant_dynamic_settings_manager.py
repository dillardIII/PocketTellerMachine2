# cole_phase14_assistant_dynamic_settings_manager.py

import os
import json
from datetime import datetime

ASSISTANT_SETTINGS_FILE = "data/assistant_persona_settings.json"
os.makedirs("data", exist_ok=True)

# === Ensure file exists ===
if not os.path.exists(ASSISTANT_SETTINGS_FILE):
    with open(ASSISTANT_SETTINGS_FILE, "w") as f:
        json.dump({}, f, indent=2)

# === Load current assistant settings ===
def load_assistant_settings():
    with open(ASSISTANT_SETTINGS_FILE, "r") as f:
        return json.load(f)

# === Update assistant setting ===
def update_assistant_setting(assistant_name, setting_key, new_value):
    settings = load_assistant_settings()
    assistant = settings.get(assistant_name, {})
    assistant[setting_key] = new_value
    settings[assistant_name] = assistant
    with open(ASSISTANT_SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=2)
    print(f"[ASSISTANT SETTINGS]: Updated {assistant_name} - {setting_key} → {new_value}")

# === View assistant setting ===
def get_assistant_setting(assistant_name, setting_key):
    settings = load_assistant_settings()
    return settings.get(assistant_name, {}).get(setting_key, None)

# === Example usage ===
if __name__ == "__main__":
    update_assistant_setting("Mo Cash", "mood", "motivational_push")
    update_assistant_setting("Mentor", "voice_style", "calm_mentor")
    update_assistant_setting("Drill Instructor", "persona_title", "Command Coach")

    # View settings
    print(load_assistant_settings())