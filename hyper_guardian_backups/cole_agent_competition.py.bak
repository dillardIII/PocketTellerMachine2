import random
from datetime import datetime

# === Agent Performance Memory ===
AGENT_SCORES = {
    "Strategist": {"wins": 0, "losses": 0, "profit": 0},
    "Hustler": {"wins": 0, "losses": 0, "profit": 0},
    "Mentor": {"correct_calls": 0, "wrong_calls": 0},
    "Shadow": {"conflict_resolved": 0}
}

# === Record Trade Result & Update Stats ===
def record_trade_result(agent, result):
    if result > 0:
        AGENT_SCORES[agent]["wins"] += 1
        AGENT_SCORES[agent]["profit"] += result
    else:
        AGENT_SCORES[agent]["losses"] += 1
        AGENT_SCORES[agent]["profit"] += result
    print(f"[{agent} REPORT]: Updated stats — {AGENT_SCORES[agent]}")

# === Agent Emotional Reaction ===
def agent_brag_or_panic(agent):
    stats = AGENT_SCORES[agent]
    if stats["wins"] > stats["losses"]:
        print(f"[{agent}]: I'm on fire! You can't beat me today!")
    else:
        print(f"[{agent}]: Okay... okay... Maybe I'm off today. Need to rethink...")

# === Display Agent Leaderboard ===
def show_leaderboard():
    print("\n=== AGENT LEADERBOARD ===")
    sorted_agents = sorted(AGENT_SCORES.items(), key=lambda x: x[1].get("profit", 0), reverse=True)
    for agent, score in sorted_agents:
        print(f"{agent}: Wins {score.get('wins', 0)}, Losses {score.get('losses', 0)}, Profit {round(score.get('profit', 0), 2)}")
    print("=========================\n")