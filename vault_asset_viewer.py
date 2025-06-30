from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 🧭 Vault Asset Viewer – Visual UI for assets found in the vault

from flask import Blueprint, render_template_string
import json
import os
from utils.logger import log_event

vault_asset_viewer = Blueprint('vault_asset_viewer', __name__)

VAULT_FILE = "vault/wallet_snapshot.json"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Vault Assets</title>
  <style>
    body { background-color: #111; color: #eee; font-family: monospace; padding: 20px; }
    table { border-collapse: collapse; width: 100%; margin-top: 20px; }
    th, td { border: 1px solid #444; padding: 8px; text-align: left; }
    th { background-color: #222; }
    tr:hover { background-color: #333; }
  </style>
</head>
<body>
  <h1>🧠 Vault Assets</h1>
  <table>
    <tr><th>Symbol</th><th>Name</th><th>Amount</th><th>USD Value</th></tr>
    {% for asset in assets %}
      <tr>
        <td>{{ asset.get('symbol', '?') }}</td>
        <td>{{ asset.get('name', 'Unknown') }}</td>
        <td>{{ asset.get('amount', 0) }}</td>
        <td>${{ "%.2f"|format(asset.get('usd_value', 0)) }}</td>
      </tr>
    {% endfor %}
  </table>
</body>
</html>
"""

@vault_asset_viewer.route("/vault-assets")
def view_assets():
    try:
        with open(VAULT_FILE, "r") as f:
            assets = json.load(f)
        log_event("VaultViewer", {"status": "✅ Loaded", "count": len(assets)})
        return render_template_string(HTML_TEMPLATE, assets=assets)
    except Exception as e:
        log_event("VaultViewer", {"error": str(e)})
        return f"<h1>❌ Failed to load assets</h1><p>{e}</p>"