"""
Cole Autopilot Cycle:
This module defines the core cycle for PTM's autonomous assistant loop.
Executes strategy recommendation, trade logic, and memory logging.
"""

from strategy_scorer import recommend_best_strategy
from trade_executor import execute_trade_flow
from cole_logger import log_event
from cole_brain import log_memory

def cole_autopilot_cycle():
    """
    Runs the main decision-making and trade execution logic.
    Can be extended with more layers: signals, filters, AI modules.
    """
    log_event("Cole Autopilot", "🧠 Starting autopilot decision cycle...", "info")

    try:
        # Step 1: Recommend a strategy
        strategy_bundle = recommend_best_strategy()

        if not strategy_bundle or not strategy_bundle.get("strategy"):
            log_event("Cole Autopilot", "❌ No strategy was returned.", "error")
            log_memory("autopilot", "No strategy recommended.")
            return

        strategy = strategy_bundle["strategy"]
        reason = strategy_bundle.get("reason", "No reason provided.")

        log_event("Cole Autopilot", f"✅ Strategy: {strategy['name']} | Reason: {reason}", "info")
        log_memory("autopilot_strategy", strategy)

        # Step 2: Execute trade flow
        execute_trade_flow(strategy)

        log_event("Cole Autopilot", "✅ Autopilot cycle completed.", "success")

    except Exception as e:
        log_event("Cole Autopilot", f"❌ Error during autopilot: {str(e)}", "error")
        log_memory("autopilot_error", {"error": str(e)})