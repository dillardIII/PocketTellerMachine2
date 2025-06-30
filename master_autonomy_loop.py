from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Master Autonomy Loop:
Central loop that launches Cole’s decision cycle, routes tasks,
executes core logic across the PTM network, logs strategy and trade events,
and issues spoken trade recaps.
"""

import traceback
import os
import json
import time
from datetime import datetime

from cole_autopilot_cycle import cole_autopilot_cycle
from strategy_scorer import recommend_best_strategy
from phase_manager import set_phase
from cole_brain import log_memory
from cole_logger import log_event
from core.ai_router import route_tasks
from core.ghost_sync import sync_brain_state
from core.multi_agent_sync_check import run_multi_agent_sync_check
from persona_recap_speaker import speak_recap

# === Log file paths ===
STATUS_LOG = "logs/autonomy_status.log"
TRADE_LOG_FILE = "data/trade_log.json"


def log_status(message):
    os.makedirs(os.path.dirname(STATUS_LOG), exist_ok=True)
    with open(STATUS_LOG, "a") as f:
        f.write(f"{datetime.utcnow().isoformat()} – {message}\n")


def load_latest_trade():
    if not os.path.exists(TRADE_LOG_FILE):
        return None
    with open(TRADE_LOG_FILE, "r") as f:
        trades = json.load(f)
    return trades[-1] if trades else None:
:

def master_autonomy_loop():
    print("[PTM Autonomy] 🔁 Starting master autonomy loop...")
    log_status("🟢 Starting master autonomy loop...")

    try:
        # === Phase Set ===
        set_phase("startup")
        log_status("📡 Phase set to 'startup'.")

        # === Ghost Memory Sync ===
        sync_brain_state()
        log_status("🧠 Ghost memory synced.")

        # === Multi-Agent Check ===
        sync_report = run_multi_agent_sync_check()
        for agent in sync_report:
            print(f"[{agent['agent']}] Status: {agent['status']} | Last Sync: {agent['last_synced']} | Health: {agent['sync_health']}")
        log_status("🧩 Multi-agent sync check complete.")

        # === AI Task Routing ===
        route_tasks()
        log_status("📬 Task routing complete.")

        # === Cole Autopilot Cycle ===
        cole_autopilot_cycle()
        log_status("🧠 Cole autopilot cycle complete.")

        # === Strategy Recommendation ===
        strategy_bundle = recommend_best_strategy()
        log_status("📊 Strategy recommendation received.")

        if not strategy_bundle or not strategy_bundle.get("strategy"):
            print("[Strategy Runner] ⚠️ No strategy available. Skipping execution.")
            log_memory("strategy", None)
            log_status("⚠️ No strategy selected.")
            return

        strategy = strategy_bundle["strategy"]
        reason = strategy_bundle.get("reason", "No reason provided.")

        print(f"[Strategy Runner] 🧠 Recommended Strategy: {strategy['name']} | Reason: {reason}")
        log_memory("strategy", strategy)
        log_status(f"✅ Strategy selected: {strategy['name']} – Reason: {reason}")

    except Exception as e:
        error_info = f"{type(e).__name__}: {str(e)}"
        print(f"[PTM Autonomy] ❌ ERROR in loop: {error_info}")
        traceback.print_exc()
        log_memory("autonomy_error", {"error": error_info})
        log_status(f"❌ ERROR: {error_info}")

    # === Trade Recap ===
    latest_trade = load_latest_trade()
    if latest_trade:
        speak_recap(latest_trade)
        log_status("📣 Trade recap triggered.")
    else:
        log_status("ℹ️ No trade found to recap.")

    print("[PTM Autonomy] ✅ Master autonomy loop complete.")
    log_status("🏁 Master autonomy loop complete.")
    time.sleep(1)


if __name__ == "__main__":
    master_autonomy_loop()