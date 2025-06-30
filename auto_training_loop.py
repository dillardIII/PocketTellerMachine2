from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: auto_training_loop.py ===
import os
from strategy_duel_engine import run_strategy_duel
from strategy_mutator import mutate_strategy

TRAINING_LOG_DIR = "duel_logs"
os.makedirs(TRAINING_LOG_DIR, exist_ok=True)

def train_strategy_until_win(loser_path, champion_path, max_generations=5, required_wins=3):
    wins = 0
    gen = 0
    current_path = loser_path
    history = []

    while gen < max_generations and wins < required_wins:
        gen += 1
        print(f"\n[TRAINING] Generation {gen}: {os.path.basename(current_path)} vs {os.path.basename(champion_path)}")

        winner, log = run_strategy_duel(current_path, champion_path)

        history.append({
            "generation": gen,
            "strategy": os.path.basename(current_path),
            "score": f"A:{log['score_A']} | B:{log['score_B']}",
            "winner": winner
        })

        if winner == "A":
            wins += 1
        else:
            wins = 0  # reset streak

        if wins >= required_wins:
            print(f"[EVOLUTION COMPLETE] {os.path.basename(current_path)} survived!")
            return current_path, history

        mutated = mutate_strategy(current_path, bot_name="Evolver")
        if not mutated:
            print("[TRAINING] No mutations made. Training stopped.")
            break
        current_path = mutated

    print("[TRAINING] Max generations reached.")
    return current_path, history

def log_event():ef drop_files_to_bridge():