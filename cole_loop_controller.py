# === FILE: cole_loop_controller.py ===

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
                tasks = [parsed] if isinstance(parsed, dict) else []

            # === Filter and Optimize Tasks ===
            filtered_tasks = [t for t in tasks if isinstance(t, dict)]
            task_list = cole_optimize_tasks(filtered_tasks)
            if not task_list:
                print("[Cole Controller] No optimized tasks to run.")
                time.sleep(5)
                continue

            print("[Cole Controller] Executing prompts...")
            for task in task_list:
                try:
                    prompt = generate_prompt(task)
                    print("[Cole Controller] Prompt:", prompt)
                except Exception as e:
                    print(f"[Cole Controller] Skipping bad task: {e}")

            print("[Cole Controller] Loop sleeping...")
            time.sleep(5)

        except Exception as e:
            print("[Cole Controller] Loop crashed. Recovering:", str(e))
            time.sleep(2)

# === Entry Point ===
if __name__ == "__main__":
    run_cole_controller_loop()