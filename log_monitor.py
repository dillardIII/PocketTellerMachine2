from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: log_monitor.py ===
# 📉 Log Monitor – Watches logs and triggers reflex fixes on error patterns

import threading
import time
import os

def start_log_monitor():
    print("[Log Monitor] 👁️ Starting log monitor...")

    log_path = "ptm_logs/system.log"
    if not os.path.exists(log_path):
        print("[Log Monitor] ⚠️ Log file not found, creating...")
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        with open(log_path, "w") as f:
            f.write("")

    def monitor_loop():
        while True:
            try:
                with open(log_path, "r") as f:
                    lines = f.readlines()
                    for line in lines[-10:]:
                        if "ERROR" in line or "❌" in line:
                            print(f"[Log Monitor] ⚠️ Detected issue: {line.strip()}")
                            # Future: Trigger reflex handler or auto-repair agent
            except Exception as e:
                print(f"[Log Monitor] ❌ Failed to read logs: {e}")

            time.sleep(10)

    threading.Thread(target=monitor_loop, daemon=True).start()

def log_event():ef drop_files_to_bridge():