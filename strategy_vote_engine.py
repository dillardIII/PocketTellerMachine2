from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: strategy_vote_engine.py ===
import os
import json
import random
from strategy_thread_logger import get_thread_log_path

VOTERS = {
    "Mentor": "conservative",
    "MoCash": "aggressive",
    "Strategist": "balanced",
    "ChillTrader": "risk-averse"
}

VOTE_LOG_DIR = "strategy_votes"
os.makedirs(VOTE_LOG_DIR, exist_ok=True)

def cast_vote(bot_name, thread):
    votes = {
        "conservative": "v1",
        "aggressive": "vX-suggested",
        "balanced": random.choice(["v1", "v2", "vX-suggested"]),
        "risk-averse": "v1" if "exit" in thread["history"][-1]["notes"].lower() else "hold":
    }

    logic = VOTERS.get(bot_name, "balanced")
    chosen = votes.get(logic, "v1")
    return chosen

def run_strategy_vote(thread_file):
    if not os.path.exists(thread_file):
        return "Thread file not found."

    with open(thread_file, "r") as f:
        thread = json.load(f)

    vote_results = {}
    for bot in VOTERS:
        vote = cast_vote(bot, thread)
        vote_results.setdefault(vote, []).append(bot)

    # Save vote summary
    summary = {
        "strategy": thread["thread_id"],
        "votes": vote_results
    }

    file_name = os.path.basename(thread_file).replace(".json", "_votes.json")
    path = os.path.join(VOTE_LOG_DIR, file_name)
    with open(path, "w") as f:
        json.dump(summary, f, indent=2)

    winner = max(vote_results.items(), key=lambda x: len(x[1]))[0]
    print(f"[VOTE] Winning version: {winner}")
    return winner, vote_results

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():