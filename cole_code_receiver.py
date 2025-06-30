from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === cole_code_receiver.py ===

import os
import json
from flask import Blueprint, request, jsonify
from datetime import datetime
import pytz

CENTRAL_TZ = pytz.timezone("US/Central")

def get_local_time():
    return datetime.now(CENTRAL_TZ)

code_receiver_bp = Blueprint("code_receiver", __name__)
INSTALL_LOG_FILE = "data/installed_code_log.json"
AUTO_CODE_FOLDER = "installed_modules"

os.makedirs("data", exist_ok=True)
os.makedirs(AUTO_CODE_FOLDER, exist_ok=True)

@code_receiver_bp.route("/install_code", methods=["POST"])
def install_code():
    try:
        data = request.get_json()
        filename = data.get("filename")
        code = data.get("code")

        if not filename or not code:
            return jsonify({"status": "error", "message": "Missing filename or code"}), 400

        filepath = os.path.join(AUTO_CODE_FOLDER, filename)

        with open(filepath, "w") as f:
            f.write(code)

        log_code_install(filename, code)

        return jsonify({
            "status": "success",
            "message": f"Code installed to {filepath}"
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def log_code_install(filename, code):
    log = {
        "timestamp": datetime.now().isoformat(),
        "filename": filename,
        "lines": len(code.splitlines())
    }

    try:
        if os.path.exists(INSTALL_LOG_FILE):
            with open(INSTALL_LOG_FILE, "r") as f:
                logs = json.load(f)
        else:
            logs = []

        logs.append(log)

        with open(INSTALL_LOG_FILE, "w") as f:
            json.dump(logs, f, indent=2)

    except Exception as e:
        print(f"[ERROR] Could not log install: {e}")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():