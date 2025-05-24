# === FILE: cole_project_planner.py ===

import json
import os

ROADMAP_FILE = "project_roadmap.json"

def generate_tasks_from_roadmap():
    if not os.path.exists(ROADMAP_FILE):
        print("[Planner] No roadmap found.")
        return []

    with open(ROADMAP_FILE, "r") as f:
        roadmap = json.load(f)

    if isinstance(roadmap, list):  # malformed roadmap.json file
        print("[Planner] ERROR: Roadmap is a list, expected dict with 'features' key.")
        return []

    tasks = []
    for feature in roadmap.get("features", []):
        if feature.get("status", "pending") == "pending":
            tasks.append({
                "id": feature.get("id"),
                "name": "cole_write_code",  # ensures compatibility with Cole's loop
                "input": f"Build feature: {feature['name']} - {feature['description']}",
                "feature_id": feature["id"],
                "priority": feature.get("priority", "medium"),
                "type": feature.get("type", "unknown"),
                "params": {
                    "type": feature.get("type"),
                    "name": feature.get("name")
                }
            })

    print(f"[Planner] Generated {len(tasks)} tasks from roadmap.")
    return tasks