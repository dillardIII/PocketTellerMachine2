# cole_voice_style_dynamic_modulator.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_STYLE_LOG_FILE = "data/voice_style_modulator_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Voice Style Mapping by Mood ===
VOICE_STYLE_MAP = {
    "happy": {"pitch": "high", "speed": "fast", "style": "cheerful"},
    "frustrated": {"pitch": "low", "speed": "medium", "style": "grumpy"},
    "calm": {"pitch": "neutral", "speed": "slow", "style": "soothing"},
    "neutral": {"pitch": "neutral", "speed": "normal", "style": "formal"}
}

# === Personas ===
PERSONAS = ["Mentor", "Mo Cash", "Drill Instructor", "Strategist", "Chill Trader", "OG"]

# === Ensure data directory exists ===
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

# === Generate voice styles per persona based on mood ===
def generate_voice_styles():
    mood_state = load_current_mood_state()
    voice_styles = {}

    for persona in PERSONAS:
        mood = mood_state.get(persona, "neutral")
        style = VOICE_STYLE_MAP.get(mood, VOICE_STYLE_MAP["neutral"])
        voice_styles[persona] = style
        log_event(f"[VOICE STYLE MODULATOR]: {persona} mood {mood} → Voice Style: {style}")

    return voice_styles

# === Logging helper ===
def log_event(message):
    logs = []
    if os.path.exists(VOICE_STYLE_LOG_FILE):
        try:
            with open(VOICE_STYLE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_STYLE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def voice_style_modulator_loop():
    print("[VOICE STYLE MODULATOR]: Adjusting voice styles dynamically...")
    while True:
        try:
            generate_voice_styles()
        except Exception as e:
            log_event(f"[VOICE STYLE MODULATOR ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run ===
if __name__ == "__main__":
    voice_style_modulator_loop()