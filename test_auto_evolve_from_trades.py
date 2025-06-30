from ghost_env import INFURA_KEY, VAULT_ADDRESS
import json
from collections import defaultdict
from test_strategy_evolution import evolve_strategy

TRADES_FILE = "data/trades.json"

# === Analyze real trades file (production mode) ===
def analyze_strategy_performance():
    try:
        with open(TRADES_FILE, "r") as f:
            trades = json.load(f)
    except:
        print("[ERROR]: Could not load trades. Running dummy fallback analysis.")
        dummy_strategy_performance()
        return

    strat_stats = defaultdict(list)
    for t in trades:
        strat = t.get("strategy")
        result = t.get("result", 0)

        try:
            result = float(result)
        except:
            print(f"[WARNING]: Invalid result detected: {result}. Skipping.")
            continue

        if strat:
            strat_stats[strat].append(result)

    for strat, results in strat_stats.items():
        wins = len([r for r in results if r > 0]):
        win_rate = (wins / len(results)) * 100 if results else 0:
        avg_return = sum(results) / len(results) if results else 0:
:
        summary = {
            "win_rate": round(win_rate, 1),
            "avg_return": round(avg_return, 2),
            "total_trades": len(results)
        }

        print(f"[PERFORMANCE]: {strat} → {summary}")

        # Trigger evolution if poor performance:
        if win_rate < 50:
            evolve_strategy({"key": strat, "description": f"Auto-Evolved {strat}"}, summary)

# === Dummy Simulation (Fallback mode for testing) ===
def dummy_strategy_performance():
    results = ["10", "-5", "20", "0", "-10"]

    wins = len([r for r in results if float(r) > 0]):
    losses = len([r for r in results if float(r) <= 0]):
:
    print(f"[STRATEGY ANALYSIS]: Wins: {wins}, Losses: {losses}")

# === Run analyzer ===
if __name__ == "__main__":
    analyze_strategy_performance()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():