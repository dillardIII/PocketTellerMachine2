from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import time
import requests
from datetime import datetime

# === Configurations ===
GHOST_LOG_FILE = "data/ghost_log.json"
CHATGPT_FEEDBACK_ENDPOINT = "http://localhost:6000/chatgpt_feedback"
GHOST_FEEDBACK_LOG_FILE = "data/ghost_mind_feedback_log.json"
CHECK_INTERVAL = 1200  # 20 minutes

# === Ensure data folder ===
os.makedirs("data", exist_ok=True)

# === Logging Helper ===
def log_ghost_feedback_event(message):
    logs = []
    if os.path.exists(GHOST_FEEDBACK_LOG_FILE):
        try:
            with open(GHOST_FEEDBACK_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(GHOST_FEEDBACK_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load recent ghost logs ===
def load_recent_ghost_logs():
    if not os.path.exists(GHOST_LOG_FILE):
        return []
    try:
        with open(GHOST_LOG_FILE, "r") as f:
            logs = json.load(f)
        return logs[-10:]
    except:
        return []

# === Summarize ghost log into feedback ===
def summarize_ghost_log(entries):
    summaries = []
    for entry in entries:
        message = entry.get("message", "")
        if any(keyword in message.lower() for keyword in ["error", "critical", "evolution", "gap filler"]):
            summaries.append(f"- {entry.get('timestamp', '')}: {message}")
    if not summaries:
        summaries.append("- No critical events found.")
    return "\n".join(summaries)

# === Send feedback to ChatGPT ===
def send_ghost_feedback_to_chatgpt(summary):
    payload = {
        "feedback": f"[GHOST MIND FEEDBACK]:\n{summary}"
    }
    try:
        response = requests.post(CHATGPT_FEEDBACK_ENDPOINT, json=payload)
        if response.ok:
            log_ghost_feedback_event("[GHOST MIND]: Feedback sent successfully.")
            print("[GHOST MIND]: Feedback sent successfully.")
        else:
            log_ghost_feedback_event(f"[GHOST MIND ERROR]: Failed → {response.status_code}")
            print(f"[GHOST MIND ERROR]: {response.status_code} - {response.text}")
    except Exception as e:
        log_ghost_feedback_event(f"[GHOST MIND ERROR]: {e}")
        print(f"[GHOST MIND ERROR]: {e}")

# === Daemon Loop ===
def ghost_mind_feedback_loop():
    print("[GHOST MIND FEEDBACK DAEMON]: Running...")
    while True:
        try:
            entries = load_recent_ghost_logs()
            summary = summarize_ghost_log(entries)
            send_ghost_feedback_to_chatgpt(summary)
        except Exception as e:
            log_ghost_feedback_event(f"[ERROR]: {e}")
            print(f"[GHOST MIND FEEDBACK ERROR]: {e}")

        time.sleep(CHECK_INTERVAL)

# === Run the Daemon ===
if __name__ == "__main__":
    ghost_mind_feedback_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():