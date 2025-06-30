from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_voice_style_preset_daemon.py

import os
import json
import time
from datetime import datetime

VOICE_PRESET_FILE = "data/persona_voice_presets.json"
VOICE_LOG_FILE = "data/persona_voice_style_log.json"
CHECK_INTERVAL = 900  # 15 minutes

os.makedirs("data", exist_ok=True)

def log_voice_change(persona_name, selected_preset):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "persona": persona_name,
        "voice_preset": selected_preset
    }
    logs = []
    if os.path.exists(VOICE_LOG_FILE):
        try:
            with open(VOICE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append(log_entry)
    with open(VOICE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)
    print(f"[VOICE STYLE]: {persona_name} changed voice to preset: {selected_preset}")

def pick_voice_preset(persona):
    mood = persona.get("mood", "Neutral")
    presets = persona.get("available_voice_styles", ["Calm", "Excited", "Professional"])
    if mood == "Happy":
        return "Excited"
    elif mood == "Frustrated":
        return "Assertive"
    else:
        return presets[0]

def persona_voice_preset_loop():
    print("[PERSONA VOICE STYLE PRESET DAEMON]: Running...")
    while True:
        try:
            if os.path.exists(VOICE_PRESET_FILE):
                with open(VOICE_PRESET_FILE, "r") as f:
                    personas = json.load(f)
                for persona in personas:
                    selected_preset = pick_voice_preset(persona)
                    log_voice_change(persona.get("name", "Unknown"), selected_preset)
            else:
                print("[VOICE STYLE ERROR]: Voice presets file missing.")
        except Exception as e:
            print(f"[VOICE STYLE ERROR]: {e}")
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_voice_preset_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():