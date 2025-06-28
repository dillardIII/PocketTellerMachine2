# === FILE: soul_reactor.py ===
# 🔥 Soul Reactor – Synthesizes trade memories, mood, and strategy wins into evolution

from soul_of_trade import SoulOfTrade
from strategy_bias_engine import StrategyBiasEngine
from mood_state_engine import MoodStateEngine
from utils.logger import log_event

class SoulReactor:
    def __init__(self):
        self.soul = SoulOfTrade()
        self.bias = StrategyBiasEngine()
        self.mood = MoodStateEngine()

    def process_trade_result(self, symbol, action, result, emotion, confidence, reason, strategy):
        self.soul.log_trade_soul(symbol, action, result, emotion, confidence, reason)
        self.bias.log_result(strategy, result)
        
        # Determine mood update
        if result == "WIN" and confidence >= 0.8:
            self.mood.update_mood("BIG_WIN")
        elif result == "LOSS" and confidence >= 0.7:
            self.mood.update_mood("BIG_LOSS")
        elif result == "WIN":
            self.mood.update_mood("MULTI_WIN")
        else:
            self.mood.update_mood("STABLE")

        log_event(f"🔗 Soul Reactor integrated trade result into all subsystems.")

# Example
if __name__ == "__main__":
    reactor = SoulReactor()
    reactor.process_trade_result(
        symbol="AAPL", action="BUY", result="WIN",
        emotion="Excited", confidence=0.92,
        reason="Bullish MACD crossover", strategy="Momentum Surge"
    )