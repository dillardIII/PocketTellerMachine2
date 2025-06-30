from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: empire_dashboard.py ===
from flask import Flask, render_template_string, send_file
import json
import os

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>🔥 EMPIRE LIVE DASHBOARD 🔥</title>
    <style>
        body { background: black; color: lime; font-family: monospace; }
        h1, h2 { color: yellow; }
        pre { background: #111; padding: 10px; border-radius: 5px; }
        a { color: cyan; text-decoration: none; }
    </style>
</head>
<body>
    <h1>🔥 EMPIRE LIVE DASHBOARD 🔥</h1>
    <h2>Quantum Brain Status</h2>
    <pre>{{ brain_status }}</pre>

    <h2>Node Map</h2>
    <pre>{{ node_map }}</pre>

    <h2>Vault Assets</h2>
    <pre>{{ vault }}</pre>

    <h2><a href="/vault_log">Download Full Vault Log</a></h2>
</body>
</html>
"""

def load_json(file):
    if os.path.exists(file):
        with open(file) as f:
            return json.dumps(json.load(f), indent=2)
    return "{}"

@app.route("/")
def dashboard():
    brain_status = load_json("brain_status.json")
    node_map = load_json("node_map.json")
    vault = load_json("vault.json")
    return render_template_string(TEMPLATE, brain_status=brain_status, node_map=node_map, vault=vault)

@app.route("/vault_log")
def vault_log():
    return send_file("vault/vault_log.json", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

def log_event():ef drop_files_to_bridge():