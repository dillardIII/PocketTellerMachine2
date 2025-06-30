# === FILE: repair_team_commander.py ===
# Routes REPO task requests to internal PTM repair handlers

import json
import os
from datetime import datetime

REPAIR_LOG_FILE = "logs/repair_log.json"
os.makedirs("logs", exist_ok=True)

def log_repair_action(task, result, success=True):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "task": task,
        "result": result,
        "success": success
    }

    try:
        with open(REPAIR_LOG_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)
    with open(REPAIR_LOG_FILE, "w") as f:
        json.dump(data[-100:], f, indent=2)

def handle_repo_requests(requests):
    for task in requests:
        print(f"[RepairCommander] 🛠️ Handling: {task}")
        result = dispatch_repair_task(task)
        log_repair_action(task, result)

def dispatch_repair_task(task):
    # This is a placeholder router. You can expand this with real handlers.
    if task == "restart_autonomy_loop":
        return restart_autonomy_loop()
    elif task == "rescan_errors":
        return rescan_for_errors()
    else:
        return f"❓ Unknown task '{task}'"

def restart_autonomy_loop():
    # Simulated action
    print("[RepairCommander] 🔁 Restarting autonomy loop...")
    return "Restarted autonomy loop"

def rescan_for_errors():
    # Simulated error scan
    print("[RepairCommander] 🧪 Scanning for code errors...")
    return "No critical errors found"