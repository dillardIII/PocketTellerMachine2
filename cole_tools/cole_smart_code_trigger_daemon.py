import os
import json
import time
from datetime import datetime
import requests

TRIGGER_FILE = "data/code_trigger_rules.json"
TRIGGER_LOG_FILE = "data/code_trigger_log.json"
COLE_WEBHOOK_URL = "http://localhost:5050/cole_webhook"
CHECK_INTERVAL = 300  # Check every 5 minutes

def load_triggers():
    if not os.path.exists(TRIGGER_FILE):
        return []
    try:
        with open(TRIGGER_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def log_trigger(message):
    logs = []
    if os.path.exists(TRIGGER_LOG_FILE):
        try:
            with open(TRIGGER_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(TRIGGER_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

def trigger_code_execution(rule):
    command = rule.get("command", "")
    if command:
        payload = {"command": command}
        try:
            response = requests.post(COLE_WEBHOOK_URL, json=payload)
            if response.ok:
                log_trigger(f"[TRIGGER]: Executed {command}")
            else:
                log_trigger(f"[TRIGGER ERROR]: Failed to execute {command} → {response.status_code}")
        except Exception as e:
            log_trigger(f"[TRIGGER ERROR]: {e}")

def trigger_daemon_loop():
    print("[SMART CODE TRIGGER DAEMON]: Running...")
    while True:
        try:
            triggers = load_triggers()
            for rule in triggers:
                trigger_code_execution(rule)
        except Exception as e:
            log_trigger(f"[ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    trigger_daemon_loop()

    # Simulated fallback loop (uncomment to simulate)
    # while True:
    #     print("[Daemon]: Smart Code Trigger running... (simulated)")
    #     # Check rules and trigger code execution
    #     time.sleep(60)