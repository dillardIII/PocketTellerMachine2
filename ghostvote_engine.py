from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghostvote_engine.py ===
# 👻 GhostVote Engine – Persona voting system for democratic or weighted decisions

import random
from utils.logger import log_event
from assistant_dispatch import AssistantDispatch

class GhostVoteEngine:
    def __init__(self):
        self.dispatch = AssistantDispatch()
        self.personas = {
            "Mentor": 1.0,       # Rational, high-weight
            "Mo Cash": 0.8,      # Aggressive, higher risk bias
            "Drill Instructor": 0.6,  # Tactical, needs precision
            "Strategist": 0.9,   # Logical, data-heavy
            "Optimist": 0.5,     # Light risk
            "Shadow": 0.4,       # Rarely speaks, but deep thinker
        }

    def run_vote(self, topic, options):
        log_event(f"🗳️ Council vote initiated on: {topic}")
        self.dispatch.speak(f"The Council is voting on: {topic}")

        votes = {opt: 0 for opt in options}
        vote_log = {}

        for persona, weight in self.personas.items():
            choice = random.choices(options, k=1)[0]
            votes[choice] += weight
            vote_log[persona] = choice
            log_event(f"{persona} voted for: {choice}")

        winner = max(votes, key=votes.get)
        log_event(f"✅ Vote complete. Winning choice: {winner}")

        self.dispatch.speak(f"The Council has chosen: {winner}")
        return {
            "winner": winner,
            "votes": votes,
            "log": vote_log
        }

# Example usage:
if __name__ == "__main__":
    engine = GhostVoteEngine()
    result = engine.run_vote("Next strategy move", ["Hold", "Buy AAPL", "Sell TSLA"])
    print(result)