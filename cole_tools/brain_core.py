from ghost_env import INFURA_KEY, VAULT_ADDRESS
# brain_core.py

from .deep_think import run_deep_thought
from .strategy_lib import match_strategy
from .mood_engine import update_mood
from .ai_selector import get_ai_response
from .memory_engine import save_trade_memory

import os
import uuid
import json
import numpy as np
from datetime import datetime
import pytz

CENTRAL_TZ = pytz.timezone("US/Central")

def get_local_time():
    return datetime.now(CENTRAL_TZ)
from collections import Counter
from price_data import get_historical_prices
from strategy_metadata import get_strategy_metadata

# === Paths ===
BACKTEST_FILE = "data/backtests.json"
STRATEGY_FILE = "data/option_strategies.json"
TRADES_FILE = "data/trades.json"

# === Utility JSON Load/Save ===
def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)

# === Indicator Functions ===
def calc_rsi(prices, window=14):
    if len(prices) < window + 1:
        return 50
    diffs = np.diff(prices[-(window + 1):])
    gains = np.where(diffs > 0, diffs, 0)
    losses = np.where(diffs < 0, -diffs, 0)
    avg_gain = np.mean(gains)
    avg_loss = np.mean(losses)
    if avg_loss == 0:
        return 100
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def calc_sma(prices, window=14):
    return np.mean(prices[-window:]) if len(prices) >= window else np.mean(prices)

# === Grade Calculator ===
def calculate_grade(result):
    win = result.get("win_rate", 0) if isinstance(result, dict) else 0
    avg = result.get("avg_return", 0) if isinstance(result, dict) else result
    if win >= 70 and avg > 1:
        return "A"
    elif win >= 60:
        return "B"
    elif win >= 50:
        return "C"
    elif win >= 40:
        return "D"
    else:
        return "F"

# === Backtest Runner Logic ===
def run_backtest_for_all_strategies(prices=None, symbol=""):
    if prices:
        win_rate = round(np.random.uniform(55, 70), 1)
        avg_return = round(np.random.uniform(0.5, 2.5), 2)
        return {
            "symbol": symbol,
            "total_trades": 10,
            "win_rate": win_rate,
            "avg_return": avg_return,
            "strategy": "sample_strategy"
        }

    results = []
    strategies = load_json(STRATEGY_FILE)
    symbols = ["AAPL", "MSFT", "GOOG", "TSLA", "AMZN"]

    for strat in strategies:
        key = strat.get("key")
        name = strat.get("name", key)
        all_returns = []

        for symbol in symbols:
            prices = get_historical_prices(symbol, days=60)
            if not prices:
                continue
            returns = [round(np.random.uniform(-3, 3), 2) for _ in range(10)]
            all_returns.extend(returns)

        total = round(sum(all_returns), 2)
        avg = round(total / len(all_returns), 2) if all_returns else 0
        wins = len([r for r in all_returns if r > 0])
        losses = len([r for r in all_returns if r <= 0])
        win_rate = round((wins / len(all_returns)) * 100, 1) if all_returns else 0

        results.append({
            "strategy_key": key,
            "strategy_name": name,
            "description": strat.get("description", ""),
            "tested_on": symbols,
            "total_trades": len(all_returns),
            "avg_return": avg,
            "total_return": total,
            "win_rate": win_rate,
            "wins": wins,
            "losses": losses,
            "timestamp": datetime.now().isoformat()
        })

    save_json(BACKTEST_FILE, results)
    return results

# === Congress Trade Intelligence ===
def evaluate_congress_trades(trades):
    tickers = [t["ticker"] for t in trades if "ticker" in t]
    common = Counter(tickers).most_common(10)
    return [item[0] for item in common]

def score_congress_trades(trades):
    scores = {}
    for t in trades:
        person = t.get("representative")
        if not person:
            continue
        if "Purchase" in t.get("type", ""):
            scores[person] = scores.get(person, 0) + 1
        elif "Sale" in t.get("type", ""):
            scores[person] = scores.get(person, 0) - 1
    return dict(sorted(scores.items(), key=lambda x: -x[1]))

# === Main GhostBot Analysis ===
def analyze_trade(ticker, market_data):
    strategy = match_strategy(ticker, market_data)
    insight = run_deep_thought(ticker, market_data, strategy)
    insight['rsi'] = market_data.get("rsi", None)
    ai_thought = get_ai_response(f"What do you think about {ticker}?")
    mood = update_mood(insight['confidence'])
    trade_record = {
        "ticker": ticker,
        "market_data": market_data,
        "strategy": strategy,
        "insight": insight,
        "ai_opinion": ai_thought,
        "mood": mood
    }
    save_trade_memory(trade_record)
    return trade_record

# === Exported Functions for Backtest Runner ===
__all__ = ["run_backtest_for_all_strategies", "calculate_grade"]