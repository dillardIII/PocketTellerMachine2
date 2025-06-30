from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_voice_avatar_sync_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
VOICE_CONFIG_FILE = "data/persona_voice_config.json"
AVATAR_CONFIG_FILE = "data/persona_avatar_config.json"
SYNC_LOG_FILE = "data/voice_avatar_sync_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(SYNC_LOG_FILE):
        try:
            with open(SYNC_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(SYNC_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load Voice and Avatar Configs ===
def load_voice_config():
    if os.path.exists(VOICE_CONFIG_FILE):
        try:
            with open(VOICE_CONFIG_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def load_avatar_config():
    if os.path.exists(AVATAR_CONFIG_FILE):
        try:
            with open(AVATAR_CONFIG_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Sync Voices and Avatars ===
def sync_voices_and_avatars():
    voices = load_voice_config()
    avatars = load_avatar_config()

    synced = {}

    for persona, voice in voices.items():
        avatar = avatars.get(persona, None)
        synced[persona] = {
            "voice": voice,
            "avatar": avatar if avatar else "No Avatar Assigned":
        }

    with open("data/persona_voice_avatar_sync.json", "w") as f:
        json.dump(synced, f, indent=2)

    log_event(f"[VOICE-AVATAR SYNC]: Synced {len(synced)} personas.")

# === Main Daemon Loop ===
def voice_avatar_sync_loop():
    print("[VOICE-AVATAR SYNC]: Running voice-avatar sync daemon...")
    while True:
        try:
            sync_voices_and_avatars()
        except Exception as e:
            log_event(f"[SYNC ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    voice_avatar_sync_loop()