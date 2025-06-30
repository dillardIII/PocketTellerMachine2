from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: run.py ===
# 🚀 Master Launcher – Starts the eternal loop and system brain

import subprocess

print("[Launcher] 🔄 Starting Eternal Loop...")
subprocess.Popen(["python3", "eternal_loop.py"])

print("[Launcher] 🧠 Launching Autopilot Brain...")
subprocess.Popen(["python3", "autopilot_daemon.py"])

# Keep run.py alive
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\n[Launcher] ⛔ Shutdown triggered.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():