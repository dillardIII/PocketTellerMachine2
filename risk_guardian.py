import os
import json
from datetime import datetime, timedelta

TRADE_LOG = "data/trades.json"
GUARDIAN_STATE = "data/risk_guardian_state.json"

DEFAULTS = {
    "max_open_trades": 10,
    "max_loss_streak": 3,
    "cooldown_minutes": 20,
    "active_loss_streak": 0,
    "last_loss_time": None
}

def load_guardian_state():
    if not os.path.exists(GUARDIAN_STATE):
        return DEFAULTS.copy()
    with open(GUARDIAN_STATE, "r") as f:
        return json.load(f)

def save_guardian_state(state):
    with open(GUARDIAN_STATE, "w") as f:
        json.dump(state, f, indent=2)

# === Risk Gatekeeper ===
def is_trade_allowed():
    state = load_guardian_state()

    # === Cooldown timer ===
    last_loss = state.get("last_loss_time")
    if last_loss:
        last_time = datetime.fromisoformat(last_loss)
        if datetime.now() < last_time + timedelta(minutes=state["cooldown_minutes"]):
            return False, "Cooldown active due to loss streak."

    # === Max trade check ===
    if os.path.exists(TRADE_LOG):
        with open(TRADE_LOG, "r") as f:
            trades = json.load(f)
        open_trades = [t for t in trades if t.get("status") != "closed"]
        if len(open_trades) >= state["max_open_trades"]:
            return False, "Too many open trades."

    return True, "Trade approved."

# === Update after trade result ===
def update_loss_streak(result):
    state = load_guardian_state()

    if result == "loss":
        state["active_loss_streak"] += 1
        state["last_loss_time"] = datetime.now().isoformat()
    else:
        state["active_loss_streak"] = 0
        state["last_loss_time"] = None

    if state["active_loss_streak"] >= state["max_loss_streak"]:
        state["last_loss_time"] = datetime.now().isoformat()
        print(f"[RiskGuardian] Loss streak triggered cooldown.")

    save_guardian_state(state)