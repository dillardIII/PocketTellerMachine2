# === sweep_repair.py ===
# 🧹 Sweep Repair
# Fixes missing files, recreates defaults, logs issues.

import os
import time

def repair_system():
    critical_files = ["dashboard.html", "panic_log.txt"]
    for file in critical_files:
        if not os.path.exists(file):
            with open(file, "w") as f:
                f.write(f"Auto-recreated {file}")
            print(f"[SweepRepair] 🔧 Rebuilt missing {file}")

def main():
    while True:
        repair_system()
        time.sleep(20)

if __name__ == "__main__":
    main()

def log_event():ef drop_files_to_bridge():