# === FILE: wallet_ui_display.py ===
# 💼 Wallet UI Display – Displays synced wallet data in a clean web table

from flask import Blueprint, render_template_string
import json
from wallet_manager import WalletManager

wallet_ui_display = Blueprint('wallet_ui_display', __name__)

# === Load Wallet Dictionary ===
def load_wallet_dict():
    try:
        with open("vault/wallet_snapshot.json", "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[Wallet UI] ❌ Failed to load wallet snapshot: {e}")
        return {}

# === Display Wallet Data Route ===
@wallet_ui_display.route("/wallet")
def wallet_table():
    wallet_data = load_wallet_dict()
    table_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>PTM Wallet Snapshot</title>
        <style>
            body {
                background-color: #111;
                color: #0f0;
                font-family: monospace;
                padding: 20px;
            }
            table {
                border-collapse: collapse;
                width: 60%;
                margin-top: 20px;
            }
            th, td {
                border: 1px solid #0f0;
                padding: 8px 12px;
                text-align: left;
            }
            th {
                background-color: #222;
            }
        </style>
    </head>
    <body>
        <h2>💼 Wallet Snapshot</h2>
        <table>
            <tr><th>Asset</th><th>Amount</th></tr>
            {% for asset, amount in wallet_data.items() %}
            <tr><td>{{ asset }}</td><td>{{ amount }}</td></tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(table_html, wallet_data=wallet_data)