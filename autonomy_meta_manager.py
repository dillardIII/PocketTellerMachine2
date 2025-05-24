# === FILE: autonomy_meta_manager.py ===

import json
import os
from datetime import datetime
from ptm_gpt_agent import run_ptm_gpt_agent
from cole_gpt_advisor import ask_gpt

ROADMAP_FILE = "project_roadmap.json"
LOG_FILE = "logs/autonomy_meta_log.json"

def review_and_reprioritize_roadmap():
    if not os.path.exists(ROADMAP_FILE):
        print("[MetaManager] No roadmap found.")
        return

    with open(ROADMAP_FILE, "r") as f:
        roadmap = json.load(f)

    features = roadmap.get("features", [])
    if not features:
        print("[MetaManager] No features to evaluate.")
        return

    print(f"[MetaManager] Reviewing {len(features)} roadmap items...")

    summary_prompt = f"""
You are a meta-strategy planner for an AI system called PTM.

Here is the current roadmap:
{json.dumps(features, indent=2)}

Reprioritize these features by urgency, complexity, and autonomy level.
Also mark any outdated, duplicate, or weak features.
Return an updated roadmap JSON.
"""

    response = ask_gpt(summary_prompt)

    try:
        updated = json.loads(response)
        with open(ROADMAP_FILE, "w") as f:
            json.dump(updated, f, indent=2)
        print("[MetaManager] Roadmap updated with GPT decisions.")
        log_meta_action("Roadmap updated", updated)
    except Exception as e:
        print("[MetaManager] Failed to parse GPT output:", e)

def log_meta_action(action, data):
    os.makedirs("logs", exist_ok=True)
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "action": action,
        "data": data
    }
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(log)
    with open(LOG_FILE, "w") as f:
        json.dump(logs[-100:], f, indent=2)