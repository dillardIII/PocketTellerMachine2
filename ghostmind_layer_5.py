from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghostmind_layer_5.py ===
# 👁️ GhostMind Layer 5 – Multi-perception + mood + forecasting integration

import random
from datetime import datetime
from utils.logger import log_event
from ghostmind_layer_4 import GhostMindLayer4
from dimensional_scanner import DimensionalScanner

class GhostMindLayer5:
    def __init__(self):
        self.layer4 = GhostMindLayer4()
        self.scanner = DimensionalScanner()
        self.perception_log = "memory/ghostmind_layer5_reflections.json"

    def generate_perception(self):
        reflection = self.layer4.reflect_on_recent_trades()
        signal = self.scanner.scan()

        perception = {
            "timestamp": str(datetime.now()),
            "overall_mood": signal["emotional_wave"],
            "intuition_level": signal["intuition_level"],
            "layer_contact": signal["layer_contact"],
            "pattern_bias": self.extract_pattern_bias(reflection),
            "forecast": self.forecast_next_behavior(signal)
        }

        log_event(f"🔮 Layer 5 Perception: {perception}")
        self.log(perception)
        return perception

    def extract_pattern_bias(self, reflections):
        bias = {"Buy": 0, "Sell": 0, "Hold": 0}
        for r in reflections:
            action = r["action"]
            bias[action] = bias.get(action, 0) + 1
        return bias

    def forecast_next_behavior(self, signal):
        if signal["emotional_wave"] == "Calm" and signal["intuition_level"] > 0.7:
            return "📈 Prepare for high-confidence trades."
        elif signal["emotional_wave"] in ["Tense", "Chaotic"]:
            return "🛑 Pause. Analyze. Too volatile."
        else:
            return "🌀 Mixed signals. Let council vote."

    def log(self, payload):
        try:
            with open(self.perception_log, "r") as f:
                data = json.load(f)
        except:
            data = []

        data.append(payload)
        with open(self.perception_log, "w") as f:
            json.dump(data, f, indent=4)

# Manual trigger
if __name__ == "__main__":
    gm5 = GhostMindLayer5()
    gm5.generate_perception()