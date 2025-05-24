import json
import os
from datetime import datetime

PHASE_STATE_FILE = "data/cole_phase_state.json"
PHASES = ["pre_market", "open_market", "midday", "closing", "after_hours"]

# === Get Current Phase ===
def get_current_phase():
    now = datetime.now().time()
    hour = now.hour

    if hour < 9:
        return "pre_market"
    elif 9 <= hour < 12:
        return "open_market"
    elif 12 <= hour < 15:
        return "midday"
    elif 15 <= hour < 16:
        return "closing"
    else:
        return "after_hours"

# === Phase-Based Task Filter ===
def phase_task_filter(tasks, current_phase):
    if not tasks:
        return []

    filtered = []
    for task in tasks:
        if current_phase in task.lower():
            filtered.append(task)
        elif current_phase == "pre_market" and "scan" in task.lower():
            filtered.append(task)
        elif current_phase == "after_hours" and "report" in task.lower():
            filtered.append(task)
        # Default: Allow all tasks for open market
        elif current_phase in ["open_market", "midday", "closing"]:
            filtered.append(task)

    return filtered

# === Save Current Phase (optional external trigger) ===
def save_current_phase():
    phase = get_current_phase()
    state = {
        "phase": phase,
        "timestamp": datetime.now().isoformat()
    }
    with open(PHASE_STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

# === Load Current Phase State ===
def load_phase_state():
    if os.path.exists(PHASE_STATE_FILE):
        with open(PHASE_STATE_FILE, "r") as f:
            return json.load(f)
    return {"phase": "unknown", "timestamp": None}

# === Auto Detect & Save Phase ===
def auto_detect_phase():
    current_phase = get_current_phase()
    save_current_phase()
    print(f"[Cole Phase Manager] Auto-detected and saved current phase: {current_phase}")
    return current_phase