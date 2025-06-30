from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghostmind_layer_4.py ===
# 🧠 GhostMind Layer 4 – Pattern recognition and self-analysis layer

import json
from datetime import datetime
from soul_of_trade import SoulOfTrade
from reflex_engine import ReflexEngine
from dimensional_scanner import DimensionalScanner
from utils.logger import log_event

class GhostMindLayer4:
    def __init__(self):
        self.soul = SoulOfTrade()
        self.reflex = ReflexEngine()
        self.scanner = DimensionalScanner()
        self.memory_log = "memory/ghostmind_reflections.json"

    def reflect_on_recent_trades(self, num=3):
        try:
            with open(self.soul.memory_file, "r") as f:
                trades = json.load(f)[-num:]
        except:
            trades = []

        patterns = []
        for trade in trades:
            score = self.evaluate_trade(trade)
            patterns.append({
                "symbol": trade["symbol"],
                "action": trade["action"],
                "result": trade["result"],
                "emotion": trade["emotion"],
                "score": score
            })

        log_event(f"🔮 Reflection: {patterns}")
        self.log_reflection(patterns)
        return patterns

    def evaluate_trade(self, trade):
        # Very basic emotion-score logic
        emotion_scale = {
            "Excited": 1.0,
            "Focused": 0.9,
            "Neutral": 0.5,
            "Worried": 0.3,
            "Panic": 0.1
        }

        emotion_score = emotion_scale.get(trade["emotion"], 0.5)
        reflex_insight = self.reflex.analyze_trade(trade["symbol"])
        combined_score = round((emotion_score + reflex_insight.get("confidence", 0.5)) / 2, 3)
        return combined_score

    def log_reflection(self, reflections):
        payload = {
            "timestamp": str(datetime.now()),
            "reflections": reflections,
            "signal": self.scanner.scan()
        }

        try:
            with open(self.memory_log, "r") as f:
                data = json.load(f)
        except:
            data = []

        data.append(payload)
        with open(self.memory_log, "w") as f:
            json.dump(data, f, indent=4)

# Example run
if __name__ == "__main__":
    ghostmind = GhostMindLayer4()
    ghostmind.reflect_on_recent_trades()