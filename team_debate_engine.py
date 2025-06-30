from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: team_debate_engine.py ===
import json
from datetime import datetime
import os

DEBATE_LOG = "team_intel/debate_log.json"
os.makedirs("team_intel", exist_ok=True)

def start_debate(topic, participants):
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "topic": topic,
        "participants": participants,
        "arguments": [],
        "winner": None
    }

def add_argument(debate, bot_name, claim, evidence):
    debate["arguments"].append({
        "bot": bot_name,
        "claim": claim,
        "evidence": evidence,
        "timestamp": datetime.utcnow().isoformat(),
    })

def resolve_debate(debate):
    # Simple logic: count the length of evidence as a proxy for "depth"
    winner = max(debate["arguments"], key=lambda x: len(x["evidence"].split()))
    debate["winner"] = winner["bot"]

    if not os.path.exists(DEBATE_LOG):
        with open(DEBATE_LOG, "w") as f:
            json.dump([], f, indent=2)

    with open(DEBATE_LOG, "r") as f:
        debates = json.load(f)
    debates.append(debate)

    with open(DEBATE_LOG, "w") as f:
        json.dump(debates, f, indent=2)

    print(f"[DEBATE] Winner: {debate['winner']} on topic '{debate['topic']}'")
    return debate["winner"]

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():