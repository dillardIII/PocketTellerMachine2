import os
import json
from datetime import datetime

# Paths
COLE_LOG_PATH = "logs/cole_trade_log.json"
MAIN_LOG_PATH = "data/trade_log.json"


def log_trade(symbol, strategy, action, price, shares, result, persona="Mentor"):
    """Logs a trade to both Cole and Main trade logs."""

    # --- Construct unified trade entry ---
    now = datetime.now()
    trade_entry = {
        "timestamp": now.isoformat(),
        "datetime": now.strftime("%Y-%m-%d %H:%M:%S"),
        "symbol": symbol,
        "strategy": strategy,
        "action": action,
        "price": round(float(price), 2),
        "shares": shares,
        "total": round(price * shares, 2),
        "result": result,
        "persona": persona
    }

    # === Save to Cole log ===
    os.makedirs(os.path.dirname(COLE_LOG_PATH), exist_ok=True)
    cole_log = []
    if os.path.exists(COLE_LOG_PATH):
        try:
            with open(COLE_LOG_PATH, "r") as f:
                cole_log = json.load(f)
        except:
            cole_log = []
    cole_log.append(trade_entry)
    with open(COLE_LOG_PATH, "w") as f:
        json.dump(cole_log[-500:], f, indent=2)

    # === Save to Main log (recap speaker) ===
    os.makedirs(os.path.dirname(MAIN_LOG_PATH), exist_ok=True)
    main_log = []
    if os.path.exists(MAIN_LOG_PATH):
        try:
            with open(MAIN_LOG_PATH, "r") as f:
                main_log = json.load(f)
        except:
            main_log = []
    # Filter down to recap-needed fields only
    recap_entry = {
        "datetime": trade_entry["datetime"],
        "symbol": symbol,
        "price": trade_entry["price"],
        "action": action,
        "strategy": strategy,
        "persona": persona,
        "result": result
    }
    main_log.append(recap_entry)
    with open(MAIN_LOG_PATH, "w") as f:
        json.dump(main_log[-500:], f, indent=2)

    print(f"[Trade Log] 📈 {action.upper()} {shares} of {symbol} at ${price:.2f} | Result: {result}")


# === Test Mode ===
if __name__ == "__main__":
    log_trade(
        symbol="AAPL",
        strategy="momentum breakout",
        action="buy",
        price=189.44,
        shares=5,
        result="win",
        persona="Mentor"
    )