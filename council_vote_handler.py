# council_vote_handler.py
# Purpose: Final voting logic for PTM's Council of Personas
# Tally votes, weigh experience, mood, memory, and pass final verdict to Trade Executor

import random
from memory.persona_memory_core import PersonaMemoryCore
from utils.logger import log_event

class CouncilVoteHandler:
    def __init__(self):
        self.personas = ["Mo Cash", "The Mentor", "Drill Instructor", "The Strategist", "The Shadow"]
        self.vote_record = []

    def collect_votes(self, symbol, strategy, signal_strength):
        """Each persona votes and casts reasoning based on their memory, personality, and trade style."""
        votes = []

        for persona in self.personas:
            memory = PersonaMemoryCore(persona)
            profile = memory.get_memory_snapshot()

            # Weighted mood influence
            mood = profile["moods"][-1] if profile["moods"] else "neutral"
            experience = len(profile["trade_logs"])

            vote, reason = self._generate_vote(persona, strategy, mood, signal_strength, experience)

            votes.append({
                "persona": persona,
                "vote": vote,
                "reason": reason,
                "mood": mood,
                "experience": experience
            })

        self.vote_record = votes
        log_event("Council Votes Cast", {"symbol": symbol, "strategy": strategy, "votes": votes})
        return votes

    def _generate_vote(self, persona, strategy, mood, signal_strength, experience):
        """Decide vote based on persona profile and trading environment."""
        weight = signal_strength + (experience * 0.005)

        if mood == "confident":
            weight += 0.05
        elif mood == "cautious":
            weight -= 0.05

        threshold = 0.60 + random.uniform(-0.03, 0.03)

        approve = weight >= threshold
        reason = f"{'Supports' if approve else 'Rejects'} based on mood '{mood}' and experience level {experience}."

        return ("approve" if approve else "reject"), reason

    def finalize_verdict(self):
        """Tally votes and determine if trade is approved."""
        approvals = sum(1 for v in self.vote_record if v["vote"] == "approve")
        rejections = len(self.vote_record) - approvals

        result = "approved" if approvals > rejections else "rejected"
        log_event("Council Verdict Finalized", {
            "approved": approvals,
            "rejected": rejections,
            "final_verdict": result
        })

        return {
            "result": result,
            "votes": self.vote_record,
            "approvals": approvals,
            "rejections": rejections
        }