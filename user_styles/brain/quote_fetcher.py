from ghost_env import INFURA_KEY, VAULT_ADDRESS
import requests
import os

TRADIER_TOKEN = os.getenv("TRADIER_API_KEY")
BASE_URL = "https://api.tradier.com/v1/markets/quotes"

def fetch_realtime_quote(symbol):
    headers = {
        "Authorization": f"Bearer {TRADIER_TOKEN}",
        "Accept": "application/json"
    }
    params = {"symbols": symbol.upper(), "greeks": "false"}

    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code != 200:
        return {"error": "Failed to fetch quote"}

    data = response.json()
    quote = data.get("quotes", {}).get("quote", {})
    return {
        "symbol": quote.get("symbol"),
        "last": quote.get("last"),
        "bid": quote.get("bid"),
        "ask": quote.get("ask"),
        "volume": quote.get("volume"),
        "timestamp": quote.get("trade_date")
    }