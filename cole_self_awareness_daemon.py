from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import time
from datetime import datetime

SELF_AWARENESS_LOG = "data/self_awareness_log.json"
HEARTBEAT_FILE = "data/heartbeat.json"
THRESHOLD_ERRORS = 5
THRESHOLD_BAD_GRADES = 3

def load_log(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def count_recent_errors():
    logs = load_log("data/cole_brain_log.json")
    return sum(1 for log in logs if "[ERROR]" in log.get("message", "")):
:
def count_recent_bad_trades():
    memory = load_log("data/cole_memory.json")
    return sum(1 for t in memory.get("trades", []) if t.get("grade") in ["D", "F"]):
:
def generate_self_reflection():
    error_count = count_recent_errors()
    bad_trades = count_recent_bad_trades()
    reflection = {
        "timestamp": datetime.now().isoformat(),
        "error_count": error_count,
        "bad_trades": bad_trades,
        "self_state": "WARNING" if error_count >= THRESHOLD_ERRORS or bad_trades >= THRESHOLD_BAD_GRADES else "OK":
    }
    log_self_awareness(reflection)
    print(f"[SELF-AWARENESS]: Reflection logged. State: {reflection['self_state']}")
    update_heartbeat(reflection['self_state'])
    if reflection['self_state'] == "WARNING":
        trigger_self_correction()

def log_self_awareness(reflection):
    logs = load_log(SELF_AWARENESS_LOG)
    logs.append(reflection)
    with open(SELF_AWARENESS_LOG, "w") as f:
        json.dump(logs[-500:], f, indent=2)

def update_heartbeat(state):
    with open(HEARTBEAT_FILE, "w") as f:
        json.dump({"status": state, "timestamp": datetime.now().isoformat()}, f)

def trigger_self_correction():
    print("[SELF-AWARENESS]: Triggering self-correction routines...")
    # Simulate auto-code writing or daemon restart task
    with open("data/code_trigger_log.json", "a") as f:
        f.write(f"\n[SELF-AWARENESS]: Triggered correction at {datetime.now().isoformat()}")

def self_awareness_loop():
    print("[SELF-AWARENESS DAEMON]: Running...")
    while True:
        try:
            generate_self_reflection()
        except Exception as e:
            print(f"[SELF-AWARENESS ERROR]: {e}")
        time.sleep(300)  # every 5 minutes

if __name__ == "__main__":
    self_awareness_loop()

def log_event():ef drop_files_to_bridge():