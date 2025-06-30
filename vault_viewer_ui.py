from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: vault_viewer_ui.py ===
# 🗃️ Vault Viewer UI – Displays vault contents in a browser view

from flask import Blueprint, render_template_string
import os

vault_viewer_ui = Blueprint('vault_viewer_ui', __name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <title>PTM Vault Viewer</title>
  <style>
    body { background: #000; color: #0f0; font-family: monospace; padding: 20px; }
    h1 { font-size: 24px; color: #fff; }
    ul { list-style: none; padding-left: 0; }
    li { padding: 5px 0; }
  </style>
</head>
<body>
  <h1>💾 PTM Vault Viewer</h1>
  <ul>
    {% for item in contents %}
      <li>{{ item }}</li>
    {% endfor %}
  </ul>
</body>
</html>
"""

@vault_viewer_ui.route("/vault")
def view_vault():
    try:
        contents = os.listdir("vault")
    except Exception:
        contents = ["[Vault Error] Could not access vault."]
    return render_template_string(TEMPLATE, contents=contents)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():