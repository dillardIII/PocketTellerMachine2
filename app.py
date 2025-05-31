# === FILE: app.py ===

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
from auto_route_loader import load_all_routes
from boot_autonomy import start_all_autonomy

# === Strategy & Phases ===
from phase_manager import set_phase
from strategy_scorer import recommend_best_strategy

# === GPT Prompt Interface ===
from gpt_prompt_api import gpt_prompt_bp

# === Voice Recap ===
from voice_recap import generate_voice_recap

# === App Init ===
app = Flask(__name__)
app.register_blueprint(gpt_prompt_bp)

# === Safe Background Start ===
def run_background_services():
    print("[BOOT] Starting background services...")
    Thread(target=start_all_autonomy).start()
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
    load_all_routes(app)
    app.run(host="0.0.0.0", port=8080, debug=True)