# === FILE: recovery_reporter.py ===
# 🩺 Recovery Reporter – Handles system recovery logging and assistant reboot simulation

import json
import os
from datetime import datetime
from flask import Blueprint, jsonify, request
from pathlib import Path

recovery_reporter_bp = Blueprint("recovery_reporter", __name__)
RECOVERY_LOG = "logs/recovery_events.json"

# Ensure logs directory exists
Path("logs").mkdir(parents=True, exist_ok=True)

def log_recovery_event(event_type, details):
    timestamp = datetime.utcnow().isoformat()
    event = {
        "timestamp": timestamp,
        "event": event_type,
        "details": details
    }
    if not os.path.exists(RECOVERY_LOG):
        with open(RECOVERY_LOG, "w", encoding="utf-8") as f:
            json.dump([event], f, indent=2)
    else:
        with open(RECOVERY_LOG, "r+", encoding="utf-8") as f:
            data = json.load(f)
            data.append(event)
            f.seek(0)
            json.dump(data, f, indent=2)

@recovery_reporter_bp.route("/log_recovery", methods=["POST"])
def log_recovery():
    data = request.json
    event_type = data.get("event", "unknown")
    details = data.get("details", {})
    log_recovery_event(event_type, details)
    return jsonify({"status": "logged", "event": event_type})

@recovery_reporter_bp.route("/recovery/reboot", methods=["POST"])
def reboot_agent():
    data = request.get_json()
    agent_name = data.get("agent", "unknown")

    if not agent_name:
        return jsonify({
            "status": "error",
            "message": "Agent name not provided"
        }), 400

    # Log the simulated reboot
    log_recovery_event("reboot", {"agent": agent_name})

    return jsonify({
        "status": "rebooting",
        "agent": agent_name,
        "timestamp": datetime.utcnow().isoformat()
    })

@recovery_reporter_bp.route("/recovery/status", methods=["GET"])
def recovery_status():
    return jsonify({
        "status": "monitoring",
        "last_agent": "mentor",
        "uptime": "1421 ticks",
        "last_error": None
    })