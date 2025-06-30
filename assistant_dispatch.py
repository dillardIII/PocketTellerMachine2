from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: assistant_dispatch.py ===
# 🎙️ Assistant Dispatch – Routes strategies, summaries, alerts, commands, and emotional tones to AI personas in PTM

import random
import time
from utils.logger import log_event

class AssistantDispatch:
    def __init__(self):
        self.active_persona = "Mentor"
        self.mood = "neutral"
        self.last_strategy = None
        print("[AssistantDispatch] 🗣️ Initialized Assistant Dispatch system.")

    # === Strategy Relay ===
    def relay_strategy(self, strategy):
        self.last_strategy = strategy
        mood = self._evaluate_mood(strategy.get("confidence", 0.5))
        message = f"{strategy['strategy']} detected using {strategy['indicator']} (Confidence: {strategy['confidence']*100:.1f}%)"
        self._speak(message, mood)
        log_event("Strategy Relayed", strategy)

    # === Alerts ===
    def send_alert(self, message):
        alert_text = f"🚨 ALERT: {message}"
        self._speak(alert_text, "urgent")
        log_event("Alert", {"message": message})

    # === Mood-Eval based on confidence ===
    def _evaluate_mood(self, confidence):
        if confidence > 0.8:
            return "hyped"
        elif confidence > 0.6:
            return "confident"
        elif confidence > 0.4:
            return "neutral"
        else:
            return "concerned"

    # === Voice Output (Simulated) ===
    def _speak(self, message, mood="neutral"):
        print(f"[{self.active_persona} | {mood.upper()}] 💬 {message}")

    # === Loop Idle Logic ===
    def relay_idle_loop(self):
        while True:
            self._speak("Standing by for new trading signals.", "neutral")
            time.sleep(60)