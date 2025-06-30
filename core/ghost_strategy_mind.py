from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: core/ghost_strategy_mind.py ===
"""
Ghost Strategy Mind
Shared AI intelligence module for tactical trading and learning.
Enables collective knowledge building, strategic adaptation, and scenario planning.
"""

import os
import json
from datetime import datetime

MIND_FILE = "memory/ghost_strategy_mind.json"

def load_mind():
    if not os.path.exists(MIND_FILE):
        return {"strategies": [], "lessons": [], "last_updated": None}
    with open(MIND_FILE, "r") as f:
        return json.load(f)

def save_mind(data):
    with open(MIND_FILE, "w") as f:
        json.dump(data, f, indent=2)

def log_strategy(name, result, notes=""):
    mind = load_mind()
    entry = {
        "strategy": name,
        "result": result,
        "notes": notes,
        "timestamp": datetime.utcnow().isoformat()
    }
    mind["strategies"].append(entry)
    mind["last_updated"] = datetime.utcnow().isoformat()
    save_mind(mind)
    print(f"[GhostMind] 📈 Logged strategy '{name}' with result: {result}")

def add_lesson(lesson_text):
    mind = load_mind()
    mind["lessons"].append({
        "text": lesson_text,
        "timestamp": datetime.utcnow().isoformat()
    })
    mind["last_updated"] = datetime.utcnow().isoformat()
    save_mind(mind)
    print("[GhostMind] 📘 New lesson added.")

def get_all_strategies():
    return load_mind().get("strategies", [])

def get_all_lessons():
    return load_mind().get("lessons", [])

# Example usage
if __name__ == "__main__":
    log_strategy("Iron Condor Test", "win", "Solid IV crush post-earnings.")
    add_lesson("Iron Condors work well in high IV pre-earnings, exit early.")