# === FILE: update_trade_dashboard.py ===

import json
import os

TRADE_LOG_FILE = "data/trade_log.json"
DASHBOARD_HTML = "templates/trade_dashboard.html"


def load_trade_log():
    if not os.path.exists(TRADE_LOG_FILE):
        return []
    with open(TRADE_LOG_FILE, "r") as f:
        return json.load(f)


def build_trade_table(trades):
    rows = ""
    for trade in reversed(trades):
        color = "green" if trade.get("result") == "win" else "red" if trade.get("result") == "loss" else "gray"
        datetime_str = trade.get("datetime", "[Unknown Time]")
        row = f"""
        <tr style="color:{color};">
            <td>{datetime_str}</td>
            <td>{trade.get('persona', 'Unknown')}</td>
            <td>{trade.get('strategy', 'Unknown')}</td>
            <td>{trade.get('symbol', 'N/A')}</td>
            <td>{trade.get('action', 'N/A').upper()}</td>
            <td>${trade.get('price', 0):.2f}</td>
            <td>{trade.get('shares', 0)}</td>
            <td>${trade.get('total', 0):.2f}</td>
            <td>{trade.get('result', 'pending')}</td>
        </tr>
        """
        rows += row
    return rows


def update_dashboard():
    print("[DashboardUpdater] 🔄 Updating trade dashboard...")
    trades = load_trade_log()
    table_html = build_trade_table(trades)

    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>PTM Trade Dashboard</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #111; color: white; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            th, td {{ padding: 10px; text-align: center; }}
            th {{ background-color: #333; }}
            tr:nth-child(even) {{ background-color: #222; }}
            h1 {{ text-align: center; color: #0f0; }}
        </style>
    </head>
    <body>
        <h1>Trade History</h1>
        <table border="1">
            <tr>
                <th>Date/Time</th>
                <th>Persona</th>
                <th>Strategy</th>
                <th>Symbol</th>
                <th>Action</th>
                <th>Price</th>
                <th>Shares</th>
                <th>Total</th>
                <th>Result</th>
            </tr>
            {table_html}
        </table>
    </body>
    </html>
    """

    os.makedirs("templates", exist_ok=True)
    with open(DASHBOARD_HTML, "w") as f:
        f.write(html_template)
    print(f"[DashboardUpdater] ✅ Dashboard written to {DASHBOARD_HTML}")


if __name__ == "__main__":
    update_dashboard()