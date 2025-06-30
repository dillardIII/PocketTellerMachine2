from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import datetime
from cole_brain import cole_think
from cole_executor import cole_auto_run
from cole_auto_task_creator import auto_generate_tasks
from resume_tasks import resume_unfinished_tasks

def log(msg):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[Checklist] {now} - {msg}")

def pre_market_checklist():
    log("Starting Pre-Market Checklist...")

    # 1. Check Cole Brain Response Capability
    try:
        log("Testing Cole Brain Thinking...")
        result = cole_think("Check TSLA RSI and decide if action is needed."):
        log(f"Cole Brain Response: {result}")
    except Exception as e:
        log(f"ERROR: Cole Brain failed to respond. {str(e)}")

    # 2. Run Auto Task Generator
    try:
        log("Running Auto Task Generator...")
        auto_generate_tasks()
        log("Auto Task Generator PASS")
    except Exception as e:
        log(f"ERROR: Auto Task Generator failed. {str(e)}")

    # 3. Run Cole Executor
    try:
        log("Executing Pending Tasks...")
        cole_auto_run()
        log("Cole Executor PASS")
    except Exception as e:
        log(f"ERROR: Cole Executor failed. {str(e)}")

    # 4. Resume any Unfinished Tasks
    try:
        log("Checking for Unfinished Tasks...")
        resume_unfinished_tasks()
        log("Resume Tasks PASS")
    except Exception as e:
        log(f"ERROR: Resume Tasks check failed. {str(e)}")

    log("Pre-Market Checklist Complete. Cole Brain is Ready.")

if __name__ == "__main__":
    pre_market_checklist()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():