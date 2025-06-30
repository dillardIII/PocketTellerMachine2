# === FILE: cole_brain.py ===
"""
Cole Brain:
Hybrid memory engine for PTM systems.
Tracks long-term and short-term memory, emotional states, strategies, and decision logs.
"""

import os
import json
from datetime import datetime
from pathlib import Path
from cole_logger import log_event

# === Paths ===
BRAIN_FILE = "data/cole_brain.json"          # Short-term memory
MEMORY_FILE = "data/cole_memory.json"        # Long-term event memory
Path("data").mkdir(parents=True, exist_ok=True)

# === Timestamp generator ===
def get_timestamp():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

# === SHORT-TERM STATE ===
def load_brain():
    if os.path.exists(BRAIN_FILE):
        try:
            with open(BRAIN_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_brain(data):
    with open(BRAIN_FILE, "w") as f:
        json.dump(data, f, indent=2)

def log_state(category, value):
    brain = load_brain()
    timestamp = get_timestamp()
    brain[category] = {
        "value": value,
        "updated": timestamp
    }
    save_brain(brain)
    print(f"[Brain] 🧠 Logged '{category}' to state.")

def get_last(category):
    brain = load_brain()
    return brain.get(category, {}).get("value")

def clear_state(category=None):
    brain = load_brain()
    if category:
        if category in brain:
            del brain[category]
            print(f"[Brain] 🧠 Cleared state: {category}")
        else:
            print(f"[Brain] ⚠️ Category '{category}' not found.")
    else:
        brain = {}
        print("[Brain] 🧠 Full state cleared.")
    save_brain(brain)

def get_brain_file():
    return BRAIN_FILE

# === LONG-TERM MEMORY ===
def init_memory():
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump([], f)

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)
            if not isinstance(memory, list):
                memory = []
            return memory
    except Exception as e:
        log_event("Cole Brain", f"❌ Failed to load memory: {e}", "error")
        return []

def log_memory(tag, data):
    memory = load_memory()
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "tag": tag,
        "data": data
    }
    memory.append(entry)
    try:
        with open(MEMORY_FILE, "w") as f:
            json.dump(memory, f, indent=2)
        log_event("Cole Brain", f"🧠 Logged memory: [{tag}] {str(data)[:100]}", "info")
    except Exception as e:
        log_event("Cole Brain", f"💾 Write error: {e}", "error")

def get_latest_memory(tag=None):
    memory = load_memory()
    if not memory:
        return None
    if tag:
        for entry in reversed(memory):
            if entry["tag"] == tag:
                return entry
        return None
    return memory[-1]

def wipe_memory():
    with open(MEMORY_FILE, "w") as f:
        json.dump([], f)
    log_event("Cole Brain", "🧽 All memory wiped.", "warning")

def get_memory_file():
    return MEMORY_FILE

# === Local Test ===
if __name__ == "__main__":
    init_memory()
    log_memory("strategy", {"name": "MACD", "score": 95})
    log_state("market_phase", "bullish")
    print("Latest Memory:", get_latest_memory("strategy"))
    print("Current Brain:", load_brain())