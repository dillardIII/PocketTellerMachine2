# === FILE: phase_manager.py ===

import os
import json

CURRENT_PHASE_FILE = "data/phase_state.json"

def get_current_phase():
    if not os.path.exists(CURRENT_PHASE_FILE):
        return "unknown"
    with open(CURRENT_PHASE_FILE, "r") as f:
        return json.load(f).get("phase", "unknown")

def set_phase(phase_name):
    os.makedirs("data", exist_ok=True)
    with open(CURRENT_PHASE_FILE, "w") as f:
        json.dump({"phase": phase_name}, f, indent=2)
    print(f"[Phase Manager] Phase set to: {phase_name}")
    return phase_name

def auto_detect_phase():
    if not os.path.exists("data/trade_history.json"):
        return set_phase("startup")

    try:
        with open("data/trade_history.json", "r") as f:
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