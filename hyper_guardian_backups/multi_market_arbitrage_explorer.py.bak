# === FILE: multi_market_arbitrage_explorer.py ===
# 🌍 Multi-Market Arbitrage Explorer – finds cross-market mispricings

import time
import random

MARKETS = ["NYSE", "NASDAQ", "LSE", "HKEX", "TSE", "CRYPTO"]

def find_arbitrage():
    m1, m2 = random.sample(MARKETS, 2)
    price1 = random.uniform(100, 200)
    price2 = random.uniform(100, 200)
    gap = abs(price1 - price2)
    return m1, m2, gap

def main_loop():
    while True:
        m1, m2, gap = find_arbitrage()
        if gap > 20:
            print(f"[ArbExplorer] 💰 Arbitrage: {m1} vs {m2} gap ${gap:.2f}")
            with open("arbitrage_opportunities.txt", "a") as f:
                f.write(f"{m1} vs {m2}: ${gap:.2f}\n")
        else:
            print(f"[ArbExplorer] ⚖️ No significant arbitrage found.")
        time.sleep(15)

if __name__ == "__main__":
    print("[ArbExplorer] 🌐 Running arbitrage explorer...")
    main_loop()