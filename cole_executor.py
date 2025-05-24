# === FILE: cole_executor.py ===

import os
import json
from datetime import datetime
from price_data import get_historical_prices
from indicators import calc_rsi

TRADE_HISTORY_FILE = "data/trade_history.json"
os.makedirs("data", exist_ok=True)

# === Run Strategy from File by Name ===
def run_trade_with_strategy(strategy_name):
    print(f"[Trade Executor] Running strategy: {strategy_name}")

    strategy_file = f"strategies/{strategy_name}.py"

    if not os.path.exists(strategy_file):
        print(f"[Trade Executor] Strategy file not found: {strategy_file}")
        return False

    try:
        with open(strategy_file, "r") as f:
            exec(f.read(), {})
        return True
    except Exception as e:
        print(f"[Trade Executor] Failed to run {strategy_name}: {e}")
        return False

# === Analyze Outcome of Strategy Using Indicators ===
def analyze_trade_result(strategy, symbol="AAPL"):
    prices = get_historical_prices(symbol)
    if not prices or len(prices) < 30:
        print("[Analyzer] Not enough price data.")
        return "neutral", 0

    rsi = calc_rsi(prices)

    # === RSI Reversal ===
    if strategy == "rsi_reversal":
        if rsi < 30:
            return "win", 120
        elif rsi > 70:
            return "loss", -90
        else:
            return "neutral", 0

    # === MACD Trend Follow ===
    if strategy == "macd_trend_follow":
        from indicators import calc_macd
        macd_line, signal_line, _ = calc_macd(prices)
        if macd_line > signal_line:
            return "win", 150
        elif macd_line < signal_line:
            return "loss", -100
        else:
            return "neutral", 0

    # === Bollinger Bounce ===
    if strategy == "bollinger_bounce":
        from indicators import calc_bollinger_bands
        lower, upper = calc_bollinger_bands(prices)
        current_price = prices[-1]
        if current_price <= lower:
            return "win", 130
        elif current_price >= upper:
            return "loss", -110
        else:
            return "neutral", 0

    return "neutral", 0

# === Log Trade Outcome to History File ===
def log_trade_outcome(strategy, result, profit=0, notes=""):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "strategy": strategy,
        "result": result,
        "profit": profit,
        "notes": notes
    }

    trades = []
    if os.path.exists(TRADE_HISTORY_FILE):
        with open(TRADE_HISTORY_FILE, "r") as f:
            try:
                trades = json.load(f)
            except:
                trades = []

    trades.append(entry)
    with open(TRADE_HISTORY_FILE, "w") as f:
        json.dump(trades[-500:], f, indent=2)

    print(f"[Trade Log] {strategy} - {result} - PnL: {profit}")