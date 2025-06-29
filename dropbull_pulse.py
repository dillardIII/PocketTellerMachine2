import time
import random

def run_dropbull():
    while True:
        markets = ["SP500", "NASDAQ", "CRYPTO", "FOREX"]
        for market in markets:
            pulse = round(random.uniform(-3, 3), 2)
            print(f"[DropBull] 📊 {market} pulse: {pulse}")
        time.sleep(60)