from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from datetime import datetime
import pytz

CENTRAL_TZ = pytz.timezone("US/Central")

def get_local_time():
    return datetime.now(CENTRAL_TZ)

# === Fixed import from correct folder ===
from cole_tools.brain import run_backtest_for_all_strategies, calculate_grade
from price_data import get_historical_prices

RESULTS_FILE = "data/backtest_training_log.json"
SYMBOLS = ["AAPL", "MSFT", "GOOG", "TSLA", "AIZN", "NVDA", "META", "NFLX", "OKTA", "MCD", "AMZN", "F", "SPY", "QQQ"]

def save_results(result):
    os.makedirs("data", exist_ok=True)
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []
    logs.append(result)
    with open(RESULTS_FILE, "w") as f:
        json.dump(logs[-1000:], f, indent=2)

def run_backtest_loop():
    print("[BacktestRunner] Starting market-wide strategy training...")
    for symbol in SYMBOLS:
        prices = get_historical_prices(symbol)
        if not prices:
            print(f"[BacktestRunner] No data for {symbol}, skipping.")
            continue
        print(f"[BacktestRunner] Running backtests for {symbol}...")
        result = run_backtests_for_all_strategies(symbol, prices)
        result["symbol"] = symbol
        result["timestamp"] = datetime.now().isoformat()
        result["grade"] = calculate_grade(result)
        save_results(result)

    print("[BacktestRunner] Training complete.")

if __name__ == "__main__":
    run_backtest_loop()