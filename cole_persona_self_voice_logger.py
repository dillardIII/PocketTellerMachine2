from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_self_voice_logger.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
VOICE_LOG_FILE = "data/persona_voice_log.json"
MOOD_STATE_FILE = "data/mood_state.json"
CHECK_INTERVAL = 1200  # Every 20 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load mood state ===
def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Voice lines map per mood ===
MOOD_VOICE_LINES = {
    "happy": [
        "That trade felt smooth. I'm on a roll!",
        "Let's keep the momentum going!",
        "Markets are smiling today."
    ],
    "frustrated": [
        "Ugh... I should have seen that loss coming.",
        "No worries, recalculating my next move.",
        "Even the best have bad days."
    ],
    "calm": [
        "Let's observe the flow patiently.",
        "Steady hands make steady gains.",
        "Breathing in... executing wisely."
    ]
}

# === Log voice event ===
def log_voice_event(persona, mood, line):
    logs = []
    if os.path.exists(VOICE_LOG_FILE):
        try:
            with open(VOICE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "persona": persona,
        "mood": mood,
        "voice_line": line
    })
    with open(VOICE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)
    print(f"[VOICE LOGGER]: {persona} ({mood}) says: '{line}'")

# === Generate self-voice lines based on mood ===
def generate_voice_lines():
    moods = load_current_mood_state()
    if not moods:
        print("[VOICE LOGGER]: No mood state available.")
        return

    for persona, mood in moods.items():
        lines = MOOD_VOICE_LINES.get(mood, ["I'm here, observing silently."])
        selected_line = random.choice(lines)
        log_voice_event(persona, mood, selected_line)

# === Main Daemon Loop ===
def persona_self_voice_logger_loop():
    print("[PERSONA SELF VOICE LOGGER]: Running...")
    while True:
        try:
            generate_voice_lines()
        except Exception as e:
            log_voice_event("System", "neutral", f"[ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_self_voice_logger_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():