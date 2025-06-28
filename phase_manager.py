# === FILE: phase_manager.py ===
# 🎛️ PTM Phase Manager – Handles operational mode control across all modules

"""
Phase Manager:
Controls current operating phase of PTM (boot, autonomy, ui, bots).
Tracks lifecycle phases like startup, pre-market, active trading, cooldown, etc.
Saves phase in memory and persists to both disk and cole_brain memory.
"""

import os
import json
from datetime import datetime
from pathlib import Path
from cole_logger import log_event
from cole_brain import log_state, get_last

# === Valid lifecycle phases ===
VALID_PHASES = [
    "startup",
    "pre_market",
    "active_trading",
    "post_market",
    "cooldown",
    "offline",
    "boot",
    "autonomy",
    "ui",
    "bots"
]

# === File Paths ===
CURRENT_PHASE_FILE = "state/ptm_phase.json"
PHASE_HISTORY_FILE = "brain/ptm_phase.json"
FALLBACK_PHASE_FILE = "data/phase.txt"

# === In-memory phase flags ===
phase_state = {phase: False for phase in VALID_PHASES}

def ensure_phase_dirs():
    Path("state").mkdir(parents=True, exist_ok=True)
    Path("brain").mkdir(parents=True, exist_ok=True)
    Path("data").mkdir(parents=True, exist_ok=True)

def set_phase(phase):
    """
    Set the current PTM phase.
    Logs to cole_brain and cole_logger.
    Persists to both state and historical backup.
    Also supports basic fallback file for simple modules.
    """
    ensure_phase_dirs()

    if phase not in VALID_PHASES:
        log_event("Phase Manager", f"❌ Invalid phase: '{phase}'", "error")
        return

    for key in phase_state:
        phase_state[key] = (key == phase)

    with open(CURRENT_PHASE_FILE, "w", encoding="utf-8") as f:
        json.dump({"phase": phase}, f)

    with open(PHASE_HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump({"phase": phase, "timestamp": datetime.utcnow().isoformat()}, f, indent=2)

    with open(FALLBACK_PHASE_FILE, "w", encoding="utf-8") as f:
        f.write(phase)

    log_state("phase", phase)
    log_event("Phase Manager", f"🔄 Phase set to: {phase}", "info")

def get_phase():
    """
    Get the current PTM phase.
    Tries full JSON, then in-memory, then fallback txt, then brain memory.
    """
    if os.path.exists(CURRENT_PHASE_FILE):
        try:
            with open(CURRENT_PHASE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                phase = data.get("phase", "undefined")
                for key in phase_state:
                    phase_state[key] = (key == phase)
                return phase
        except Exception as e:
            log_event("Phase Manager", f"⚠️ Failed to read phase from file: {e}", "warning")

    for key, active in phase_state.items():
        if active:
            return key

    if os.path.exists(FALLBACK_PHASE_FILE):
        try:
            with open(FALLBACK_PHASE_FILE, "r", encoding="utf-8") as f:
                return f.read().strip()
        except Exception as e:
            log_event("Phase Manager", f"⚠️ Failed to read fallback phase.txt: {e}", "warning")

    brain_phase = get_last("phase")
    if brain_phase:
        return brain_phase

    log_event("Phase Manager", "⚠️ Phase unknown. Defaulting to 'startup'.", "warning")
    return "startup"

def is_phase(active_phase):
    return get_phase() == active_phase

def log_phase_transition(prev, new):
    print(f"[PHASE TRANSITION] {prev} → {new}")

# === Manual Test ===
if __name__ == "__main__":
    print("🟡 Current Phase:", get_phase())
    set_phase("active_trading")
    print("🟢 Updated Phase:", get_phase())