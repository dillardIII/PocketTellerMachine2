from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from datetime import datetime

LEADERBOARD_FILE = "data/strategy_leaderboard.json"
PROMOTIONS_LOG = "data/cole_memory.json"

# === Load all promotion logs from memory ===
def load_promoted_strategies():
    if not os.path.exists(PROMOTIONS_LOG):
        return []

    with open(PROMOTIONS_LOG, "r") as f:
        try:
            memory = json.load(f)
        except json.JSONDecodeError:
            return []

    promos = memory.get("strategy_promotions", [])
    return promos[-100:]  # Limit to most recent 100 promotions

# === Build sorted leaderboard ===
def build_leaderboard():
    strategies = load_promoted_strategies()
    leaderboard = {}

    for entry in strategies:
        strat = entry["strategy"]
        win_rate = entry.get("win_rate", 0)
        wins = entry.get("wins", 0)

        if strat not in leaderboard:
            leaderboard[strat] = {
                "strategy": strat,
                "total_wins": 0,
                "avg_win_rate": 0,
                "entries": 0
            }

        lb_entry = leaderboard[strat]
        lb_entry["total_wins"] += wins
        lb_entry["avg_win_rate"] += win_rate
        lb_entry["entries"] += 1

    # Finalize averages
    for strat in leaderboard:
        lb_entry = leaderboard[strat]
        lb_entry["avg_win_rate"] = round(lb_entry["avg_win_rate"] / lb_entry["entries"], 2)

    sorted_leaderboard = sorted(
        leaderboard.values(),
        key=lambda x: (x["avg_win_rate"], x["total_wins"]),
        reverse=True
    )

    return sorted_leaderboard

# === Save to JSON ===
def save_leaderboard_snapshot():
    leaderboard = build_leaderboard()
    snapshot = {
        "timestamp": datetime.now().isoformat(),
        "leaderboard": leaderboard
    }

    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(snapshot, f, indent=2)

    print(f"[LEADERBOARD] Snapshot saved to {LEADERBOARD_FILE}")

# === Optional: Print top 5 ===
def print_top_strategies(n=5):
    leaderboard = build_leaderboard()
    print(f"\n=== Top {n} Strategies ===")
    for entry in leaderboard[:n]:
        print(f"{entry['strategy']}: {entry['avg_win_rate']} win rate, {entry['total_wins']} wins")

# === Real-time Trade Logger ===
def load_leaderboard_live():
    if not os.path.exists(LEADERBOARD_FILE):
        return {}
    with open(LEADERBOARD_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return {}

def save_leaderboard_live(data):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=2)

def update_leaderboard_with_trade(trade):
    if not trade.get("strategy") or not trade.get("result"):
        return

    board = load_leaderboard_live()
    strat = trade["strategy"]
    result = trade["result"]

    if strat not in board:
        board[strat] = {
            "strategy": strat,
            "wins": 0,
            "losses": 0,
            "last_updated": None
        }

    if result == "win":
        board[strat]["wins"] += 1
    elif result == "loss":
        board[strat]["losses"] += 1

    board[strat]["last_updated"] = datetime.now().isoformat()
    save_leaderboard_live(board)

def log_event():ef drop_files_to_bridge():