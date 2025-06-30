# === FILE: auto_cycle_builder.py ===

import json
import time
import os
from cole_project_planner import generate_tasks_from_roadmap
from cole_feature_builder import build_feature
from cole_tester import test_feature
from roadmap_thinker import run_thinking_cycle
from voice_recap_engine import recap_build  # << NEW

ROADMAP_FILE = "project_roadmap.json"

def update_roadmap_status(feature_id, passed):
    if not os.path.exists(ROADMAP_FILE):
        print("[Cycle] Roadmap file missing.")
        return

    with open(ROADMAP_FILE, "r") as f:
        roadmap = json.load(f)

    updated = False
    for feature in roadmap.get("features", []):
        if feature["id"] == feature_id:
            feature["status"] = "complete" if passed else "failed"
            updated = True
            print(f"[Cycle] Marked {feature_id} as {'complete' if passed else 'failed'}.")
            break

    if updated:
        with open(ROADMAP_FILE, "w") as f:
            json.dump(roadmap, f, indent=2)

def run_build_autonomy_cycle():
    print("[PTM BuildBot] Starting feature auto-builder loop...")

    while True:
        # === Generate new ideas on every build loop ===
        run_thinking_cycle()

        tasks = generate_tasks_from_roadmap()

        if not tasks:
            print("[PTM BuildBot] All roadmap tasks are complete or none exist.")
            break

        for task in tasks:
            print(f"[PTM BuildBot] Working on: {task.get('description', 'No description')}")  # ✅ FIXED
            result = build_feature(task)
            print(f"[PTM BuildBot] Build Result: {result}")

            test_result = test_feature(task)
            print(f"[PTM BuildBot] Test Result: {test_result}")

            if test_result["passed"]:
                recap_build(task["params"]["name"])  # << NEW: voice recap

            update_roadmap_status(task["feature_id"], test_result["passed"])

        time.sleep(5)  # Optional: delay between task batches