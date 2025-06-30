from ghost_env import INFURA_KEY, VAULT_ADDRESS
# train_stocks.py

import json
from brain import run_backtest_for_all_strategies, calculate_grade
from price_data import get_historical_prices
from datetime import datetime

UNIVERSE_FILE = "data/universe_tickers.json"
TRAINING_RESULTS = "data/stock_training_results.json"

def load_universe():
    with open(UNIVERSE_FILE, "r") as f:
        return json.load(f).get("tickers", [])

def log_result(result):
    try:
        with open(TRAINING_RESULTS, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(result)
    with open(TRAINING_RESULTS, "w") as f:
        json.dump(data[-500:], f, indent=2)

def run_full_stock_training():
    tickers = load_universe()
    print(f"[Stock Trainer] Starting backtest on {len(tickers)} stocks...")

    for symbol in tickers:
        try:
            print(f"[Stock Trainer] Backtesting {symbol}...")
            prices = get_historical_prices(symbol, days=90)
            if not prices:
                print(f"[Stock Trainer] No data for {symbol}")
                continue

            result = run_backtest_for_all_strategies(prices, symbol=symbol)
            result["grade"] = calculate_grade(result)
            log_result(result)

            print(f"[Stock Trainer] {symbol} - Grade: {result['grade']} | Return: {result['avg_return']} | Win Rate: {result['win_rate']}%")
        except Exception as e:
            print(f"[Stock Trainer] Error on {symbol}: {e}")

if __name__ == "__main__":
    run_full_stock_training()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():