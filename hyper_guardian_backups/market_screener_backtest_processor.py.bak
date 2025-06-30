import os
import json
from datetime import datetime

BACKTEST_LOG_FILE = "data/market_backtest_logs.json"
SCREENER_DATA_FILE = "data/market_screener_data.json"
FILTERS_FILE = "data/screener_filters.json"

# === Load Screener Filters ===
def load_screener_filters():
    if os.path.exists(FILTERS_FILE):
        with open(FILTERS_FILE, "r") as f:
            return json.load(f)
    return {}

# === Load Screener Data ===
def load_screener_data():
    if os.path.exists(SCREENER_DATA_FILE):
        with open(SCREENER_DATA_FILE, "r") as f:
            return json.load(f).get("results", [])
    return []

# === Save Backtest Log ===
def save_backtest_log(log_entry):
    logs = []
    if os.path.exists(BACKTEST_LOG_FILE):
        with open(BACKTEST_LOG_FILE, "r") as f:
            logs = json.load(f).get("logs", [])

    logs.append(log_entry)
    with open(BACKTEST_LOG_FILE, "w") as f:
        json.dump({"logs": logs[-500:]}, f, indent=2)  # Keep only latest 500 logs

# === Backtest Screener Logic ===
def run_screener_backtest():
    screener_data = load_screener_data()
    filters = load_screener_filters()

    print(f"[Backtest] Running backtest on {len(screener_data)} screener results...")

    for stock in screener_data:
        result = backtest_signal_logic(stock, filters)
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ticker": stock["ticker"],
            "price": stock["price"],
            "volume": stock["volume"],
            "rsi": stock["rsi"],
            "signal": stock["signal"],
            "result": result
        }
        save_backtest_log(log_entry)

# === Example Signal Logic ===
def backtest_signal_logic(stock, filters):
    if stock["rsi"] < 30 and stock["volume"] > 1000000:
        return "BUY Signal Passed"
    elif stock["rsi"] > 70 and stock["volume"] > 1000000:
        return "SELL Signal Passed"
    else:
        return "No Action"

# === CLI Test Mode ===
if __name__ == "__main__":
    run_screener_backtest()