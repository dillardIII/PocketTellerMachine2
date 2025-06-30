# health_check_route.py – Provides a system health check endpoint

from flask import Blueprint, jsonify

health_check_bp = Blueprint("health_check", __name__)

@health_check_bp.route("/health", methods=["GET"])
def health_status():
    return jsonify({
        "status": "OK",
        "uptime": "Stable",
        "timestamp": "2025-05-31T00:00:00Z"
    })