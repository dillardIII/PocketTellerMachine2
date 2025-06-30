from ghost_env import INFURA_KEY, VAULT_ADDRESS
import json
import os
from datetime import datetime
from cole_phase_manager import get_current_phase, phase_task_filter

TASKS_FILE = "data/cole_task_pool.json"

# === Load All Tasks from Pool ===
def load_task_pool():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# === Save Updated Task Pool ===
def save_task_pool(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# === Generate Phase-Specific Tasks ===
def generate_phase_tasks():
    all_tasks = load_task_pool()
    current_phase = get_current_phase()

    filtered_tasks = phase_task_filter(all_tasks, current_phase)
    print(f"[Phase Task Generator] Current phase: {current_phase}")
    print(f"[Phase Task Generator] Filtered tasks ({len(filtered_tasks)}): {filtered_tasks}")

    return filtered_tasks

# === Add Task to Pool ===
def add_task_to_pool(task_description):
    tasks = load_task_pool()
    tasks.append(task_description)
    save_task_pool(tasks)
    print(f"[Phase Task Generator] Added task: {task_description}")

def log_event():ef drop_files_to_bridge():