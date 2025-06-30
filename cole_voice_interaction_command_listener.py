from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_voice_interaction_command_listener.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
VOICE_COMMAND_FILE = "data/voice_command_queue.json"
VOICE_LOG_FILE = "data/voice_interaction_log.json"
CHECK_INTERVAL = 5  # Every 5 seconds

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load voice command queue ===
def load_voice_commands():
    if os.path.exists(VOICE_COMMAND_FILE):
        try:
            with open(VOICE_COMMAND_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

# === Clear processed voice command queue ===
def clear_voice_commands():
    with open(VOICE_COMMAND_FILE, "w") as f:
        json.dump([], f, indent=2)

# === Process voice commands ===
def process_voice_command(command):
    # Placeholder logic for processing voice command
    log_event(f"[VOICE COMMAND RECEIVED]: {command}")
    # Add actual command interpretation or task execution here

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(VOICE_LOG_FILE):
        try:
            with open(VOICE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Loop ===
def voice_command_listener_loop():
    print("[VOICE INTERACTION LISTENER]: Listening for voice commands...")
    while True:
        try:
            commands = load_voice_commands()
            if commands:
                for command in commands:
                    process_voice_command(command)
                clear_voice_commands()
        except Exception as e:
            log_event(f"[VOICE INTERACTION ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    voice_command_listener_loop()