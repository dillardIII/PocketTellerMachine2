# === FILE: ghostbacktester_ai.py ===
# 📉 GhostBacktester – AI-powered trade simulator with grading and memory logging

import random
import json
from datetime import datetime
from utils.logger import log_event

BACKTEST_LOG = "memory/backtest_results.json"

class GhostBacktesterAI:
    def __init__(self):
        self.grades = []

    def simulate_strategy(self, strategy_name, num_trades=10):
        wins = 0
        losses = 0

        for _ in range(num_trades):
            if random.random() > 0.4:
                wins += 1
            else:
                losses += 1

        grade = self.grade_strategy(wins, losses)
        result = {
            "strategy": strategy_name,
            "wins": wins,
            "losses": losses,
            "grade": grade,
            "timestamp": str(datetime.now())
        }

        log_event(f"📘 Backtest: {result}")
        self.log_result(result)
        return result

    def grade_strategy(self, wins, losses):
        win_rate = wins / (wins + losses)
        if win_rate >= 0.9:
            return "A+"
        elif win_rate >= 0.75:
            return "A"
        elif win_rate >= 0.6:
            return "B"
        elif win_rate >= 0.45:
            return "C"
        else:
            return "F"

    def log_result(self, result):
        try:
            with open(BACKTEST_LOG, "r") as f:
                data = json.load(f)
        except:
            data = []

        data.append(result)
        with open(BACKTEST_LOG, "w") as f:
            json.dump(data, f, indent=4)

# Manual run
if __name__ == "__main__":
    backtester = GhostBacktesterAI()
    print(backtester.simulate_strategy("Iron Condor"))