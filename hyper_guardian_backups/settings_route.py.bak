# === FILE: settings_route.py ===

from flask import Blueprint, request, jsonify
import os
import json

settings_bp = Blueprint("settings_bp", __name__)
SETTINGS_FILE = "data/settings.json"

# === API: Get current settings ===
@settings_bp.route("/api/settings", methods=["GET"])
def get_settings():
    if not os.path.exists(SETTINGS_FILE):
        return jsonify({})

    with open(SETTINGS_FILE, "r") as f:
        try:
            settings = json.load(f)
        except:
            settings = {}

    return jsonify(settings)

# === API: Save updated settings ===
@settings_bp.route("/api/settings", methods=["POST"])
def save_settings():
    new_settings = request.json or {}
    os.makedirs("data", exist_ok=True)

    with open(SETTINGS_FILE, "w") as f:
        json.dump(new_settings, f, indent=2)

    return jsonify({"status": "saved"})