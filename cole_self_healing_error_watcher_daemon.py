import os
import json
import time
from datetime import datetime
import requests
from error_parser import get_latest_error
from ai_code_generator import generate_code_fix
from auto_deployer import deploy_fix
from fix_logger import log_fix

# === Configuration ===
CHECK_INTERVAL = 60  # seconds
SELF_HEALING_LOG_FILE = "data/self_healing_error_watcher_log.json"

# === Logging Helper ===
def log_self_healing_event(message):
    logs = []
    if os.path.exists(SELF_HEALING_LOG_FILE):
        try:
            with open(SELF_HEALING_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(SELF_HEALING_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Self-Healing Watcher ===
def cole_self_healing_error_watcher():
    print("[Cole Self-Healing Daemon] Started error watcher loop...")

    while True:
        print("[Cole Self-Healing Daemon] Scanning for recent errors...")

        error_data = get_latest_error()

        if error_data:
            print(f"[Cole Self-Healing] Detected error in {error_data['file']}: {error_data['error']}")
            log_self_healing_event(f"Detected error in {error_data['file']}: {error_data['error']}")

            fix_code = generate_code_fix(error_data)

            if fix_code:
                print(f"[Cole Self-Healing] Generated potential fix for {error_data['file']}")
                deployed = deploy_fix(error_data['file'], fix_code)

                if deployed:
                    log_fix(error_data, fix_code)
                    log_self_healing_event(f"Fix deployed and logged for {error_data['file']}")
                    print(f"[Cole Self-Healing] Fix deployed and logged for {error_data['file']}")
                else:
                    log_self_healing_event(f"Fix deployment failed for {error_data['file']}")
                    print(f"[Cole Self-Healing] Fix deployment failed validation. Skipped {error_data['file']}")
            else:
                log_self_healing_event(f"No fix generated for {error_data['file']}")
                print(f"[Cole Self-Healing] No fix generated for {error_data['file']}")
        else:
            print("[Cole Self-Healing] No new errors found.")

        time.sleep(CHECK_INTERVAL)

# === Run Daemon ===
if __name__ == "__main__":
    cole_self_healing_error_watcher()