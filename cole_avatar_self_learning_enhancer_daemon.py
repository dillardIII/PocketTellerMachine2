from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_avatar_self_learning_enhancer_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
LEARNING_LOG_FILE = "data/avatar_self_learning_log.json"
PERSONALITY_TRAINING_FILE = "data/avatar_personality_training.json"
CHECK_INTERVAL = 3600  # Every 1 hour

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load personality profiles ===
def load_personality_profiles():
    if os.path.exists(PERSONALITY_TRAINING_FILE):
        try:
            with open(PERSONALITY_TRAINING_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Enhance learning profile ===
def enhance_learning():
    profiles = load_personality_profiles()

    for avatar, profile in profiles.items():
        knowledge_level = profile.get("knowledge_level", 0)
        new_level = knowledge_level + 1
        profile["knowledge_level"] = new_level
        log_event(f"[SELF-LEARNING]: {avatar} knowledge increased to level {new_level}")

    with open(PERSONALITY_TRAINING_FILE, "w") as f:
        json.dump(profiles, f, indent=2)

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(LEARNING_LOG_FILE):
        try:
            with open(LEARNING_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(LEARNING_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def avatar_self_learning_loop():
    print("[AVATAR SELF-LEARNING]: Running enhancer daemon...")
    while True:
        try:
            enhance_learning()
        except Exception as e:
            log_event(f"[SELF-LEARNING ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run the Daemon ===
if __name__ == "__main__":
    avatar_self_learning_loop()