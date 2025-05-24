# === FILE: master_autonomy_loop.py ===

import os
import time
import json
from strategy_scorer import recommend_best_strategy
from phase_manager import auto_detect_phase
from cole_autopilot_cycle import cole_autopilot_cycle
from cole_self_learning_task_generator import generate_self_learning_tasks
from cole_task_optimizer import cole_optimize_tasks
from cole_executor import (
    run_trade_with_strategy,
    analyze_trade_result,
    log_trade_outcome
)
from cole_tools.cole_auto_runner import cole_auto_run
from cole_brain import check_brain_health, log_phase_and_strategy, log_strategy_reason
from cole_code_writer import cole_write_code
from cole_code_results import evaluate_last_code_results
from cole_self_healing_error_watcher import run_self_healing_autofix
from assistants.malik import malik_report
from cole_strategy_runner import execute_best_strategy
from roadmap_thinker import run_thinking_cycle
from ptm_gpt_agent import run_ptm_gpt_agent  # GPT integration for features

def master_autonomy_loop():
    print("[PTM Autonomy] Starting master loop.")
    while True:
        try:
            # === Optional toggle for control ===
            if os.path.exists("settings.json"):
                with open("settings.json") as f:
                    settings = json.load(f)
                if not settings.get("full_autonomy", False):
                    print("[PTM Autonomy] Autonomy is OFF.")
                    time.sleep(10)
                    continue

            # === Phase and Strategy Detection ===
            phase = auto_detect_phase()
            strategy = recommend_best_strategy()

            print(f"[PTM Autonomy] Current phase: {phase}")
            print(f"[PTM Autonomy] Recommended Strategy: {strategy}")

            # === Log Strategy and Phase ===
            log_phase_and_strategy(phase, strategy)
            log_strategy_reason(strategy=strategy.get("strategy"), reason=strategy.get("reason"))

            # === Health Check ===
            check_brain_health()

            # === Strategy Execution ===
            execute_best_strategy()

            # === Autonomous Thinking ===
            run_thinking_cycle()

            # === GPT Feature Suggestion ===
            run_ptm_gpt_agent("Suggest a new advanced feature for PTM.")

            # === Core Cole Cycle ===
            cole_autopilot_cycle()

            time.sleep(10)

        except Exception as e:
            print(f"[PTM Autonomy] ERROR in loop: {e}")
            run_self_healing_autofix()