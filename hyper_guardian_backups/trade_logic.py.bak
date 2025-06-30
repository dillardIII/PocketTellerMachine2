# trade_logic.py
import random
from datetime import datetime

# Sample tickers it can pick from for now
watchlist = ["AAPL", "TSLA", "NVDA", "MSFT", "AMD"]

# Strategy options
strategies = ["covered_call", "credit_spread", "iron_condor", "cash_secured_put"]

def pick_ticker():
    return random.choice(watchlist)

def pick_strategy():
    return random.choice(strategies)

def generate_trade():
    ticker = pick_ticker()
    strategy = pick_strategy()
    
    # Simulate entry and exit points (will improve later)
    entry_price = round(random.uniform(100, 300), 2)
    exit_price = round(entry_price + random.uniform(-5, 10), 2)
    profit_loss = round(exit_price - entry_price, 2)
    
    return {
        "timestamp": datetime.now().isoformat(),
        "ticker": ticker,
        "strategy": strategy,
        "entry_price": entry_price,
        "exit_price": exit_price,
        "profit_loss": profit_loss,
        "result": "win" if profit_loss > 0 else "loss"
    }