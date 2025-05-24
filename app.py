from flask import Flask, jsonify, request, redirect, url_for, render_template
from threading import Thread
import os
import json
from datetime import datetime

# === Cole Core Imports ===
from cole_autopilot_cycle import cole_autopilot_cycle
from error_parser import get_latest_error, save_error_to_log
from ai_code_generator import generate_code_fix
from auto_deployer import deploy_fix

# === Autonomy Imports ===
from master_autonomy_loop import master_autonomy_loop
from auto_cycle_builder import run_build_autonomy_cycle
from autonomy_loop_controller import start_autonomy_daemon
from auto_route_loader import load_all_routes
from boot_autonomy import start_all_autonomy

# === Strategy + Phase ===
from phase_manager import set_phase
from strategy_scorer import recommend_best_strategy

# === GPT Prompt UI ===
from gpt_prompt_api import gpt_prompt_bp
from autonomy_status_api import autonomy_status_bp
from real_time_market_trend_analysis_route import real_time_market_trend_analysis_bp
from real_time_trend_analysis_route import real_time_trend_analysis_bp

# === Flask App Init ===
app = Flask(__name__)

# === Load all dynamic blueprints ===
load_all_routes(app)
app.register_blueprint(gpt_prompt_bp)
app.register_blueprint(autonomy_status_bp)
app.register_blueprint(real_time_market_trend_analysis_bp)
app.register_blueprint(real_time_trend_analysis_bp)

# === Launch Autonomy Threads on Startup ===
start_all_autonomy()

def run_autopilot_safe():
    try:
        cole_autopilot_cycle()
    except Exception as e:
        import sys
        save_error_to_log(sys.exc_info())
        print("[Cole Autopilot] Logged error:", e)

# === Fix Broken Code via API ===
@app.route("/fix_now")
def manual_fix_now():
    error = get_latest_error()
    if not error:
        return jsonify({"status": "no error found"})

    fix = generate_code_fix(error)
    if not fix:
        return jsonify({"status": "fix generation failed"})

    success = deploy_fix(error["file"], fix)
    if success:
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "file": error["file"],
            "error": error["error"],
            "fix": fix
        }
        os.makedirs("data", exist_ok=True)
        fixes_log = "data/fixes_log.json"
        try:
            if os.path.exists(fixes_log):
                with open(fixes_log, "r") as f:
                    data = json.load(f)
            else:
                data = []
            data.append(log_entry)
            with open(fixes_log, "w") as f:
                json.dump(data, f, indent=2)
        except:
            pass
        return jsonify({"status": "fixed", "file": error["file"]})
    else:
        return jsonify({"status": "fix failed", "file": error["file"]})

# === Manual Phase Setter ===
@app.route("/set_phase/<phase_name>")
def set_phase_route(phase_name):
    new_phase = set_phase(phase_name)
    return jsonify({"status": "updated", "phase": new_phase})

# === Trade History Viewer ===
@app.route("/trades")
def view_trades():
    trades = []
    if os.path.exists("data/trade_history.json"):
        with open("data/trade_history.json", "r") as f:
            trades = json.load(f)
    return render_template("trade_history.html", trades=trades)

# === Strategy Leaderboard View ===
@app.route("/strategy_leaderboard")
def strategy_leaderboard():
    try:
        with open("data/backtest_results.json", "r") as f:
            results = json.load(f)
    except:
        results = []

    return render_template("strategy_leaderboard.html", strategies=results)

@app.route("/api/strategy_leaderboard")
def api_strategy_leaderboard():
    try:
        with open("data/backtest_results.json", "r") as f:
            results = json.load(f)
        return jsonify({"status": "ok", "strategies": results})
    except:
        return jsonify({"status": "error", "strategies": []})

@app.route("/api/recommend_strategy")
def api_recommend_strategy():
    result = recommend_best_strategy()
    return jsonify(result)

# === Autonomy Log Viewer ===
@app.route("/autonomy_log")
def view_autonomy_log():
    log_path = "logs/autonomy_loop.log"
    log_lines = []

    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            log_lines = f.readlines()[-100:]

    return render_template("autonomy_log.html", logs=log_lines[::-1])

# === Test Cole + GPT Code Generation ===
@app.route("/test_cole_gpt_connection")
def test_cole_gpt_connection():
    try:
        from cole_command_interpreter import cole_interpret_command
        from cole_code_results import evaluate_last_code_results

        test_prompt = "Create a simple strategy that prints 'Test Passed: Cole and GPT are working together.'"
        cole_interpret_command(test_prompt)

        result = evaluate_last_code_results()

        return jsonify({
            "status": "success",
            "test_prompt": test_prompt,
            "last_result": result
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# === Test Cole-GPT Conversation ===
@app.route("/test_cole_gpt_chat")
def test_cole_gpt_chat():
    try:
        from cole_gpt_advisor import ask_gpt

        prompt = "Explain to Cole how to trade using a simple moving average (SMA)."
        gpt_reply = ask_gpt(prompt)

        return jsonify({
            "status": "success",
            "from_cole": prompt,
            "from_gpt": gpt_reply
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# === Chat Log Viewer ===
@app.route("/cole_chat_history")
def cole_chat_history():
    log_file = "data/cole_gpt_chat_log.json"
    chats = []
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            chats = json.load(f)
    return render_template("cole_chat_history.html", chats=chats[::-1])

# === Ghost Memory Monitor ===
@app.route("/ghost_memory_monitor")
def ghost_memory_monitor():
    phase = "unknown"
    if os.path.exists("data/phase.json"):
        with open("data/phase.json") as f:
            phase = json.load(f).get("current_phase", "unknown")

    strategy = "N/A"
    if os.path.exists("data/cole_code_log.json"):
        with open("data/cole_code_log.json") as f:
            code_log = json.load(f)
            if code_log:
                strategy = code_log[-1]["task"]

    reply = "N/A"
    if os.path.exists("data/cole_gpt_chat_log.json"):
        with open("data/cole_gpt_chat_log.json") as f:
            gpt_log = json.load(f)
            if gpt_log:
                reply = gpt_log[-1]["reply"]

    trade = "N/A"
    if os.path.exists("data/trade_history.json"):
        with open("data/trade_history.json") as f:
            trades = json.load(f)
            if trades:
                last = trades[-1]
                trade = f"{last['symbol']} — {last['strategy']} — ${last['result']} — Grade: {last['grade']}"

    mood = "neutral"
    if os.path.exists("data/mood_state.json"):
        with open("data/mood_state.json") as f:
            mood = json.load(f).get("current_mood", "neutral")

    return render_template("ghost_memory_monitor.html", phase=phase, strategy=strategy, reply=reply, trade=trade, mood=mood)

# === Progress Tracker Route ===
@app.route("/cole_progress_tracker")
def cole_progress_tracker():
    tasks = [
        {"name": "Cole-GPT Chat Log Viewer", "status": "complete", "route": "/cole_chat_history"},
        {"name": "Ghost Memory Monitor", "status": "complete", "route": "/ghost_memory_monitor"},
        {"name": "Market Trend Route Fix", "status": "complete", "route": "/api/market_trend"},
        {"name": "Progress Tracker UI", "status": "in_progress", "route": "/cole_progress_tracker"},
        {"name": "Cole Thought Stream Viewer", "status": "in_progress", "route": "/cole_thought_stream"},
        {"name": "Mobile App Install (PWA)", "status": "in_progress", "route": None},
        {"name": "Voice Chat Assistant", "status": "not_started", "route": "/cole_chat"},
    ]
    return render_template("cole_progress_tracker.html", tasks=tasks)

# === Home Page + System Status ===
@app.route("/")
def home():
    return """
    <h1>PTM Online</h1>
    <p>Build Autonomy + Trading Autonomy both active.</p>
    <ul>
        <li><a href="/status">System Status</a></li>
        <li><a href="/roadmap">Roadmap Viewer (coming soon)</a></li>
        <li><a href="/trades">Trade History</a></li>
        <li><a href="/strategy_leaderboard">Strategy Leaderboard</a></li>
        <li><a href="/autonomy_log">Autonomy Log</a></li>
        <li><a href="/gpt_prompt">Submit GPT Prompt</a></li>
        <li><a href="/autonomy_status">Autonomy Status</a></li>
        <li><a href="/cole_chat_history">Cole-GPT Chat Log</a></li>
        <li><a href="/ghost_memory_monitor">Ghost Memory Monitor</a></li>
        <li><a href="/cole_progress_tracker">Progress Tracker</a></li>
    </ul>
    """

@app.route("/status")
def status():
    return {
        "autonomy_mode": "full",
        "build_loop": "active",
        "trading_loop": "active"
    }

# === Final Launch for Render ===
if __name__ == "__main__":
    print("[PTM App] Launching Flask app with autonomy loops...")
    app.run(host="0.0.0.0", port=10000)