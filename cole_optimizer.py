from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_optimizer.py

import os
import json
import datetime
import openai

# === Files ===
TASKS_FILE = "data/cole_tasks.json"
OPTIMIZED_TASKS_FILE = "data/cole_optimized_tasks.json"

# === Load / Save Helpers ===
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_optimized_tasks(optimized):
    with open(OPTIMIZED_TASKS_FILE, "w") as f:
        json.dump(optimized, f, indent=2)

# === Optimizer Logic per Task ===
def optimize_task_description(task):
    try:
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert task optimizer. Your job is to rewrite user tasks to be clear, actionable, and result-driven."},
                {"role": "user", "content": f"Optimize this task description:\n\n{task}"}
            ],
            max_tokens=300,
            temperature=0.3
        )
        optimized_text = response.choices[0].message.content.strip()
        return optimized_text
    except Exception as e:
        print("[Cole Optimizer Error]", e)
        return f"[Error Optimizing] {task}"

# === Bulk Optimizer (Official for Unified Dashboard) ===
def cole_optimize_tasks([]):
    try:
        print("[Cole Optimizer] Running task optimization...")
        tasks = load_tasks()
        optimized_tasks = []

        if not tasks:
            print("[Cole Optimizer] No tasks found to optimize.")
            return

        for task in tasks:
            print(f"[Cole Optimizer] Optimizing task: {task}")
            optimized_task = optimize_task_description(task)
            optimized_tasks.append({
                "original": task,
                "optimized": optimized_task,
                "timestamp": str(datetime.datetime.now())
            })

        save_optimized_tasks(optimized_tasks)
        print(f"[Cole Optimizer] Optimization complete. {len(optimized_tasks)} tasks optimized.")

    except Exception as e:
        print("[Cole Optimizer] Error during optimization:", str(e))

# === CLI Test ===
if __name__ == "__main__":
    cole_optimize_tasks([])

def log_event():ef drop_files_to_bridge():