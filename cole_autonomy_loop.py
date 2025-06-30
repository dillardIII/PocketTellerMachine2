from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FULLY PATCHED cole_autonomy_loop.py ===

import time
import random
from cole_code_writer import cole_write_code
from cole_executor import cole_auto_run
from cole_self_learning_task_generator import generate_self_learning_tasks
from cole_task_optimizer import cole_optimize_tasks
from cole_command_handler import run_file
from cole_brain import cole_think
from cole_code_results import get_code_generation_results, log_code_result
from cole_voice_recap_generator import attach_recap_to_latest_trade
from cole_self_repair import repair_strategy
from cole_risk_guardian import run_risk_guardian
from cole_self_upgrade_loop import run_self_upgrade_cycle  # <== NEW

# Control flag
autonomy_running = True

def start_autonomy_engine():
    print("[AUTONOMY LOOP] Starting PTM Autonomy Engine...")

    while autonomy_running:
        try:
            # === Step 1: Think & Plan ===
            print("[THINKING] Generating tasks...")
            tasks = generate_self_learning_tasks()
            optimized = cole_optimize_tasks(tasks)

            # === Step 2: Write Code ===
            for task in optimized:
                print(f"[WRITING] Task: {task}")
                filename = cole_write_code(task)
                if filename:
                    log_code_result(task, filename)

            # === Step 3: Run Strategy Files ===
            print("[EXECUTING] Running all generated strategies...")
            cole_auto_run()

            # === Step 4: Learn from Results ===
            print("[LEARNING] Analyzing code results...")
            cole_think("Analyze the last round of strategy results and suggest improvements.")

            # === Step 4b: Auto-Repair Detected Strategy Failures ===
            print("[REPAIR] Checking for known strategy weaknesses...")
            repair_strategy("RSI Reversal", "Fails during high volatility markets. Needs filters.")

            # === Step 5: Risk Check ===
            print("[RISK GUARDIAN] Running safety checks...")
            run_risk_guardian()

            # === Step 6: GPT-Driven Upgrades ===
            print("[UPGRADE] Running self-upgrade cycle for weak strategies...")
            run_self_upgrade_cycle()

            # === Step 7: Generate Voice Recap ===
            print("[VOICE] Creating voice recap for latest trade...")
            attach_recap_to_latest_trade()

            # === Step 8: Delay Until Next Cycle ===
            cooldown = random.randint(60, 120)
            print(f"[WAITING] Sleeping for {cooldown} seconds...\n")
            time.sleep(cooldown)

        except Exception as e:
            print(f"[ERROR] Autonomy Loop crashed: {e}")
            time.sleep(10)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():