from ghost_env import INFURA_KEY, VAULT_ADDRESS
import subprocess
import time
import os
import json
from datetime import datetime

# === Phase 11 Critical Daemons ===
DAEMONS = {
    "cole_self_healing_error_watcher_daemon": ["python", "cole_self_healing_error_watcher_daemon.py"],
    "cole_smart_decision_trigger_daemon": ["python", "cole_smart_decision_trigger_daemon.py"],
    "cole_self_improving_strategy_loop_daemon": ["python", "cole_self_improving_strategy_loop_daemon.py"],
    "cole_auto_correction_loop_daemon": ["python", "cole_auto_correction_loop_daemon.py"],
    "cole_autonomous_execution_handler": ["python", "cole_autonomous_execution_handler.py"],
    "cole_brain_auto_executor": ["python", "cole_brain_auto_executor.py"],
    "cole_smart_code_requestor_daemon": ["python", "cole_smart_code_requestor_daemon.py"],
    "cole_phase11_brain_memory_feedback_daemon": ["python", "cole_phase11_brain_memory_feedback_daemon.py"]
}

# === Log file ===
PHASE11_LAUNCHER_LOG = "data/phase11_launcher_log.json"
os.makedirs("data", exist_ok=True)

# === Track processes ===
processes = {}

def log_launcher_event(message):
    logs = []
    if os.path.exists(PHASE11_LAUNCHER_LOG):
        try:
            with open(PHASE11_LAUNCHER_LOG, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(PHASE11_LAUNCHER_LOG, "w") as f:
        json.dump(logs[-500:], f, indent=2)

def start_daemon(name, cmd):
    print(f"[PHASE 11 LAUNCHER]: Starting {name}...")
    try:
        processes[name] = subprocess.Popen(cmd)
        log_launcher_event(f"[START]: {name} started successfully.")
    except Exception as e:
        log_launcher_event(f"[START ERROR]: {name} failed to start → {e}")
        print(f"[LAUNCH ERROR]: {name} → {e}")

def check_and_restart_daemons():
    for name, cmd in DAEMONS.items():
        proc = processes.get(name)
        if proc is None or proc.poll() is not None:
            print(f"[PHASE 11 LAUNCHER]: {name} is down. Restarting...")
            log_launcher_event(f"[RESTART]: {name} was down. Restarting...")
            start_daemon(name, cmd)

def phase11_launcher_loop(interval=60):
    print("[PHASE 11 LAUNCHER]: Starting Phase 11 Autonomous Daemons...")
    for name, cmd in DAEMONS.items():
        start_daemon(name, cmd)

    while True:
        check_and_restart_daemons()
        time.sleep(interval)

# === Run Launcher ===
if __name__ == "__main__":
    phase11_launcher_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():