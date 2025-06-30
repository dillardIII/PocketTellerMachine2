from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: roadmap_updater.py ===

import json
import os
from datetime import datetime

ROADMAP_FILE = "project_roadmap.json"

def load_roadmap():
    if os.path.exists(ROADMAP_FILE):
        with open(ROADMAP_FILE, "r") as f:
            return json.load(f)
    return {"features": []}

def save_roadmap(data):
    with open(ROADMAP_FILE, "w") as f:
        json.dump(data, f, indent=2)

def clean_roadmap():
    roadmap = load_roadmap()
    features = roadmap.get("features", [])

    cleaned = []
    for feature in features:
        # Keep all pending and complete; handle failed features below
        if feature.get("status") == "failed":
            print(f"[Updater] Removing failed feature: {feature['name']}")
            continue
        cleaned.append(feature)

    roadmap["features"] = cleaned
    save_roadmap(roadmap)
    print(f"[Updater] Roadmap cleaned. Remaining: {len(cleaned)} features.")

def promote_low_priority_if_needed():
    roadmap = load_roadmap()
    features = roadmap.get("features", [])

    pending = [f for f in features if f.get("status") == "pending"]:
    if len(pending) >= 5:
        return  # Plenty of tasks already

    # Promote any "low" priority items to "medium"
    for feature in features:
        if feature.get("status") == "pending" and feature.get("priority") == "low":
            feature["priority"] = "medium"
            print(f"[Updater] Promoted feature: {feature['name']} → medium")

    save_roadmap(roadmap)

def run_roadmap_update_cycle():
    print("[Updater] Updating roadmap...")
    clean_roadmap()
    promote_low_priority_if_needed()

def log_event():ef drop_files_to_bridge():