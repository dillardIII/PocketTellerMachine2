# === FILE: roadmap_thinker.py ===

import json
import os
import time

ROADMAP_FILE = "data/project_roadmap.json"

# === Load the roadmap safely ===
def load_roadmap():
    if not os.path.exists(ROADMAP_FILE):
        print("[Roadmap Thinker] No roadmap file found. Creating default.")
        default = []
        save_roadmap(default)
        return default
    try:
        with open(ROADMAP_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"[Roadmap Thinker] JSON parse error: {e}")
        return []

# === Save roadmap to file ===
def save_roadmap(roadmap):
    os.makedirs("data", exist_ok=True)
    with open(ROADMAP_FILE, "w") as f:
        json.dump(roadmap, f, indent=2)

# === Append new feature idea to roadmap ===
def append_feature_to_roadmap(feature):
    roadmap = load_roadmap()
    roadmap.append(feature)
    save_roadmap(roadmap)
    print(f"[Roadmap Thinker] Logged new feature: {feature.get('title', 'Untitled')}")

# === GPT-driven logic to suggest a new feature ===
def run_thinking_cycle():
    print("[Roadmap Thinker] Thinking...")
    try:
        with open("data/last_gpt_feature.json", "r") as f:
            gpt_response = json.load(f)
        feature = gpt_response.get("feature")
        if feature:
            append_feature_to_roadmap(feature)
        else:
            print("[Roadmap Thinker] No valid feature found in GPT response.")
    except Exception as e:
        print(f"[Roadmap Thinker] Error in thinking cycle: {e}")