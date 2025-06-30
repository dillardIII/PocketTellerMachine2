from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_gateway_api.py ===

import os
import json
from datetime import datetime
import pytz

CENTRAL_TZ = pytz.timezone("US/Central")

def get_local_time():
    return datetime.now(CENTRAL_TZ)
from flask import Blueprint, request, jsonify
from cole_command_handler import handle_injection_command

gateway_bp = Blueprint("gateway_bp", __name__)

SECRET_KEY = os.getenv("PTM_GATEWAY_KEY", "test-key")

@gateway_bp.route("/api/gateway/command", methods=["POST"])
def handle_gateway_command():
    data = request.get_json()

    if not data or data.get("key") != SECRET_KEY:
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

    command_type = data.get("type")
    
    if command_type == "inject_code":
        filename = data.get("filename")
        code = data.get("code")
        folder = data.get("folder", "remote_code")
        run_after = data.get("run_after", True)

        if not filename or not code:
            return jsonify({"status": "error", "message": "Missing filename or code"}), 400

        result = handle_injection_command({
            "filename": filename,
            "code": code,
            "folder": folder,
            "run_after": run_after
        })
        return jsonify(result)

    elif command_type == "add_task":
        task = {
            "description": data.get("description"),
            "filename": data.get("filename"),
            "folder": "auto_uploaded_code",
            "run_after": True
        }
        queue_file = "data/autopilot_queue.json"
        queue = []
        if os.path.exists(queue_file):
            with open(queue_file) as f:
                try:
                    queue = json.load(f)
                except:
                    pass
        queue.append(task)
        with open(queue_file, "w") as f:
            json.dump(queue, f, indent=2)
        return jsonify({"status": "ok", "task": task})

    return jsonify({"status": "error", "message": "Unknown command type"}), 400

def log_event():ef drop_files_to_bridge():