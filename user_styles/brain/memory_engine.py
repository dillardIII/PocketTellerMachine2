# memory_engine.py

import json
from datetime import datetime
import pytz

CENTRAL_TZ = pytz.timezone("US/Central")

def get_local_time():
    return datetime.now(CENTRAL_TZ)
import os

# Path to where trade memory will be stored
MEMORY_PATH = "logs/trade_memory.json"

# --- Load all recorded trades ---
def load_memory():
    if not os.path.exists(MEMORY_PATH):
        return []
    with open(MEMORY_PATH, "r") as f:
        return json.load(f)

# --- Save a single trade record ---
def save_trade_memory(trade):
    memory = load_memory()
    trade['timestamp'] = datetime.now().isoformat()
    memory.append(trade)

    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=2)

# --- Count how many times a strategy was used ---
def count_strategy_usage(strategy_name):
    memory = load_memory()
    return len([t for t in memory if t.get("strategy", {}).get("name") == strategy_name])

# --- Count wins based on confidence threshold ---
def count_strategy_wins(strategy_name, threshold=0.75):
    memory = load_memory()
    return len([
        t for t in memory
        if t.get("strategy", {}).get("name") == strategy_name
        and t.get("insight", {}).get("confidence", 0) >= threshold
    ])

# --- Retrieve recent N trades ---
def get_recent_trades(limit=10):
    memory = load_memory()
    return memory[-limit:]