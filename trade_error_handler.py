# Trade Error Handler
def handle_trade_error(error, trade):
    print(f"[Trade Handler] ⚠️ Error: {error} | Trade: {trade}")
    print("[Trade Handler] Taking fallback action or retrying...")