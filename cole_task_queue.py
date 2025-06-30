from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_task_queue.py ===

import os
import json
from datetime import datetime

TASKS_FILE = "data/cole_tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks[-100:], f, indent=2)

def add_task(task):
    tasks = load_tasks()
    if task in tasks:
        return False
    tasks.append({
        "task": task,
        "timestamp": datetime.now().isoformat()
    })
    save_tasks(tasks)
    return True

def get_latest_tasks(limit=5):
    tasks = load_tasks()
    return tasks[-limit:]

# Optional CLI test
if __name__ == "__main__":
    print("[Task Queue] Adding example task...")
    add_task("Example Task")
    print("[Task Queue] Current tasks:")
    print(get_latest_tasks())

def log_event():ef drop_files_to_bridge():