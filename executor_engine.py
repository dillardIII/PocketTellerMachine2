from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: executor_engine.py ===
# ⚙️ Executor Engine – Handles queued tasks from other bots or user commands

import os
import json
import time
from utils.logger import log_event

TASK_QUEUE = "bridge/task_queue.json"

def execute_pending_tasks():
    print("[Executor] ⚙️ Executing queued tasks...")
    while True:
        try:
            if os.path.exists(TASK_QUEUE):
                with open(TASK_QUEUE, "r") as f:
                    tasks = json.load(f)

                if tasks:
                    for task in tasks:
                        print(f"[Executor] 🔄 Running task: {task['type']} -> {task.get('detail')}")
                        log_event("Task Executed", task)

                    with open(TASK_QUEUE, "w") as f:
                        json.dump([], f)

            time.sleep(15)

        except Exception as e:
            print(f"[Executor] ❌ Error: {e}")
            time.sleep(30)