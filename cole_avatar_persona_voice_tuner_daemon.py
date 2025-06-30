from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_avatar_persona_voice_tuner_daemon.py

import os
import json
import time
from datetime import datetime
import pytz

CENTRAL_TZ = pytz.timezone("US/Central")

def get_local_time():
    return datetime.now(CENTRAL_TZ)

# === Configurations ===
PERSONA_FILE = "data/avatar_personas.json"
VOICE_TUNER_LOG_FILE = "data/avatar_persona_voice_tuner_log.json"
CHECK_INTERVAL = 900  # Every 15 minutes

os.makedirs("data", exist_ok=True)

# === Voice tuning presets ===
VOICE_PRESETS = {
    "calm": {"pitch": "low", "pace": "slow"},
    "energetic": {"pitch": "high", "pace": "fast"},
    "strong": {"pitch": "medium", "pace": "firm"},
    "cheerful": {"pitch": "high", "pace": "medium"},
    "measured": {"pitch": "neutral", "pace": "slow"}
}

def load_personas():
    if os.path.exists(PERSONA_FILE):
        try:
            with open(PERSONA_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def tune_persona_voice(personas):
    for name, props in personas.items():
        voice_style = props.get("voice", "neutral")
        preset = VOICE_PRESETS.get(voice_style, {"pitch": "neutral", "pace": "medium"})
        props["voice_tuning"] = preset
        log_event(f"[VOICE TUNER]: Applied voice tuning for {name} → {preset}")

    with open(PERSONA_FILE, "w") as f:
        json.dump(personas, f, indent=2)

def log_event(message):
    logs = []
    if os.path.exists(VOICE_TUNER_LOG_FILE):
        try:
            with open(VOICE_TUNER_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_TUNER_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

def voice_tuner_loop():
    print("[VOICE TUNER]: Running...")
    while True:
        try:
            personas = load_personas()
            if personas:
                tune_persona_voice(personas)
        except Exception as e:
            log_event(f"[VOICE TUNER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    voice_tuner_loop()