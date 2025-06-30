from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: strategy_brain.py ===
# 🧠 Strategy Brain – Chooses which persona runs which strategy and executes logic

import json
import time
from ai_memory_trainer import log_experience
from reflex_macro_log import log_macro

STRATEGY_FILE = "strategy_registry.json"

def run_strategy(strategy):
    print(f"[StrategyBrain] ⚔️ Running strategy: {strategy['name']} (via {strategy['assigned']})")

    # Simulated strategy logic
    success = strategy["name"] != "Breakout Sniper"  # Fake condition
    time.sleep(1)

    log_macro(strategy["name"], "Success" if success else "Failure", strategy["assigned"]):
    log_experience(strategy["name"], success)
    return success

def run_all_assigned():
    with open(STRATEGY_FILE, "r") as f:
        strategies = json.load(f)

    for strat in strategies:
        if strat.get("assigned"):
            run_strategy(strat)

if __name__ == "__main__":
    run_all_assigned()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():