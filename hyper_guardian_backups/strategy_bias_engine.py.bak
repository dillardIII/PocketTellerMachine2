# === FILE: strategy_bias_engine.py ===
# 🧠 Strategy Bias Engine – Learns what styles PTM wins or loses with & adjusts

import json
from datetime import datetime
from utils.logger import log_event

BIAS_FILE = "memory/strategy_bias_profile.json"

class StrategyBiasEngine:
    def __init__(self):
        self.biases = {}
        self.log_path = BIAS_FILE

    def log_result(self, strategy_name, result):
        if strategy_name not in self.biases:
            self.biases[strategy_name] = {"wins": 0, "losses": 0}

        if result == "WIN":
            self.biases[strategy_name]["wins"] += 1
        else:
            self.biases[strategy_name]["losses"] += 1

        log_event(f"📊 Strategy Bias Updated: {strategy_name} – {result}")
        self.save()

    def recommend(self):
        recommendations = []
        for name, record in self.biases.items():
            total = record["wins"] + record["losses"]
            win_rate = record["wins"] / total if total > 0 else 0
            recommendations.append((name, round(win_rate, 2)))
        
        recommendations.sort(key=lambda x: x[1], reverse=True)
        return recommendations[:3]

    def save(self):
        with open(self.log_path, "w") as f:
            json.dump(self.biases, f, indent=4)

# Example
if __name__ == "__main__":
    engine = StrategyBiasEngine()
    engine.log_result("Iron Condor", "WIN")
    engine.log_result("Credit Spread", "LOSS")
    print(engine.recommend())