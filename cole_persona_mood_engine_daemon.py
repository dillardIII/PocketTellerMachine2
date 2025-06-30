from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_mood_engine_daemon.py

import os
import json
import time
from datetime import datetime

PERSONAS_FILE = "data/personas.json"
MOOD_LOG_FILE = "data/persona_mood_log.json"
CHECK_INTERVAL = 600  # 10 minutes

MOODS = ["Happy", "Excited", "Neutral", "Concerned", "Angry", "Sad"]

os.makedirs("data", exist_ok=True)

def log_mood_event(message):
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

def update_persona_mood(persona, new_mood):
    persona["mood"] = new_mood
    print(f"[MOOD ENGINE]: {persona['name']} mood updated to {new_mood}.")
    log_mood_event(f"[MOOD]: {persona['name']} switched to {new_mood}.")

def randomize_persona_moods(personas):
    for persona in personas:
        new_mood = random_choice(MOODS)
        update_persona_mood(persona, new_mood)
    with open(PERSONAS_FILE, "w") as f:
        json.dump(personas, f, indent=2)

def random_choice(options):
    import random
    return random.choice(options)

def persona_mood_engine_loop():
    print("[PERSONA MOOD ENGINE DAEMON]: Running...")
    while True:
        try:
            if os.path.exists(PERSONAS_FILE):
                with open(PERSONAS_FILE, "r") as f:
                    personas = json.load(f)
                randomize_persona_moods(personas)
            else:
                log_mood_event("[MOOD ENGINE ERROR]: Personas file missing.")
                print("[MOOD ENGINE ERROR]: Personas file missing.")
        except Exception as e:
            log_mood_event(f"[ERROR]: {e}")
            print(f"[MOOD ENGINE ERROR]: {e}")
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_mood_engine_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():