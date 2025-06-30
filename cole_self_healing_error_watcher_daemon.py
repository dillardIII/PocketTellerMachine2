from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_self_healing_error_watcher_daemon.py ===

import os
import json
import time
import traceback
from datetime import datetime

from error_parser import get_latest_error
from ai_code_generator import generate_code_fix
from auto_deployer import deploy_fix
from fix_logger import log_fix

# === Configuration ===
CHECK_INTERVAL = 60  # seconds
SELF_HEALING_LOG_FILE = "data/self_healing_error_watcher_log.json"

# === Logging Helper ===
def log_self_healing_event(message):
    os.makedirs("data", exist_ok=True)
    logs = []
    if os.path.exists(SELF_HEALING_LOG_FILE):
        try:
            with open(SELF_HEALING_LOG_FILE, "r") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []

    logs.append({
        "timestamp": datetime.now().isoformat(),
        "event": message
    })

    with open(SELF_HEALING_LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

# === Self-Healing Loop ===
def run_self_healing_watcher():
    log_self_healing_event("✅ Self-Healing Watcher Started")

    while True:
        try:
            error_info = get_latest_error()
            if error_info:
                log_self_healing_event(f"⚠️ Detected Error: {error_info['error_message']}")
                
                fix_code = generate_code_fix(error_info)
                if fix_code:
                    log_self_healing_event("🛠️ Generated Fix. Deploying...")

                    deployed = deploy_fix(error_info['file'], fix_code)
                    if deployed:
                        log_self_healing_event(f"✅ Deployed Fix to {error_info['file']}")
                        log_fix(error_info, fix_code)
                    else:
                        log_self_healing_event(f"❌ Failed to Deploy Fix to {error_info['file']}")
                else:
                    log_self_healing_event("❌ No fix could be generated.")
            else:
                log_self_healing_event("✅ No new errors found.")
        except Exception as e:
            log_self_healing_event(f"🔥 Exception in Self-Healing Watcher: {traceback.format_exc()}")

        time.sleep(CHECK_INTERVAL)

# === Standalone Launch ===
if __name__ == "__main__":
    run_self_healing_watcher()


def log_event():ef drop_files_to_bridge():