import time
import requests
from datetime import datetime

# === Configuration ===
COLE_WEBHOOK_URL = "http://localhost:5050/cole_webhook"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Orchestration commands ===
COMMANDS = [
    "RUN_SELF_HEALING_CYCLE",
    "RUN_AUTO_CORRECTION_CYCLE",
    "RUN_SMART_DECISION_ANALYSIS",
    "RUN_STRATEGY_IMPROVEMENT_CYCLE",
    "RUN_BRAIN_AUTO_EXECUTION"
]

# === Main Orchestration Loop ===
def phase11_command_orchestrator_loop():
    print("[COLE PHASE 11 COMMAND ORCHESTRATOR]: Running...")
    while True:
        try:
            for command in COMMANDS:
                try:
                    response = requests.post(COLE_WEBHOOK_URL, json={"command": command})
                    if response.ok:
                        print(f"[ORCHESTRATOR]: Triggered command → {command}")
                    else:
                        print(f"[ORCHESTRATOR ERROR]: Failed → {response.status_code}")
                except Exception as e:
                    print(f"[ORCHESTRATOR ERROR]: {e}")
            print(f"[ORCHESTRATOR]: Completed orchestration cycle at {datetime.now().isoformat()}")
        except Exception as e:
            print(f"[ORCHESTRATOR LOOP ERROR]: {e}")

        time.sleep(CHECK_INTERVAL)

# === Run Daemon ===
if __name__ == "__main__":
    phase11_command_orchestrator_loop()