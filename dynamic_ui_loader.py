from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: dynamic_ui_loader.py ===
# 🖼️ Dynamic UI Loader – Handles HTML injection, dashboard loading, and route preview logic

import os
from flask import Blueprint, render_template

dynamic_ui_bp = Blueprint("dynamic_ui", __name__)

@dynamic_ui_bp.route("/dashboard/<page>")
def load_dashboard_page(page):
    file_path = f"templates/dashboard/{page}.html"
    if not os.path.exists(file_path):
        return f"❌ Page '{page}' not found.", 404
    return render_template(f"dashboard/{page}.html")

@dynamic_ui_bp.route("/assistant/<name>")
def load_assistant_profile(name):
    try:
        return render_template("assistants/profile_view.html", name=name)
    except Exception as e:
        return f"❌ Assistant profile failed to load: {e}", 500

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():