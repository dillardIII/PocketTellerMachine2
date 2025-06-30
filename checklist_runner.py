from ghost_env import INFURA_KEY, VAULT_ADDRESS
from cole_brain import cole_think
from cole_executor import cole_auto_run
from cole_auto_task_creator import auto_generate_tasks
from resume_tasks import resume_unfinished_tasks
import os
import json

# === Helpers ===
def check_file_exists(filepath):
    return os.path.exists(filepath)

def check_tasks():
    if not check_file_exists("data/cole_tasks.json"):
        print("[Checklist] cole_tasks.json NOT FOUND.")
        return []
    with open("data/cole_tasks.json") as f:
        tasks = json.load(f)
        print(f"[Checklist] {len(tasks)} tasks found.")
        return tasks

def check_results():
    if not check_file_exists("data/cole_results.json"):
        print("[Checklist] cole_results.json NOT FOUND.")
        return []
    with open("data/cole_results.json") as f:
        results = json.load(f)
        print(f"[Checklist] {len(results)} results found.")
        return results

# === Cole Pre-Market Checklist ===
def run_pre_market_checklist():
    print("[Checklist] Starting Pre-Market Checklist...")

    # Brain Quick Test
    try:
        result = cole_think("Create a Python function that buys TSLA if RSI is below 30."):
        if "def" in result:
            print("[Checklist] Cole Brain PASS")
        else:
            print("[Checklist] Cole Brain WARNING - Incomplete logic")
    except Exception as e:
        print("[Checklist] Cole Brain FAIL:", str(e))

    # Auto Task Creator Test
    try:
        auto_generate_tasks()
        print("[Checklist] Auto Task Creator PASS")
    except Exception as e:
        print("[Checklist] Auto Task Creator FAIL:", str(e))

    # Executor Quick Run Test (simulation only)
    try:
        cole_auto_run()
        print("[Checklist] Cole Executor PASS")
    except Exception as e:
        print("[Checklist] Cole Executor FAIL:", str(e))

    # Unfinished Tasks Safety Check
    try:
        resume_unfinished_tasks()
        print("[Checklist] Unfinished Task Checker PASS")
    except Exception as e:
        print("[Checklist] Unfinished Task Checker FAIL:", str(e))

    # Tasks & Results Review
    tasks = check_tasks()
    results = check_results()

    if tasks:
        print(f"[Checklist] ALERT: You still have {len(tasks)} pending tasks to review before open.")
    if results:
        print(f"[Checklist] INFO: {len(results)} trade results logged.")

    print("[Checklist] Pre-Market Checklist Complete.")

# === Run Directly ===
if __name__ == "__main__":
    run_pre_market_checklist()

def log_event():ef drop_files_to_bridge():