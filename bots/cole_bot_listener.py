from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bots/cole_bot_listener.py ===
# Purpose: Simulates Cole reading and responding to tasks

import json
import time
import os

COLE_TASKS = "logs/data/cole_tasks.json"
REPO_QUEUE = "settings/repo_queue.json"
LOG_PATH = "logs/autonomy_log.json"

def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def cole_listen_loop():
    print("🧠 [Cole] Listening for tasks...")
    while True:
        cole_tasks = load_json(COLE_TASKS)
        repo = load_json(REPO_QUEUE)

        active = repo.get("active_tasks", [])
        if not active:
            time.sleep(10)
            continue

        for task in active[:]:  # Copy the list to avoid mutation during loop
            if task["assigned_bot"] != "Cole":
                continue

            print(f"✅ [Cole] Acknowledging task: {task['task_id']}")
            log_result(task, "completed")

            # Mark as completed
            active.remove(task)
            repo.setdefault("completed_tasks", []).append(task)
            cole_tasks.setdefault("processed_tasks", []).append(task)

        save_json(REPO_QUEUE, repo)
        save_json(COLE_TASKS, cole_tasks)
        time.sleep(10)

def log_result(task, status):
    log = load_json(LOG_PATH)
    entry = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "bot": "Cole",
        "action": f"{task['type']}",
        "target": task["target"],
        "result": status
    }
    log.setdefault("bot_logs", []).append(entry)
    log["last_updated"] = entry["timestamp"]
    save_json(LOG_PATH, log)