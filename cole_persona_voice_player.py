# cole_persona_voice_player.py

import os
import json
from datetime import datetime

# === Configurations ===
VOICE_SELECTION_FILE = "data/persona_voice_selection.json"
MOOD_LOG_FILE = "data/mood_engine_log.json"
os.makedirs("data", exist_ok=True)

# === Mock Voice Playback (Placeholder for real TTS) ===
def play_voice_line(persona, message):
    try:
        voice_selection = load_voice_selection()
        selected_voice = voice_selection.get(persona, {}).get("voice", "DefaultVoice")
        print(f"[VOICE PLAYER]: {persona} ({selected_voice}) says: '{message}'")
        log_voice_event(f"[{persona} ({selected_voice})]: {message}")
    except Exception as e:
        log_voice_event(f"[VOICE PLAYER ERROR]: {e}")

# === Load Voice Selection ===
def load_voice_selection():
    if os.path.exists(VOICE_SELECTION_FILE):
        try:
            with open(VOICE_SELECTION_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Logging ===
def log_voice_event(message):
    logs = []
    if os.path.exists(MOOD_LOG_FILE):
        try:
            with open(MOOD_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(MOOD_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Example Playback ===
if __name__ == "__main__":
    play_voice_line("DefaultPersona", "Hello, I'm your assistant. How can I help you?")