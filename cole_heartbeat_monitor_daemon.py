import os
import json
import time
import subprocess
import psutil
from datetime import datetime
from assistants.malik import malik_report

# === Config ===
HEARTBEAT_LOG_FILE = "data/cole_heartbeat_log.json"
HEARTBEAT_FILE = "data/heartbeat.json"
CHECK_INTERVAL = 60  # 1 minute

# === Critical Daemons to Monitor ===
DAEMONS = {
    "cole_brain_auto_executor": ["python", "cole_brain_auto_executor.py"],
    "cole_autonomous_execution_handler": ["python", "cole_autonomous_execution_handler.py"],
    "cole_smart_decision_trigger_daemon": ["python", "cole_smart_decision_trigger_daemon.py"],
    "cole_self_improving_strategy_loop_daemon": ["python", "cole_self_improving_strategy_loop_daemon.py"],
    "cole_auto_correction_loop_daemon": ["python", "cole_tools/cole_auto_correction_loop_daemon.py"],
    "cole_self_healing_error_watcher_daemon": ["python", "cole_self_healing_error_watcher_daemon.py"],
    "cole_heartbeat_monitor_daemon": ["python", "cole_heartbeat_monitor_daemon.py"]
}

os.makedirs("data", exist_ok=True)

# === Track Daemon Processes ===
processes = {}

# === Logging Helper ===
def log_heartbeat_event(message):
    logs = []
    if os.path.exists(HEARTBEAT_LOG_FILE):
        try:
            with open(HEARTBEAT_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(HEARTBEAT_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Update Heartbeat Metrics ===
def update_heartbeat():
    status = {
        "timestamp": datetime.now().isoformat(),
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
        "load_avg": os.getloadavg(),
        "process_count": len(psutil.pids())
    }

    with open(HEARTBEAT_FILE, "w") as f:
        json.dump(status, f, indent=2)

    log_heartbeat_event("Heartbeat updated successfully.")
    malik_report(f"[HEARTBEAT] Updated: CPU {status['cpu_percent']}% | Mem {status['memory_percent']}%")

# === Start Daemon Process ===
def start_daemon(name, cmd):
    print(f"[HEARTBEAT]: Starting {name}...")
    processes[name] = subprocess.Popen(cmd)
    log_heartbeat_event(f"[START]: {name} started.")

# === Check & Restart Daemons if Down ===
def check_and_restart_daemons():
    for name, cmd in DAEMONS.items():
        proc = processes.get(name)
        if proc is None or proc.poll() is not None:
            print(f"[HEARTBEAT]: {name} is not running. Restarting...")
            log_heartbeat_event(f"[RESTART]: {name} was down. Restarting...")
            start_daemon(name, cmd)

# === Combined Heartbeat & Daemon Monitor Loop ===
def monitor_heartbeat():
    print("[HEARTBEAT]: Monitoring daemons and system heartbeat...")
    # Start all daemons initially
    for name, cmd in DAEMONS.items():
        start_daemon(name, cmd)

    # Continuous loop
    while True:
        check_and_restart_daemons()
        update_heartbeat()
        time.sleep(CHECK_INTERVAL)

# === CLI Trigger ===
if __name__ == "__main__":
    monitor_heartbeat()