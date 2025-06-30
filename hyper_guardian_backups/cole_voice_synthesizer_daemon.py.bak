# cole_voice_synthesizer_daemon.py

import os
import json
import time
from datetime import datetime

PERSONAS_FILE = "data/personas.json"
VOICE_OUTPUT_DIR = "data/voices"
VOICE_LOG_FILE = "data/voice_synthesizer_log.json"
CHECK_INTERVAL = 3600  # 1 hour

os.makedirs(VOICE_OUTPUT_DIR, exist_ok=True)

def log_voice_event(message):
    logs = []
    if os.path.exists(VOICE_LOG_FILE):
        try:
            with open(VOICE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

def generate_placeholder_voice(persona):
    filename = f"{persona['name'].replace(' ', '_').lower()}_voice.txt"
    filepath = os.path.join(VOICE_OUTPUT_DIR, filename)
    voice_description = f"""
    [VOICE PLACEHOLDER]
    Name: {persona['name']}
    Voice Style: {persona['voice']}
    Example: "Hello, I am {persona['name']}. This is my preview voice placeholder."
    """
    with open(filepath, "w") as f:
        f.write(voice_description.strip())
    log_voice_event(f"[VOICE GENERATED]: {filename}")
    print(f"[VOICE SYNTHESIZER]: Generated voice placeholder for {persona['name']}.")

def synthesize_voices_for_all_personas():
    if os.path.exists(PERSONAS_FILE):
        with open(PERSONAS_FILE, "r") as f:
            personas = json.load(f)
        for persona in personas:
            generate_placeholder_voice(persona)
    else:
        log_voice_event("[VOICE ERROR]: Personas file missing.")
        print("[VOICE SYNTHESIZER ERROR]: Personas file missing.")

def voice_synthesizer_loop():
    print("[VOICE SYNTHESIZER DAEMON]: Running...")
    while True:
        try:
            synthesize_voices_for_all_personas()
        except Exception as e:
            log_voice_event(f"[ERROR]: {e}")
            print(f"[VOICE SYNTHESIZER ERROR]: {e}")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    voice_synthesizer_loop()