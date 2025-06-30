# === FILE: runtime_watcher.py ===
# 👁️ PTM Runtime Watcher – Monitors PTM scripts and triggers rebuild on crash

import time
import subprocess
import traceback
from self_rebuilder import manual_self_rebuild

WATCH_TARGET = "ptm_core.py"  # 🔍 Replace with actual main PTM file
RESTART_ON_CRASH = True
CHECK_INTERVAL = 10  # seconds

def is_process_running(name):
    try:
        result = subprocess.run(
            ["pgrep", "-f", name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return bool(result.stdout.strip())
    except Exception as e:
        print(f"[WATCHER] ⚠️ Check failed: {e}")
        return False

def monitor_and_heal():
    print(f"[WATCHER] 🔍 Monitoring: {WATCH_TARGET}")
    while True:
        running = is_process_running(WATCH_TARGET)
        if not running:
            print(f"[WATCHER] 🚨 {WATCH_TARGET} not running!")

            if RESTART_ON_CRASH:
                print("[WATCHER] 🛠️ Triggering rebuild...")
                try:
                    result = manual_self_rebuild()
                    print(f"[WATCHER] 🧠 Rebuild Result: {result}")
                except Exception:
                    print(f"[WATCHER] ❌ Failed during rebuild:\n{traceback.format_exc()}")

        time.sleep(CHECK_INTERVAL)

# === If run directly ===
if __name__ == "__main__":
    monitor_and_heal()