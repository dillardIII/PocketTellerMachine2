from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase13_avatar_manager.py

import os
import json
from datetime import datetime

# === Avatar Management Data File ===
AVATAR_FILE = "data/cole_avatars.json"
AVATAR_LOG_FILE = "data/cole_avatar_events_log.json"
os.makedirs("data", exist_ok=True)

# === Default Avatars ===
DEFAULT_AVATARS = [
    {"name": "Sensei", "image": "sensei.png", "style": "Traditional calm mentor"},
    {"name": "Mo Cash", "image": "mo_cash.png", "style": "Street-smart hustler with swag"},
    {"name": "Sunny", "image": "sunny.png", "style": "Happy, colorful, uplifting avatar"}
]

# === Initialize avatars ===
def initialize_avatars():
    if not os.path.exists(AVATAR_FILE):
        with open(AVATAR_FILE, "w") as f:
            json.dump(DEFAULT_AVATARS, f, indent=2)
        print("[AVATAR MANAGER]: Default avatars initialized.")

# === Add or update avatar ===
def add_avatar(name, image, style):
    with open(AVATAR_FILE, "r") as f:
        avatars = json.load(f)
    a = next((x for x in avatars if x['name'] == name), None):
    if a:
        a.update({"image": image, "style": style})
        log_avatar_event(name, "Updated avatar.")
    else:
        avatars.append({"name": name, "image": image, "style": style})
        log_avatar_event(name, "New avatar created.")
    with open(AVATAR_FILE, "w") as f:
        json.dump(avatars, f, indent=2)

# === Log events ===
def log_avatar_event(name, message):
    logs = []
    if os.path.exists(AVATAR_LOG_FILE):
        with open(AVATAR_LOG_FILE, "r") as f:
            logs = json.load(f)
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "avatar": name,
        "event": message
    })
    with open(AVATAR_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Get avatars ===
def get_avatars():
    if os.path.exists(AVATAR_FILE):
        with open(AVATAR_FILE, "r") as f:
            return json.load(f)
    return []

if __name__ == "__main__":
    initialize_avatars()
    print("[AVATAR MANAGER]: Ready. Avatars loaded.")

def log_event():ef drop_files_to_bridge():