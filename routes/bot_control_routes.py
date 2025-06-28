# === FILE: bot_control_routes.py ===
# 🎮 Bot Control Panel Routes – HTML routes for UI control panel and stats

from flask import Blueprint, render_template

bot_control = Blueprint("bot_control", __name__)

@bot_control.route("/dashboard")
def control_dashboard():
    return render_template("bot_control_panel.html")

@bot_control.route("/credits")
def system_credits():
    return render_template("credits.html")