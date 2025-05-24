import os
import json
from datetime import datetime
from price_data import get_historical_prices
from indicators import calc_rsi, calc_sma
from brain import evaluate_option_strategy

# === File Paths ===
BACKTEST_LOG_FILE = "data/market_backtest_logs.json"
RESULTS_FILE = "data/market_backtest_results.json"

# === Load Option Strategies ===
def load_strategies():
    with open("data/option_strategies.json", "r") as f:
        return json.load(f)

# === Run Backtest for a Single Strategy ===
def backtest_strategy(strategy_name, symbol, prices):
    strategy = evaluate_option_strategy(strategy_name, prices)
    return {
        "symbol": symbol,
        "strategy": strategy_name,
        "result": strategy.get("result", "neutral"),
        "details": strategy
    }

# === Run Full Backtest ===
def run_backtest(symbols):
    strategies = load_strategies()
    logs = []
    results = {}

    for symbol in symbols:
        prices = get_historical_prices(symbol)
        if not prices:
            continue

        results[symbol] = {}

        for strategy_name in strategies.keys():
            outcome = backtest_strategy(strategy_name, symbol, prices)
            logs.append(outcome)
            results[symbol][strategy_name] = outcome["result"]

    # Save logs
    save_backtest_logs(logs)
    save_backtest_results(results)

    return logs, results

# === Save Backtest Logs ===
def save_backtest_logs(logs):
    os.makedirs("data", exist_ok=True)
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "logs": logs
    }
    with open(BACKTEST_LOG_FILE, "w") as f:
        json.dump(log_data, f, indent=2)

# === Save Summary Results ===
def save_backtest_results(results):
    os.makedirs("data", exist_ok=True)
    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=2)

# === Run if executed directly ===
if __name__ == "__main__":
    test_symbols = ["AAPL", "TSLA", "MSFT", "NVDA"]
    run_backtest(test_symbols)