# === FILE: bridge/inbox/test_strategy.py ===
print("[TestStrategy] 🔍 Executing basic RSI test strategy.")

symbol = "AAPL"
rsi = 28
trend = "down"

if rsi < 30 and trend == "down":
    print(f"[TestStrategy] ✅ BUY SIGNAL for {symbol}!")
else:
    print(f"[TestStrategy] ❌ No buy signal for {symbol}.")