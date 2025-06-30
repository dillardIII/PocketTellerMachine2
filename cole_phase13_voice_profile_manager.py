from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase13_voice_profile_manager.py

import os
import json
from datetime import datetime

# === Voice Profiles Data File ===
VOICE_PROFILE_FILE = "data/cole_voice_profiles.json"
VOICE_LOG_FILE = "data/cole_voice_profile_events_log.json"
os.makedirs("data", exist_ok=True)

# === Default Voice Profiles ===
DEFAULT_PROFILES = [
    {"name": "Sensei", "style": "mentor", "voice_id": "mentor_voice", "description": "Calm, wise, and patient tone."},
    {"name": "Mo Cash", "style": "hustler", "voice_id": "mocash_voice", "description": "Fast-talking, energetic, street-smart."},
    {"name": "Sunny", "style": "optimist", "voice_id": "sunny_voice", "description": "Positive, cheerful, high energy."},
    {"name": "Chessmaster", "style": "strategist", "voice_id": "chessmaster_voice", "description": "Calculated, slow, and methodical."}
]

# === Initialize profiles ===
def initialize_voice_profiles():
    if not os.path.exists(VOICE_PROFILE_FILE):
        with open(VOICE_PROFILE_FILE, "w") as f:
            json.dump(DEFAULT_PROFILES, f, indent=2)
        print("[VOICE PROFILE MANAGER]: Default voice profiles initialized.")

# === Add or update voice profile ===
def add_voice_profile(name, style, voice_id, description):
    with open(VOICE_PROFILE_FILE, "r") as f:
        profiles = json.load(f)
    profile = next((p for p in profiles if p['name'] == name), None):
    if profile:
        profile.update({"style": style, "voice_id": voice_id, "description": description})
        log_voice_event(name, "Updated voice profile.")
    else:
        profiles.append({"name": name, "style": style, "voice_id": voice_id, "description": description})
        log_voice_event(name, "New voice profile created.")
    with open(VOICE_PROFILE_FILE, "w") as f:
        json.dump(profiles, f, indent=2)

# === Log voice events ===
def log_voice_event(name, message):
    logs = []
    if os.path.exists(VOICE_LOG_FILE):
        with open(VOICE_LOG_FILE, "r") as f:
            logs = json.load(f)
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "voice": name,
        "event": message
    })
    with open(VOICE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Get voice profiles list ===
def get_voice_profiles():
    if os.path.exists(VOICE_PROFILE_FILE):
        with open(VOICE_PROFILE_FILE, "r") as f:
            return json.load(f)
    return []

if __name__ == "__main__":
    initialize_voice_profiles()
    print("[VOICE PROFILE MANAGER]: Ready. Voice profiles loaded.")

def log_event():ef drop_files_to_bridge():