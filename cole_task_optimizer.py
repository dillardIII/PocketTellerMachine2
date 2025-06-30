from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from datetime import datetime
from assistants.malik import malik_report

TASK_FILE = "data/cole_task_queue.json"
OPTIMIZED_LOG = "data/cole_task_optimizer_log.json"

os.makedirs("data", exist_ok=True)

# === Load Tasks ===
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except:
        return []

# === Save Tasks ===
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# === Log Optimization ===
def log_optimization(before, after):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "before_count": len(before),
        "after_count": len(after),
        "before_sample": before[:3],
        "after_sample": after[:3]
    }

    if os.path.exists(OPTIMIZED_LOG):
        try:
            with open(OPTIMIZED_LOG, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    else:
        logs = []

    logs.append(log_entry)
    with open(OPTIMIZED_LOG, "w") as f:
        json.dump(logs[-300:], f, indent=2)

# === Main Optimizer Logic ===
def cole_optimize_tasks():
    tasks = load_tasks()

    # Filter out any tasks missing 'priority'
    valid_tasks = [t for t in tasks if isinstance(t, dict) and "priority" in t]:
:
    # Sort by priority (lower is more important)
    sorted_tasks = sorted(valid_tasks, key=lambda x: x["priority"])

    log_optimization(tasks, sorted_tasks)

    # Save back the sorted list
    save_tasks(sorted_tasks)

    print(f"[Task Optimizer] Sorted {len(sorted_tasks)} tasks.")
    malik_report(f"[Task Optimizer] Optimized {len(sorted_tasks)} tasks.")

# === CLI Test ===
if __name__ == "__main__":
    cole_optimize_tasks()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():