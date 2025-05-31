# === FILE: master_autonomy_loop.py ===

from cole_autopilot_cycle import cole_autopilot_cycle
from strategy_scorer import recommend_best_strategy
from phase_manager import set_phase
from cole_brain import log_memory
import traceback

def master_autonomy_loop():
    print("[PTM Autonomy] Starting master autonomy loop...")

    try:
        # Set initial phase
        set_phase("startup")

        # Run Cole's autopilot logic
        cole_autopilot_cycle()

        # Recommend strategy
        strategy_bundle = recommend_best_strategy()

        if not strategy_bundle or not strategy_bundle.get("strategy"):
            print("[Strategy Runner] No strategy available. Skipping execution.")
            log_memory("strategy", None)
            return

        strategy = strategy_bundle.get("strategy")
        reason = strategy_bundle.get("reason", "No reason provided.")

        print(f"[Strategy Runner] Recommended Strategy: {strategy} | Reason: {reason}")
        log_memory("strategy", strategy)

        # Optional: Insert strategy execution logic here

    except Exception as e:
        print(f"[PTM Autonomy] ERROR in loop: {e}")
        traceback.print_exc()
        # Optional: Log or recover depending on severity

    print("[PTM Autonomy] Master autonomy loop complete.")