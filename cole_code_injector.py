from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from flask import Blueprint, request, jsonify
from datetime import datetime
from pathlib import Path
import importlib.util

from assistants.malik import malik_report

code_injector_bp = Blueprint("code_injector", __name__)

GENERATED_DIR = "cole_generated_code"
INJECTION_LOG = "data/code_injection_log.json"
os.makedirs(GENERATED_DIR, exist_ok=True)
os.makedirs("data", exist_ok=True)

# === Save code to file ===
def save_code_to_file(task_name, code):
    filename = f"{task_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
    file_path = os.path.join(GENERATED_DIR, filename)
    with open(file_path, "w") as f:
        f.write(code)
    return file_path

# === Inject and run ===
def inject_and_run_code(code, task_name="Untitled Task"):
    try:
        file_path = save_code_to_file(task_name, code)

        spec = importlib.util.spec_from_file_location("module.name", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "cole_generated_function"):
            result = module.cole_generated_function()
            status = "executed"
            malik_report(f"[Injected Execution] {task_name}: {result}")
        else:
            result = "No `cole_generated_function()` found"
            status = "no-entry-point"

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "task": task_name,
            "file": file_path,
            "status": status,
            "result": str(result)
        }

        log_injection(log_entry)
        return log_entry

    except Exception as e:
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "task": task_name,
            "file": "N/A",
            "status": "error",
            "error": str(e)
        }
        log_injection(log_entry)
        malik_report(f"[Injection Error] {task_name}: {str(e)}")
        return log_entry

# === Log the injection ===
def log_injection(entry):
    if os.path.exists(INJECTION_LOG):
        with open(INJECTION_LOG, "r") as f:
            logs = json.load(f)
    else:
        logs = []
    logs.append(entry)
    with open(INJECTION_LOG, "w") as f:
        json.dump(logs[-300:], f, indent=2)

# === API Endpoint ===
@code_injector_bp.route("/inject_code", methods=["POST"])
def inject_code_api():
    data = request.json
    code = data.get("code", "")
    task = data.get("task", "Unnamed Task")
    if not code:
        return jsonify({"error": "Missing code"}), 400
    result = inject_and_run_code(code, task)
    return jsonify(result)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():