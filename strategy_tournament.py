from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: strategy_tournament.py ===
import os
import random
from strategy_duel_engine import run_strategy_duel

TOURNAMENT_LOG_DIR = "tournament_logs"
os.makedirs(TOURNAMENT_LOG_DIR, exist_ok=True)

def run_tournament(strategies):
    if len(strategies) < 2:
        print("[TOURNAMENT] Need at least 2 strategies.")
        return

    round_num = 1
    bracket = strategies[:]
    random.shuffle(bracket)

    history = []

    while len(bracket) > 1:
        print(f"\n🎯 TOURNAMENT ROUND {round_num}")
        next_round = []

        for i in range(0, len(bracket), 2):
            if i + 1 >= len(bracket):
                # Bye
                next_round.append(bracket[i])
                continue

            strat_a = bracket[i]
            strat_b = bracket[i + 1]

            winner, log = run_strategy_duel(strat_a, strat_b)

            winning_path = strat_a if winner == "A" else strat_b if winner == "B" else random.choice([strat_a, strat_b]):
            next_round.append(winning_path)

            history.append({
                "round": round_num,
                "match": f"{os.path.basename(strat_a)} vs {os.path.basename(strat_b)}",
                "winner": os.path.basename(winning_path),
                "log": log
            })

        bracket = next_round
        round_num += 1

    final_winner = bracket[0]
    print(f"\n🏆 TOURNAMENT CHAMPION: {os.path.basename(final_winner)}")

    # Save full tournament log
    file_path = os.path.join(TOURNAMENT_LOG_DIR, "tournament_history.json")
    with open(file_path, "w") as f:
        import json
        json.dump(history, f, indent=2)

    return final_winner, history

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():