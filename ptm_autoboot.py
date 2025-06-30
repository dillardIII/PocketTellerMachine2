from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ptm_autoboot.py ===

# 🧠 PTM Autoboot – Unified startup sequence that launches all bots, bridge agents, UI routes, vault, and repair engine

import threading
import os
from flask import Flask

# === System Modules ===
from bridge_team_launcher import start_bridge_team
from startup_sequencer import StartupSequencer
from ghostforge_core import GhostForge
from file_exec_engine import FileExecEngine

# === UI Blueprints ===
from bot_status_ui import bot_status_ui
from vault_log_ui import vault_log_ui
from inspector_ui import inspector_ui

# === Flask App Initialization ===
app = Flask(__name__)

# === Register UI Routes ===
app.register_blueprint(bot_status_ui)
app.register_blueprint(vault_log_ui)
app.register_blueprint(inspector_ui)

# === Start Bridge Team ===
def launch_bridge():
    try:
        start_bridge_team()
    except Exception as e:
        print(f"[PTM Autoboot] ❌ Bridge launch failed: {e}")

# === Start Startup Sequencer ===
def launch_repair():
    try:
        sequencer = StartupSequencer()
        sequencer.run()
    except Exception as e:
        print(f"[PTM Autoboot] ❌ Startup sequencer failed: {e}")

# === Start GhostForge and FileExec ===
def launch_autocreators():
    try:
        ghost = GhostForge()
        ghost.listen()

        exec_engine = FileExecEngine()
        exec_thread = threading.Thread(target=exec_engine.watch_folder, daemon=True)
        exec_thread.start()

        print("[PTM Autoboot] 🧠 GhostForge and FileExec are running.")
    except Exception as e:
        print(f"[PTM Autoboot] ❌ Auto-creation engines failed: {e}")

# === Master Boot Sequence ===
def start_everything():
    print("[PTM Autoboot] 🔁 Starting all PTM systems...")
    launch_bridge()
    launch_repair()
    launch_autocreators()
    print("[PTM Autoboot] ✅ All systems triggered. Flask server starting...")

# === Root Route for Browser Entry Point ===
@app.route("/")
def home():
    return """
    <html>
    <head><title>PTM Online</title></head>
    <body style="background-color: #000; color: #0f0; font-family: monospace;">
        <h1>🧠 PocketTellerMachine is Live</h1>
        <p>Welcome, Commander Boo. All systems are humming.</p>
        <ul>
            <li><a href="/bot-status" style="color:#0ff;">🔍 Bot Status UI</a></li>
            <li><a href="/vault-log" style="color:#0ff;">💼 Vault Log</a></li>
            <li><a href="/inspector" style="color:#0ff;">🕵️‍♂️ Inspector UI</a></li>
        </ul>
    </body>
    </html>
    """

# === Launch Everything ===
if __name__ == "__main__":
    start_everything()
    app.run(host="0.0.0.0", port=8080, debug=True)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():