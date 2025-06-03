# trade_logger.py – Logs trade details for recordkeeping and analysis

def log_trade(symbol, action, price, quantity):
    print(f"[Trade Logger] 📝 Logging trade: {action} {quantity} shares of {symbol} at ${price:.2f}")
    # Future: Save to JSON, database, or cloud