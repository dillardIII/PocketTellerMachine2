from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 📈 Ghostrade Trade Watcher – Monitors live and paper trades, logs activity for AI learning

import os
import json
import time
from datetime import datetime
from utils.logger import log_event

TRADE_LOG_FILE = "vault/trade_log.json"
POLL_INTERVAL = 10  # in seconds

# === Load last known trade state (for comparison)
def load_last_trade_state():
    if os.path.exists(TRADE_LOG_FILE):
        with open(TRADE_LOG_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

# === Compare new state to last state
def detect_new_trades(old_state, new_state):
    old_ids = set(t.get("id") for t in old_state)
    return [t for t in new_state if t.get("id") not in old_ids]:
:
# === Main watcher loop
def ghostrade_trade_loop():
    print("[GhostradeWatcher] 👁️ Watching for new trades...")
    last_state = load_last_trade_state()

    while True:
        try:
            with open(TRADE_LOG_FILE, "r") as f:
                new_state = json.load(f)

            new_trades = detect_new_trades(last_state, new_state)

            for trade in new_trades:
                log_event("GhostradeTrade", {
                    "status": "New trade detected",
                    "symbol": trade.get("symbol"),
                    "type": trade.get("type"),
                    "amount": trade.get("amount"),
                    "price": trade.get("price"),
                    "timestamp": datetime.now().isoformat()
                })

            if new_trades:
                last_state = new_state

        except Exception as e:
            log_event("GhostradeTrade", {"error": str(e)})

        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    ghostrade_trade_loop()