# cole_assistant_voice_preview_generator.py

import os
import json
from datetime import datetime

# === Configurations ===
AVATAR_FILE = "data/assistant_avatars.json"
VOICE_PREVIEW_FOLDER = "data/voice_previews"
PREVIEW_LOG_FILE = "data/voice_preview_generator_log.json"

# === Ensure folders exist ===
os.makedirs("data", exist_ok=True)
os.makedirs(VOICE_PREVIEW_FOLDER, exist_ok=True)

# === Load avatar profiles ===
def load_avatar_profiles():
    if os.path.exists(AVATAR_FILE):
        try:
            with open(AVATAR_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Generate fake preview placeholder (simulated) ===
def generate_voice_preview(name, style):
    filename = f"{VOICE_PREVIEW_FOLDER}/{name}_{style}.mp3"
    with open(filename, "w") as f:
        f.write(f"Simulated voice preview for {name} with {style} style.")
    log_event(f"[VOICE PREVIEW]: Generated preview → {filename}")
    return filename

# === Generate all previews ===
def generate_all_previews():
    avatars = load_avatar_profiles()
    for name, avatar in avatars.items():
        style = avatar.get("voice_style", "neutral")
        generate_voice_preview(name, style)

# === Logging Helper ===
def log_event(message):
    logs = []
    if os.path.exists(PREVIEW_LOG_FILE):
        try:
            with open(PREVIEW_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(PREVIEW_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Execute as CLI utility ===
if __name__ == "__main__":
    generate_all_previews()