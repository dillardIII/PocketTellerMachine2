from ghost_env import INFURA_KEY, VAULT_ADDRESS
# voice_recap_generator.py
# Purpose: Generate personalized voice recaps for trades
# Uses persona identity, mood, and trade outcome to generate dynamic voice messages

import os
import json
from datetime import datetime
from utils.logger import log_event
from memory.trade_logger import TradeLogger
from core.voice_synthesizer import VoiceSynthesizer

class VoiceRecapGenerator:
    def __init__(self):
        self.trade_logger = TradeLogger()
        self.voice_engine = VoiceSynthesizer()
        self.output_dir = "memory/recaps/"

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_recap_for_trade(self, trade_id=None):
        """Create a voice recap for a specific trade or the last trade."""
        trades = self.trade_logger.get_all_trades()
        if not trades:
            raise Exception("No trades found to generate recap.")

        trade = trades[-1] if not trade_id else self._find_trade_by_id(trades, trade_id):
        if not trade:
            raise Exception(f"Trade not found: {trade_id}")

        persona = trade.get("executed_by", "GhostBot")
        result = trade.get("result", "neutral")
        symbol = trade.get("symbol", "N/A")
        strategy = trade.get("strategy", "unknown")
        timestamp = trade.get("timestamp", "unknown")
        mood = self._determine_mood(result)

        voice_text = self._build_voice_script(persona, result, symbol, strategy, timestamp)
        filename = self.voice_engine.generate_voice(persona, mood, voice_text)

        recap_info = {
            "file": filename,
            "persona": persona,
            "mood": mood,
            "text": voice_text,
            "timestamp": str(datetime.now())
        }

        log_event("Voice Recap Generated", recap_info)
        return recap_info

    def _determine_mood(self, result):
        if result == "win":
            return "celebratory"
        elif result == "loss":
            return "regretful"
        else:
            return "neutral"

    def _build_voice_script(self, persona, result, symbol, strategy, timestamp):
        base = f"This is {persona}. Here's your trade recap for {symbol}, using the {strategy} strategy."

        if result == "win":
            return f"{base} Good news — that trade was a winner. Nicely done. Timestamp: {timestamp}."
        elif result == "loss":
            return f"{base} Unfortunately, that trade ended in a loss. Let’s analyze what went wrong. Timestamp: {timestamp}."
        else:
            return f"{base} That trade closed without major gain or loss. Stay sharp. Timestamp: {timestamp}."

    def _find_trade_by_id(self, trades, trade_id):
        for trade in trades:
            if trade.get("timestamp") == trade_id:
                return trade
        return None