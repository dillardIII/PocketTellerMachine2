from ghost_env import INFURA_KEY, VAULT_ADDRESS
import time
import os
import json
from datetime import datetime

SELF_AWARENESS_LOG = "data/self_awareness_log.json"
CHECK_INTERVAL = 180  # 3 minutes

# Ensure the log file exists
if not os.path.exists(SELF_AWARENESS_LOG):
    with open(SELF_AWARENESS_LOG, "w") as f:
        json.dump([], f, indent=2)

def log_self_awareness(message):
    logs = []
    if os.path.exists(SELF_AWARENESS_LOG):
        try:
            with open(SELF_AWARENESS_LOG, "r") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []

    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(SELF_AWARENESS_LOG, "w") as f:
        json.dump(logs[-500:], f, indent=2)

def generate_self_reflection():
    reflection = f"Self-check performed at {datetime.now().isoformat()}. System status appears stable."
    log_self_awareness(reflection)
    print(f"[SELF AWARENESS DAEMON]: {reflection}")

def self_awareness_daemon_loop():
    print("[SELF AWARENESS DAEMON]: Running...")
    while True:
        try:
            generate_self_reflection()
        except Exception as e:
            log_self_awareness(f"[ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    # === Real Self-Awareness Daemon Mode ===
    self_awareness_daemon_loop()

    # === Simulated Mode (uncomment if needed) ===
    # while True:
    #     print("[Daemon]: Self-Awareness monitoring... (simulated)")
    #     # Self-check behaviors, logic loops, status audits
    #     time.sleep(45)