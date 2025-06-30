import os
import json
import time
import requests
from datetime import datetime

# === Configurations ===
MEMORY_FILE = "data/cole_memory.json"
CHATGPT_FEEDBACK_ENDPOINT = "http://localhost:6000/chatgpt_feedback"
MEMORY_FEEDBACK_LOG_FILE = "data/brain_memory_feedback_log.json"
CHECK_INTERVAL = 1800  # 30 minutes

# === Ensure data folder ===
os.makedirs("data", exist_ok=True)

# === Logging Helper ===
def log_memory_feedback_event(message):
    logs = []
    if os.path.exists(MEMORY_FEEDBACK_LOG_FILE):
        try:
            with open(MEMORY_FEEDBACK_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(MEMORY_FEEDBACK_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load Cole's Memory ===
def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

# === Analyze memory for gaps ===
def analyze_memory_for_feedback(memory):
    feedback = []
    trades = memory.get("trades", [])
    strategies_used = set(t.get("strategy", "") for t in trades)
    if not any("RSI" in s for s in strategies_used):
        feedback.append("- Missing RSI Reversal strategies in recent memory.")
    if not any("SMA" in s for s in strategies_used):
        feedback.append("- Missing SMA Cross strategies in recent memory.")
    if len(trades) == 0:
        feedback.append("- No trades logged recently.")
    if not feedback:
        feedback.append("- No critical memory gaps detected.")
    return "\n".join(feedback)

# === Send feedback to ChatGPT ===
def send_memory_feedback_to_chatgpt(summary):
    payload = {
        "feedback": f"[BRAIN MEMORY FEEDBACK]:\n{summary}"
    }
    try:
        response = requests.post(CHATGPT_FEEDBACK_ENDPOINT, json=payload)
        if response.ok:
            log_memory_feedback_event("[BRAIN MEMORY]: Feedback sent successfully.")
            print("[BRAIN MEMORY]: Feedback sent successfully.")
        else:
            log_memory_feedback_event(f"[BRAIN MEMORY ERROR]: Failed → {response.status_code}")
            print(f"[BRAIN MEMORY ERROR]: {response.status_code} - {response.text}")
    except Exception as e:
        log_memory_feedback_event(f"[BRAIN MEMORY ERROR]: {e}")
        print(f"[BRAIN MEMORY ERROR]: {e}")

# === Daemon Loop ===
def brain_memory_feedback_loop():
    print("[BRAIN MEMORY FEEDBACK DAEMON]: Running...")
    while True:
        try:
            memory = load_memory()
            summary = analyze_memory_for_feedback(memory)
            send_memory_feedback_to_chatgpt(summary)
        except Exception as e:
            log_memory_feedback_event(f"[ERROR]: {e}")
            print(f"[BRAIN MEMORY FEEDBACK ERROR]: {e}")

        time.sleep(CHECK_INTERVAL)

# === Run the Daemon ===
if __name__ == "__main__":
    brain_memory_feedback_loop()