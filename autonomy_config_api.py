# === FILE: autonomy_config_api.py ===

from flask import Blueprint, render_template, request, jsonify
import json
import os

autonomy_config_bp = Blueprint("autonomy_config", __name__)
CONFIG_FILE = "autonomy_config.json"

@autonomy_config_bp.route("/autonomy_config")
def config_ui():
    config = load_config()
    return render_template("autonomy_config.html", config=config)

@autonomy_config_bp.route("/api/save_config", methods=["POST"])
def save_config():
    try:
        data = request.json
        with open(CONFIG_FILE, "w") as f:
            json.dump(data, f, indent=2)
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE) as f:
        return json.load(f)