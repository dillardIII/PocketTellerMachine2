# Trade Logger
trade_history = []

def log_trade(symbol, action, price, quantity):
    trade = {
        "symbol": symbol,
        "action": action,
        "price": price,
        "quantity": quantity
    }
    trade_history.append(trade)
    print(f"[Trade Logger] Logged trade: {trade}")

def get_trade_history():
    return trade_history