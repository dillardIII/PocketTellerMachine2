from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: strategy_loader.py ===

import os
import json

STRATEGY_DIR = "strategies"
STRATEGY_INDEX_FILE = "strategy_index.json"

# Default strategy index
DEFAULT_STRATEGIES = [
    {
        "id": "rsi_reversal",
        "name": "RSI Reversal",
        "type": "momentum",
        "description": "Buys when RSI < 30, sells when RSI > 70",
        "tags": ["rsi", "reversal", "momentum", "tech analysis"]
    },
    {
        "id": "macd_trend_follow",
        "name": "MACD Trend Follower",
        "type": "trend",
        "description": "Follows upward MACD crossovers, exits on downward cross",
        "tags": ["macd", "trend", "momentum"]
    },
    {
        "id": "bollinger_bounce",
        "name": "Bollinger Bounce",
        "type": "range",
        "description": "Buys at lower band, sells at upper band",
        "tags": ["bollinger", "volatility", "range"]
    },
    {
        "id": "safe_hold",
        "name": "Safe Hold",
        "type": "passive",
        "description": "Holds position with minimal activity for long-term trend",
        "tags": ["safe", "passive", "long-term"]
    }
]


def save_strategy_index(index):
    with open(STRATEGY_INDEX_FILE, "w") as f:
        json.dump(index, f, indent=2)


def load_strategy_index():
    if not os.path.exists(STRATEGY_INDEX_FILE):
        save_strategy_index(DEFAULT_STRATEGIES)
        return DEFAULT_STRATEGIES
    with open(STRATEGY_INDEX_FILE, "r") as f:
        return json.load(f)


def get_strategy_by_id(strategy_id):
    index = load_strategy_index()
    return next((s for s in index if s["id"] == strategy_id), None):
:

def list_strategies_by_tag(tag):
    index = load_strategy_index()
    return [s for s in index if tag in s["tags"]]:
:

def list_all_strategy_names():
    index = load_strategy_index()
    return [s["name"] for s in index]


if __name__ == "__main__":
    print("Available Strategies:")
    for strat in load_strategy_index():
        print(f"- {strat['name']} ({strat['id']})")

    print("\nMomentum strategies:")
    for strat in list_strategies_by_tag("momentum"):
        print(f"  {strat['name']} — {strat['description']}")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():