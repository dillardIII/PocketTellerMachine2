import os
import uuid
import json
import numpy as np
import requests
import warnings
from datetime import datetime
from collections import Counter
from price_data import get_historical_prices
from strategy_metadata import get_strategy_metadata

# === Suppress Warnings ===
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
warnings.filterwarnings('ignore', category=UserWarning, module='keras')

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
def calc_sma(prices, window=14):
    if len(prices) < window:
        return np.mean(prices) if prices else 0
    return np.mean(prices[-window:])

def calc_ema(prices, window=14):
    if len(prices) < window:
        return np.mean(prices) if prices else 0
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()
    ema = np.convolve(prices, weights, mode='valid')[-1]
    return ema

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

# === Strategy Simulations ===
def credit_spread(prices):
    entry = prices[-2]
    exit = prices[-1]
    return round(2.00 if exit >= entry else -1.00, 2)

def covered_call(prices):
    entry = prices[-2]
    exit = prices[-1]
    return round((exit - entry) + 1.50, 2)

def protective_put(prices):
    entry = prices[-2]
    exit = prices[-1]
    return round(max(entry - exit, 0) - 1.00, 2)

def iron_condor(prices):
    entry = prices[-2]
    exit = prices[-1]
    return round(1.50 if (entry - 5) <= exit <= (entry + 5) else -2.00, 2)

def basic_buy_sell(prices):
    entry = prices[-2]
    exit = prices[-1]
    return round(exit - entry, 2)

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

# === Trade Logger ===
def execute_trade(symbol, strategy, result, voice_summary=None):
    trade = {
        "id": str(uuid.uuid4()),
        "symbol": symbol,
        "strategy": strategy,
        "result": result,
        "grade": calculate_grade(result),
        "timestamp": datetime.now().isoformat(),
        "voice_summary": voice_summary or f"Trade executed using {strategy} on {symbol} with result ${result}."
    }
    trades = load_json(TRADES_FILE)
    trades.append(trade)
    save_json(TRADES_FILE, trades)
    return trade

def execute_option_trade(symbol, strategy, return_pct, voice_file=None, voice_summary=None):
    result = {
        "id": str(uuid.uuid4()),
        "ticker": symbol,
        "strategy": strategy,
        "return_pct": return_pct,
        "grade": calculate_grade(return_pct),
        "timestamp": datetime.now().isoformat(),
        "voice_file": voice_file,
        "voice_summary": voice_summary or f"Strategy {strategy} returned {return_pct}% on {symbol}."
    }
    results = load_json(BACKTEST_FILE)
    results.append(result)
    save_json(BACKTEST_FILE, results)
    return result

# === Option Strategy Selector ===
def select_option_strategy(prices):
    if not prices or len(prices) < 15:
        return "protective_put"
    entry = prices[-2]
    exit = prices[-1]
    sma = calc_sma(prices)
    rsi = calc_rsi(prices)

    trend = "neutral"
    if exit > sma and rsi > 60:
        trend = "bullish"
    elif exit < sma and rsi < 40:
        trend = "bearish"

    recent_range = max(prices[-5:]) - min(prices[-5:])
    volatility = "high" if recent_range > entry * 0.03 else "low"

    if trend == "bullish":
        if volatility == "high":
            return "debit_call_spread"
        elif rsi < 70:
            return "buy_call"
        else:
            return "credit_put_spread"
    elif trend == "bearish":
        if volatility == "high":
            return "debit_put_spread"
        elif rsi > 20:
            return "buy_put"
        else:
            return "credit_call_spread"
    elif trend == "neutral":
        return "iron_condor" if volatility == "low" else "straddle"

    return "covered_call"

# === Simulated Strategy Test ===
def simulate_strategy(prices, strategy_key):
    if len(prices) < 10:
        return None
    returns = []
    for i in range(10, len(prices)):
        past = prices[i - 10:i]
        if strategy_key == "sma_cross":
            sma_short = np.mean(past[-5:])
            sma_long = np.mean(past)
            profit = round(np.random.uniform(1, 5), 2) if sma_short > sma_long else round(np.random.uniform(-5, -1), 2)
        elif strategy_key == "rsi_reversal":
            changes = np.diff(past)
            gains = np.where(changes > 0, changes, 0)
            losses = np.where(changes < 0, -changes, 0)
            avg_gain = np.mean(gains)
            avg_loss = np.mean(losses)
            rs = avg_gain / avg_loss if avg_loss else 100
            rsi = 100 - (100 / (1 + rs))
            profit = round(np.random.uniform(1, 4), 2) if rsi < 30 else round(np.random.uniform(-4, -1), 2)
        else:
            profit = round(np.random.uniform(-3, 3), 2)
        returns.append(profit)
    return returns

# === Market-Wide Backtest ===
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
            outcome = simulate_strategy(prices, key)
            if outcome:
                all_returns.extend(outcome)

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

# === Export Functions ===
from cole_tools.brain_core import run_backtests_for_all_strategies, calculate_grade

__all__ = ["run_backtests_for_all_strategies", "calculate_grade"]