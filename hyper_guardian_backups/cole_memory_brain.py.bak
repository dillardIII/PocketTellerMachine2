import json
import os
from datetime import datetime

MEMORY_FILE = "data/cole_memory.json"

# === Load Entire Memory ===
def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {"trades": [], "strategies": [], "hybrids": [], "journals": [], "patterns": {}}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

# === Save Entire Memory ===
def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

# === Log Generic Memory Event (Trades, Strategies, Hybrids, Journals) ===
def log_memory_event(event_type, data):
    memory = load_memory()
    if event_type in memory:
        memory[event_type].append(data)
    else:
        memory[event_type] = [data]
    save_memory(memory)
    print(f"[MEMORY LOGGED]: {event_type} → {data.get('id', 'No ID')}")

# === Log Pattern Observation (Mistakes, Notes, Insights) ===
def log_pattern_observation(pattern_name, note):
    memory = load_memory()
    if "patterns" not in memory:
        memory["patterns"] = {}
    if pattern_name not in memory["patterns"]:
        memory["patterns"][pattern_name] = []
    memory["patterns"][pattern_name].append({
        "note": note,
        "timestamp": datetime.now().isoformat()
    })
    save_memory(memory)
    print(f"[PATTERN OBSERVED]: {pattern_name} → {note}")

# === Example: Logging a trade into memory ===
example_trade = {
    "id": "trade001",
    "symbol": "AAPL",
    "strategy": "covered_call",
    "result": 22.5,
    "grade": "B",
    "timestamp": datetime.now().isoformat()
}

log_memory_event("trades", example_trade)

# === Example: Logging a pattern observation ===
log_pattern_observation("RSI Reversal", "Fails during high volatility markets. Needs filters.")