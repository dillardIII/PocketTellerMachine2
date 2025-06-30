
# === FILE: ema_atr_6493.py ===
# Auto-generated multi-strategy using EMA, ATR

import random
def run():
    ema = random.uniform(-1,1)
    atr = random.uniform(-1,1)

    if ema > 0 and atr > 0:
        print("🚀 BUY signal based on EMA, ATR combo")
    else:
        print("🚫 NO BUY - waiting for better signal")

if __name__ == "__main__":
    run()
