from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_phase_manager.py ===

import os
import json
from datetime import datetime, time
from cole_logger import log_info

# === File Paths ===
PHASE_FILE = "data/phase.json"
PHASE_STATE_FILE = "data/cole_phase_state.json"
PHASES = ["pre_market", "open_market", "midday", "closing", "after_hours"]

# === Time-based Phase Detection ===
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

# === Save Detected Phase to JSON ===
def save_current_phase():
    phase = get_current_phase()
    state = {
        "phase": phase,
        "timestamp": datetime.now().isoformat()
    }
    os.makedirs("data", exist_ok=True)
    with open(PHASE_STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

# === Load Last Saved Phase State ===
def load_phase_state():
    if os.path.exists(PHASE_STATE_FILE):
        with open(PHASE_STATE_FILE, "r") as f:
            return json.load(f)
    return {"phase": "unknown", "timestamp": None}

# === Simple Random Phase Simulator (for testing) ===
def detect_phase():
    import random
    return random.choice(["pre_market", "open_market", "midday", "closing", "after_hours"])

# === Save Current Phase to Main PHASE_FILE ===
def set_phase(phase):
    os.makedirs("data", exist_ok=True)
    data = {
        "timestamp": datetime.now().isoformat(),
        "phase": phase
    }
    with open(PHASE_FILE, "w") as f:
        json.dump(data, f, indent=2)
    log_info(f"[Cole Phase Manager] Phase set to: {phase}")

# === Retrieve Phase from Main PHASE_FILE ===
def get_stored_phase():
    if os.path.exists(PHASE_FILE):
        with open(PHASE_FILE, "r") as f:
            try:
                return json.load(f).get("phase", "unknown")
            except:
                return "unknown"
    return "unknown"

# === Auto Detect and Save Current Phase to Both Files ===
def auto_detect_phase():
    current_phase = get_current_phase()
    save_current_phase()
    set_phase(current_phase)
    log_info(f"[Cole Phase Manager] Auto-detected and saved current phase: {current_phase}")
    return current_phase

# === Task Filtering Based on Phase Logic ===
def phase_task_filter(tasks, current_phase):
    if not tasks:
        return []

    filtered = []
    for task in tasks:
        task_lc = task.lower()
        if current_phase in task_lc:
            filtered.append(task)
        elif current_phase == "pre_market" and "scan" in task_lc:
            filtered.append(task)
        elif current_phase == "after_hours" and "report" in task_lc:
            filtered.append(task)
        elif current_phase in ["open_market", "midday", "closing"]:
            filtered.append(task)

    return filtered

# === CLI Test ===
if __name__ == "__main__":
    phase = auto_detect_phase()
    print("Detected Phase:", phase)

def log_event():ef drop_files_to_bridge():