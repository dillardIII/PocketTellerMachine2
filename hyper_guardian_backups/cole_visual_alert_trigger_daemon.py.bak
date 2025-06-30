# cole_visual_alert_trigger_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
ALERT_QUEUE_FILE = "data/visual_alert_queue.json"
ALERT_LOG_FILE = "data/visual_alert_trigger_log.json"
CHECK_INTERVAL = 60  # Every 1 minute

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load or create alert queue ===
def load_alert_queue():
    if os.path.exists(ALERT_QUEUE_FILE):
        try:
            with open(ALERT_QUEUE_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_alert_queue(queue):
    with open(ALERT_QUEUE_FILE, "w") as f:
        json.dump(queue[-50:], f, indent=2)

# === Add alert to queue ===
def trigger_visual_alert(level, message):
    alert = {
        "timestamp": datetime.now().isoformat(),
        "level": level,
        "message": message
    }
    queue = load_alert_queue()
    queue.append(alert)
    save_alert_queue(queue)
    log_event(f"[VISUAL ALERT TRIGGERED]: {level} - {message}")

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(ALERT_LOG_FILE):
        try:
            with open(ALERT_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(ALERT_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def visual_alert_trigger_loop():
    print("[VISUAL ALERT TRIGGER DAEMON]: Running...")
    while True:
        try:
            # This is where Cole would check its logs or systems
            # Example simulation alert:
            trigger_visual_alert("CRITICAL", "Simulated System Check: Possible Market Volatility Detected.")
        except Exception as e:
            log_event(f"[ERROR]: {e}")
            print(f"[VISUAL ALERT ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    visual_alert_trigger_loop()