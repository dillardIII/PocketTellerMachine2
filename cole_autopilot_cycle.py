# === FILE: cole_autopilot_cycle.py ===

import os
import traceback
from strategy_executor import run_trade_with_strategy, analyze_trade_result, log_trade_outcome
from cole_task_optimizer import cole_optimize_tasks
from cole_self_learning_task_generator import generate_self_learning_tasks

def cole_autopilot_cycle():
    print("[Cole Autopilot] Starting cycle...")

    try:
        # Step 1: Load strategy tasks
        task_list = generate_self_learning_tasks()
        if not task_list:
            print("[Cole Autopilot] No tasks generated. Skipping strategy run.")
            return

        # Step 2: Validate and Optimize task list
        clean_tasks = [t for t in task_list if isinstance(t, dict) and 'description' in t]
        optimized_tasks = cole_optimize_tasks(clean_tasks)
        print(f"[Cole Autopilot] Optimized {len(optimized_tasks)} tasks.")

        for task in optimized_tasks:
            try:
                result = run_trade_with_strategy(task)
                grade = analyze_trade_result(result)
                log_trade_outcome(task, result, grade)
            except Exception as e:
                print(f"[Autopilot Task Error] Skipping bad task: {e}")

    except Exception as e:
        print("[Cole Autopilot] ERROR during autopilot run:")
        traceback.print_exc()
        os.makedirs("logs", exist_ok=True)
        with open("logs/autopilot_error.log", "a") as f:
            f.write(traceback.format_exc())

    print("[Cole Autopilot] Cycle complete.")