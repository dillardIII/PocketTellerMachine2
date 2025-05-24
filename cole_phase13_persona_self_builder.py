# cole_phase13_persona_self_builder.py

import os
import json
from datetime import datetime

PERSONAS_FILE = "data/personas.json"
PERSONA_BUILDER_LOG_FILE = "data/persona_self_builder_log.json"

os.makedirs("data", exist_ok=True)

# === Logging Helper ===
def log_persona_event(message):
    logs = []
    if os.path.exists(PERSONA_BUILDER_LOG_FILE):
        try:
            with open(PERSONA_BUILDER_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(PERSONA_BUILDER_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Persona Self Builder ===
def create_new_persona(name, voice_style, avatar_url):
    try:
        if os.path.exists(PERSONAS_FILE):
            with open(PERSONAS_FILE, "r") as f:
                personas = json.load(f)
        else:
            personas = []

        new_persona = {
            "name": name,
            "voice_style": voice_style,
            "avatar_url": avatar_url,
            "created_at": datetime.now().isoformat()
        }

        personas.append(new_persona)
        with open(PERSONAS_FILE, "w") as f:
            json.dump(personas, f, indent=2)

        log_persona_event(f"[PERSONA BUILDER]: Created new persona → {name}")
        print(f"[PERSONA BUILDER]: Created new persona → {name}")
    except Exception as e:
        log_persona_event(f"[PERSONA BUILDER ERROR]: {e}")
        print(f"[PERSONA BUILDER ERROR]: {e}")

# === Example Self-Build Trigger ===
def persona_self_builder_trigger():
    print("[PERSONA SELF BUILDER]: Running...")
    create_new_persona(
        name="AI Strategist",
        voice_style="Calm and Analytical",
        avatar_url="https://example.com/avatar/ai_strategist.png"
    )

if __name__ == "__main__":
    persona_self_builder_trigger()