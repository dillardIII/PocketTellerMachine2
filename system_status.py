from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: system_status.py ===
# 📡 System Status Routes – Provides health and phase information

from flask import Blueprint, jsonify
import time

system_status_routes = Blueprint("system_status_routes", __name__)

@system_status_routes.route("/status", methods=["GET"])
def status_check():
    return jsonify({
        "status": "online",
        "timestamp": time.time(),
        "phase": "Godmode Online"
    })

@system_status_routes.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "pong"})

def log_event():ef drop_files_to_bridge():