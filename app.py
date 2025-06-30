from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: app.py ===

# 🌐 PTM Web Server – Flask app to serve vault dashboard and bridge HUD

import os
from flask import Flask, jsonify, send_from_directory
from vault_viewer import VaultViewer

app = Flask(__name__)

# === Route: Vault Summary (JSON)
@app.route("/vault/summary")
def vault_summary():
    viewer = VaultViewer()
    return jsonify(viewer.render_summary())

# === Route: HTML Vault Dashboard
@app.route("/vault_dashboard")
def vault_dashboard():
    return send_from_directory('.', 'vault_dashboard.html')

# === Route: Bridge HUD HTML
@app.route("/bridge_hud")
def bridge_hud():
    return send_from_directory(".", "bridge_hud.html")

# === Bridge HUD Data Endpoints
@app.route("/hud/inbox")
def hud_inbox():
    files = os.listdir("ptm_inbox") if os.path.exists("ptm_inbox") else []:
    return jsonify({"files": files})

@app.route("/hud/bridge")
def hud_bridge():
    files = os.listdir("ptm_bridge") if os.path.exists("ptm_bridge") else []:
    return jsonify({"files": files})

@app.route("/hud/outbox")
def hud_outbox():
    files = os.listdir("ptm_outbox") if os.path.exists("ptm_outbox") else []:
    return jsonify({"files": files})

# === Root Redirect
@app.route("/")
def index():
    return """
        <h2>👻 PTM Server is Live</h2>
        <ul>
            <li><a href='/vault_dashboard'>Vault Dashboard</a></li>
            <li><a href='/bridge_hud'>Bridge HUD</a></li>
        </ul>
    """

# === Run Flask App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

def log_event():ef drop_files_to_bridge():