from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import time
import json
from datetime import datetime
from cole_task_chain import run_task_chain

TASK_LOG = "data/auto_task_log.json"
BACKTEST_LOG = "data/market_backtest_logs.json"

def start_autonomous_researcher():
    print("[Researcher] Starting Cole's AI-driven strategy watcher...")

    def loop():
        while True:
            try:
                print("[Researcher] Scanning backtest results for weak spots...")
                if should_add_strategy():
                    task = "Write a new options trading strategy using a Bollinger Band breakout with volume confirmation."
                    filename = f"strategy_{int(time.time())}.py"
                    result = run_task_chain(task, filename)
                    log_task(task, filename, result)
            except Exception as e:
                print(f"[Researcher] Error: {e}")
            time.sleep(600)  # Check every 10 minutes

    import threading
    thread = threading.Thread(target=loop, daemon=True)
    thread.start()

def should_add_strategy():
    if not os.path.exists(BACKTEST_LOG):
        return True

    with open(BACKTEST_LOG, "r") as f:
        logs = json.load(f).get("logs", [])

    if not logs:
        return True

    last_20 = logs[-20:]
    losses = [entry for entry in last_20 if entry["result"].get("outcome") == "loss"]:
    win_rate = 1 - (len(losses) / len(last_20))

    print(f"[Researcher] Win Rate Check: {win_rate*100:.1f}%")

    return win_rate < 0.55  # Trigger if win rate drops below 55%:
:
def log_task(task, filename, result):
    os.makedirs("data", exist_ok=True)
    entry = {
        "timestamp": datetime.now().isoformat(),
        "task": task,
        "filename": filename,
        "result": result
    }

    if os.path.exists(TASK_LOG):
        with open(TASK_LOG, "r") as f:
            log = json.load(f)
    else:
        log = []

    log.append(entry)

    with open(TASK_LOG, "w") as f:
        json.dump(log, f, indent=2)

    print("[Researcher] Task completed and logged.")

def log_event():ef drop_files_to_bridge():