from ghost_env import INFURA_KEY, VAULT_ADDRESS
# auto_feedback_sender_daemon.py

import os
import json
import time
from datetime import datetime
import requests

# === Configurations ===
FEEDBACK_URL = "http://localhost:6000/chatgpt_feedback"  # For direct feedback listener (optional)
COLE_WEBHOOK_URL = "http://localhost:5050/cole_webhook"   # Main webhook target for autonomous command delivery
AUTO_FEEDBACK_LOG_FILE = "data/auto_feedback_sender_log.json"
CHECK_INTERVAL = 900  # 15 minutes

# === Ensure data folder ===
os.makedirs("data", exist_ok=True)

# === Logging Helper ===
def log_auto_feedback(message):
    logs = []
    if os.path.exists(AUTO_FEEDBACK_LOG_FILE):
        try:
            with open(AUTO_FEEDBACK_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(AUTO_FEEDBACK_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Option 1: Send generic feedback message to ChatGPT Feedback Listener ===
def send_feedback(feedback_message):
    payload = {"feedback": feedback_message}
    try:
        response = requests.post(FEEDBACK_URL, json=payload)
        if response.ok:
            log_auto_feedback(f"[AUTO FEEDBACK]: Sent to Feedback Listener → {feedback_message}")
            print(f"[AUTO FEEDBACK]: Sent to Feedback Listener.")
        else:
            log_auto_feedback(f"[AUTO FEEDBACK ERROR]: Status {response.status_code} → {response.text}")
            print(f"[AUTO FEEDBACK ERROR]: Status {response.status_code} - {response.text}")
    except Exception as e:
        log_auto_feedback(f"[AUTO FEEDBACK ERROR]: {e}")
        print(f"[AUTO FEEDBACK ERROR]: {e}")

# === Option 2: Send system trigger command to Cole Webhook (recommended) ===
def send_feedback_to_cole():
    feedback_command = "GENERATE_AUTO_FEEDBACK_REPORT"
    try:
        response = requests.post(COLE_WEBHOOK_URL, json={"command": feedback_command})
        if response.ok:
            log_auto_feedback(f"[AUTO FEEDBACK]: Sent system command → {feedback_command}")
            print(f"[AUTO FEEDBACK]: Sent system command to Cole.")
        else:
            log_auto_feedback(f"[AUTO FEEDBACK ERROR]: Failed → {response.status_code}")
            print(f"[AUTO FEEDBACK ERROR]: {response.status_code} - {response.text}")
    except Exception as e:
        log_auto_feedback(f"[AUTO FEEDBACK ERROR]: {e}")
        print(f"[AUTO FEEDBACK ERROR]: {e}")

# === Main Autonomous Daemon Loop ===
def auto_feedback_sender_loop():
    print("[AUTO FEEDBACK SENDER DAEMON]: Running...")
    while True:
        try:
            print("[AUTO FEEDBACK]: Triggering feedback flow...")
            # You can use either or both options below
            send_feedback_to_cole()
            # send_feedback(f"Cole completed a task at {datetime.now().isoformat()}.")
        except Exception as e:
            log_auto_feedback(f"[ERROR]: {e}")
            print(f"[AUTO FEEDBACK ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    auto_feedback_sender_loop()

    # === Optional simulation fallback ===
    # while True:
    #     print("[Daemon]: Auto Feedback Sender Daemon running... (simulated)")
    #     time.sleep(900)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():