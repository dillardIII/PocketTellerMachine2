from ghost_env import INFURA_KEY, VAULT_ADDRESS
import subprocess
import time
import os
import json
from datetime import datetime

# === Configurations ===
LOG_FILE = "data/cole_autonomous_supervisor_log.json"
os.makedirs("data", exist_ok=True)

# === Daemons to monitor ===
DAEMONS = {
    "cole_bridge_webhook_listener": ["python", "cole_bridge_webhook_listener.py"],
    "cole_phase11_launcher": ["python", "cole_phase11_launcher.py"]
}

# === Track processes ===
processes = {}

def log_supervisor_event(message):
    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

def start_daemon(name, cmd):
    print(f"[SUPERVISOR]: Starting {name}...")
    processes[name] = subprocess.Popen(cmd)
    log_supervisor_event(f"[STARTED]: {name} started.")

def check_and_restart_daemons():
    for name, cmd in DAEMONS.items():
        proc = processes.get(name)
        if proc is None or proc.poll() is not None:
            print(f"[SUPERVISOR]: {name} is not running. Restarting...")
            log_supervisor_event(f"[RESTART]: {name} was down. Restarting...")
            start_daemon(name, cmd)

def supervisor_loop(interval=60):
    print("[SUPERVISOR]: Monitoring bridge and launcher...")
    for name, cmd in DAEMONS.items():
        start_daemon(name, cmd)
    while True:
        check_and_restart_daemons()
        time.sleep(interval)

# === Run the supervisor ===
if __name__ == "__main__":
    supervisor_loop()

    # === Optional simulation mode (disabled) ===
    # while True:
    #     print("[SUPERVISOR]: Monitoring in simulated mode...")
    #     time.sleep(60)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():