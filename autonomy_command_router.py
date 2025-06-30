from ghost_env import INFURA_KEY, VAULT_ADDRESS
# autonomy_command_router.py – Routes external AI or assistant commands into PTM actions

from flask import Blueprint, request, jsonify
import subprocess

command_router = Blueprint('command_router', __name__)

@command_router.route("/api/command", methods=["POST"])
def handle_command():
    data = request.get_json()

    if not data or "command" not in data:
        return jsonify({"error": "Missing 'command' in request"}), 400

    command = data["command"].lower()

    try:
        if command == "restart_ptm":
            subprocess.Popen(["python3", "boot_autonomy.py"])
            return jsonify({"status": "PTM restarted"}), 200

        elif command == "reboot_vps":
            subprocess.call(["sudo", "reboot"])
            return jsonify({"status": "Rebooting VPS..."}), 200

        elif command == "status":
            return jsonify({"status": "online", "uptime": "active"}), 200

        else:
            return jsonify({"error": f"Unknown command: {command}"}), 400

    except Exception as e:
        return jsonify({"error": f"Command execution failed: {str(e)}"}), 500

def log_event():ef drop_files_to_bridge():