# === FILE: app.py ===
# PTM Core Flask App – Bootstraps services, routes, bots, and AI handlers

from flask import Flask, render_template, jsonify, request, redirect, url_for, send_from_directory
from threading import Thread
from datetime import datetime
import subprocess
import os
import json

# === PTM Core System Imports ===
from cole_autopilot_cycle import cole_autopilot_cycle
from error_parser import get_latest_error, save_error_to_log
from ai_code_generator import generate_code_fix
from auto_deployer import deploy_fix

# === Autonomy + Loop Control ===
from master_autonomy_loop import master_autonomy_loop
from auto_cycle_builder import run_build_autonomy_cycle
from autonomy_loop_controller import start_autonomy_daemon
from auto_route_loader import load_dynamic_routes
from boot_autonomy import start_all_autonomy

# === Strategy & Phases ===
from phase_manager import set_phase
from strategy_scorer import recommend_best_strategy

# === GPT Prompt Interface ===
from gpt_prompt_api import gpt_prompt_bp

# === Voice Recap ===
from voice_recap import generate_voice_recap

# === Bridge Communication Bot ===
from bridge_heartbeat_sync import start_bridge_sync

# === Comm Bridge Fix (Corrected Import) ===
from bridge_repo_comm_channel import send_to_repo, get_repo_status

# === Inter-Bot Router (Hybrid Loop Mode) ===
from ptm.inter_bot_router import relay_messages, start_relay_loop

# === Cole Bot Listener ===
from bots.cole_bot_listener import cole_listen_loop

# === Brain Syncer (🧠 Memory Logger & Streamer) ===
from ptm_brain_sync import run_brain_sync  # 🔁 Real-time memory streamer

# === Log Merger Bot (🧩 Log Joiner Daemon) ===
from log_merger_bot import start_merger_bot

# === Replit Error Watchdog (🐶 File Error Scanner) ===
from ptm_watchdog import start_watchdog

# === Auto Error Repair Loop (🛠️ Self-healing bot) ===
from auto_error_repair_loop import auto_error_repair_loop

# === Self-Rebuilder (🧠 Self-Fixing AI Core) ===
from self_rebuilder import self_rebuilder_loop, get_rebuilder_status, manual_self_rebuild

# === App Init ===
app = Flask(__name__)
app.register_blueprint(gpt_prompt_bp)

# === Safe Background Boot ===
def run_background_services():
    print("[BOOT] Starting background services...")

    # 🚀 Launch REPAIR + AUTONOMY + BRIDGE + ROUTER + COLE + MEMORY SYNC + MERGER + WATCHDOG + ERROR REPAIR + SELF-REBUILDER
    Thread(target=start_all_autonomy).start()
    Thread(target=start_bridge_sync).start()
    Thread(target=start_relay_loop, daemon=True).start()
    Thread(target=cole_listen_loop, daemon=True).start()
    Thread(target=run_brain_sync, daemon=True).start()
    Thread(target=start_merger_bot, daemon=True).start()
    Thread(target=start_watchdog, daemon=True).start()
    Thread(target=auto_error_repair_loop, daemon=True).start()  # 🛠️ Auto Repair Bot
    Thread(target=self_rebuilder_loop, daemon=True).start()     # 🧠 Self-Rebuilder

    print("[BOOT] All background services launched.")

# === Root Dashboard Route ===
@app.route("/")
def index():
    return render_template("index.html")

# === Manual Strategy Trigger (For Testing) ===
@app.route("/run_strategy", methods=["POST"])
def run_strategy():
    strategy_data = request.json
    strategy = strategy_data.get("strategy", "default_strategy")
    print(f"[Manual Trigger] Running strategy: {strategy}")
    return jsonify({"status": "executed", "strategy": strategy})

# === View Last Error Route ===
@app.route("/last_error")
def view_last_error():
    error_info = get_latest_error()
    return jsonify(error_info)

# === GPT Code Fix Trigger ===
@app.route("/fix_error", methods=["POST"])
def fix_error():
    latest_error = get_latest_error()
    fixed_code = generate_code_fix(latest_error["traceback"])
    deploy_result = deploy_fix(fixed_code)
    return jsonify({"fix": deploy_result})

# === Start Cole Autopilot (Manual) ===
@app.route("/start_autopilot")
def start_autopilot():
    Thread(target=cole_autopilot_cycle).start()
    return jsonify({"status": "Cole Autopilot Cycle started"})

# === Voice Recap Route ===
@app.route("/voice_recap", methods=["POST"])
def voice_recap():
    recap_text = request.json.get("text", "No summary provided.")
    audio_path = generate_voice_recap(recap_text)
    return jsonify({"audio_path": audio_path})

# === Screeps Recon Terminal ===
@app.route("/recon")
def recon_terminal():
    return render_template("recon_terminal.html")

@app.route("/run-recon", methods=["POST"])
def run_recon():
    subprocess.Popen(["node", "index.js"])
    return redirect(url_for("recon_terminal"))

# === Ghostshade Status Route (for Recon Card UI) ===
@app.route("/ghostshade/status")
def ghostshade_status():
    try:
        with open("memory/ghostshade_core.json") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": "Unable to load Ghostshade memory", "details": str(e)}), 500

# === Manual Merge Trigger (On Demand) ===
@app.route("/merge_logs_now", methods=["POST"])
def merge_logs_now():
    from log_merger_bot import manual_merge
    result = manual_merge()
    return jsonify({"status": "merged", "info": result})

# === Live Merger Status Check ===
@app.route("/merger_status")
def merger_status():
    from log_merger_bot import get_merger_status
    status = get_merger_status()
    return jsonify(status)

# === 📊 Rebuilder Status Route ===
@app.route("/self_rebuilder/status")
def self_rebuilder_status():
    return jsonify(get_rebuilder_status())

# === 🔧 Manual Self-Rebuild Trigger ===
@app.route("/self_rebuilder/manual", methods=["POST"])
def self_rebuilder_manual():
    result = manual_self_rebuild()
    return jsonify(result)

# === Optional: Serve static/ui HTML files ===
@app.route("/ui/<path:filename>")
def serve_ui(filename):
    return send_from_directory("static/ui", filename)

# === Serve Screenshots ===
@app.route('/screenshots/<filename>')
def serve_screenshot(filename):
    return send_from_directory('screenshots', filename)

# === Main Entry Point ===
if __name__ == "__main__":
    set_phase("startup")
    run_background_services()
    load_dynamic_routes(app)
    app.run(host="0.0.0.0", port=8080, debug=True)