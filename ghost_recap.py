from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_recap.py ===

import os
import json
from datetime import datetime
from assistants.malik import malik_report

TRADE_LOG = "data/cole_trade_decision_log.json"
STRATEGY_GRADES_FILE = "data/strategy_grades.json"

# === Load Trade Log ===
def get_last_trade():
    if os.path.exists(TRADE_LOG):
        with open(TRADE_LOG, "r") as f:
            logs = json.load(f)
            if logs:
                return logs[-1]
    return None

# === Load Strategy Grades (Optional Enhancement) ===
def load_strategy_grades():
    if os.path.exists(STRATEGY_GRADES_FILE):
        with open(STRATEGY_GRADES_FILE, "r") as f:
            return json.load(f)
    return {}

# === GhostRecap Logic ===
def generate_ghostrecap():
    trade = get_last_trade()

    if not trade:
        print("[GhostRecap] No trade found.")
        return

    ticker = trade.get("ticker", "Unknown")
    confidence = trade.get("final_confidence", 0.0)
    result = trade.get("result", "unknown")
    action = trade.get("action", "n/a")
    pnl = trade.get("pnl", 0)
    strategy_name = trade.get("strategy", "Unlabeled Strategy")  # Optional field

    grades = load_strategy_grades()
    strategy_grade = grades.get(strategy_name, "C")

    recap = (
        f"Trade Recap: {ticker} | Action: {action} | Confidence: {confidence:.2f} | "
        f"Result: {result.upper()} | PnL: {pnl} | Strategy Grade: {strategy_grade}"
    )

    malik_report(recap)
    print(f"[GhostRecap] {recap}")

def log_event():ef drop_files_to_bridge():