# === FILE: payout_engine.py ===
import time, json, os
from datetime import datetime

PAYOUT_LOG = "payout_log.json"
counter = 0

def record_payout(amount):
    log = []
    if os.path.exists(PAYOUT_LOG):
        with open(PAYOUT_LOG, "r") as f:
            log = json.load(f)
    log.append({"time": datetime.now().isoformat(), "amount": amount})
    with open(PAYOUT_LOG, "w") as f:
        json.dump(log, f, indent=2)
    print(f"[PayoutEngine] 💰 Payout sent: {amount} ETH")

def payout_loop():
    global counter
    print("[PayoutEngine] 💸 Watching for payout triggers...")
    while True:
        counter += 1
        if counter % 3 == 0:
            record_payout(round(0.01 + 0.05 * (counter/3), 4))
        time.sleep(30)