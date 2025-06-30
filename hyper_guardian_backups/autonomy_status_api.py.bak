# autonomy_status_api.py – Real-time autonomy status API for external services and dashboards

from flask import Blueprint, jsonify
from memory_kernel_core import MemoryKernel

status_api = Blueprint("status_api", __name__)
memory = MemoryKernel()

@status_api.route("/api/autonomy-status", methods=["GET"])
def check_autonomy_status():
    mode = memory.recall("mode") or "unknown"
    return jsonify({
        "status": "online" if mode == "full_autonomy" else "offline",
        "mode": mode
    })