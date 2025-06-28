"""
Council Protocol
Assistant personas analyze high-impact decisions, cast weighted votes,
and generate a unified response with rationale.
"""

import random
from datetime import datetime

COUNCIL_LOG = "memory/council_votes.json"

# Sample personas with voting weights
PERSONAS = {
    "mentor": 1.0,
    "mo_cash": 1.2,
    "strategist": 1.3,
    "drill_instructor": 0.8,
    "shadow": 1.1,
    "optimist": 1.0
}

def evaluate_decision(prompt):
    votes = {}
    reasons = {}

    for name, weight in PERSONAS.items():
        opinion = random.choice(["yes", "no"])
        votes[name] = {"vote": opinion, "weight": weight}
        reasons[name] = f"{name.title()} voted '{opinion}' based on {generate_reason(name, prompt)}"

    log_council_vote(prompt, votes)

    return {
        "decision": final_vote(votes),
        "rationale": reasons
    }

def generate_reason(name, prompt):
    if "risk" in prompt.lower():
        return "perceived trade risk level"
    if "spend" in prompt.lower():
        return "capital preservation logic"
    if "teach" in prompt.lower():
        return "educational priority protocol"
    return "instinct tied to AI profile"

def final_vote(votes):
    score = sum((1 if v["vote"] == "yes" else -1) * v["weight"] for v in votes.values())
    return "approved" if score >= 0 else "rejected"

def log_council_vote(prompt, votes):
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "votes": votes
    }

    if not os.path.exists(COUNCIL_LOG):
        history = []
    else:
        with open(COUNCIL_LOG, "r") as f:
            history = json.load(f)

    history.append(record)

    with open(COUNCIL_LOG, "w") as f:
        json.dump(history[-300:], f, indent=2)

    print(f"[Council] 🗳️ Vote logged for: '{prompt}'")

# Optional manual test
if __name__ == "__main__":
    outcome = evaluate_decision("Should we deploy the new auto-trade protocol?")
    print(outcome)