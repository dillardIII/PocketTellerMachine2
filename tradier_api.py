# tradier_api.py

import requests
from tradier_config import TRADIER_API_KEY, TRADIER_ENDPOINT

def get_latest_price(symbol):
    """
    Fetch the most recent market price for a given symbol using Tradier's quotes endpoint.
    """
    url = f"{TRADIER_ENDPOINT}/markets/quotes"
    headers = {
        "Authorization": f"Bearer {TRADIER_API_KEY}",
        "Accept": "application/json"
    }
    params = {"symbols": symbol}
    resp = requests.get(url, headers=headers, params=params)
    data = resp.json()
    quote = data.get("quotes", {}).get("quote")
    if not quote:
        raise Exception("No quote data found for symbol.")
    # Handle both single and multi-symbol responses
    if isinstance(quote, list):
        price = quote[0].get("last")
    else:
        price = quote.get("last")
    return float(price)

def get_history_bars(symbol, interval="daily", limit=10):
    """
    Fetch historical OHLC bars for a symbol.
    """
    url = f"{TRADIER_ENDPOINT}/markets/history"
    headers = {
        "Authorization": f"Bearer {TRADIER_API_KEY}",
        "Accept": "application/json"
    }
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }
    resp = requests.get(url, headers=headers, params=params)
    data = resp.json()
    bars = data.get("history", {}).get("day", [])
    closes = [float(bar["close"]) for bar in bars if "close" in bar]
    return closes

def place_order(symbol, qty, side, order_type="market", duration="day"):
    """
    Place a trade order through Tradier.
    """
    account_number = "VA29130166"  # Use your sandbox or live account number
    url = f"{TRADIER_ENDPOINT}/accounts/{account_number}/orders"
    headers = {
        "Authorization": f"Bearer {TRADIER_API_KEY}",
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "class": "equity",
        "symbol": symbol,
        "side": side,          # "buy" or "sell"
        "quantity": qty,
        "type": order_type,    # "market", "limit", etc.
        "duration": duration   # "day", "gtc", etc.
    }
    resp = requests.post(url, headers=headers, data=payload)
    if resp.status_code != 200:
        raise Exception(f"Tradier API error: {resp.status_code} {resp.text}")
    return resp.json()