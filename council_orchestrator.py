from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: council_orchestrator.py ===
# 🧠 Council Orchestrator – Manages debates, votes, and resolutions among assistant personas

import time
from ghostvote_engine import GhostVoteEngine
from assistant_dispatch import AssistantDispatch
from utils.logger import log_event

class CouncilOrchestrator:
    def __init__(self):
        self.vote_engine = GhostVoteEngine()
        self.dispatch = AssistantDispatch()

    def call_meeting(self, topic, options, urgency="normal"):
        self.dispatch.speak(f"🧑‍⚖️ Council meeting called. Topic: {topic}")
        time.sleep(1)

        # Introduce topic with urgency tone
        if urgency == "critical":
            self.dispatch.speak("⚠️ This is a high-priority situation.")
        elif urgency == "low":
            self.dispatch.speak("🛋️ This is a casual review.")
        else:
            self.dispatch.speak("🔍 Standard review in progress.")

        # Delay for dramatic effect
        time.sleep(1)

        result = self.vote_engine.run_vote(topic, options)

        self.dispatch.speak("📜 Summary of council discussion:")
        for persona, choice in result["log"].items():
            self.dispatch.speak(f"{persona} voted for {choice}")

        self.dispatch.speak(f"🗳️ Final decision: {result['winner']}")
        return result

# 🔁 Optional test meeting
if __name__ == "__main__":
    council = CouncilOrchestrator()
    council.call_meeting("Should we short NVDA?", ["Yes", "No", "Wait"], urgency="critical")