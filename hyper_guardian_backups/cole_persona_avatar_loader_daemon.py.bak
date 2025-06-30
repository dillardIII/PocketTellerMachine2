# cole_persona_avatar_loader_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
AVATAR_DIRECTORY = "avatars"
AVATAR_LOG_FILE = "data/avatar_loader_log.json"
AVATAR_CONFIG_FILE = "data/persona_avatar_config.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Ensure directories ===
os.makedirs("data", exist_ok=True)
os.makedirs(AVATAR_DIRECTORY, exist_ok=True)

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(AVATAR_LOG_FILE):
        try:
            with open(AVATAR_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(AVATAR_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load or Initialize Avatar Config ===
def load_avatar_config():
    if os.path.exists(AVATAR_CONFIG_FILE):
        try:
            with open(AVATAR_CONFIG_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_avatar_config(config):
    with open(AVATAR_CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

# === Scan Avatars ===
def scan_avatars():
    return [f for f in os.listdir(AVATAR_DIRECTORY) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# === Update Avatar Config ===
def update_avatar_config():
    avatars = scan_avatars()
    config = load_avatar_config()

    for avatar in avatars:
        persona_name = os.path.splitext(avatar)[0]
        config[persona_name] = os.path.join(AVATAR_DIRECTORY, avatar)

    save_avatar_config(config)
    log_event(f"[AVATAR LOADER]: Loaded {len(avatars)} avatars.")

# === Main Loop ===
def avatar_loader_loop():
    print("[AVATAR LOADER]: Starting avatar scanner...")
    while True:
        try:
            update_avatar_config()
        except Exception as e:
            log_event(f"[AVATAR LOADER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    avatar_loader_loop()