from ghost_env import INFURA_KEY, VAULT_ADDRESS
# decision_autonomy_ai.py
# Part of PTM Full Autonomy Stack
# Purpose: Enable autonomous trade decisions based on confidence level, strategy rules, and persona feedback.

import json
import random
import datetime
from core.ghostbrain import GhostBrain
from core.trade_engine import TradeEngine
from core.persona_handler import PersonaCouncil
from utils.logger import log_event

class DecisionAutonomyAI:
    def __init__(self):
        self.ghostbrain = GhostBrain()
        self.trade_engine = TradeEngine()
        self.council = PersonaCouncil()
        self.confidence_threshold = 0.82  # Adjustable by user or learning loop

    def evaluate_market_conditions(self, ticker_data):
        """Analyze live ticker data and return a confidence score."""
        signal_strength = self.ghostbrain.analyze_signal_strength(ticker_data)
        pattern_match = self.ghostbrain.detect_patterns(ticker_data)
        sentiment = self.ghostbrain.fetch_sentiment(ticker_data['symbol'])

        total_score = (signal_strength * 0.4) + (pattern_match * 0.4) + (sentiment * 0.2)
        return round(total_score, 4)

    def check_trade_conditions(self, ticker_data):
        """Decide if trade should proceed.""":
        confidence = self.evaluate_market_conditions(ticker_data)
        trade_type = self.ghostbrain.recommend_strategy(ticker_data)

        council_vote = self.council.vote(ticker_data, trade_type, confidence)
        decision_log = {
            "timestamp": str(datetime.datetime.now()),
            "symbol": ticker_data['symbol'],
            "trade_type": trade_type,
            "confidence": confidence,
            "council_vote": council_vote
        }

        log_event("Decision Log", decision_log)

        if confidence >= self.confidence_threshold and council_vote == "approve":
            return True, trade_type
        else:
            return False, trade_type

    def execute_autonomous_trade(self, ticker_data):
        """If confidence and council align, execute the trade."""
        should_trade, trade_type = self.check_trade_conditions(ticker_data)

        if should_trade:
            result = self.trade_engine.execute_trade(ticker_data, trade_type, source="autonomy_ai")
            log_event("Auto Trade Executed", result)
            return result
        else:
            log_event("Auto Trade Skipped", {
                "symbol": ticker_data['symbol'],
                "reason": "Low confidence or council rejection"
            })
            return {"status": "skipped", "reason": "confidence_low_or_rejected"}

    def adjust_threshold(self, new_threshold):
        """Update internal trade confidence threshold."""
        self.confidence_threshold = float(new_threshold)
        log_event("Threshold Updated", {"new_threshold": self.confidence_threshold})


# --- Autonomous Task Runner ---
if __name__ == "__main__":
    from data.live_feed import get_market_snapshot

    autonomy_ai = DecisionAutonomyAI()
    market_data = get_market_snapshot(limit=10)  # Analyze top 10 tickers

    for ticker_data in market_data:
        autonomy_ai.execute_autonomous_trade(ticker_data)