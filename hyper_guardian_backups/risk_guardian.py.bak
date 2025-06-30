# risk_guardian.py
# Purpose: Block unsafe trades based on configured thresholds and loss behavior

import os
import json
from datetime import datetime, timedelta

TRADE_LOG = "data/trades.json"
GUARDIAN_STATE = "data/risk_guardian_state.json"
TRADE_STATS = "memory/trade_stats.json"

DEFAULTS = {
    "max_open_trades": 10,
    "max_loss_streak": 3,
    "cooldown_minutes": 20,
    "active_loss_streak": 0,
    "last_loss_time": None
}

class RiskGuardian:
    def __init__(self):
        self.state = self.load_guardian_state()
        self.trade_stats = self.load_trade_stats()

    def load_guardian_state(self):
        if not os.path.exists(GUARDIAN_STATE):
            return DEFAULTS.copy()
        with open(GUARDIAN_STATE, "r") as f:
            return json.load(f)

    def save_guardian_state(self):
        with open(GUARDIAN_STATE, "w") as f:
            json.dump(self.state, f, indent=2)

    def load_trade_stats(self):
        if not os.path.exists(TRADE_STATS):
            return {
                "daily_loss": 0.0,
                "drawdown_pct": 0.0,
                "consecutive_losses": 0,
                "last_reset": str(datetime.now())
            }
        with open(TRADE_STATS, "r") as f:
            return json.load(f)

    def save_trade_stats(self):
        with open(TRADE_STATS, "w") as f:
            json.dump(self.trade_stats, f, indent=4)

    def update_trade_result(self, result, pnl):
        if result == "loss":
            self.trade_stats["daily_loss"] += abs(pnl)
            self.trade_stats["consecutive_losses"] += 1
            self.state["active_loss_streak"] += 1
            self.state["last_loss_time"] = datetime.now().isoformat()
        elif result == "win":
            self.trade_stats["consecutive_losses"] = 0
            self.state["active_loss_streak"] = 0
            self.state["last_loss_time"] = None

        if self.state["active_loss_streak"] >= self.state["max_loss_streak"]:
            self.state["last_loss_time"] = datetime.now().isoformat()
            print(f"[RiskGuardian] Loss streak triggered cooldown.")

        self.save_guardian_state()
        self.save_trade_stats()

    def is_trade_allowed(self, trade=None, config=None):
        config = config or {}
        max_daily_loss = config.get("max_daily_loss", 1000)
        max_drawdown = config.get("max_drawdown_pct", 10)
        max_consec_losses = config.get("max_consecutive_losses", 5)
        max_open_trades = self.state.get("max_open_trades", 10)

        # Cooldown check
        last_loss = self.state.get("last_loss_time")
        if last_loss:
            last_time = datetime.fromisoformat(last_loss)
            if datetime.now() < last_time + timedelta(minutes=self.state["cooldown_minutes"]):
                return False, "Cooldown active due to loss streak."

        # Open trades check
        if os.path.exists(TRADE_LOG):
            with open(TRADE_LOG, "r") as f:
                trades = json.load(f)
            open_trades = [t for t in trades if t.get("status") != "closed"]
            if len(open_trades) >= max_open_trades:
                return False, "Too many open trades."

        # Fail-safe config checks
        if self.trade_stats["daily_loss"] >= max_daily_loss:
            return False, "Daily loss limit exceeded."

        if self.trade_stats["drawdown_pct"] >= max_drawdown:
            return False, "Account drawdown exceeded."

        if self.trade_stats["consecutive_losses"] >= max_consec_losses:
            return False, "Too many consecutive losses."

        return True, "Trade approved."