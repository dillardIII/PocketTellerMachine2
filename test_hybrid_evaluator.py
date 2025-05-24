import json
from test_hybrid_backtest import test_hybrid_performance

def evaluate_and_promote_hybrids():
    try:
        with open("data/cole_hybrid_strategies.json", "r") as f:
            hybrids = [json.loads(line) for line in f]
    except:
        print("[ERROR]: No hybrid strategies found.")
        return

    for hybrid in hybrids:
        performance = test_hybrid_performance()

        if performance["win_rate"] >= 60:
            print(f"[PROMOTED HYBRID]: {hybrid['key']} → Performance: {performance}")
        else:
            print(f"[FAILED HYBRID]: {hybrid['key']} → Performance: {performance}")

# Run evaluator
evaluate_and_promote_hybrids()