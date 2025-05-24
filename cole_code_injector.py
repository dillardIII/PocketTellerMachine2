import os
import json
from flask import Blueprint, request, jsonify
from datetime import datetime

code_injector_bp = Blueprint("code_injector", __name__)

# === Config ===
DEFAULT_FOLDER = "cole_generated_code"
LOG_FILE = "data/code_injection_log.json"
AUTH_TOKEN = os.getenv("GPT_INJECTOR_TOKEN")  # Set this in your .env

# === Ensure directories ===
os.makedirs(DEFAULT_FOLDER, exist_ok=True)
os.makedirs("data", exist_ok=True)

# === Logging ===
def log_injection(filename, folder, source="ChatGPT"):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "filename": filename,
        "folder": folder,
        "source": source
    }
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    logs.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs[-300:], f, indent=2)

# === POST Route to Inject Code ===
@code_injector_bp.route("/api/inject_code", methods=["POST"])
def inject_code():
    data = request.get_json()

    token = request.headers.get("Authorization")
    if token != f"Bearer {AUTH_TOKEN}":
        return jsonify({"status": "unauthorized"}), 401

    filename = data.get("filename")
    code = data.get("code")
    folder = data.get("folder", DEFAULT_FOLDER)

    if not filename or not code:
        return jsonify({"status": "error", "message": "Missing filename or code"}), 400

    os.makedirs(folder, exist_ok=True)
    full_path = os.path.join(folder, filename)

    with open(full_path, "w") as f:
        f.write(code)

    log_injection(filename, folder)
    return jsonify({"status": "success", "path": full_path})

# === Inject Code in Runtime (for Cole AI Core) ===
def inject_generated_code(code, module_name="generated_module"):
    """
    Injects the provided Python code string into a module and returns the module object.
    """
    import types
    module = types.ModuleType(module_name)
    exec(code, module.__dict__)
    return module