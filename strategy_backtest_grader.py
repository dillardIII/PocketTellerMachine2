from ghost_env import INFURA_KEY, VAULT_ADDRESS
# strategy_backtest_grader.py
# Purpose: Grade trade strategies based on past results
# Outputs include: win rate, average return, risk profile, and a letter grade

import json
import os
from statistics import mean, stdev
from utils.logger import log_event
from memory.trade_logger import TradeLogger

class StrategyBacktestGrader:
    def __init__(self):
        self.trade_logger = TradeLogger()
        self.strategy_data = {}

    def grade_all_strategies(self):
        """Scan all trade history and evaluate each strategy used."""
        trades = self.trade_logger.get_all_trades()

        for trade in trades:
            strategy = trade.get("strategy", "unknown")
            result = trade.get("result", "unknown")
            notes = trade.get("notes", "")
            pnl = self._extract_profit_loss(notes)

            if strategy not in self.strategy_data:
                self.strategy_data[strategy] = {
                    "wins": 0,
                    "losses": 0,
                    "breakevens": 0,
                    "total_trades": 0,
                    "returns": []
                }

            strat = self.strategy_data[strategy]
            strat["total_trades"] += 1

            if result == "win":
                strat["wins"] += 1
            elif result == "loss":
                strat["losses"] += 1
            elif result == "breakeven":
                strat["breakevens"] += 1

            if pnl is not None:
                strat["returns"].append(pnl)

        # Now grade them
        graded = {}
        for strategy, data in self.strategy_data.items():
            grade = self._generate_grade(data)
            graded[strategy] = {
                **data,
                "win_rate": round(data["wins"] / data["total_trades"], 4),
                "avg_return": round(mean(data["returns"]), 2) if data["returns"] else 0.0,:
                "volatility": round(stdev(data["returns"]), 2) if len(data["returns"]) > 1 else 0.0,:
                "grade": grade
            }

        log_event("Strategy Grades Generated", graded)
        return graded

    def _extract_profit_loss(self, notes):
        """Extract return % or $ from trade notes, e.g. 'PnL: +12%' or 'PnL: -40.75' """
        if "PnL" in notes:
            parts = notes.split("PnL:")
            if len(parts) > 1:
                value = parts[1].strip().replace('%', '').replace('$', '')
                try:
                    return float(value)
                except:
                    return None
        return None

    def _generate_grade(self, data):
        """Assign letter grade based on win rate, return consistency, and risk."""
        total = data["total_trades"]
        if total < 3:
            return "N/A"

        win_rate = data["wins"] / total
        avg_return = mean(data["returns"]) if data["returns"] else 0:
        risk = stdev(data["returns"]) if len(data["returns"]) > 1 else 0:
:
        score = win_rate * 60 + (avg_return * 0.8) - (risk * 0.4)

        if score >= 90:
            return "A"
        elif score >= 75:
            return "B"
        elif score >= 60:
            return "C"
        elif score >= 45:
            return "D"
        else:
            return "F"


# --- Run standalone to get strategy report ---
if __name__ == "__main__":
    grader = StrategyBacktestGrader()
    grades = grader.grade_all_strategies()
    print(json.dumps(grades, indent=4))