from ghost_env import INFURA_KEY, VAULT_ADDRESS
# resume_tasks.py

import os
import json
import datetime

# === Files ===
TASKS_FILE = "data/cole_tasks.json"
RESULTS_FILE = "data/cole_results.json"

# === Load Helpers ===
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def load_results():
    if not os.path.exists(RESULTS_FILE):
        return []
    with open(RESULTS_FILE, "r") as f:
        return json.load(f)

# === Resume Logic (placeholder - extend later) ===
def resume_unfinished_tasks():
    print("[ResumeTasks] Checking for unfinished tasks...")

    tasks = load_tasks()
    results = load_results()

    if not tasks or not results:
        print("[ResumeTasks] No tasks or results found.")
        return

    unfinished = []
    for task in tasks:
        if not any(task in r.get("task", "") and r.get("status") == "completed" for r in results):
            unfinished.append(task)

    if unfinished:
        print(f"[ResumeTasks] Found {len(unfinished)} unfinished tasks:")
        for ut in unfinished:
            print(f"  - {ut}")
        # Here you could requeue them, but now just reporting.
    else:
        print("[ResumeTasks] All tasks appear completed or no logs found.")

# === Test Run ===
if __name__ == "__main__":
    resume_unfinished_tasks()

def log_event():ef drop_files_to_bridge():