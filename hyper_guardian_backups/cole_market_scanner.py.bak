# cole_market_scanner.py

import asyncio
import json
import os
from price_data import get_current_rsi

# === Load Stock List Dynamically or fallback ===
def load_stock_list():
    filepath = "data/stock_list.json"
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            stock_list = json.load(f)
            print(f"[Cole Scanner] Loaded {len(stock_list)} stocks from stock_list.json.")
            return stock_list
    else:
        print("[Cole Scanner] stock_list.json not found. Using default stock list.")
        return [
            "AAPL", "TSLA", "GOOG", "MSFT", "AMZN", "NVDA", "META", "NFLX", "AMD", "INTC",
            "BA", "CRM", "CSCO", "DIS", "XOM", "PFE", "JNJ", "KO", "PEP", "WMT"
        ]

# === Async Scanner Task for One Symbol ===
async def scan_stock(symbol):
    await asyncio.sleep(0.1)  # Simulate API delay
    rsi = get_current_rsi(symbol)
    result = {
        "symbol": symbol,
        "rsi": rsi,
        "signal": "Buy" if rsi < 30 else "No action"
    }
    print(f"[Cole Scanner] {symbol}: RSI={rsi} => {result['signal']}")
    return result

# === Master Market Scanner ===
async def cole_market_scan():
    stock_list = load_stock_list()
    print(f"[Cole Scanner] Scanning {len(stock_list)} stocks...")
    tasks = [scan_stock(symbol) for symbol in stock_list]
    results = await asyncio.gather(*tasks)
    print("[Cole Scanner] Market scan complete.")
    return results

# === CLI Runner ===
if __name__ == "__main__":
    asyncio.run(cole_market_scan())