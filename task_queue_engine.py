from ghost_env import INFURA_KEY, VAULT_ADDRESS
# Task Queue Engine
task_queue = []

def add_task(task):
    if task not in task_queue:
        task_queue.append(task)
        print(f"[TaskQueue] Task added: {task}")
    else:
        print(f"[TaskQueue] Task already exists: {task}")

def get_tasks():
    return task_queue

def log_event():ef drop_files_to_bridge():