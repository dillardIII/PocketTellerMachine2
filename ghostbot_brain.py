from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import random
from datetime import datetime

from price_data import get_historical_prices
from indicators import calc_rsi, calc_sma
from brain_memory import load_brain_memory, save_brain_memory
from strategy_metadata import get_strategy_metadata
from recap_voice import speak_trade_recap

from trade_execution_engine import execute_trade
from trade_grader import grade_trade
from trade_logger import log_trade
from risk_guardian import is_trade_allowed, update_loss_streak
from market_schedule import is_market_open
from market_context import detect_market_context

BRAIN_LOG_FILE = "data/cole_brain_log.json"
BRAIN_MEMORY_FILE = "data/cole_brain_memory.json"

# === Context-Aware Strategy Grading ===
def update_brain_bias(strategy_name, result, context):
    memory = load_brain_memory()
    bias = memory.get("strategy_bias", {})

    if strategy_name not in bias:
        bias[strategy_name] = {
            "overall": {"wins": 0, "losses": 0},
            "bullish": {"wins": 0, "losses": 0},
            "bearish": {"wins": 0, "losses": 0},
            "sideways": {"wins": 0, "losses": 0}
        }

    for scope in ["overall", context]:
        if result == "win":
            bias[strategy_name][scope]["wins"] += 1
        elif result == "loss":
            bias[strategy_name][scope]["losses"] += 1

    memory["strategy_bias"] = bias
    save_brain_memory(memory)

# === Load Selected Assistant Persona ===
def get_selected_persona():
    try:
        with open("data/selected_persona.json", "r") as f:
            return json.load(f).get("persona", "Mo Cash")
    except:
        return "Mo Cash"

# === Core Thinking Logic ===
def ghostbot_think_and_trade(ticker="AAPL"):
    print(f"[GhostBot] Thinking about {ticker}...")

    # === Check Market Hours ===
    if not is_market_open():
        print("[GhostBot] Market is closed. No trade executed.")
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "event": "Market closed. No trade executed."
        }
        os.makedirs("data", exist_ok=True)
        if os.path.exists(BRAIN_LOG_FILE):
            with open(BRAIN_LOG_FILE, "r") as f:
                logs = json.load(f)
        else:
            logs = []

        logs.append(log_entry)

        with open(BRAIN_LOG_FILE, "w") as f:
            json.dump(logs, f, indent=2)
        return log_entry

    # === RiskGuardian: Check if trade is allowed ===:
    allowed, reason = is_trade_allowed()
    if not allowed:
        print(f"[RiskGuardian] Trade Blocked: {reason}")
        return {"status": "blocked", "reason": reason}

    # 1. Get recent price data
    prices = get_historical_prices(ticker)
    rsi = calc_rsi(prices)
    sma = calc_sma(prices)

    # 2. Select best strategy from memory bias
    all_strategies = get_strategy_metadata()
    strategy_scores = {}

    bias = load_brain_memory().get("strategy_bias", {})
    entry_price = round(prices[-1], 2)
    context = detect_market_context(rsi, sma, entry_price)

    for strat in all_strategies:
        name = strat["name"]
        wins = bias.get(name, {}).get(context, {}).get("wins", 0)
        losses = bias.get(name, {}).get(context, {}).get("losses", 0)
        score = wins - losses
        strategy_scores[name] = score

    # 3. Pick top strategy based on score
    if strategy_scores:
        best_strategy = max(strategy_scores, key=strategy_scores.get)
    else:
        best_strategy = all_strategies[0]["name"]  # fallback

    print(f"[GhostBot] Selected strategy: {best_strategy}")

    # === Simulate trade decision ===
    decision = "buy_call"
    qty = 1
    simulated_result = round(random.uniform(-100, 300), 2)
    outcome = "win" if simulated_result > 0 else "loss":
:
    # === Execute the Trade ===
    execution = execute_trade(
        strategy=best_strategy,
        ticker=ticker,
        side=decision,
        qty=qty,
        entry_price=entry_price
    )

    # === Grade the Trade ===
    grade = grade_trade(execution, result=simulated_result)

    # === Log Entry for Brain + Trade Log ===
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "ticker": ticker,
        "strategy": best_strategy,
        "action": decision,
        "entry": entry_price,
        "qty": qty,
        "rsi": rsi,
        "sma": sma,
        "result": outcome,
        "profit": simulated_result,
        "grade": grade
    }

    # === Log to Brain ===
    os.makedirs("data", exist_ok=True)
    if os.path.exists(BRAIN_LOG_FILE):
        with open(BRAIN_LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(log_entry)

    with open(BRAIN_LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

    # === Log Trade ===
    log_trade(log_entry)

    # === Update Bias with Market Context ===
    update_brain_bias(best_strategy, outcome, context)

    # === Update RiskGuardian Loss Tracker ===
    update_loss_streak(outcome)

    # === Speak Recap ===
    active_persona = get_selected_persona()
    speak_trade_recap(log_entry, speaker=active_persona)

    return log_entry

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():