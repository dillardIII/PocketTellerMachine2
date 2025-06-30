# tradier_api.py

import requests
import json
import os

class TradierAPI:
    def __init__(self, api_key, account_id="paper123", sandbox=True):
        self.api_key = api_key
        self.account_id = account_id
        self.base_url = "https://sandbox.tradier.com/v1" if sandbox else "https://api.tradier.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json"
        }
        self.portfolio_file = "data/paper_portfolio.json"
        self._init_portfolio_file()

    def _init_portfolio_file(self):
        if not os.path.exists(self.portfolio_file):
            with open(self.portfolio_file, "w") as f:
                json.dump({}, f)

    def get_quote(self, symbol):
        endpoint = f"{self.base_url}/markets/quotes"
        try:
            response = requests.get(endpoint, headers=self.headers, params={"symbols": symbol})
            return response.json().get("quotes", {}).get("quote", {})
        except Exception as e:
            print(f"[TradierAPI] Quote error: {e}")
            return {}

    def get_option_chain(self, symbol, expiration=None):
        endpoint = f"{self.base_url}/markets/options/chains"
        params = {"symbol": symbol}
        if expiration:
            params["expiration"] = expiration
        try:
            response = requests.get(endpoint, headers=self.headers, params=params)
            return response.json()
        except Exception as e:
            print(f"[TradierAPI] Option chain error: {e}")
            return {}

    def get_history(self, symbol, interval="daily", start=None, end=None):
        endpoint = f"{self.base_url}/markets/history"
        params = {"symbol": symbol, "interval": interval}
        if start: params["start"] = start
        if end: params["end"] = end
        try:
            response = requests.get(endpoint, headers=self.headers, params=params)
            return response.json()
        except Exception as e:
            print(f"[TradierAPI] History error: {e}")
            return {}

    # === PAPER TRADE LOGIC ===
    def paper_trade(self, symbol, action, quantity=1, price=None):
        quote = self.get_quote(symbol)
        market_price = price if price else float(quote.get("last", 0))
        side = action.lower()

        try:
            with open(self.portfolio_file, "r") as f:
                portfolio = json.load(f)
        except:
            portfolio = {}

        if side == "buy":
            portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        elif side == "sell":
            portfolio[symbol] = max(0, portfolio.get(symbol, 0) - quantity)

        with open(self.portfolio_file, "w") as f:
            json.dump(portfolio, f, indent=2)

        return {
            "action": side,
            "symbol": symbol,
            "quantity": quantity,
            "price": market_price,
            "status": "paper trade complete"
        }

    def get_paper_portfolio(self):
        try:
            with open(self.portfolio_file, "r") as f:
                portfolio = json.load(f)
        except:
            portfolio = {}

        result = {}
        for symbol, qty in portfolio.items():
            quote = self.get_quote(symbol)
            result[symbol] = {
                "quantity": qty,
                "last_price": float(quote.get("last", 0)),
                "value": round(qty * float(quote.get("last", 0)), 2)
            }
        return result

    # === OPTION STRATEGY BUILDER ===
    def build_option_strategy(self, symbol, legs):
        """
        legs = [
            {"action": "buy", "type": "call", "strike": 100, "expiration": "2025-06-21"},
            {"action": "sell", "type": "call", "strike": 110, "expiration": "2025-06-21"}
        ]
        """
        strategy = {"symbol": symbol, "legs": []}
        for leg in legs:
            strategy["legs"].append({
                "action": leg["action"],
                "option_type": leg["type"],
                "strike": leg["strike"],
                "expiration": leg["expiration"]
            })
        return strategy