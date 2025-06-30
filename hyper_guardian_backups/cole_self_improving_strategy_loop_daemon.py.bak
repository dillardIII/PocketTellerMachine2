import os
import json
import time
from datetime import datetime
from assistants.malik import malik_report
from cole_task_queue import add_task
from cole_brain import cole_think

STRATEGY_LOG_FILE = "data/cole_strategy_improvement_log.json"
CHECK_INTERVAL = 1800  # 30 minutes

# === Logging Helper ===
def log_strategy_event(message):
    logs = []
    if os.path.exists(STRATEGY_LOG_FILE):
        try:
            with open(STRATEGY_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(STRATEGY_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Strategy Improvement Cycle ===
def run_strategy_improvement_cycle():
    print("[Cole Strategy Improvement Loop] Running cycle...")

    prompt = """
    Review current AI trading strategies and suggest improvements.
    Focus on:
    - Increasing win rate.
    - Reducing drawdown.
    - Improving entry/exit accuracy.
    Provide 3 actionable strategy enhancements as a JSON list.
    """

    try:
        response = cole_think(prompt)
        suggestions = json.loads(response)

        if isinstance(suggestions, list):
            for suggestion in suggestions:
                added = add_task(suggestion, task_type="strategy_improvement")
                if added:
                    log_strategy_event(f"Added strategy task: {suggestion}")
                    malik_report(f"Strategy Improvement Triggered Task: {suggestion}")
        else:
            log_strategy_event("Response format error: Expected list.")
            malik_report("[Strategy Loop] Invalid response format received.")

    except Exception as e:
        log_strategy_event(f"[Strategy Loop Error]: {e}")
        malik_report(f"[Strategy Loop Error] {e}")

# === Main Loop ===
def strategy_improvement_loop():
    print("[Cole Self-Improving Strategy Loop] Monitoring started.")
    while True:
        run_strategy_improvement_cycle()
        time.sleep(CHECK_INTERVAL)

# === CLI Trigger ===
if __name__ == "__main__":
    strategy_improvement_loop()