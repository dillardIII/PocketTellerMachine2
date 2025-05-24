import os
import json
import time
from datetime import datetime
from error_parser import get_latest_error
from ai_code_generator import generate_code_fix
from auto_deployer import deploy_fix
from fix_logger import log_fix

# === Configuration ===
CHECK_INTERVAL = 120  # Run every 2 minutes
AUTO_CORRECTION_LOG_FILE = "data/auto_correction_loop_log.json"

# === Logging Helper ===
def log_auto_correction_event(message):
    logs = []
    if os.path.exists(AUTO_CORRECTION_LOG_FILE):
        try:
            with open(AUTO_CORRECTION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(AUTO_CORRECTION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Auto-Correction Loop ===
def auto_correction_loop():
    print("[Cole Auto-Correction Loop] Started monitoring...")

    while True:
        print("[Cole Auto-Correction Loop] Checking for unresolved errors...")

        error_data = get_latest_error()

        if error_data:
            print(f"[Auto-Correction] Found error in {error_data['file']}: {error_data['error']}")
            log_auto_correction_event(f"Found error in {error_data['file']}: {error_data['error']}")

            fix_code = generate_code_fix(error_data)

            if fix_code:
                print(f"[Auto-Correction] Generated fix for {error_data['file']}")
                deployed = deploy_fix(error_data['file'], fix_code)

                if deployed:
                    log_fix(error_data, fix_code)
                    log_auto_correction_event(f"Fix applied and logged for {error_data['file']}")
                    print(f"[Auto-Correction] Fix applied successfully.")
                else:
                    log_auto_correction_event(f"Fix validation failed. Skipped {error_data['file']}")
                    print(f"[Auto-Correction] Validation failed. Fix skipped.")
            else:
                log_auto_correction_event(f"Failed to generate fix for {error_data['file']}")
                print(f"[Auto-Correction] No fix generated.")
        else:
            print("[Auto-Correction] No new errors found.")

        time.sleep(CHECK_INTERVAL)

# === Run Daemon ===
if __name__ == "__main__":
    auto_correction_loop()