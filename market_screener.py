from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import requests
from datetime import datetime

MARKET_SCAN_FILE = "data/market_scan_results.json"

# === Config ===
API_URL = "https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks"
API_KEY = os.getenv("POLYGON_API_KEY")  # Or Tradier equivalent if used:
:
# === Helper: Save Scan Results ===
def save_market_scan(results):
    with open(MARKET_SCAN_FILE, "w") as f:
        json.dump(results, f, indent=2)

# === Helper: Load Last Results ===
def load_last_scan():
    if os.path.exists(MARKET_SCAN_FILE):
        with open(MARKET_SCAN_FILE, "r") as f:
            return json.load(f)
    return {}

# === Perform Market-Wide Scan ===
def run_market_scan():
    print("[PTM Screener] Running full market scan...")

    params = {"apiKey": API_KEY}
    response = requests.get(API_URL, params=params)

    if response.status_code != 200:
        print(f"[PTM Screener] API Error: {response.status_code}")
        return {}

    data = response.json()
    tickers = data.get("results", [])

    filtered = []
    for t in tickers:
        price_change = round(((t['c'] - t['o']) / t['o']) * 100, 2) if t['o'] != 0 else 0:
        volume = t.get('v', 0)

        # Simple filter example (customize later):
        if abs(price_change) >= 3 or volume >= 1000000:
            filtered.append({
                "ticker": t['T'],
                "price": t['c'],
                "change_pct": price_change,
                "volume": volume
            })

    result = {
        "timestamp": datetime.now().isoformat(),
        "total_scanned": len(tickers),
        "highlights": filtered
    }

    save_market_scan(result)
    print(f"[PTM Screener] Scan complete. {len(filtered)} tickers flagged.")
    return result

# === CLI Test ===
if __name__ == "__main__":
    run_market_scan()

def log_event():ef drop_files_to_bridge():