# === FILE: cole_autopilot_cycle.py ===

from strategy_scorer import recommend_best_strategy
from strategy_runner import run_strategy
from cole_brain import log_strategy_reason, log_memory
from cole_logger import log_info

def cole_autopilot_cycle():
    log_info("[Cole Autopilot] 🚀 Starting Cole Autopilot Cycle...")

    strategy_bundle = recommend_best_strategy()

    # === 💡 Force fallback if strategy is missing ===
    if not strategy_bundle or not strategy_bundle.get("strategy"):
        log_info("[Cole Autopilot] ⚠️ No valid strategy to run. Injecting fallback strategy.")
        strategy_bundle = {
            "strategy": {
                "name": "Fallback Covered Call",
                "type": "bullish",
                "win_rate": 68,
                "confidence": 20
            },
            "reason": "Fallback injected due to missing backtest data."
        }

    strategy = strategy_bundle["strategy"]
    reason = strategy_bundle.get("reason", "No reason provided.")

    log_memory("strategy", strategy)
    log_strategy_reason(strategy, reason)

    log_info(f"[Cole Autopilot] ✅ Strategy selected: {strategy['name']} | Reason: {reason}")
    run_strategy(strategy)