from ghost_env import INFURA_KEY, VAULT_ADDRESS
# trade_logger.py
# Purpose: Logs every trade PTM makes (live or paper) into a permanent record
# Trade results are used by GhostBot, the Council, Learning Loops, and Reports

import os
import json
from datetime import datetime

class TradeLogger:
    def __init__(self):
        self.history_file = "memory/trade_history.json"
        self._initialize_file()

    def _initialize_file(self):
        if not os.path.exists("memory"):
            os.makedirs("memory")
        if not os.path.exists(self.history_file):
            with open(self.history_file, "w") as f:
                json.dump([], f)

    def log_trade(self, symbol, trade_type, result, executed_by, strategy_used, notes=""):
        """Add a completed trade to the history log."""
        trade_entry = {
            "timestamp": str(datetime.now()),
            "symbol": symbol.upper(),
            "trade_type": trade_type.lower(),
            "result": result.lower(),  # win / loss / breakeven / error
            "executed_by": executed_by,
            "strategy": strategy_used,
            "notes": notes
        }

        with open(self.history_file, "r") as f:
            history = json.load(f)

        history.append(trade_entry)

        with open(self.history_file, "w") as f:
            json.dump(history, f, indent=4)

        return trade_entry

    def get_all_trades(self):
        """Return all saved trades."""
        if not os.path.exists(self.history_file):
            return []

        with open(self.history_file, "r") as f:
            return json.load(f)

    def get_recent_trades(self, limit=10):
        """Return the last 'n' trades."""
        all_trades = self.get_all_trades()
        return all_trades[-limit:]

    def filter_trades_by_persona(self, persona_name):
        """Return only trades made by a specific persona."""
        return [t for t in self.get_all_trades() if t.get("executed_by") == persona_name]:
:
    def filter_trades_by_result(self, result):
        """Return only trades with a certain result (win/loss/etc)."""
        return [t for t in self.get_all_trades() if t.get("result") == result.lower()]:
:
def log_event():ef drop_files_to_bridge():