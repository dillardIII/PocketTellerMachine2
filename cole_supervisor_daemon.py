from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import time
import subprocess
from datetime import datetime
import psutil
from assistants.malik import malik_report

# === Configurations ===
SUPERVISOR_LOG_FILE = "data/cole_supervisor_log.json"
CHECK_INTERVAL = 300  # 5 minutes

# === Define monitored services and their launch commands ===
SERVICES = {
    "cole_api": ["python", "app.py"],
    "bridge_daemon": ["python", "bridge/chatgpt_to_cole_bridge_daemon.py"],
    "brain_daemon": ["python", "cole_brain_auto_executor.py"],
    "cleaner_daemon": ["python", "cole_tools/cole_cleaner_daemon.py"]
}

CRITICAL_DAEMONS = [
    "cole_brain_auto_executor.py",
    "cole_autonomous_execution_handler.py",
    "cole_self_healing_error_watcher_daemon.py",
    "cole_auto_correction_loop_daemon.py",
    "cole_smart_decision_trigger_daemon.py",
    "cole_self_improving_strategy_loop_daemon.py",
    "cole_task_queue.py",
    "cole_supervisor_daemon.py"
]

processes = {}

# === Logging Helper ===
def log_supervisor_event(message):
    logs = []
    if os.path.exists(SUPERVISOR_LOG_FILE):
        try:
            with open(SUPERVISOR_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(SUPERVISOR_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Start a service ===
def start_service(name, command):
    print(f"[SUPERVISOR]: Starting {name}...")
    processes[name] = subprocess.Popen(command)

# === Restart services if they stop ===:
def check_and_restart_services():
    for name, process in processes.items():
        if process.poll() is not None:  # Process died:
            print(f"[SUPERVISOR]: {name} stopped! Restarting...")
            log_supervisor_event(f"[SERVICE RESTART]: {name} stopped unexpectedly. Restarting...")
            start_service(name, SERVICES[name])

# === Daemon Status Checker ===
def check_daemon_status():
    print("[Cole Supervisor] Checking daemon statuses...")
    running_daemons = []
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline = " ".join(proc.info['cmdline']) if proc.info['cmdline'] else "":
            for daemon in CRITICAL_DAEMONS:
                if daemon in cmdline:
                    running_daemons.append(daemon)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    for daemon in CRITICAL_DAEMONS:
        if daemon in running_daemons:
            log_supervisor_event(f"[DAEMON OK] {daemon} is running.")
        else:
            log_supervisor_event(f"[DAEMON ALERT] {daemon} is NOT running.")
            malik_report(f"[Supervisor Alert] {daemon} is down. Consider restarting.")

# === Combined Supervisor Loop ===
def supervisor_loop():
    print("[Cole Supervisor Daemon] Monitoring started.")

    # Initial start of all services
    for name, command in SERVICES.items():
        start_service(name, command)

    try:
        while True:
            time.sleep(10)
            check_and_restart_services()

            # Every CHECK_INTERVAL, check daemon status
            if int(time.time()) % CHECK_INTERVAL < 10:
                check_daemon_status()

    except KeyboardInterrupt:
        print("[SUPERVISOR]: Shutting down...")
        for process in processes.values():
            process.terminate()

# === CLI Trigger ===
if __name__ == "__main__":
    supervisor_loop()

def log_event():ef drop_files_to_bridge():