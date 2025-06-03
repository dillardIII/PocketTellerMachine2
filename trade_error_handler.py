# trade_error_handler.py – Handles trade execution errors gracefully

def handle_trade_error(error_message, strategy=None):
    print(f"[Trade Error Handler] ⚠️ Error occurred: {error_message}")
    if strategy:
        print(f"[Trade Error Handler] 🧠 Strategy that failed: {strategy}")
    # Future: Add retry logic, fallback strategy, or alert system here