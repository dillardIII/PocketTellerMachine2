# === FILE: strategy_scorer.py ===

import json
import os
from datetime import datetime

STRATEGY_LOG = "data/strategy_scores.json"
BACKTEST_FILE = "memory/backtest_results.json"

# === Score strategies based on win rate + confidence ===
def score_strategies(strategies):
    """
    Scores a list of strategies based on win rate and confidence.
    Adds a 'score' key to each strategy.
    Saves the scored strategies to a JSON file.
    Returns the list sorted by score descending.
    """
    scored = []
    for s in strategies:
        score = s.get("win_rate", 50) + s.get("confidence", 0)
        s["score"] = score
        scored.append(s)
    save_scores(scored)
    return sorted(scored, key=lambda x: x["score"], reverse=True)

# === Save strategy scores to disk ===
def save_scores(strategies):
    try:
        os.makedirs("data", exist_ok=True)
        with open(STRATEGY_LOG, "w") as f:
            json.dump(strategies, f, indent=2)
        print(f"[Strategy Scorer] ✅ Saved {len(strategies)} strategy scores.")
    except Exception as e:
        print(f"[Strategy Scorer] ❌ Failed to save strategy scores: {e}")

# === Recommend Best Strategy from Backtest or Scored List ===
def recommend_best_strategy():
    """
    Recommends a strategy by checking backtest results first,
    falling back to scored strategy file if needed.
    Always returns a consistent dictionary.
    """
    # === Try Backtest First ===
    try:
        if os.path.exists(BACKTEST_FILE):
            with open(BACKTEST_FILE, "r") as f:
                backtest_data = json.load(f)

            if isinstance(backtest_data, list) and len(backtest_data) > 0:
                sorted_data = sorted(backtest_data, key=lambda x: x.get("total_profit", 0), reverse=True)
                top = sorted_data[0]
                strategy = top.get("strategy")
                profit = top.get("total_profit")

                if strategy:
                    reason = f"Top performer in backtests with profit: {profit}"
                    print(f"[Strategy Scorer] ✅ Selected from backtest: {strategy} | {reason}")
                    return {"strategy": strategy, "reason": reason}
                else:
                    print("[Strategy Scorer] ⚠️ Top backtest entry missing strategy.")
    except Exception as e:
        print(f"[Strategy Scorer] ⚠️ Backtest error: {e}")

    # === Fallback to Strategy Scores ===
    try:
        if not os.path.exists(STRATEGY_LOG):
            return {"strategy": None, "reason": "No strategy scores available."}

        with open(STRATEGY_LOG, "r") as f:
            scored_data = json.load(f)

        if not scored_data:
            return {"strategy": None, "reason": "Strategy score list is empty."}

        sorted_strats = sorted(scored_data, key=lambda x: x.get("score", 0), reverse=True)
        best = sorted_strats[0]
        return {
            "strategy": best.get("strategy", "Unknown"),
            "reason": f"Top fallback score: {best.get('score', 0)}"
        }
    except Exception as e:
        print(f"[Strategy Scorer] ❌ Failed to recommend fallback strategy: {e}")
        return {"strategy": None, "reason": "Error during fallback strategy scoring."}