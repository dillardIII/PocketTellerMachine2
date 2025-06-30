from ghost_env import INFURA_KEY, VAULT_ADDRESS
# persona_learning_loop.py
# Purpose: Let AI personas learn from trade outcomes and evolve behavior over time
# Each persona develops a unique trading profile based on results, feedback, and trade memory

import json
import os
from datetime import datetime
from utils.logger import log_event
from memory.trade_logger import TradeLogger

class PersonaLearningLoop:
    def __init__(self):
        self.persona_dir = "memory/persona_profiles/"
        self.trade_logger = TradeLogger()

        if not os.path.exists(self.persona_dir):
            os.makedirs(self.persona_dir)

    def load_persona(self, name):
        """Load a persona's learning profile."""
        path = os.path.join(self.persona_dir, f"{name}.json")
        if os.path.exists(path):
            with open(path, "r") as f:
                return json.load(f)
        else:
            # Initialize new profile
            return {
                "name": name,
                "trades_analyzed": 0,
                "win_rate": 0.0,
                "preferred_strategies": {},
                "recent_emotion": "neutral",
                "last_updated": str(datetime.now())
            }

    def save_persona(self, data):
        """Save persona profile to file."""
        path = os.path.join(self.persona_dir, f"{data['name']}.json")
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    def analyze_trade(self, trade):
        """Evaluate the result of a trade."""
        result = trade.get("result")
        strategy = trade.get("strategy")
        persona = trade.get("executed_by")

        profile = self.load_persona(persona)
        profile["trades_analyzed"] += 1

        # Update win rate
        wins = profile["win_rate"] * (profile["trades_analyzed"] - 1)
        if result == "win":
            wins += 1
        profile["win_rate"] = round(wins / profile["trades_analyzed"], 4)

        # Adjust strategy preferences
        strat_stats = profile["preferred_strategies"]
        if strategy not in strat_stats:
            strat_stats[strategy] = {"used": 1, "wins": 1 if result == "win" else 0}:
        else:
            strat_stats[strategy]["used"] += 1
            if result == "win":
                strat_stats[strategy]["wins"] += 1

        # Update emotional tone
        if profile["win_rate"] >= 0.7:
            profile["recent_emotion"] = "confident"
        elif profile["win_rate"] <= 0.4:
            profile["recent_emotion"] = "cautious"
        else:
            profile["recent_emotion"] = "neutral"

        profile["last_updated"] = str(datetime.now())
        self.save_persona(profile)

        log_event("Persona Updated", {
            "persona": persona,
            "win_rate": profile["win_rate"],
            "emotion": profile["recent_emotion"]
        })

    def run_learning_cycle(self):
        """Analyze all trades and update each persona."""
        history = self.trade_logger.get_all_trades()

        for trade in history:
            if "executed_by" in trade and "result" in trade:
                self.analyze_trade(trade)


# --- Run as Standalone ---
if __name__ == "__main__":
    learner = PersonaLearningLoop()
    learner.run_learning_cycle()