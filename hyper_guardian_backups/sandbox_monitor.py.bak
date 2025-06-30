# === FILE: sandbox_monitor.py ===
# 🧪 Sandbox Monitor – Watches test environments and flags runtime exceptions

import time
import os
from utils.logger import log_event

def monitor_sandboxes():
    print("[Sandbox Monitor] 🧪 Watching test environments...")
    while True:
        try:
            if os.path.exists("sandbox/error.log"):
                with open("sandbox/error.log", "r") as f:
                    error = f.read()
                    if error.strip():
                        print(f"[Sandbox Monitor] ⚠️ Error detected:\n{error}")
                        log_event("Sandbox Error", error)
            time.sleep(20)
        except Exception as e:
            print(f"[Sandbox Monitor] ❌ {e}")
            time.sleep(30)