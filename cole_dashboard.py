from ghost_env import INFURA_KEY, VAULT_ADDRESS
from flask import Flask, render_template_string, jsonify
from cole_autopilot_cycle import cole_autopilot_cycle  # ✅ Corrected import
from cole_self_learning_task_generator import generate_self_learning_tasks
from cole_task_optimizer import cole_optimize_tasks
import os

# === Create Dashboard as a Flask App (optional standalone mode) ===
app = Flask(__name__)

# === Dashboard Page as callable function ===
def dashboard_page():
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cole AI Trading System Dashboard</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #121212; color: #f0f0f0; padding: 20px; text-align: center; }
            h1 { color: #6fd672; }
            .btn { display: block; margin: 15px auto; padding: 12px 20px; background: #6fd672; color: #121212; border: none; text-decoration: none; font-weight: bold; border-radius: 5px; width: 320px; cursor: pointer; }
            .btn:hover { background: #89f58c; }
            #log { background-color: #1e1e1e; border-radius: 10px; padding: 15px; margin-top: 30px; height: 300px; overflow-y: auto; text-align: left; font-family: monospace; font-size: 13px; }
        </style>
        <script>
            function fetchLog() {
                fetch('/api/malik_log')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('log').innerText = data.log.join('\\n');
                    });
            }
            setInterval(fetchLog, 5000);
            window.onload = fetchLog;
        </script>
    </head>
    <body>
        <h1>Welcome to Cole's AI Trading System Dashboard</h1>

        <a class="btn" href="/api/self_learning_log">View Self-Learning Log</a>
        <a class="btn" href="/api/help">Help Guide</a>
        <a class="btn" href="/api/get_tasks">View Current Task Queue</a>
        <a class="btn" href="/api/get_results">View Code Generation Results</a>
        <a class="btn" href="/api/get_generated_code">List Generated Code Files (API)</a>
        <a class="btn" href="/dashboard_code_viewer">Open Code Viewer Dashboard</a>
        <a class="btn" href="/payment_dashboard">Payment & Subscription Dashboard</a>
        <a class="btn" href="/trade_health">System Health Check</a>

        <br>

        <button class="btn" onclick="fetch('/force_autopilot').then(r => r.json()).then(d => alert(d.message));">
            Launch Brain & Trade Bots (Priority Mode)
        </button>

        <button class="btn" onclick="fetch('/run_self_learning_optimizer').then(r => r.json()).then(d => alert(d.message));">
            Run Self-Learning Trade Optimizer
        </button>

        <button class="btn" onclick="fetch('/run_task_optimizer').then(r => r.json()).then(d => alert(d.message));">
            Run Task Queue Optimizer
        </button>

        <div id="log">Loading Malik logs...</div>

    </body>
    </html>
    """
    return render_template_string(html_template)

# === Routes if running cole_dashboard.py directly ===:
@app.route('/')
def dashboard_direct():
    return dashboard_page()

@app.route('/force_autopilot', methods=['GET'])
def force_autopilot_direct():
    try:
        cole_autopilot_cycle()
        return jsonify({"message": "Cole Autopilot forced cycle started. Brain and bots are prioritizing readiness for live morning trading."})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/run_self_learning_optimizer', methods=['GET'])
def run_self_learning_optimizer_direct():
    try:
        generate_self_learning_tasks()
        return jsonify({"message": "Cole Self-Learning Trade Optimizer has completed task analysis and updated the queue."})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/run_task_optimizer', methods=['GET'])
def run_task_optimizer_direct():
    try:
        cole_optimize_tasks()
        return jsonify({"message": "Cole Task Optimizer ran successfully and optimized the queue."})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/api/malik_log', methods=['GET'])
def get_malik_log():
    log_file = "data/malik_log.txt"
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            logs = f.readlines()
        logs = [line.strip() for line in logs[-100:]]
    else:
        logs = ["No logs found yet."]
    return jsonify({"log": logs})

# === CLI direct run mode ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():