from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_project_planner.py ===

import json
import os

ROADMAP_FILE = "data/project_roadmap.json"

# === Load Roadmap Features ===
def load_roadmap():
    if not os.path.exists(ROADMAP_FILE):
        return []
    try:
        with open(ROADMAP_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"[Cole Planner] JSON read error: {e}")
        return []

# === Generate Tasks from Roadmap ===
def generate_tasks_from_roadmap():
    print("[Planner] Converting roadmap to task list...")
    roadmap = load_roadmap()
    tasks = []

    for feature in roadmap:
        if feature.get("status", "pending") == "pending":
            task = {
                "task_id": f"feature_{int(time.time())}",
                "title": feature.get("title", "Untitled Task"),
                "description": feature.get("description", ""),
                "type": "feature_build"
            }
            tasks.append(task)

    print(f"[Planner] Generated {len(tasks)} tasks from roadmap.")
    return tasks

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():