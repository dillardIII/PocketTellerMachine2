# strategy_router.py – Routes Validated Strategy to Proper Handler

def route_strategy(strategy):
    print(f"[Strategy Router] 🚦 Routing strategy: {strategy}")

    # Validate basic format
    if not strategy or "symbol" not in strategy or "action" not in strategy:
        print("[Strategy Router] ❌ Invalid strategy format.")
        return False

    # Type-specific handling
    if "type" in strategy:
        if strategy["type"] == "stock":
            return handle_stock_strategy(strategy)
        elif strategy["type"] == "options":
            return handle_options_strategy(strategy)
        elif strategy["type"] == "forex":
            return handle_forex_strategy(strategy)
        elif strategy["type"] == "crypto":
            return handle_crypto_strategy(strategy)
        else:
            print(f"[Router] ❌ Unknown strategy type: {strategy['type']}")
            return False
    else:
        # Fallback to action-based logic
        symbol = strategy["symbol"]
        action = strategy["action"]

        if action == "BUY":
            print(f"[Router] ➕ Route to BUY handler for {symbol}")
            return True
        elif action == "SELL":
            print(f"[Router] ➖ Route to SELL handler for {symbol}")
            return True
        else:
            print(f"[Router] ❌ Unknown action: {action}")
            return False

def handle_stock_strategy(strategy):
    print(f"[Router] 📈 Handling stock strategy: {strategy}")
    # Placeholder for future stock-specific logic
    return True

def handle_options_strategy(strategy):
    print(f"[Router] 🧾 Handling options strategy: {strategy}")
    # Placeholder for options logic (credit spreads, condors, etc.)
    return True

def handle_forex_strategy(strategy):
    print(f"[Router] 💱 Handling forex strategy: {strategy}")
    # Placeholder for forex-specific logic
    return True

def handle_crypto_strategy(strategy):
    print(f"[Router] 🪙 Handling crypto strategy: {strategy}")
    # Placeholder for crypto-specific logic
    return True