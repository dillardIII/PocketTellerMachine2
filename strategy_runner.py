# === FILE: strategy_runner.py ===

from trading_engine import execute_trade
from cole_logger import log_info
from cole_task_queue import add_task

def run_strategy(strategy):
    """
    Executes the selected strategy and performs all linked actions.
    Logs and triggers tasks based on strategy type.
    """
    if not strategy:
        log_info("[Strategy Runner] ❌ No strategy provided.")
        return

    try:
        name = strategy.get("name", "Unnamed Strategy")
        strategy_type = strategy.get("type", "neutral")

        log_info(f"[Strategy Runner] 🚀 Running strategy: {name} ({strategy_type})")

        # Trigger key trade execution logic
        execute_trade(strategy)

        # Add post-trade tasks
        if strategy_type == "bullish":
            add_task("Monitor for bullish continuation")
        elif strategy_type == "bearish":
            add_task("Set trailing stop")
        else:
            add_task("General review")

        # Final confirmation log
        print(f"[Strategy Runner] Strategy execution complete: {name}")

    except Exception as e:
        log_info(f"[Strategy Runner] ❌ Error executing strategy: {str(e)}")