# trading_execution_engine.py – Executes Validated Trades

import random

def execute_trade(symbol, action, price, quantity):
    print(f"[Execution Engine] 🚀 Executing {action} order for {quantity} shares of {symbol} at ${price}")

    # Simulated success or failure
    success = random.choice([True, True, True, False])  # 75% success rate
    if success:
        print(f"[Execution Engine] ✅ Trade executed successfully for {symbol}")
        return True
    else:
        print(f"[Execution Engine] ❌ Trade execution failed for {symbol}")
        return False