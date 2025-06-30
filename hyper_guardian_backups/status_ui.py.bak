# === FILE: status_ui.py ===
# 📊 PTM Status UI Bridge – Exposes rebuild system health for frontends

from flask import Blueprint, jsonify
from self_rebuilder import get_rebuilder_status

status_api = Blueprint("status_api", __name__)

@status_api.route("/api/status/rebuilder", methods=["GET"])
def get_status():
    """
    REST API endpoint to return the current PTM self-rebuilder status.

    Returns:
        JSON containing rebuild status information.
    """
    status = get_rebuilder_status()
    return jsonify({
        "status": "ok",
        "data": status
    })