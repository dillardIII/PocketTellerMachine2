# tradier_module.py

import requests

class TradierClient:
    def __init__(self, api_key, sandbox=True):
        self.api_key = api_key
        # Use sandbox.tradier.com for paper trading, api.tradier.com for live
        self.base_url = "https://sandbox.tradier.com/v1" if sandbox else "https://api.tradier.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json"
        }

    def get_quote(self, symbol):
        """
        Gets the latest quote for a given symbol.
        """
        endpoint = f"{self.base_url}/markets/quotes"
        params = {"symbols": symbol}
        response = requests.get(endpoint, headers=self.headers, params=params)
        if response.status_code == 200:
            return response.json()["quotes"]["quote"]
        else:
            print(f"Error getting quote: {response.status_code} - {response.text}")
            return None

    def place_order(self, symbol, action, qty=1, paper=True):
        """
        Places a trade order. Default is paper trading in sandbox.
        """
        endpoint = f"{self.base_url}/accounts/YOUR_ACCOUNT_NUMBER/orders"
        data = {
            "class": "equity",
            "symbol": symbol,
            "side": action.lower(),  # "buy" or "sell"
            "quantity": qty,
            "type": "market",
            "duration": "gtc"  # Good 'til canceled
        }
        response = requests.post(endpoint, headers=self.headers, data=data)
        if response.status_code in [200, 201]:
            print(f"Order placed: {action.upper()} {qty} shares of {symbol}")
            return response.json()
        else:
            print(f"Error placing order: {response.status_code} - {response.text}")
            return None