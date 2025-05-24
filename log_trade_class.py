class TradeLogger:
    def __init__(self, tradier_api, sentiment_func, risk_grader):
        self.tradier = tradier_api                  # API client to get quotes
        self.get_sentiment = sentiment_func         # Function to fetch sentiment
        self.grade_risk = risk_grader               # Function to grade trade risk
        self.trade_history = []                     # Stores logged trades
        self.total_trades = 0                       # Counter for analytics

    def log_trade(self, ticker, action, quantity=1, price=None):
        quote = self.tradier.get_quote(ticker)
        sentiment = self.get_sentiment(ticker)
        risk_grade = self.grade_risk(ticker)

        trade = {
            "ticker": ticker,
            "action": action,
            "quantity": quantity,
            "price": price if price is not None else 0.0,
            "open": quote.get("open", 0) if quote else 0,
            "high": quote.get("high", 0) if quote else 0,
            "low": quote.get("low", 0) if quote else 0,
            "volume": quote.get("volume", 0) if quote else 0,
            "sentiment": sentiment,
            "risk_grade": risk_grade,
            "result": "pending",
            "profit": 0.0
        }

        self.trade_history.append(trade)
        self.total_trades += 1
        print(f"[TradeLogger] Logged trade for {ticker} | Action: {action}")