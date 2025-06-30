# bot_router.py
# Routes AI bot commands to appropriate modules

from flask import Blueprint, request, jsonify

bot_router_bp = Blueprint("bot_router_bp", __name__)

@bot_router_bp.route("/bot/command", methods=["POST"])
def route_bot_command():
    data = request.get_json()
    command = data.get("command")

    if not command:
        return jsonify({
            "status": "error",
            "message": "No command provided"
        }), 400

    # Placeholder for bot command routing logic
    print(f"[BotRouter] 🤖 Received command: {command}")

    return jsonify({
        "status": "success",
        "message": f"Command '{command}' received and logged"
    })