from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_voice_command_queue_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
VOICE_COMMAND_QUEUE_FILE = "data/voice_command_queue.json"
VOICE_ENGINE_LOG_FILE = "data/voice_engine_log.json"
CHECK_INTERVAL = 60  # Check every 1 minute

# === Ensure data directory exists ===
os.makedirs("data", exist_ok=True)

# === Load Command Queue ===
def load_command_queue():
    if os.path.exists(VOICE_COMMAND_QUEUE_FILE):
        try:
            with open(VOICE_COMMAND_QUEUE_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_command_queue(queue):
    with open(VOICE_COMMAND_QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=2)

# === Logging Helper ===
def log_event(message):
    logs = []
    if os.path.exists(VOICE_ENGINE_LOG_FILE):
        try:
            with open(VOICE_ENGINE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_ENGINE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Process Voice Commands ===
def process_voice_commands():
    queue = load_command_queue()
    if not queue:
        return

    for command in queue:
        # Simulate sending the command to the voice engine or assistant
        log_event(f"[VOICE ENGINE]: Executing voice command → {command}")
        print(f"[VOICE ENGINE]: Executing voice command → {command}")

    # Clear queue after processing
    save_command_queue([])

# === Main Daemon Loop ===
def voice_command_queue_loop():
    print("[VOICE ENGINE]: Voice Command Queue Daemon running...")
    while True:
        try:
            process_voice_commands()
        except Exception as e:
            log_event(f"[VOICE ENGINE ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    voice_command_queue_loop()