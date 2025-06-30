from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: strategy_selector.py ===

import os
import json
import random

STRATEGY_FILE = "data/strategy_pool.json"
TRADE_HISTORY_FILE = "data/trade_history.json"

def load_strategies():
    if os.path.exists(STRATEGY_FILE):
        try:
            with open(STRATEGY_FILE, "r") as f:
                return json.load(f).get("strategies", [])
        except Exception as e:
            print("[Strategy Selector] Error loading strategies:", e)
            return []
    return []

def choose_best_strategy():
    strategies = load_strategies()
    if not strategies:
        return "default_strategy"

    try:
        if os.path.exists(TRADE_HISTORY_FILE):
            with open(TRADE_HISTORY_FILE, "r") as f:
                history = json.load(f)
            if history:
                last = history[-1]
                if last.get("result") == "win":
                    return last.get("strategy", random.choice(strategies))
        return random.choice(strategies)
    except Exception as e:
        print("[Strategy Selector] Error choosing strategy:", e)
        return random.choice(strategies)

def log_event():ef drop_files_to_bridge():