# === FILE: cole_autopilot_cycle.py ===

from strategy_scorer import recommend_best_strategy
from strategy_executor import run_trade_with_strategy, analyze_trade_result, log_trade_outcome
from phase_manager import get_current_phase
from cole_brain_logger import log_strategy_reason

def cole_autopilot_cycle():
    print("[2025-05-25] Cole: Starting Full Autopilot Cycle...")

    # Determine phase
    current_phase = get_current_phase()
    print(f"[Cole Autopilot] Current Phase: {current_phase}")

    # Recommend a strategy
    recommendation = recommend_best_strategy()
    strategy = recommendation.get("strategy", "None")
    reason = recommendation.get("reason", "No explanation")

    log_strategy_reason(strategy=strategy, reason=reason)

    if strategy == "None":
        print("[Strategy Runner] No strategy available.")
        return

    # Run trade
    result = run_trade_with_strategy(strategy)
    analysis = analyze_trade_result(result)

    # Log result
    log_trade_outcome(strategy, result, analysis)