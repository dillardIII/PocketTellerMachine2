from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_executor_daemon.py

import time
import traceback
from cole_task_queue import get_pending_tasks, mark_task_done
from cole_brain import cole_think

def run_task(task):
    print(f"[Cole Executor] Executing task: {task['description']}")
    try:
        result = cole_think(task['description'])
        print(f"[Cole Executor] Result:\n{result}")
        mark_task_done(task['id'])
    except Exception as e:
        print(f"[Cole Executor] Error during task: {e}\n{traceback.format_exc()}")

def run_daemon_loop(interval=300):
    print("[Cole Executor Daemon] Running in autonomous loop...")
    while True:
        pending = get_pending_tasks()
        if not pending:
            print("[Cole Executor] No pending tasks. Sleeping...")
        for task in pending:
            run_task(task)
        time.sleep(interval)

if __name__ == "__main__":
    run_daemon_loop()

def log_event():ef drop_files_to_bridge():