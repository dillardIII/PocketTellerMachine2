from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json

FILTERS_FILE = "data/market_screener_filters.json"
SCREENER_SOURCE_FILE = "data/market_screener_data.json"
SCREENER_OUTPUT_FILE = "data/market_screener.json"

def load_filters():
    if os.path.exists(FILTERS_FILE):
        with open(FILTERS_FILE, "r") as f:
            return json.load(f)
    return {}

def load_screener_data():
    if os.path.exists(SCREENER_SOURCE_FILE):
        with open(SCREENER_SOURCE_FILE, "r") as f:
            return json.load(f).get("stocks", [])
    return []

def apply_filters(stocks, filters):
    def passes_filters(stock):
        # RSI Filter
        rsi_filter = filters.get("rsi", {})
        if rsi_filter.get("min") is not None and stock.get("rsi", 0) < rsi_filter["min"]:
            return False
        if rsi_filter.get("max") is not None and stock.get("rsi", 0) > rsi_filter["max"]:
            return False

        # Volume Filter
        volume_filter = filters.get("volume", {})
        if volume_filter.get("min") is not None and stock.get("volume", 0) < volume_filter["min"]:
            return False

        # Price Filter
        price_filter = filters.get("price", {})
        if price_filter.get("min") is not None and stock.get("price", 0) < price_filter["min"]:
            return False
        if price_filter.get("max") is not None and stock.get("price", 0) > price_filter["max"]:
            return False

        return True

    return [stock for stock in stocks if passes_filters(stock)]:
:
def process_market_screener():
    print("[Market Screener] Processing screener data...")

    filters = load_filters()
    stocks = load_screener_data()
    filtered_stocks = apply_filters(stocks, filters)

    output = {"results": filtered_stocks}

    with open(SCREENER_OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2)

    print(f"[Market Screener] Screener processed. {len(filtered_stocks)} results saved.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():