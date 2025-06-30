from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_avatar_dynamic_emotion_voice_synthesizer.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_PRESET_FILE = "data/avatar_voice_presets.json"
SYNTH_LOG_FILE = "data/avatar_voice_synthesizer_log.json"
CHECK_INTERVAL = 300  # Every 5 minutes

# === Ensure data directory ===
os.makedirs("data", exist_ok=True)

# === Loaders ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def load_voice_presets():
    if os.path.exists(VOICE_PRESET_FILE):
        try:
            with open(VOICE_PRESET_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Synthesizer Logic ===
def synthesize_voice_profiles():
    mood_state = load_mood_state()
    presets = load_voice_presets()

    for persona in presets:
        mood = mood_state.get(persona, "calm")
        presets[persona]["tone"] = adjust_tone(mood)
        presets[persona]["energy"] = adjust_energy(mood)
        log_event(f"[VOICE SYNTHESIZER]: {persona} tone set to {presets[persona]['tone']} with energy {presets[persona]['energy']}")

    with open(VOICE_PRESET_FILE, "w") as f:
        json.dump(presets, f, indent=2)

def adjust_tone(mood):
    return {
        "happy": "Bright",
        "frustrated": "Firm",
        "calm": "Soft"
    }.get(mood, "Neutral")

def adjust_energy(mood):
    return {
        "happy": "High",
        "frustrated": "Medium",
        "calm": "Low"
    }.get(mood, "Medium")

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(SYNTH_LOG_FILE):
        try:
            with open(SYNTH_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(SYNTH_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def voice_synthesizer_loop():
    print("[VOICE SYNTHESIZER]: Avatar voice & tone synthesizer running...")
    while True:
        try:
            synthesize_voice_profiles()
        except Exception as e:
            log_event(f"[VOICE SYNTHESIZER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    voice_synthesizer_loop()