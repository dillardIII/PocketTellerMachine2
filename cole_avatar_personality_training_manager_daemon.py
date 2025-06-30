from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_avatar_personality_training_manager_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
PERSONALITY_TRAINING_FILE = "data/avatar_personality_training.json"
TRAINING_LOG_FILE = "data/personality_training_log.json"
CHECK_INTERVAL = 1800  # Every 30 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load training records ===
def load_training_sessions():
    if os.path.exists(PERSONALITY_TRAINING_FILE):
        try:
            with open(PERSONALITY_TRAINING_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Update training session for avatars ===
def conduct_personality_training():
    sessions = load_training_sessions()

    for avatar, profile in sessions.items():
        training_level = profile.get("training_level", 0)
        new_level = training_level + 1
        profile["training_level"] = new_level
        log_event(f"[PERSONALITY TRAINING]: {avatar} advanced to level {new_level}")

    with open(PERSONALITY_TRAINING_FILE, "w") as f:
        json.dump(sessions, f, indent=2)

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(TRAINING_LOG_FILE):
        try:
            with open(TRAINING_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(TRAINING_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def personality_training_manager_loop():
    print("[PERSONALITY TRAINING MANAGER]: Running training manager daemon...")
    while True:
        try:
            conduct_personality_training()
        except Exception as e:
            log_event(f"[TRAINING ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run the Daemon ===
if __name__ == "__main__":
    personality_training_manager_loop()