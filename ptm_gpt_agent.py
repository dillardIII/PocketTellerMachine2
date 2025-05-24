# === FILE: ptm_gpt_agent.py ===

import json
import os
from datetime import datetime
from cole_gpt_advisor import ask_gpt

ROADMAP_FILE = "project_roadmap.json"

def handle_agent_input(user_command):
    prompt = f"""
You are PTM's AI assistant. A user said:

\"{user_command}\"

Turn that into a roadmap feature in this format:
{{
  "id": "featureXXX",
  "name": "...",
  "type": "dashboard | strategy | api | education | automation | repair | assistant",
  "status": "pending",
  "priority": "high | medium | low",
  "description": "..."
}}

Return ONLY the JSON.
"""

    response = ask_gpt(prompt)

    try:
        feature = json.loads(response)
        if not isinstance(feature, dict) or "id" not in feature:
            raise ValueError("Invalid feature format.")
        print(f"[GPT Agent] Feature parsed: {feature['name']}")
        return feature
    except Exception as e:
        print(f"[GPT Agent] Failed to parse GPT response: {e}")
        return None

def append_to_roadmap(feature):
    if os.path.exists(ROADMAP_FILE):
        with open(ROADMAP_FILE, "r") as f:
            roadmap = json.load(f)
    else:
        roadmap = {"features": []}

    roadmap["features"].append(feature)

    with open(ROADMAP_FILE, "w") as f:
        json.dump(roadmap, f, indent=2)

    print(f"[GPT Agent] Appended feature: {feature['name']}")

def run_ptm_gpt_agent(user_command):
    print(f"[GPT Agent] Processing command: {user_command}")
    feature = handle_agent_input(user_command)
    if feature:
        append_to_roadmap(feature)
        return {"status": "added", "feature": feature}
    else:
        return {"status": "failed"}