from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_mood_to_voice_bridge_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_COMMAND_FILE = "data/voice_command_queue.json"
MOOD_TO_VOICE_MAP_FILE = "data/mood_to_voice_map.json"
LOG_FILE = "data/persona_mood_to_voice_bridge_log.json"
CHECK_INTERVAL = 60  # Check every 60 seconds

# Ensure directories
os.makedirs("data", exist_ok=True)

# === Loaders ===
def load_json_file(file_path, default_value):
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except:
            return default_value
    return default_value

def save_json_file(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

# === Core Logic ===
def bridge_mood_to_voice():
    mood_state = load_json_file(MOOD_STATE_FILE, {})
    mood_to_voice_map = load_json_file(MOOD_TO_VOICE_MAP_FILE, {})
    voice_queue = load_json_file(VOICE_COMMAND_FILE, [])

    for persona, mood in mood_state.items():
        voice_tone = mood_to_voice_map.get(mood, "neutral_voice")
        command = f"{persona} use_voice_tone {voice_tone}"
        if command not in voice_queue:
            voice_queue.append(command)
            log_event(f"[MOOD->VOICE]: {persona} mood {mood} → assigned voice tone {voice_tone}")

    save_json_file(VOICE_COMMAND_FILE, voice_queue)

# === Logging ===
def log_event(message):
    logs = load_json_file(LOG_FILE, [])
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    save_json_file(LOG_FILE, logs[-500:])

# === Daemon Loop ===
def mood_to_voice_bridge_loop():
    print("[MOOD->VOICE BRIDGE]: Running...")
    while True:
        try:
            bridge_mood_to_voice()
        except Exception as e:
            log_event(f"[ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    mood_to_voice_bridge_loop()