from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: eternal_loop.py ===
# 💚 Eternal Loop – Keeps PTM alive, logs heartbeat, and triggers self-repair

import time
import subprocess
import datetime
import os

CORE_SCRIPT = "autopilot_daemon.py"

def heartbeat():
    ts = datetime.datetime.now().isoformat()
    print(f"[EternalLoop] 💚 Heartbeat @ {ts}")

def restart_core():
    print(f"[EternalLoop] ♻️ Restarting core: {CORE_SCRIPT}")
    subprocess.Popen(["python3", CORE_SCRIPT])

def check_and_repair():
    if not os.path.exists(CORE_SCRIPT):
        print("[EternalLoop] 🛠️ Core missing. Attempting to regenerate...")
        with open(CORE_SCRIPT, "w") as f:
            f.write("# Auto-regenerated core\nprint('[Autopilot] ✅ Regenerated.')\n")
    else:
        print("[EternalLoop] ✅ Core verified.")

def eternal_loop():
    while True:
        heartbeat()
        check_and_repair()
        restart_core()
        time.sleep(300)

if __name__ == "__main__":
    eternal_loop()

def log_event():ef drop_files_to_bridge():