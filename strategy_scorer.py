import json
import os

def load_backtest_results():
    path = "data/backtest_results.json"
    if not os.path.exists(path):
        return []

    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return []

def score_strategy(result):
    # Basic scoring weights
    win_rate = result.get("win_rate", 0)
    pnl = result.get("total_pnl", result.get("return_pct", 0))
    trades = result.get("trades", 1)
    grade = result.get("grade", "D")

    grade_map = {"A": 25, "B": 15, "C": 5, "D": 0, "F": -15}
    score = (win_rate * 0.5) + (pnl * 0.3) + (grade_map.get(grade, 0)) + (trades * 0.1)

    return round(score, 2)

def recommend_best_strategy():
    results = load_backtest_results()
    if not results:
        return {"strategy": None, "reason": "No backtest results found."}

    scored = []
    for r in results:
        r["score"] = score_strategy(r)
        scored.append(r)

    sorted_strategies = sorted(scored, key=lambda x: x["score"], reverse=True)

    best = sorted_strategies[0] if sorted_strategies else None
    return {
        "strategy": best["strategy"],
        "score": best["score"],
        "win_rate": best.get("win_rate"),
        "pnl": best.get("total_pnl", best.get("return_pct")),
        "trades": best.get("trades"),
        "grade": best.get("grade"),
        "details": best
    }