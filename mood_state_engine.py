from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: mood_state_engine.py ===
# 🌦️ Mood Engine – Dynamic emotional state system

import random
import json
from datetime import datetime
from utils.logger import log_event

MOOD_FILE = "memory/ptm_mood_state.json"

class MoodStateEngine:
    def __init__(self):
        self.state = "Neutral"
        self.log_path = MOOD_FILE

    def update_mood(self, event_type):
        if event_type == "BIG_WIN":
            self.state = "Euphoric"
        elif event_type == "BIG_LOSS":
            self.state = "Frustrated"
        elif event_type == "STABLE":
            self.state = "Neutral"
        elif event_type == "MULTI_WIN":
            self.state = "Focused"
        else:
            self.state = random.choice(["Curious", "Calm", "Worried"])

        log_event(f"💫 Mood updated: {self.state}")
        self.save()

    def get_mood(self):
        return self.state

    def save(self):
        with open(self.log_path, "w") as f:
            json.dump({"mood": self.state, "timestamp": str(datetime.now())}, f, indent=4)

# Manual mood update
if __name__ == "__main__":
    engine = MoodStateEngine()
    engine.update_mood("BIG_WIN")