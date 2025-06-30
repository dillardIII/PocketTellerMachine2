from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_autonomy_cycle.py ===

import time
import traceback
from cole_thinker import cole_think
from cole_agent_cycle import run_agent_cycle
from cole_code_writer import cole_write_code
from cole_code_results import evaluate_last_code_results
from cole_command_handler import run_all_in_dir
from assistants.malik import malik_report

LOOP_INTERVAL = 60  # seconds between each full cycle

def log_cycle(message):
    print(f"[Cole Autonomy Cycle] {message}")
    malik_report(message)

def cole_autonomy_cycle():
    log_cycle("Starting full Cole autonomy cycle...")

    while True:
        try:
            log_cycle("1. Thinking new tasks...")
            cole_think()

            log_cycle("2. Calling GPT to generate code...")
            run_agent_cycle()

            log_cycle("3. Injecting and saving code...")
            cole_write_code()

            log_cycle("4. Evaluating generated code...")
            evaluate_last_code_results()

            log_cycle("5. Executing all strategies...")
            run_all_in_dir()

            log_cycle("Cycle complete. Sleeping...")
            time.sleep(LOOP_INTERVAL)

        except Exception as e:
            error_msg = f"[Autonomy Error] {traceback.format_exc()}"
            print(error_msg)
            malik_report(error_msg)
            time.sleep(30)  # cool down after error before retry

if __name__ == "__main__":
    cole_autonomy_cycle()

def log_event():ef drop_files_to_bridge():