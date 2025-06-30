# paper_trader.py

import json
from datetime import datetime
from brain import TradingBrain

# Load API keys from env or config (replace with real values or load from settings)
tradier_key = "your_tradier_key"
perplexity_key = "your_perplexity_key"
openai_key = "your_openai_key"
wolfram_key = "your_wolfram_key"
claude_key = "your_claude_key"

brain = TradingBrain(tradier_key, perplexity_key, openai_key, wolfram_key, claude_key)

def simulate_trade():
    ticker = "AAPL"  # You can later randomize or pick from watchlist
    signal = brain.decide_trade(ticker)
    quote = brain.tradier.get_quote(ticker)

    trade = {
        "ticker": ticker,
        "strategy": signal,
        "price": float(quote.get("last", 0)),
        "confidence": 0.92,  # Placeholder
        "timestamp": datetime.utcnow().isoformat(),
        "result": "pending",
        "recap": brain.last_explanation or "No explanation available."
    }

    # Save to trade_log
    log_file = "data/trade_log.json"
    try:
        with open(log_file, "r") as f:
            trades = json.load(f)
    except FileNotFoundError:
        trades = []

    trades.append(trade)
    with open(log_file, "w") as f:
        json.dump(trades, f, indent=2)

    return trade