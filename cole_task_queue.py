import os
import json
from datetime import datetime

TASK_QUEUE_FILE = "data/cole_task_queue.json"
TASK_LOG_FILE = "data/cole_task_queue_log.json"

# === Load Task Queue ===
def load_task_queue():
    if not os.path.exists(TASK_QUEUE_FILE):
        return []
    with open(TASK_QUEUE_FILE, "r") as f:
        return json.load(f)

# === Save Task Queue ===
def save_task_queue(tasks):
    with open(TASK_QUEUE_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# === Check if Task Exists (by task text only) ===
def task_exists(tasks, task_text):
    return any(t["task"] == task_text for t in tasks)

# === Add Task to Queue with Type and Logging ===
def add_task(task_text, task_type="general"):
    tasks = load_task_queue()
    if task_exists(tasks, task_text):
        print(f"[Cole Queue] Task already exists: {task_text}")
        return False

    task = {
        "timestamp": str(datetime.now()),
        "task": task_text,
        "type": task_type,
        "status": "pending"
    }

    tasks.append(task)
    save_task_queue(tasks)
    log_task_action(task_text, f"Added ({task_type})")
    print(f"[Cole Queue] Task added: {task_text}")
    return True

# === Mark Task Complete by Text ===
def mark_task_complete(task_text):
    tasks = load_task_queue()
    found = False
    for t in tasks:
        if t["task"] == task_text:
            t["status"] = "completed"
            t["completed"] = str(datetime.now())
            found = True
            log_task_action(task_text, "Completed")
            print(f"[Cole Queue] Marked complete: {task_text}")
            break

    if found:
        save_task_queue(tasks)
    else:
        print(f"[Cole Queue] Task not found to mark complete: {task_text}")

# === Get Only Pending Tasks ===
def get_pending_tasks():
    tasks = load_task_queue()
    return [t for t in tasks if t.get("status") == "pending"]

# === Clear Completed Tasks Only (Safe Cleanup) ===
def clear_completed_tasks():
    tasks = load_task_queue()
    tasks = [t for t in tasks if t["status"] != "completed"]
    save_task_queue(tasks)
    print("[Cole Queue] Completed tasks cleared.")

# === Full Queue Clear (Use with caution) ===
def clear_queue():
    save_task_queue([])
    print("[Cole Queue] Task queue fully cleared.")

# === Action Logger (Persistent Audit Trail) ===
def log_task_action(task_text, action):
    log = []
    if os.path.exists(TASK_LOG_FILE):
        with open(TASK_LOG_FILE, "r") as f:
            log = json.load(f)

    log_entry = {
        "timestamp": str(datetime.now()),
        "task": task_text,
        "action": action
    }
    log.append(log_entry)

    with open(TASK_LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)

# === CLI Testing Mode ===
if __name__ == "__main__":
    print("[Cole Queue] Testing task queue module...")

    # Add task test
    add_task("Test task from CLI", task_type="self_write")

    # Get tasks test
    print("[Cole Queue] Pending tasks:", get_pending_tasks())

    # Mark complete test
    mark_task_complete("Test task from CLI")

    # Clear completed test
    clear_completed_tasks()
    print("[Cole Queue] Queue after clearing completed:", load_task_queue())

# === Alternate Interface for General Task Queue ===
def legacy_add_task(task_description, tags=None):
    if tags is None:
        tags = []
    task_entry = {
        "task": task_description,
        "tags": tags,
        "added_at": datetime.now().isoformat()
    }

    tasks = get_pending_tasks()
    tasks.append(task_entry)
    save_task_queue(tasks)
    print(f"[Task Queue] Added new task: {task_description}")

def legacy_remove_task(index):
    tasks = get_pending_tasks()
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        save_task_queue(tasks)
        print(f"[Task Queue] Removed task: {removed_task['task']}")
    else:
        print(f"[Task Queue] Invalid task index: {index}")

def legacy_clear_task_queue():
    save_task_queue([])
    print("[Task Queue] Cleared all tasks.")

if __name__ == "__main__":
    # Legacy testing block
    legacy_add_task("Optimize portfolio analysis module", ["urgent"])
    legacy_add_task("Clean up logging inconsistencies", ["maintenance"])
    print(get_pending_tasks())
    legacy_remove_task(0)

# === Task Queue Export for Autopilot Loop ===
def get_task_queue():
    """
    Simplified interface to return current task queue for Autopilot loop.
    Adjust this to fit real data logic when ready.
    """
    pending_tasks = get_pending_tasks()
    return [task["task"] for task in pending_tasks]