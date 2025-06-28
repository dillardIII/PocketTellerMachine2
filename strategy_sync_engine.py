# === FILE: strategy_sync_engine.py ===
# 🔁 Strategy Sync Engine – Ensures bots have their strategies assigned and updated

import json
import os

STRATEGY_FILE = "strategy_registry.json"
ASSISTANT_FILE = "assistant_moods.json"

def sync_assignments():
    if not os.path.exists(STRATEGY_FILE):
        print("[StrategySync] ❌ strategy_registry.json not found.")
        return

    with open(STRATEGY_FILE, "r") as f:
        strategies = json.load(f)

    assignments = {}
    for s in strategies:
        bot = s.get("assigned", "Unassigned")
        if bot not in assignments:
            assignments[bot] = []
        assignments[bot].append(s["name"])

    print("[StrategySync] ✅ Current Strategy Assignments:")
    for bot, plans in assignments.items():
        print(f"  • {bot}: {', '.join(plans)}")

if __name__ == "__main__":
    sync_assignments()