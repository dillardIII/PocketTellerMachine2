# === FILE: predator_ops_agent.py ===
# 🛡️ Predator Ops Agent – Executes OS-level repair tasks and logs results

import subprocess
import datetime

LOG_FILE = "ue_launcher_status_log.txt"

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"[PredatorOps] {message}")

def execute_unreal_rebuild():
    log("Initializing Unreal rebuild...")
    try:
        subprocess.run(["python3", "unreal_installer_bot.py"], check=True)
        log("🎮 Unreal rebuild complete.")
    except Exception as e:
        log(f"❌ Unreal rebuild failed: {e}")

if __name__ == "__main__":
    execute_unreal_rebuild()