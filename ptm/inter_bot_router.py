from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ptm/inter_bot_router.py ===
# Purpose: Routes tasks between PTM bots using the shared repo_queue
# This handles:
# - Reading pending tasks
# - Assigning them to bots
# - Logging bot actions
# - Updating autonomy logs
# - Includes both one-time relay and looped relay for background execution

import json
import time
import os

# === Paths to shared resources ===
QUEUE_PATH = "settings/repo_queue.json"
LOG_PATH = "logs/autonomy_log.json"

# === Load JSON safely ===
def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)

# === Save JSON safely ===
def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

# === Core Relay Logic: Route tasks to their assigned bots ===
def relay_messages():
    queue = load_json(QUEUE_PATH)
    tasks = queue.get("pending_tasks", [])

    if not tasks:
        print("📭 No tasks in queue.")
        return

    for task in tasks:
        print(f"📡 Routing task {task['task_id']} to {task['assigned_bot']}...")

        # Log the handoff (actual execution will come later)
        log_task(task, "routed")

        # Move task to active
        queue["pending_tasks"].remove(task)
        queue.setdefault("active_tasks", []).append(task)

    save_json(QUEUE_PATH, queue)

# === Log task event to autonomy log ===
def log_task(task, result):
    log = load_json(LOG_PATH)
    log_entry = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "bot": task["assigned_bot"],
        "action": task["type"],
        "target": task["target"],
        "result": result
    }
    log.setdefault("bot_logs", []).append(log_entry)
    log["last_updated"] = log_entry["timestamp"]
    save_json(LOG_PATH, log)

# === Loop Relay: Continuously route messages in the background ===
def start_relay_loop():
    while True:
        relay_messages()
        time.sleep(15)  # ⏲️ Low CPU drain interval