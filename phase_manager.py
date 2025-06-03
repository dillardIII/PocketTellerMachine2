# === FILE: phase_manager.py ===
# 🎛️ Phase Manager – Controls current operating phase of PTM (boot, autonomy, ui, bots)
# Supports both in-memory state and persistent JSON file tracking

import json
import os
from pathlib import Path

CURRENT_PHASE_FILE = "state/ptm_phase.json"

# === In-memory tracker ===
phase_state = {
    "boot": False,
    "autonomy": False,
    "bots": False,
    "ui": False
}

# === Persistent storage setter ===
def set_phase(phase):
    # Update memory state
    for key in phase_state:
        phase_state[key] = False
    if phase in phase_state:
        phase_state[phase] = True
    else:
        print(f"[PhaseManager] ⚠️ Unknown phase: {phase}")

    # Save to disk
    Path("state").mkdir(parents=True, exist_ok=True)
    with open(CURRENT_PHASE_FILE, "w", encoding="utf-8") as f:
        json.dump({"phase": phase}, f)

    print(f"[PhaseManager] 🌕 Phase set to: {phase}")

# === Phase fetcher ===
def get_phase():
    # Load from disk first
    if os.path.exists(CURRENT_PHASE_FILE):
        with open(CURRENT_PHASE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            phase = data.get("phase", "undefined")
            # Update memory state
            for key in phase_state:
                phase_state[key] = (key == phase)
            return phase

    # Fallback to in-memory state
    for key, active in phase_state.items():
        if active:
            return key
    return "unknown"