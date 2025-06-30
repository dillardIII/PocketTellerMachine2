from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import time
from datetime import datetime
import requests

# === Configurations ===
CHATGPT_FEEDBACK_ENDPOINT = "http://localhost:6000/chatgpt_feedback"
COLE_WEBHOOK_URL = "http://localhost:5050/cole_webhook"
PERSONA_LOG_FILE = "data/cole_persona_mediator_log.json"
CHECK_INTERVAL = 900  # Every 15 minutes

# === Ensure data folder ===
os.makedirs("data", exist_ok=True)

# === Logging Helper ===
def log_persona_event(message):
    logs = []
    if os.path.exists(PERSONA_LOG_FILE):
        try:
            with open(PERSONA_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(PERSONA_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Persona and Mood Simulation ===
def generate_persona_message():
    mood = random.choice(["Optimistic", "Serious", "Analytical", "Curious", "Playful"])
    message = f"[PERSONA UPDATE]: Cole is currently feeling {mood} and ready to assist."
    log_persona_event(message)
    return message

# === Send Persona Updates to ChatGPT ===
def send_persona_update_to_chatgpt(message):
    try:
        payload = {
            "feedback": message
        }
        response = requests.post(CHATGPT_FEEDBACK_ENDPOINT, json=payload)
        if response.ok:
            log_persona_event(f"[PERSONA MEDIATOR]: Sent persona update to ChatGPT.")
        else:
            log_persona_event(f"[PERSONA MEDIATOR ERROR]: Failed → {response.status_code}")
    except Exception as e:
        log_persona_event(f"[PERSONA MEDIATOR ERROR]: {e}")

# === Daemon Loop ===
def persona_mediator_loop():
    print("[AI PERSONA MEDIATOR DAEMON]: Running...")
    while True:
        try:
            message = generate_persona_message()
            send_persona_update_to_chatgpt(message)
        except Exception as e:
            log_persona_event(f"[ERROR]: {e}")
            print(f"[AI PERSONA MEDIATOR ERROR]: {e}")

        time.sleep(CHECK_INTERVAL)

# === Run the Daemon ===
if __name__ == "__main__":
    persona_mediator_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():