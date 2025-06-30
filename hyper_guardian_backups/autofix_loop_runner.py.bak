# === FILE: autofix_loop_runner.py ===
# Runs AutoFix Engine on a loop to detect and resolve issues hourly

import time
import traceback
from autofix_engine import run_autofix_engine

def start_autofix_loop(interval=3600):  # 3600 sec = 1 hour
    print("[AutoFix Loop] 🔄 Hourly fixer engaged.")
    while True:
        try:
            print("[AutoFix Loop] 🧠 Running AutoFix Engine...")
            run_autofix_engine()
        except Exception as e:
            print(f"[AutoFix Loop] ❌ Error: {e}")
            traceback.print_exc()
        time.sleep(interval)

if __name__ == "__main__":
    start_autofix_loop()