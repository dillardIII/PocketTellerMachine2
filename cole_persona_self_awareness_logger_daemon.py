# cole_persona_self_awareness_logger_daemon.py

import os
import json
import time
from datetime import datetime

PERSONAS_FILE = "data/personas.json"
AWARENESS_LOG_FILE = "data/persona_self_awareness_log.json"
CHECK_INTERVAL = 600  # 10 minutes

os.makedirs("data", exist_ok=True)

def log_self_awareness(persona_name, mood, voice_tone, reflection):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "persona": persona_name,
        "mood": mood,
        "voice_tone": voice_tone,
        "reflection": reflection
    }
    logs = []
    if os.path.exists(AWARENESS_LOG_FILE):
        try:
            with open(AWARENESS_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append(log_entry)
    with open(AWARENESS_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)
    print(f"[SELF AWARENESS]: {persona_name} reflected: {reflection}")

def generate_reflection(persona):
    mood = persona.get("mood", "Neutral")
    voice_tone = persona.get("voice_tone", "Calm")
    reflection = f"I am currently feeling {mood}. My voice is in {voice_tone} tone. I will adjust my behavior accordingly."
    return reflection

def persona_self_awareness_loop():
    print("[PERSONA SELF-AWARENESS LOGGER DAEMON]: Running...")
    while True:
        try:
            if os.path.exists(PERSONAS_FILE):
                with open(PERSONAS_FILE, "r") as f:
                    personas = json.load(f)
                for persona in personas:
                    reflection = generate_reflection(persona)
                    log_self_awareness(persona.get("name", "Unknown"), persona.get("mood", "Neutral"), persona.get("voice_tone", "Calm"), reflection)
            else:
                print("[SELF AWARENESS ERROR]: Personas file missing.")
        except Exception as e:
            print(f"[SELF AWARENESS ERROR]: {e}")
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_self_awareness_loop()