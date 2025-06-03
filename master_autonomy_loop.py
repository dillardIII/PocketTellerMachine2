# === FILE: master_autonomy_loop.py ===

from cole_autopilot_cycle import cole_autopilot_cycle
from strategy_scorer import recommend_best_strategy
from phase_manager import set_phase
from cole_brain import log_memory
import traceback
from datetime import datetime

def log_status(message):
    with open("logs/autonomy_status.log", "a") as f:
        f.write(f"{datetime.utcnow().isoformat()} – {message}\n")

def master_autonomy_loop():
    print("[PTM Autonomy] Starting master autonomy loop...")
    log_status("🟢 Starting master autonomy loop...")

    try:
        # Set initial phase
        set_phase("startup")
        log_status("📡 Phase set to 'startup'.")

        # Run Cole's autopilot logic
        cole_autopilot_cycle()
        log_status("🧠 Cole autopilot cycle complete.")

        # Recommend strategy
        strategy_bundle = recommend_best_strategy()
        log_status("📊 Strategy recommendation received.")

        if not strategy_bundle or not strategy_bundle.get("strategy"):
            print("[Strategy Runner] No strategy available. Skipping execution.")
            log_memory("strategy", None)
            log_status("⚠️ No strategy selected.")
            return

        strategy = strategy_bundle.get("strategy")
        reason = strategy_bundle.get("reason", "No reason provided.")

        print(f"[Strategy Runner] Recommended Strategy: {strategy} | Reason: {reason}")
        log_memory("strategy", strategy)
        log_status(f"✅ Strategy selected: {strategy} – Reason: {reason}")

        # Optional: Insert strategy execution logic here

    except Exception as e:
        print(f"[PTM Autonomy] ERROR in loop: {e}")
        traceback.print_exc()
        log_status(f"❌ ERROR: {e}")

    print("[PTM Autonomy] Master autonomy loop complete.")
    log_status("🏁 Master autonomy loop complete.")