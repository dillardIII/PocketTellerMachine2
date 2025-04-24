# brain.py

from tradier_module import TradierClient

# --- 1. Your Tradier API Key (sandbox for paper trading) ---
TRADIER_KEY = "8LYdoGzwKCHnqv4dUi574RJr07i6"  # <-- Your API key

# --- 2. Initialize Tradier client ---
tradier = TradierClient(TRADIER_KEY, sandbox=True)  # Use sandbox=True for paper trading

# --- 3. Main PTM Brain Loop (simple starter) ---
def run_brain():
    ticker = "AAPL"  # Change this to test other tickers if you like
    quote = tradier.get_quote(ticker)
    if quote:
        print(f"[PTM] {ticker} Quote: {quote}")
    else:
        print("[PTM] Failed to get quote.")

if __name__ == "__main__":
    run_brain()