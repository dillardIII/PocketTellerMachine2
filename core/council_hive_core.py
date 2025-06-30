from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: core/council_hive_core.py ===
"""
Council Hive Core:
Multi-agent collaboration system. Allows assistant personas to contribute, vote, and co-write decisions.
"""

import json
import random
from datetime import datetime

COUNCIL_LOG = "memory/council_votes.json"
COUNCIL_AGENTS = {
    "Mentor": {"weight": 0.9, "mood": "calm"},
    "Mo Cash": {"weight": 0.75, "mood": "aggressive"},
    "Strategist": {"weight": 0.85, "mood": "cautious"},
    "Shadow": {"weight": 0.7, "mood": "calculating"},
    "Optimist": {"weight": 0.8, "mood": "hopeful"},
    "Drill Instructor": {"weight": 0.6, "mood": "strict"}
}

def log_vote(topic, votes):
    log = []
    if os.path.exists(COUNCIL_LOG):
        with open(COUNCIL_LOG, "r") as f:
            log = json.load(f)

    log.append({
        "timestamp": datetime.utcnow().isoformat(),
        "topic": topic,
        "votes": votes
    })

    with open(COUNCIL_LOG, "w") as f:
        json.dump(log[-200:], f, indent=2)

def cast_votes(topic: str, options: list):
    votes = {}
    for persona, traits in COUNCIL_AGENTS.items():
        choice = random.choices(options, weights=[traits["weight"]] * len(options))[0]
        votes[persona] = {
            "vote": choice,
            "mood": traits["mood"]
        }

    log_vote(topic, votes)
    result = max(set([v["vote"] for v in votes.values()]), key=lambda o: list(v["vote"] for v in votes.values()).count(o))
    return result, votes

def run_council(topic, options):
    print(f"[Council] 🧠 Discussing: {topic}")
    decision, full_votes = cast_votes(topic, options)
    print(f"[Council] ✅ Final Decision: {decision}")
    return decision

# Example run
if __name__ == "__main__":
    run_council("New trade strategy", ["Momentum Boost", "Risk-Off", "Iron Condor"])