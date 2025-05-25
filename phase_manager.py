# === FILE: phase_manager.py ===

import os
import json
import random

CURRENT_PHASE_FILE = "data/phase_state.json"
PHASES = ["startup", "calibration", "trading", "adjustment", "midday", "close", "afterhours"]

def get_current_phase():
    if not os.path.exists(CURRENT_PHASE_FILE):
        return "unknown"
    with open(CURRENT_PHASE_FILE, "r") as f:
        return json.load(f).get("phase", "unknown")

def set_phase(phase_name):
    if phase_name not in PHASES:
        print(f"[Phase Manager] Unknown phase: {phase_name}")
        return "unknown"

    os.makedirs("data", exist_ok=True)
    with open(CURRENT_PHASE_FILE, "w") as f:
        json.dump({"phase": phase_name}, f, indent=2)
    print(f"[Phase Manager] Phase set to: {phase_name}")
    return phase_name

def auto_detect_phase():
    trade_file = "data/trade_history.json"

    if not os.path.exists(trade_file):
        return set_phase("startup")

    try:
        with open(trade_file, "r") as f:
            trades = json.load(f)
    except Exception as e:
        print("[Phase Manager] Error reading trade history:", e)
        return set_phase("startup")

    if not trades:
        return set_phase("startup")

    wins = [t for t in trades if t.get("result", 0) > 0]
    losses = [t for t in trades if t.get("result", 0) <= 0]

    if len(trades) < 10:
        return set_phase("calibration")
    elif len(wins) > len(losses):
        return set_phase("trading")
    else:
        return set_phase("adjustment")

    # Fallback random detection if logic above doesn't cover it
    fallback_phase = random.choice(["midday", "close", "afterhours"])
    return set_phase(fallback_phase)