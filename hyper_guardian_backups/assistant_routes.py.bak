# === FILE: assistant_routes.py ===
# 🧠 Assistant Selector – Allows switching AI assistant personas

from flask import Blueprint, request, jsonify

assistant_routes = Blueprint('assistant_routes', __name__)

active_persona = "Mentor"

@assistant_routes.route("/assistants/select", methods=["POST"])
def select_persona():
    global active_persona
    data = request.get_json()
    name = data.get("name")

    if name:
        active_persona = name
        return jsonify({"message": f"Assistant switched to {name}"}), 200
    return jsonify({"error": "No assistant name provided"}), 400

@assistant_routes.route("/assistants/active", methods=["GET"])
def current_persona():
    return jsonify({"active": active_persona})