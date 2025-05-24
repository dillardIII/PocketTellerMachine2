# === FILE: autonomy_status_api.py ===

import os
import json
from flask import Blueprint, jsonify
from datetime import datetime

autonomy_status_bp = Blueprint("autonomy_status", __name__)

def get_file_timestamp(file_path):
    if os.path.exists(file_path):
        ts = os.path.getmtime(file_path)
        return datetime.fromtimestamp(ts).isoformat()
    return None

@autonomy_status_bp.route("/autonomy/status", methods=["GET"])
def autonomy_status():
    try:
        memory_path = "data/cole_brain_memory.json"
        task_queue_path = "data/autopilot_queue.json"
        loop_log_path = "logs/loop.log"  # optional if you log loop start/finish

        memory = {}
        if os.path.exists(memory_path):
            with open(memory_path, "r") as f:
                memory = json.load(f)

        trades = memory.get("trades", [])
        last_trade = trades[-1] if trades else {}
        trade_count = len(trades)
        avg_win_rate = "N/A"

        if trades:
            wins = [t for t in trades if t.get("result", 0) > 0]
            avg_win_rate = f"{round(len(wins)/len(trades)*100, 1)}%"

        tasks = []
        if os.path.exists(task_queue_path):
            with open(task_queue_path, "r") as f:
                tasks = json.load(f)

        return jsonify({
            "autonomy_status": "online",
            "last_loop_time": get_file_timestamp(loop_log_path),
            "trades_logged": trade_count,
            "latest_trade": last_trade,
            "average_win_rate": avg_win_rate,
            "pending_tasks": len(tasks),
            "timestamp": datetime.utcnow().isoformat()
        })

    except Exception as e:
        return jsonify({
            "autonomy_status": "error",
            "error": str(e),
            "timestamp": datetime.utcnow().isoformat()
        })