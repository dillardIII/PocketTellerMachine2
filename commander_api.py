"""
Commander API – Controls main interface commands between PTM and user

Features:
- Handle incoming commands (voice, button, script)
- Route to proper AI module (team responder, lesson engine, etc.)
- Return real-time status and feedback
"""

from flask import Blueprint, request, jsonify
import datetime
import os
import json

commander = Blueprint("commander", __name__)

COMMAND_LOG_DIR = "team_files/command_logs"
os.makedirs(COMMAND_LOG_DIR, exist_ok=True)

@commander.route("/api/command/issue", methods=["POST"])
def issue_command():
    data = request.get_json()
    command_type = data.get("type", "generic")
    content = data.get("content", "")
    issued_by = data.get("source", "user")

    # Save command
    timestamp = datetime.datetime.utcnow().isoformat()
    filename = f"cmd_{timestamp.replace(':', '-')}.json"
    filepath = os.path.join(COMMAND_LOG_DIR, filename)

    with open(filepath, "w") as f:
        json.dump({
            "timestamp": timestamp,
            "type": command_type,
            "source": issued_by,
            "content": content
        }, f, indent=2)

    print(f"[Commander] Command received: {command_type} – '{content}'")
    return jsonify({"status": "received", "command": command_type, "content": content})

@commander.route("/api/command/status", methods=["GET"])
def get_status():
    now = datetime.datetime.utcnow().isoformat()
    return jsonify({
        "status": "online",
        "module": "Commander",
        "timestamp": now,
        "message": "Command center standing by. All systems nominal."
    })