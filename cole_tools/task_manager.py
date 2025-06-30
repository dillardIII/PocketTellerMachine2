from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_tools/task_manager.py ===

import os
import json
from datetime import datetime
from assistants.malik import malik_report

# === Inline logger (replaces broken import) ===
def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"
    print(log_line)
    os.makedirs("logs", exist_ok=True)
    with open("logs/event_log.txt", "a") as log_file:
        log_file.write(log_line + "\n")

TASK_LOG_FILE = "data/task_generation_log.json"

# === Logging Helper ===
def log_task_event(event, payload=None):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "event": event,
        "payload": payload or {}
    }
    logs = []
    os.makedirs("data", exist_ok=True)
    if os.path.exists(TASK_LOG_FILE):
        try:
            with open(TASK_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append(entry)
    with open(TASK_LOG_FILE, "w") as f:
        json.dump(logs[-300:], f, indent=2)

# === Task Generator ===
def generate_tasks(task_response_text):
    """
    Attempt to parse the GPT response into a list of task dictionaries.
    Returns an empty list if parsing fails.
    """
    try:
        # Strip common bad wrapping like ```json blocks or stray newlines
        cleaned = task_response_text.strip().lstrip("```json").rstrip("```").strip()

        if not cleaned.startswith("["):
            raise ValueError("GPT did not return a JSON array.")

        tasks = json.loads(cleaned)
        if not isinstance(tasks, list):
            raise ValueError("Parsed data is not a list.")

        validated_tasks = [task for task in tasks if isinstance(task, dict) or isinstance(task, str)]
        log_task_event("Tasks Parsed Successfully", {"count": len(validated_tasks)})
        return validated_tasks

    except Exception as e:
        error_msg = f"[Task Generator Error] {str(e)}"
        log_event(f"[Task Manager] Task Parse Error: {str(e)}")
        log_task_event("Task Parse Failed", {"error": str(e), "raw": task_response_text})
        malik_report(error_msg)
        return []

# === Task Optimizer ===
def optimize_tasks(tasks):
    """
    Placeholder for task optimization logic.
    Currently returns the same task list, but logs the number of input tasks.
    """
    log_event(f"[Task Manager] Optimizing {len(tasks)} tasks...")
    return tasks