# assistant_interaction_matrix.py
# Purpose: Create persona-to-persona interactions for PTM's internal council logic
# Enables AI assistants to debate, challenge, teach, and influence one another

import random
import json
from datetime import datetime
from utils.logger import log_event

class AssistantInteractionMatrix:
    def __init__(self):
        self.personas = ["Mo Cash", "The Mentor", "Drill Instructor", "The Strategist", "The Shadow"]
        self.relationship_map = self._default_relationship_map()

    def _default_relationship_map(self):
        return {
            "Mo Cash": {
                "The Mentor": "respects",
                "Drill Instructor": "argues_with",
                "The Strategist": "competes_with",
                "The Shadow": "distrusts"
            },
            "The Mentor": {
                "Mo Cash": "guides",
                "Drill Instructor": "balances",
                "The Strategist": "collaborates_with",
                "The Shadow": "observes"
            },
            "Drill Instructor": {
                "Mo Cash": "corrects",
                "The Mentor": "questions",
                "The Strategist": "compares",
                "The Shadow": "warns"
            },
            "The Strategist": {
                "Mo Cash": "challenges",
                "The Mentor": "supports",
                "Drill Instructor": "aligns_with",
                "The Shadow": "analyzes"
            },
            "The Shadow": {
                "Mo Cash": "undermines",
                "The Mentor": "respects_silently",
                "Drill Instructor": "avoids",
                "The Strategist": "counters"
            }
        }

    def simulate_conversation(self, topic):
        """Generate a multi-persona council discussion around a trade or lesson topic."""
        convo = []
        starters = random.sample(self.personas, 3)

        for persona in starters:
            for target in self.personas:
                if persona == target:
                    continue

                relation = self.relationship_map[persona].get(target, "neutral")
                message = self._generate_message(persona, target, topic, relation)
                convo.append({
                    "speaker": persona,
                    "to": target,
                    "relation": relation,
                    "topic": topic,
                    "message": message
                })

        log_event("Council Conversation", {"topic": topic, "lines": len(convo)})
        return convo

    def _generate_message(self, speaker, target, topic, relation):
        """Craft a simple response line based on relationship and context."""
        templates = {
            "respects": f"{speaker} says: '{target} brings wisdom to this trade.'",
            "guides": f"{speaker} says: 'Let me explain to {target} why this matters.'",
            "argues_with": f"{speaker} says: 'No way, {target} is missing the real signal here.'",
            "competes_with": f"{speaker} says: 'Let’s see who nails the better entry point, {target}.'",
            "distrusts": f"{speaker} says: 'I don’t trust {target} on this play.'",
            "supports": f"{speaker} says: 'I agree with {target}, this logic checks out.'",
            "corrects": f"{speaker} says: 'Stand down, {target}, your logic is flawed.'",
            "balances": f"{speaker} says: 'Easy, {target}. Let’s look at the bigger picture.'",
            "observes": f"{speaker} watches {target} and says nothing... for now.",
            "warns": f"{speaker} says: 'Danger zone, {target}. Tread lightly.'",
            "counters": f"{speaker} says: 'I see an alternate angle to {target}’s view.'",
            "neutral": f"{speaker} says: 'Let’s analyze this play without bias.'"
        }

        return templates.get(relation, f"{speaker} discusses the topic: {topic}")

# --- Manual Run Example ---
if __name__ == "__main__":
    matrix = AssistantInteractionMatrix()
    convo = matrix.simulate_conversation("AAPL breakout strategy")
    print(json.dumps(convo, indent=4))