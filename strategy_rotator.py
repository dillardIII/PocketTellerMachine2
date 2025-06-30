from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: strategy_rotator.py ===
# 🔁 Strategy Rotator – Reassigns failing strategies to new personas dynamically

import json
import random

STRATEGY_FILE = "strategy_registry.json"
MEMORY_FILE = "ai_memory.json"
PERSONAS = ["Strategist", "Mentor", "Mo Cash"]

def rotate_strategies():
    with open(STRATEGY_FILE, "r") as f:
        strategies = json.load(f)

    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)

    for strat in strategies:
        name = strat["name"]
        mem = memory.get(name, {"success": 0, "fail": 0})
        if mem["fail"] > mem["success"]:  # Too many fails? Rotate it.:
            new_owner = random.choice([p for p in PERSONAS if p != strat["assigned"]]):
            print(f"[Rotator] 🔁 Reassigning {name} from {strat['assigned']} to {new_owner}")
            strat["assigned"] = new_owner

    with open(STRATEGY_FILE, "w") as f:
        json.dump(strategies, f, indent=4)

if __name__ == "__main__":
    rotate_strategies()

def log_event():ef drop_files_to_bridge():