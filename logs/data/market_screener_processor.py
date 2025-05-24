import os
import json

SCREENER_DATA_FILE = "data/market_screener.json"
FILTERS_FILE = "data/screener_filters.json"

def process_market_screener():
    if not os.path.exists(SCREENER_DATA_FILE):
        print("[Market Screener] Data file not found.")
        return []

    with open(SCREENER_DATA_FILE, "r") as f:
        screener_data = json.load(f)

    filters = load_screener_filters()

    filtered_results = []
    for stock in screener_data:
        if not passes_filters(stock, filters):
            continue
        filtered_results.append(stock)

    with open("data/market_screener_filtered.json", "w") as f:
        json.dump(filtered_results, f, indent=2)

    print(f"[Market Screener] Processed {len(filtered_results)} results after filters.")

def load_screener_filters():
    if os.path.exists(FILTERS_FILE):
        with open(FILTERS_FILE, "r") as f:
            return json.load(f)
    return {}

def passes_filters(stock, filters):
    # RSI filter
    rsi = stock.get("rsi", 0)
    if "rsi" in filters:
        if filters["rsi"].get("min") is not None and rsi < filters["rsi"]["min"]:
            return False
        if filters["rsi"].get("max") is not None and rsi > filters["rsi"]["max"]:
            return False

    # Volume filter
    volume = stock.get("volume", 0)
    if "volume" in filters and filters["volume"].get("min") is not None:
        if volume < filters["volume"]["min"]:
            return False

    # Price filter
    price = stock.get("price", 0)
    if "price" in filters:
        if filters["price"].get("min") is not None and price < filters["price"]["min"]:
            return False
        if filters["price"].get("max") is not None and price > filters["price"]["max"]:
            return False

    return True