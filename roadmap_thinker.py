# === FILE: roadmap_thinker.py ===

import json
import os
from datetime import datetime
from cole_gpt_advisor import ask_gpt

ROADMAP_FILE = "project_roadmap.json"

def think_of_new_feature():
    prompt = """
    You are part of an autonomous trading bot called PTM.
    You generate helpful feature ideas to improve the trading system.
    Return a new feature in this JSON format:

    {
        "id": "featureXXX",
        "name": "Feature Name",
        "type": "dashboard | education | trading | repair | persona_feature | api",
        "status": "pending",
        "priority": "high | medium | low",
        "description": "One sentence describing what the feature does."
    }

    Return only the JSON. Do not add commentary.
    """

    response = ask_gpt(prompt)

    try:
        feature = json.loads(response)
        if not isinstance(feature, dict) or "id" not in feature:
            raise ValueError("Invalid feature format.")
    except Exception as e:
        print(f"[Thinker] Failed to parse GPT output: {e}")
        return None

    return feature

def add_feature_to_roadmap(feature):
    os.makedirs("data", exist_ok=True)

    if os.path.exists(ROADMAP_FILE):
        with open(ROADMAP_FILE, "r") as f:
            roadmap = json.load(f)
    else:
        roadmap = {"features": []}

    roadmap["features"].append(feature)

    with open(ROADMAP_FILE, "w") as f:
        json.dump(roadmap, f, indent=2)

    print(f"[Thinker] Added new feature to roadmap: {feature['name']}")

def run_thinking_cycle():
    print("[Thinker] Thinking of new roadmap feature...")
    feature = think_of_new_feature()
    if feature:
        add_feature_to_roadmap(feature)
    else:
        print("[Thinker] No valid idea returned.")