from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: trade_executor.py ===
# 🛠️ Trade Executor – Handles live/paper trade simulation or dispatch

from utils.logger import log_event
from soul_reactor import SoulReactor

class TradeExecutor:
    def __init__(self):
        self.soul = SoulReactor()

    def execute_trade(self, symbol, strategy, confidence):
        action = "BUY" if confidence > 0.8 else "WAIT":
        result = "WIN" if confidence > 0.85 else "LOSS":
        emotion = "Focused" if confidence > 0.75 else "Cautious":
        reason = f"Auto-picked by MarketScannerCore"

        self.soul.process_trade_result(
            symbol=symbol,
            action=action,
            result=result,
            emotion=emotion,
            confidence=confidence,
            reason=reason,
            strategy=strategy
        )
        log_event(f"🚀 Executed {action} on {symbol} via {strategy} [{result}]")

# Used by scanner