"""
Strategy Scorer:
This module evaluates available trading strategies based on
market data, risk profiles, and AI signal layers. It returns
the most optimal strategy with context and reasoning.
"""

from cole_logger import log_event
from cole_brain import log_memory

# Sample strategy pool
STRATEGY_POOL = [
    {"name": "Iron Condor", "type": "neutral", "risk": "medium"},
    {"name": "Credit Spread", "type": "bearish", "risk": "low"},
    {"name": "Covered Call", "type": "bullish", "risk": "low"},
    {"name": "Iron Butterfly", "type": "neutral", "risk": "high"},
    {"name": "Straddle", "type": "volatile", "risk": "high"},
]

def score_strategy(strategy):
    """
    Placeholder scoring logic.
    Expand this to consider technical signals, macro events, and AI insights.
    """
    score = 0

    if strategy["risk"] == "low":
        score += 3
    elif strategy["risk"] == "medium":
        score += 2
    elif strategy["risk"] == "high":
        score += 1

    if strategy["type"] == "neutral":
        score += 2
    elif strategy["type"] == "bullish":
        score += 1

    return score

def recommend_best_strategy():
    """
    Returns the highest-scoring strategy bundle.
    Can be enhanced with filters, AI classifiers, and simulation results.
    """
    log_event("Strategy Scorer", "🔎 Evaluating strategies...", "info")

    if not STRATEGY_POOL:
        log_event("Strategy Scorer", "⚠️ No strategies available.", "warn")
        return None

    scored = []
    for strat in STRATEGY_POOL:
        score = score_strategy(strat)
        strat["score"] = score
        scored.append(strat)

    top = sorted(scored, key=lambda x: x["score"], reverse=True)[0]
    log_event("Strategy Scorer", f"📈 Selected: {top['name']} (score: {top['score']})", "success")

    result = {
        "strategy": top,
        "reason": f"{top['name']} had the highest score of {top['score']}."
    }
    log_memory("strategy_scorer", result)
    return result

# Manual run
if __name__ == "__main__":
    result = recommend_best_strategy()
    if result:
        print(f"Strategy: {result['strategy']['name']} | Reason: {result['reason']}")
    else:
        print("❌ No strategy recommended.")