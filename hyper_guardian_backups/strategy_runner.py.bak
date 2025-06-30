# === FILE: strategy_runner.py ===

import time
from log_trade import log_trade
from persona_recap_speaker import speak_recap
from cole_logger import log_info

def run_strategy(strategy_bundle):
    try:
        # Extract fields
        symbol = strategy_bundle.get("symbol", "AAPL")
        strategy_name = strategy_bundle.get("name", "Unnamed Strategy")
        price = 100.00  # Placeholder for market price
        shares = 10
        action = "buy"
        persona = strategy_bundle.get("persona", "MoCash")
        result_status = "win"

        # Log execution start
        log_info(f"[Strategy Runner] 🛠️ Executing '{strategy_name}' on {symbol}...")

        # Simulate execution time
        time.sleep(1)

        # Log trade
        log_trade(
            symbol=symbol,
            strategy=strategy_name,
            action=action,
            price=price,
            shares=shares,
            result=result_status,
            persona=persona
        )

        # Trigger voice recap
        speak_recap({
            "symbol": symbol,
            "strategy": strategy_name,
            "action": action,
            "price": price,
            "shares": shares,
            "total": price * shares,
            "datetime": "now",
            "persona": persona,
            "result": result_status
        })

        log_info(f"[Strategy Runner] ✅ Strategy '{strategy_name}' complete.")

    except Exception as e:
        log_info(f"[Strategy Runner] ❌ Error during execution: {e}")