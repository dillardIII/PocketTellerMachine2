from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_auto_task_creator.py

import os
import json
import datetime
from assistants.malik import malik_report
from cole_code_results import save_code_generation_result

TASK_FILE = "data/task_queue.json"
CODE_FOLDER = "cole_generated_code"

# === Ensure Task Queue File ===
def ensure_task_file():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w") as f:
            json.dump([], f, indent=4)

# === Ensure Code Folder ===
def ensure_code_folder():
    os.makedirs(CODE_FOLDER, exist_ok=True)

# === Auto Generate Tasks with Code ===
def auto_generate_tasks():
    ensure_task_file()
    ensure_code_folder()

    # Example: Generate a unique task name and Python code
    task_name = f"Auto Strategy {datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
    filename = f"{task_name.replace(' ', '_')}.py"
    code_content = f"print('Executing {task_name}')"

    # Save code to file
    code_path = os.path.join(CODE_FOLDER, filename)
    with open(code_path, "w") as f:
        f.write(code_content)

    # Log the code generation result
    save_code_generation_result(filename, code_content)

    # Load task queue
    with open(TASK_FILE, "r") as f:
        tasks = json.load(f)

    # Create task object
    task = {
        "task": f"Execute {filename}",
        "code": code_content,
        "file": filename
    }

    # Append to queue
    tasks.append(task)

    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

    malik_report(f"Cole auto-generated task and code: {filename}")

# === Get Task Queue ===
def get_task_queue():
    ensure_task_file()
    with open(TASK_FILE, "r") as f:
        return json.load(f)

# === CLI Test Run ===
if __name__ == "__main__":
    auto_generate_tasks()
    print(get_task_queue())

def log_event():ef drop_files_to_bridge():