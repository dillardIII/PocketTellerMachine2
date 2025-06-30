from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_dynamic_persona_scheduler_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
PERSONA_STATE_FILE = "data/persona_current_state.json"
MOOD_STATE_FILE = "data/mood_state.json"
SCHEDULER_LOG_FILE = "data/persona_scheduler_log.json"
CHECK_INTERVAL = 600  # Check every 10 minutes

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# === Helper Functions ===
def load_json_file(file_path, default):
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except:
            return default
    return default

def save_json_file(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

def log_scheduler_event(message):
    logs = load_json_file(SCHEDULER_LOG_FILE, [])
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    save_json_file(SCHEDULER_LOG_FILE, logs[-500:])

# === Dynamic Persona Selection Logic ===
def decide_best_persona(mood_state):
    if not mood_state:
        return "Mentor"
    
    # Example logic based on mood data across personas
    frustrated_personas = [p for p, m in mood_state.items() if m == "frustrated"]:
    if frustrated_personas:
        return "ChillTrader"
    if all(m == "happy" for m in mood_state.values()):
        return "MoCash"
    return "Mentor"

# === Main Scheduler Logic ===
def update_persona_state():
    mood_state = load_json_file(MOOD_STATE_FILE, {})
    persona_state = load_json_file(PERSONA_STATE_FILE, {})

    new_persona = decide_best_persona(mood_state)
    current_persona = persona_state.get("active_persona", "")

    if new_persona != current_persona:
        persona_state["active_persona"] = new_persona
        persona_state["timestamp"] = datetime.now().isoformat()
        save_json_file(PERSONA_STATE_FILE, persona_state)
        log_scheduler_event(f"[PERSONA SCHEDULER]: Persona switched to {new_persona}")
    else:
        log_scheduler_event(f"[PERSONA SCHEDULER]: No change. Current persona remains {current_persona}")

# === Daemon Loop ===
def persona_scheduler_loop():
    print("[PERSONA SCHEDULER]: Running dynamic scheduler...")
    while True:
        try:
            update_persona_state()
        except Exception as e:
            log_scheduler_event(f"[ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run the Daemon ===
if __name__ == "__main__":
    persona_scheduler_loop()

def log_event():ef drop_files_to_bridge():