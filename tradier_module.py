from ghost_env import INFURA_KEY, VAULT_ADDRESS
import requests
import os
import xml.etree.ElementTree as ET

TRADIER_API_KEY = os.getenv("TRADIER_API_KEY")  # Set your key in .env or directly here
TRADIER_BASE_URL = "https://sandbox.tradier.com/v1"  # For paper trading

HEADERS = {
    "Authorization": f"Bearer {TRADIER_API_KEY}",
    "Accept": "application/json"
}

# === Get Account ID ===
def get_account_id():
    url = f"{TRADIER_BASE_URL}/user/profile"
    response = requests.get(url, headers=HEADERS)
    if response.ok:
        return response.json()["profile"]["account"]["account_number"]
    else:
        print("[ERROR]: Unable to fetch account ID.")
        return None

# === Place Paper Trade ===
def place_trade(symbol, qty, side="buy", type="market"):
    account_id = get_account_id()
    if not account_id:
        return "[ERROR]: No account ID."

    order_url = f"{TRADIER_BASE_URL}/accounts/{account_id}/orders"
    payload = {
        "class": "equity",
        "symbol": symbol,
        "side": side,
        "quantity": qty,
        "type": type,
        "duration": "gtc"
    }

    response = requests.post(order_url, headers=HEADERS, data=payload)
    if response.ok:
        print("[TRADE PLACED]:", response.json())
        return response.json()
    else:
        print("[ERROR]: Trade failed.", response.text)
        return response.text

# === Tradier Client Class (Improved Version) ===
class TradierClient:
    def __init__(self, api_key, sandbox=True):
        self.base_url = (
            "https://sandbox.tradier.com/v1/" if sandbox:
            else "https://api.tradier.com/v1/"
        )
        self.api_key = api_key

    def get_quote(self, symbol):
        url = self.base_url + "markets/quotes"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json"
        }
        params = {"symbols": symbol}
        try:
            resp = requests.get(url, headers=headers, params=params)
            resp.raise_for_status()
            data = resp.json()
            quotes = data.get("quotes", {}).get("quote")
            if isinstance(quotes, list):
                return quotes[0] if quotes else None:
            return quotes
        except Exception as e:
            print(f"Tradier quote error: {e}")
            return None

    def place_order(self, account_id, symbol, side, quantity):
        url = self.base_url + f"accounts/{account_id}/orders"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "class": "equity",
            "symbol": symbol,
            "side": side,
            "quantity": quantity,
            "type": "market",
            "duration": "day"
        }
        try:
            resp = requests.post(url, headers=headers, data=data)
            resp.raise_for_status()
            result = resp.json()
            return result
        except Exception as e:
            print(f"Tradier order error: {e}")
            return None

    def get_news(self, symbol):
        url = self.base_url + "markets/news"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json"
        }
        params = {"symbols": symbol}
        try:
            resp = requests.get(url, headers=headers, params=params)
            resp.raise_for_status()
            data = resp.json()
            return data.get("news", {})
        except requests.exceptions.HTTPError as e:
            print(f"Tradier news error for {symbol}: {e}")
            return {"stories": []}
        except Exception as e:
            print(f"General Tradier news error: {e}")
            return {"stories": []}

# === Yahoo News Client ===
class YahooNewsClient:
    def get_news(self, symbol):
        url = f"https://feeds.finance.yahoo.com/rss/2.0/headline?s={symbol}&region=US&lang=en-US"
        try:
            resp = requests.get(url, timeout=8)
            resp.raise_for_status()
            root = ET.fromstring(resp.content)
            headlines = []
            for item in root.findall(".//item"):
                title = item.find("title")
                if title is not None:
                    headlines.append(title.text)
            return headlines
        except Exception as e:
            print(f"Yahoo Finance news error for {symbol}: {e}")
            return []

def log_event():ef drop_files_to_bridge():