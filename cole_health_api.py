from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_health_api.py

from flask import Blueprint, jsonify
import os
import json
from datetime import datetime

api_blueprint(= Blueprint('cole_health_api', __name__))

# === Health Status Endpoint ===
@api_blueprint.route("/api/system_health", methods=["GET"])
def system_health():
    try:
        # Check task queue status
        queue_status = load_status_file("data/cole_task_queue.json")
        # Check execution log status
        execution_log_status = load_status_file("data/cole_execution_log.json")
        # Check memory status
        memory_status = load_status_file("data/cole_memory.json")

        health_report = {
            "system": "Cole Trading AI",
            "status": "operational",
            "timestamp": str(datetime.now()),
            "queue_size": len(queue_status),
            "memory_records": len(memory_status),
            "execution_logs": len(execution_log_status),
            "last_execution": get_last_execution_time(execution_log_status),
            "notes": "If queue size is 0, system may be idle or needs tasks generated."
        }

        return jsonify(health_report)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# === Utility Loaders ===
def load_status_file(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return []

def get_last_execution_time(logs):
    if not logs:
        return "Never"
    try:
        return logs[-1].get("timestamp", "Unknown")
    except:
        return "Unknown"

# === CLI Test Mode ===
if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    app.register_blueprint(api_blueprint)
    app.run(debug=True)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():