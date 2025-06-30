from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ptm_autonomy_manager.py ===
# 🧠 PTM Autonomy Manager – Ensures all autonomous modules are always running

import subprocess
import threading
import time
import os

MODULES = [
    ("main.py", "python3 main.py"),
    ("file_exec_engine.py", "python3 -c 'import file_exec_engine; file_exec_engine.start_exec_engine()'"),
    ("self_rebuilder.py", "python3 self_rebuilder.py"),
    ("bridge_team_launcher.py", "python3 -c 'import bridge_team_launcher; bridge_team_launcher.start_bridge_team()'"),
    ("vault_manager.py", "python3 -c 'import vault_manager; vault_manager.force_recombine_partials()'"),
]

def monitor_and_run():
    print("[AutonomyManager] 🔥 Ensuring all empire modules are alive...")
    while True:
        for fname, cmd in MODULES:
            if not is_running(fname):
                print(f"[AutonomyManager] ⚠️ {fname} not running. Relaunching...")
                threading.Thread(target=lambda: subprocess.run(cmd, shell=True)).start()
            else:
                print(f"[AutonomyManager] ✅ {fname} running.")
        time.sleep(15)

def is_running(filename):
    try:
        out = subprocess.check_output(f"ps aux | grep {filename} | grep -v grep", shell=True)
        return bool(out)
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    monitor_and_run()

def log_event():ef drop_files_to_bridge():