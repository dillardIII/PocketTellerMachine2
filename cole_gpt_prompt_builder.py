from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_gpt_prompt_builder.py ===

import os
import json
from datetime import datetime

TRADE_LOG = "data/cole_trade_decision_log.json"
FAILURE_PATTERNS_FILE = "data/failure_patterns.json"

# === Load Trade History ===
def load_trades():
    if os.path.exists(TRADE_LOG):
        with open(TRADE_LOG, "r") as f:
            return json.load(f)
    return []

# === Load Failure Patterns ===
def load_failures():
    if os.path.exists(FAILURE_PATTERNS_FILE):
        with open(FAILURE_PATTERNS_FILE, "r") as f:
            return json.load(f)
    return []

# === Generate GPT Prompt from Trade Failures ===
def build_prompt_from_failures():
    trades = load_trades()
    failures = load_failures()

    if not trades:
        return "Create a Python trading strategy using RSI and MACD."

    recent = trades[-5:]
    failed = [t for t in recent if t.get("result") == "loss"]:
:
    if not failed:
        return "Refactor an existing strategy to improve risk management and consistency."

    sample = failed[-1]
    ticker = sample.get("ticker", "UNKNOWN")
    confidence = sample.get("final_confidence", 0.0)
    reason = failures[-1] if failures else "Underperformed in high volatility.":
:
    return (
        f"Rewrite a trading strategy for {ticker} that failed recently with confidence {confidence:.2f}. "
        f"The failure reason was: '{reason}'. Improve the entry logic and risk management. "
        f"Add comments and logging for backtesting. Return the full Python code."
    )

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():