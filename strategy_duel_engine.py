from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: strategy_duel_engine.py ===
import importlib.util
import os
import random

DUEL_RESULTS_DIR = "duel_logs"
os.makedirs(DUEL_RESULTS_DIR, exist_ok=True)

def load_strategy_module(file_path):
    name = os.path.splitext(os.path.basename(file_path))[0]
    spec = importlib.util.spec_from_file_location(name, file_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def simulate_trade(data_point, strategy_func):
    try:
        decision = strategy_func(data_point)
        return decision
    except Exception as e:
        return f"error: {e}"

def generate_market_data(n=10):
    data = []
    for _ in range(n):
        data.append({
            "price": random.randint(160, 200),
            "volume": random.randint(1000, 10000),
            "rsi": random.randint(10, 90),
            "macd": random.choice(["bullish", "bearish", "neutral"]),
            "5MA": random.randint(160, 200),
            "20MA": random.randint(160, 200)
        })
    return data

def score_strategy(results):
    score = 0
    for r in results:
        if "Buy" in r:
            score += 1
        elif "Sell" in r:
            score -= 1
    return score

def run_strategy_duel(file_a, file_b, rounds=10):
    strat_a = load_strategy_module(file_a)
    strat_b = load_strategy_module(file_b)

    data_stream = generate_market_data(rounds)

    results_a = []
    results_b = []

    for data in data_stream:
        res_a = simulate_trade(data, strat_a.run_strategy)
        res_b = simulate_trade(data, strat_b.run_strategy)
        results_a.append(res_a)
        results_b.append(res_b)

    score_a = score_strategy(results_a)
    score_b = score_strategy(results_b)

    winner = "A" if score_a > score_b else "B" if score_b > score_a else "Draw":
:
    log = {
        "strategy_A": os.path.basename(file_a),
        "strategy_B": os.path.basename(file_b),
        "score_A": score_a,
        "score_B": score_b,
        "winner": winner,
        "results_A": results_a,
        "results_B": results_b
    }

    filename = f"{os.path.basename(file_a).split('.')[0]}_vs_{os.path.basename(file_b).split('.')[0]}.json"
    path = os.path.join(DUEL_RESULTS_DIR, filename)
    with open(path, "w") as f:
        import json
        json.dump(log, f, indent=2)

    print(f"[DUEL] {log['strategy_A']} vs {log['strategy_B']} — Winner: {winner}")
    return winner, log

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():