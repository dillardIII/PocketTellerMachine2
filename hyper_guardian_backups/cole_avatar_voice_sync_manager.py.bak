# cole_avatar_voice_sync_manager.py

import os
import json
from datetime import datetime

# === Configurations ===
AVATAR_VOICE_FILE = "data/avatar_voice_profiles.json"
AVATAR_VOICE_LOG_FILE = "data/avatar_voice_log.json"

# === Ensure folders ===
os.makedirs("data", exist_ok=True)

# === Default Avatar Voice Mappings ===
AVATAR_VOICE_PROFILES = {
    "Mo Cash": {"voice_id": "mo_cash_voice_01", "tone": "aggressive", "speed": "fast"},
    "Mentor": {"voice_id": "mentor_voice_01", "tone": "calm", "speed": "moderate"},
    "Drill Instructor": {"voice_id": "drill_instructor_voice_01", "tone": "commanding", "speed": "loud_fast"},
    "Optimist": {"voice_id": "optimist_voice_01", "tone": "cheerful", "speed": "fast"},
    "Chill Trader": {"voice_id": "chill_trader_voice_01", "tone": "laid-back", "speed": "slow"},
    "Strategist": {"voice_id": "strategist_voice_01", "tone": "analytical", "speed": "moderate"},
    "OG": {"voice_id": "og_voice_01", "tone": "wise", "speed": "slow"},
    "Shadow": {"voice_id": "shadow_voice_01", "tone": "mysterious", "speed": "whisper"}
}

# === Save avatar voice profiles ===
def save_avatar_voice_profiles():
    with open(AVATAR_VOICE_FILE, "w") as f:
        json.dump(AVATAR_VOICE_PROFILES, f, indent=2)
    log_event("[AVATAR VOICE SYNC]: Avatar voice profiles saved.")

# === Logging helper ===
def log_event(message):
    logs = []
    if os.path.exists(AVATAR_VOICE_LOG_FILE):
        try:
            with open(AVATAR_VOICE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(AVATAR_VOICE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Example usage ===
if __name__ == "__main__":
    save_avatar_voice_profiles()
    print("[AVATAR VOICE SYNC]: Voice profiles initialized.")