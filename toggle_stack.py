from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: toggle_stack.py ===
# 🔁 Toggle Stack – Handles bot status on/off updates from Command Center

from flask import request, redirect
import json

def register_toggle_route(app):
    @app.route("/toggle", methods=["POST"])
    def toggle():
        try:
            with open("bot_status.json", "r") as f:
                current_status = json.load(f)
        except:
            current_status = {}

        for bot in current_status:
            current_status[bot] = (bot in request.form)

        with open("bot_status.json", "w") as f:
            json.dump(current_status, f, indent=4)

        return redirect("/command-panel")

def log_event():ef drop_files_to_bridge():