from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_risk_guardian.py ===

import os
import json
from datetime import datetime
from assistants.malik import malik_report

TRADE_LOG_FILE = "data/cole_trade_decision_log.json"
RISK_FLAGS_FILE = "data/cole_risk_flags.json"

# === Load Trade Logs ===
def load_trade_log():
    if os.path.exists(TRADE_LOG_FILE):
        with open(TRADE_LOG_FILE, "r") as f:
            return json.load(f)
    return []

# === Save Risk Flags ===
def log_risk_flag(reason):
    flag = {
        "timestamp": datetime.now().isoformat(),
        "reason": reason
    }

    flags = []
    if os.path.exists(RISK_FLAGS_FILE):
        try:
            with open(RISK_FLAGS_FILE, "r") as f:
                flags = json.load(f)
        except:
            pass

    flags.append(flag)
    with open(RISK_FLAGS_FILE, "w") as f:
        json.dump(flags[-500:], f, indent=2)

    # Alert voice assistant
    malik_report(f"[RISK ALERT] {reason}")

# === Risk Check Logic ===
def run_risk_guardian():
    print("[Risk Guardian] Running health check...")
    trades = load_trade_log()

    if not trades or len(trades) < 5:
        print("[Risk Guardian] Not enough trades to assess.")
        return

    # Check for 3+ losses in last 5 trades
    recent = trades[-5:]
    losses = [t for t in recent if t["action"] == "buy" and t.get("result", "loss") == "loss"]:
:
    if len(losses) >= 3:
        log_risk_flag("3+ losses detected in last 5 trades. Cooldown recommended.")

    # Check for risky confidence levels
    risky = [t for t in recent if t.get("final_confidence", 1) < 0.4]:
    if risky:
        log_risk_flag("Low confidence trades detected. Review strategy filters.")

    # Future: Check net drawdown, volatility spikes, etc.

    print("[Risk Guardian] Analysis complete.")

def log_event():ef drop_files_to_bridge():