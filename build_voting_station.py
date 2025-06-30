from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: build_voting_station.py ===
import os
import json
from datetime import datetime

VOTE_LOG = "evolution/vote_log.json"
CHAMPION_FILE = "evolution/current_champion.txt"
os.makedirs("evolution", exist_ok=True)

def cast_vote(voter, candidates, preferred, reason=""):
    if preferred not in candidates:
        raise ValueError(f"Preferred build '{preferred}' not in candidate list.")

    vote_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "voter": voter,
        "candidates": candidates,
        "chosen": preferred,
        "reason": reason
    }

    if not os.path.exists(VOTE_LOG):
        with open(VOTE_LOG, "w") as f:
            json.dump([], f, indent=2)

    with open(VOTE_LOG, "r") as f:
        votes = json.load(f)
    votes.append(vote_entry)

    with open(VOTE_LOG, "w") as f:
        json.dump(votes, f, indent=2)

    print(f"[VOTE] {voter} voted for {preferred} as best build.")
    return preferred

def promote_champion(build_name):
    with open(CHAMPION_FILE, "w") as f:
        f.write(build_name)
    print(f"[🏆] Promoted champion: {build_name}")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():