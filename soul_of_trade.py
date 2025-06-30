from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: soul_of_trade.py ===
# 💎 Soul of Trade – Stores the emotional + memory imprint(of each trade for future reflection)

import json
from datetime import datetime
from utils.logger import log_event

SOUL_FILE = "memory/trade_souls.json"

class SoulOfTrade:
    def __init__(self):
        self.memory_file = SOUL_FILE

    def log_trade_soul(self, symbol, action, result, emotion, confidence, reason):
        soul = {
            "timestamp": str(datetime.now()),
            "symbol": symbol,
            "action": action,
            "result": result,
            "emotion": emotion,
            "confidence": confidence,
            "reason": reason,
        }

        try:
            with open(self.memory_file, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append(soul)

        with open(self.memory_file, "w") as f:
            json.dump(data, f, indent=4)

        log_event(f"💠 Soul logged: {soul}")
        return soul

# 🔁 Sample use
if __name__ == "__main__":
    soul = SoulOfTrade()
    soul.log_trade_soul("TSLA", "BUY", "WIN", "Excited", 0.88, "MACD and RSI alignment")