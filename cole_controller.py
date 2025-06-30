from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_controller.py ===

import time
from cole_task_optimizer import cole_optimize_tasks
from cole_prompt_generator import generate_prompt
from cole_command_engine import submit_command
from cole_project_planner import generate_tasks_from_roadmap

def run_cole_controller_loop():
    print("[Cole Controller] Starting main loop...")
    while True:
        try:
            print("[Cole Controller] Choosing next core function...")

            # === Generate Tasks from Roadmap ===
            tasks = generate_tasks_from_roadmap()
            if not tasks:
                print("[Cole Controller] No tasks returned from roadmap. Using fallback command.")
                task_input = "Develop an algorithm for predicting market trends using historical data and current news."
                parsed = submit_command(task_input)
                tasks = [parsed]

            # === Optimize Tasks ===
            task_list = cole_optimize_tasks(tasks)
            if not task_list:
                print("[Cole Controller] No optimized tasks to run.")
                time.sleep(5)
                continue

            print("[Cole Controller] Executing strategy...")
            for task in task_list:
                prompt = generate_prompt(task)
                print("[Cole Controller] Prompt:", prompt)

            print("[Cole Controller] Loop sleeping...")
            time.sleep(5)

        except Exception as e:
            print("[Cole Controller] Loop crashed. Recovering:", str(e))
            time.sleep(2)

# === Direct Execution ===
if __name__ == "__main__":
    run_cole_controller_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():