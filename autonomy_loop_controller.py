# === FILE: Autonomy_Loop_Controller.py ===

import os
import time
import json
import threading
from datetime import datetime  # Added for logging timestamps

# === PTM Core Logic Imports ===
from strategy_scorer import recommend_best_strategy
from phase_manager import auto_detect_phase
from cole_autopilot_cycle import cole_autopilot_cycle
from cole_self_learning_task_generator import generate_self_learning_tasks
from cole_task_optimizer import cole_optimize_tasks

# === Trade Execution Modules ===
from cole_executor import (
    run_trade_with_strategy,
    analyze_trade_result,
    log_trade_outcome
)

# === Core Utilities ===
from cole_tools.cole_auto_runner import cole_auto_run
from cole_brain import (
    check_brain_health,
    log_phase_and_strategy,
    log_strategy_reason
)
from cole_code_writer import cole_write_code
from cole_code_results import evaluate_last_code_results
from cole_self_healing_error_watcher import run_self_healing_autofix

# === Assistant Interfaces ===
from assistants.malik import malik_report

# === Logging Utility ===
def log_autonomy_event(message):
    timestamp = datetime.utcnow().isoformat()
    os.makedirs("logs", exist_ok=True)
    with open("logs/autonomy_loop.log", "a") as f:
        f.write(f"[{timestamp}] {message}\n")

# === Autonomy Loop Controller ===
def master_autonomy_loop():
    print("[PTM Autonomy] Starting master loop.")
    log_autonomy_event("Starting master loop.")

    while True:
        try:
            # === Optional Autonomy Toggle Check ===
            if os.path.exists("settings.json"):
                with open("settings.json") as f:
                    settings = json.load(f)
                if not settings.get("full_autonomy", False):
                    msg = "[PTM Autonomy] Autonomy is OFF."
                    print(msg)
                    log_autonomy_event("Autonomy is OFF.")
                    time.sleep(30)
                    continue

            # === Phase Detection ===
            current_phase = auto_detect_phase()
            msg = f"[PTM Autonomy] Current phase: {current_phase}"
            print(msg)
            log_autonomy_event(msg)

            # === Strategy Recommendation ===
            strategy = recommend_best_strategy()
            msg = f"[PTM Autonomy] Recommended Strategy: {strategy}"
            print(msg)
            log_autonomy_event(msg)

            log_phase_and_strategy(current_phase, strategy)
            log_strategy_reason(strategy)

            # === Self-Learning Tasks ===
            learning_tasks = generate_self_learning_tasks()
            optimized_tasks = cole_optimize_tasks(learning_tasks)

            # === Run Trades ===
            trade_result = run_trade_with_strategy(strategy)
            analyze_trade_result(trade_result)
            log_trade_outcome(trade_result)
            log_autonomy_event(f"Trade executed with strategy: {strategy}")

            # === Trigger Brain Health Checks ===
            check_brain_health()

            # === Write and Evaluate Code ===
            cole_write_code()
            evaluate_last_code_results()

            # === Run Self-Healing If Needed ===
            run_self_healing_autofix()

            # === Side Process: Background Autopilot ===
            threading.Thread(target=cole_autopilot_cycle).start()

            # === Assistant Report (Optional) ===
            malik_report()

            # === Cooldown Between Loops ===
            time.sleep(60)

        except Exception as e:
            error_msg = f"[PTM Autonomy] ERROR in loop: {str(e)}"
            print(error_msg)
            log_autonomy_event(error_msg)
            time.sleep(10)  # Retry after short cooldown

# === Boot Autonomy Controller (Optional Direct Run) ===
if __name__ == "__main__":
    master_autonomy_loop()

# === Daemon Launcher ===
def start_autonomy_daemon():
    thread = threading.Thread(target=master_autonomy_loop, daemon=True)
    thread.start()
    print("[PTM Autonomy] Autonomy daemon started.")
    log_autonomy_event("Autonomy daemon started.")