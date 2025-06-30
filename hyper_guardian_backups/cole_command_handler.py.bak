# === FILE: cole_command_handler.py ===

import os
import json
import subprocess
import traceback
from datetime import datetime

# === File Paths ===
COMMAND_LOG_FILE = "logs/command_runner.log"
INJECTION_LOG = "data/cole_code_injections.json"
EXECUTION_LOG = "data/cole_code_exec_log.json"
AUTO_FOLDER = "auto_uploaded_code"
BASE_DIR = "cole_generated_code"

# === Ensure Directories Exist ===
os.makedirs("logs", exist_ok=True)
os.makedirs("data", exist_ok=True)
os.makedirs(BASE_DIR, exist_ok=True)
os.makedirs(AUTO_FOLDER, exist_ok=True)

# === Time Helper ===
def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# === Log Command Run ===
def log_command_run(command, success, output, error=None):
    timestamp = datetime.utcnow().isoformat()
    log_entry = f"[{timestamp}] CMD: {command}\nSTATUS: {'SUCCESS' if success else 'FAIL'}\n"

    if output:
        log_entry += f"OUTPUT:\n{output.strip()}\n"
    if error:
        log_entry += f"ERROR:\n{error.strip()}\n"

    log_entry += "\n" + "=" * 60 + "\n"

    with open(COMMAND_LOG_FILE, "a") as f:
        f.write(log_entry)

    print(f"[Command Runner] {'SUCCESS' if success else 'FAIL'} → {command}")

# === Log File Injection ===
def log_injection(entry):
    if os.path.exists(INJECTION_LOG):
        with open(INJECTION_LOG, 'r+') as f:
            try:
                logs = json.load(f)
            except:
                logs = []
            logs.append(entry)
            f.seek(0)
            f.truncate()
            json.dump(logs, f, indent=2)
    else:
        with open(INJECTION_LOG, 'w') as f:
            json.dump([entry], f, indent=2)

# === Log Code Execution ===
def log_execution(entry):
    if os.path.exists(EXECUTION_LOG):
        with open(EXECUTION_LOG, 'r+') as f:
            try:
                logs = json.load(f)
            except:
                logs = []
            logs.append(entry)
            f.seek(0)
            f.truncate()
            json.dump(logs, f, indent=2)
    else:
        with open(EXECUTION_LOG, 'w') as f:
            json.dump([entry], f, indent=2)

# === Run File (subprocess-based) ===
def run_file(file_path):
    if not os.path.exists(file_path):
        print(f"[Command Runner] File not found: {file_path}")
        log_command_run(file_path, False, "", "File not found.")
        return

    try:
        result = subprocess.run(
            ["python", file_path],
            capture_output=True,
            text=True,
            timeout=30
        )

        success = result.returncode == 0
        log_command_run(file_path, success, result.stdout, result.stderr if not success else "")
        log_execution({
            "timestamp": now(),
            "path": file_path,
            "output": result.stdout.strip(),
            "error": result.stderr.strip() if not success else ""
        })
    except subprocess.TimeoutExpired:
        log_command_run(file_path, False, "", "Execution timed out.")
        log_execution({
            "timestamp": now(),
            "path": file_path,
            "output": "",
            "error": "Execution timed out."
        })
    except Exception as e:
        log_command_run(file_path, False, "", str(e))
        log_execution({
            "timestamp": now(),
            "path": file_path,
            "output": "",
            "error": str(e)
        })

# === Run All .py Files in a Folder ===
def run_all_in_dir(directory=BASE_DIR):
    print(f"[Command Runner] Running all files in {directory}")
    for file in os.listdir(directory):
        if file.endswith(".py"):
            run_file(os.path.join(directory, file))

# === Handle GPT Injection Command ===
def handle_injection_command(command_data):
    """
    Accepts: filename, code, run_after, folder (optional)
    """
    filename = command_data.get("filename")
    code = command_data.get("code")
    folder = command_data.get("folder", AUTO_FOLDER)
    run_after = command_data.get("run_after", False)

    if not filename or not code:
        return {"status": "error", "message": "Missing filename or code."}

    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)

    try:
        with open(filepath, "w") as f:
            f.write(code)
    except Exception as e:
        return {"status": "error", "message": f"Failed to write file: {str(e)}"}

    log_injection({
        "filename": filename,
        "path": filepath,
        "source": "ChatGPT",
        "status": "injected",
        "timestamp": now()
    })

    if run_after:
        return run_file(filepath)
    else:
        return {"status": "success", "message": f"{filename} injected to {folder}"}

# === Manual CLI ===
if __name__ == "__main__":
    print("[Command Runner] Manual test start")
    run_all_in_dir()