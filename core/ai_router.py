"""
AI Task Router:
This module handles routing of tasks across assistant personas
and PTM subsystems. Tasks can include trade execution,
education delivery, strategy evaluation, and inter-bot coordination.
"""

import os
import json
from datetime import datetime, timezone
from cole_logger import log_event
from cole_brain import log_memory

ROUTED_TASKS_FILE = "data/routed_tasks.json"
SYNC_LOG_FILE = "logs/ai_router_sync.json"

PERSONA_HANDLERS = {
    "MoCash": "recap",
    "Mentor": "education",
    "Strategist": "analysis",
    "DrillInstructor": "warning",
    "Malik": "intel"
}

def get_timestamp():
    return datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()

def load_tasks():
    if not os.path.exists(ROUTED_TASKS_FILE):
        return []
    with open(ROUTED_TASKS_FILE, "r") as f:
        return json.load(f)

def log_sync(status):
    data = {
        "status": "ok" if status else "error",
        "last_sync": get_timestamp(),
        "health": "✅ Healthy" if status else "❌ Unhealthy"
    }
    with open(SYNC_LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)

def route_tasks():
    log_event("AI Router", "📬 Routing tasks to assistant modules...", "info")
    print("[AI Router] 🔄 Beginning task routing...")

    try:
        tasks = load_tasks()
        if not tasks:
            log_event("AI Router", "📭 No tasks found. Using fallback dummy task.", "warn")
            print("[AI Router] 📭 No tasks found. Using fallback dummy task.")
            tasks = [{"task_type": "recap", "from": "system", "to": "MoCash", "details": "No task"}]

        for task in tasks[-1:]:  # Only the latest task
            if isinstance(task, str):
                print(f"[AI Router] ⚠️ Invalid task format: {task}")
                continue

            assigned = task.get("to", "Unknown")
            task_type = task.get("task_type", "unknown")
            print(f"[AI Router] 🔄 Routing task '{task_type}' to: {assigned}")

            log_event("AI Router", f"🔄 Task: {task_type} => {assigned}", "info")
            log_memory("routed_task", {
                "task_type": task_type,
                "to": assigned,
                "from": task.get("from", "unknown"),
                "details": task.get("details", "")
            })

            print(f"[{get_timestamp()}] [AI Router] 💰 Task assigned to {assigned}: {task.get('details')}")

        log_sync(True)
        log_event("AI Router", "✅ Task routing complete.", "success")

    except Exception as e:
        error_msg = f"❌ Error: {e}"
        print(f"[AI Router] {error_msg}")
        log_event("AI Router", error_msg, "error")
        log_sync(False)
        log_memory("ai_router_error", str(e))

if __name__ == "__main__":
    route_tasks()