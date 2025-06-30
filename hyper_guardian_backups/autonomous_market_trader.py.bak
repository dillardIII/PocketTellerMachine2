# === FILE: autonomous_market_trader.py ===
# 💰 Fully Autonomous Market Trader – scans, decides, trades.

import random
import time

def scan_market():
    price = random.uniform(1000, 5000)
    print(f"[MarketScanner] 📊 Current asset price: ${price:.2f}")
    return price

def decide_and_trade(price):
    decision = random.choice(["buy", "hold", "sell"])
    print(f"[TraderAI] 🧠 Decision: {decision.upper()} at ${price:.2f}")
    if decision == "buy":
        execute_trade("buy", price)
    elif decision == "sell":
        execute_trade("sell", price)

def execute_trade(action, price):
    print(f"[TraderAI] 💵 {action.upper()} executed at ${price:.2f}")

if __name__ == "__main__":
    while True:
        p = scan_market()
        decide_and_trade(p)
        time.sleep(60)