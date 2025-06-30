from ghost_env import INFURA_KEY, VAULT_ADDRESS
from flask import Flask, jsonify, send_from_directory
import os
import json
from datetime import datetime

app = Flask(__name__)

# === Log files to aggregate ===
LOG_FILES = [
    "data/cole_brain_log.json",
    "data/cole_heartbeat_monitor_log.json",
    "data/cole_brain_auto_executor_log.json",
    "data/cole_autonomous_execution_log.json",
    "data/decision_trigger_log.json",
    "data/self_improving_strategy_log.json",
    "data/self_healing_error_watcher_log.json",
    "data/auto_correction_loop_log.json",
    "data/smart_code_requestor_log.json",
    "data/smart_feedback_responder_log.json",
    "data/chatgpt_feedback_log.json",
    "data/cole_webhook_log.json",
    "data/cole_bridge_log.json",
    "data/cole_cleaner_log.json",
    "data/cole_trade_review_log.json",
    "data/ghost_log.json",
    "data/heartbeat_monitor_log.json"
]

@app.route('/cole_phase11_log_streamer')
def get_logs():
    all_logs = []
    for file_path in LOG_FILES:
        if os.path.exists(file_path):
            try:
                with open(file_path, "r") as f:
                    logs = json.load(f)
                    all_logs.extend(logs)
            except:
                continue
    all_logs = sorted(all_logs, key=lambda x: x.get("timestamp", ""), reverse=True)
    return jsonify({"logs": all_logs[-500:]})

@app.route('/')
def home():
    return send_from_directory('.', 'cole_phase11_log_streamer.html')

if __name__ == "__main__":
    print("[COLE PHASE 11 LOG STREAMER]: Running on port 8080...")
    app.run(host='0.0.0.0', port=8080, debug=True)

def log_event():ef drop_files_to_bridge():