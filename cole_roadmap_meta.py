# === FILE: cole_roadmap_meta.py ===

import json
import os

ROADMAP_FILE = "project_roadmap.json"

def load_roadmap_features():
    if not os.path.exists(ROADMAP_FILE):
        print("[GPT Roadmap Meta] Roadmap file missing.")
        return []

    try:
        with open(ROADMAP_FILE, "r") as f:
            roadmap = json.load(f)

        # Safety: If it's a list, convert to dict with "features" key
        if isinstance(roadmap, list):
            print("[GPT Roadmap Meta] Warning: roadmap.json is a list, converting...")
            roadmap = {"features": roadmap}

        features = roadmap.get("features", [])
        valid = [f for f in features if isinstance(f, dict) and f.get("status") == "pending"]
        print(f"[GPT Roadmap Meta] Loaded {len(valid)} pending features.")
        return valid

    except Exception as e:
        print(f"[GPT Roadmap Meta] Error loading roadmap: {e}")
        return []