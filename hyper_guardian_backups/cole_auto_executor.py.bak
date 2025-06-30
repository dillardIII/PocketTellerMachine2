# cole_auto_executor.py

import os
import subprocess
import traceback
import datetime
import json

# === Configurations ===
GENERATED_CODE_FILE = "data/cole_generated_code.py"
EXECUTION_LOG_FILE = "data/cole_execution_log.json"

# === Execution Log Saver ===
def save_execution_log(entry):
    """Append execution result to the log file safely."""
    if not os.path.exists(EXECUTION_LOG_FILE):
        logs = []
    else:
        try:
            with open(EXECUTION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append(entry)

    with open(EXECUTION_LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

# === Main Auto Execution Logic ===
def auto_execute_generated_code():
    """Automatically execute the latest generated code with safety checks and logging."""
    if not os.path.exists(GENERATED_CODE_FILE):
        print("[Cole Auto Executor] No code found to execute.")
        return False

    try:
        print(f"[Cole Auto Executor] Executing: {GENERATED_CODE_FILE}")

        # Execute in a subprocess for isolation and safety
        result = subprocess.run(
            ["python3", GENERATED_CODE_FILE],
            capture_output=True,
            text=True,
            timeout=20  # Safety timeout to prevent infinite loops
        )

        output = result.stdout.strip()
        errors = result.stderr.strip()

        # Log the result
        log_entry = {
            "timestamp": str(datetime.datetime.now()),
            "executed_file": GENERATED_CODE_FILE,
            "output": output,
            "errors": errors,
            "returncode": result.returncode
        }
        save_execution_log(log_entry)

        # Console feedback
        if result.returncode == 0:
            print("[Cole Auto Executor] Code executed successfully.")
            print("[Cole Auto Executor Output]:\n", output)
        else:
            print("[Cole Auto Executor] Code executed with errors.")
            print("[Cole Auto Executor Error]:\n", errors)

        return True

    except subprocess.TimeoutExpired:
        log_entry = {
            "timestamp": str(datetime.datetime.now()),
            "executed_file": GENERATED_CODE_FILE,
            "output": "",
            "errors": "Execution timed out after 20 seconds.",
            "returncode": -1
        }
        save_execution_log(log_entry)
        print("[Cole Auto Executor] Execution timed out.")
        return False

    except Exception as e:
        log_entry = {
            "timestamp": str(datetime.datetime.now()),
            "executed_file": GENERATED_CODE_FILE,
            "output": "",
            "errors": f"Exception occurred: {traceback.format_exc()}",
            "returncode": -2
        }
        save_execution_log(log_entry)
        print("[Cole Auto Executor] Critical execution error:", str(e))
        return False

# === Manual Test Mode ===
if __name__ == "__main__":
    auto_execute_generated_code()