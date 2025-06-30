# === FILE: vault_dashboard.py ===
from flask import Flask, render_template_string, redirect, url_for
import json
import os
from vault_manager import force_recombine_partials

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>🔑 VAULT DASHBOARD</title>
    <style>
        body { background: #111; color: #0f0; font-family: monospace; }
        pre { background: #222; padding: 10px; border-radius: 5px; }
        a { color: cyan; text-decoration: none; margin-right: 15px; }
    </style>
</head>
<body>
    <h1>🔑 VAULT DASHBOARD</h1>
    <a href="/recombine">Force Recombine Partials</a>
    <h2>Vault Data</h2>
    <pre>{{ vault }}</pre>
</body>
</html>
"""

def load_vault():
    if os.path.exists("vault.json"):
        with open("vault.json") as f:
            return json.dumps(json.load(f), indent=2)
    return "{}"

@app.route("/")
def home():
    vault_data = load_vault()
    return render_template_string(TEMPLATE, vault=vault_data)

@app.route("/recombine")
def recombine():
    force_recombine_partials()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)