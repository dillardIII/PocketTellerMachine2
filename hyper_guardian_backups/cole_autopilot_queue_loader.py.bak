# === FILE: cole_autopilot_queue_loader.py ===

import os
import json

QUEUE_FILE = "data/autopilot_queue.json"

def normalize_autopilot_tasks(raw_tasks):
    """
    Normalize raw queue items into task objects with 'name' and 'input'.
    """
    normalized = []
    for task in raw_tasks:
        if isinstance(task, dict) and "name" in task:
            normalized.append(task)
        elif isinstance(task, dict) and "description" in task:
            normalized.append({
                "name": "cole_write_code",
                "input": task["description"]
            })
        elif isinstance(task, str):
            normalized.append({
                "name": "cole_write_code",
                "input": task
            })
    return normalized

def load_autopilot_queue():
    """
    Loads and normalizes tasks from the autopilot queue file.
    """
    if not os.path.exists(QUEUE_FILE):
        print("[Autopilot Queue] File not found.")
        return []

    try:
        with open(QUEUE_FILE, "r") as f:
            raw_tasks = json.load(f)
        normalized = normalize_autopilot_tasks(raw_tasks)
        print(f"[Autopilot Queue] Loaded {len(normalized)} tasks.")
        return normalized
    except Exception as e:
        print(f"[Autopilot Queue] Error loading queue: {e}")
        return []