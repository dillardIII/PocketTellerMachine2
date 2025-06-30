from ghost_env import INFURA_KEY, VAULT_ADDRESS
# auto_trade_executor.py
# Purpose: Execute trades automatically when in full_auto mode
# Reads autonomy_mode_config.json and executes or blocks trades accordingly

import json
import os
from utils.logger import log_event
from core.wallet_bridge_core import WalletBridgeCore
from core.risk_guardian import RiskGuardian

class AutoTradeExecutor:
    def __init__(self):
        self.config_path = "autonomy_mode_config.json"
        self.bridge = WalletBridgeCore()
        self.risk_guard = RiskGuardian()
        self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError("Missing autonomy_mode_config.json")

        with open(self.config_path, "r") as f:
            self.config = json.load(f)

    def check_fail_safe(self, trade):
        """Consult RiskGuardian to block trades if thresholds are breached.""":
        return self.risk_guard.is_trade_allowed(trade, self.config.get("fail_safe", {}))

    def execute_trade(self, trade):
        """Main trade handler — will auto-execute or skip based on mode + safety."""
        self.load_config()

        mode = self.config.get("mode", "manual")
        if mode != "full_auto":
            log_event("AutoTrade Blocked", {
                "reason": "autonomy_mode not full_auto",
                "mode": mode
            })
            return {"status": "blocked", "reason": "not_in_full_auto_mode"}

        if not self.check_fail_safe(trade):
            log_event("AutoTrade Blocked", {
                "reason": "failsafe triggered",
                "trade": trade
            })
            return {"status": "blocked", "reason": "failsafe_limit_exceeded"}

        result = self.bridge.place_trade(trade["platform"], trade)
        log_event("AutoTrade Executed", result)
        return result