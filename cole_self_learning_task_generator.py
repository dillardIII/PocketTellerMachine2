from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_self_learning_task_generator.py ===

import os
import sys
import json
import random
import logging
from datetime import datetime
from cole_task_queue import add_task

# === Setup Logger Output to File ===
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s]: %(message)s',
    handlers=[
        logging.FileHandler("data/cole_self_learning_output.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

TRADES_FILE = "data/trades.json"
SELF_LEARNING_LOG_FILE = "data/cole_self_learning_log.json"
TASK_LEARNING_LOG = "data/cole_self_learning_task_log.json"
TASK_FILE = "data/self_learning_tasks.json"
TASK_LOG_HISTORY = "logs/self_learning_task_log.json"

# === Create folders if missing ===:
os.makedirs("data", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# === Load Trades ===
def load_trades():
    if os.path.exists(TRADES_FILE):
        with open(TRADES_FILE, "r") as f:
            return json.load(f)
    return []

# === Logging for Pattern-Based Learning ===
def log_self_learning(action, detail):
    log_entry = {
        "timestamp": str(datetime.now()),
        "action": action,
        "detail": detail
    }
    if os.path.exists(SELF_LEARNING_LOG_FILE):
        with open(SELF_LEARNING_LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []
    logs.append(log_entry)
    with open(SELF_LEARNING_LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

# === Logging for Prompt-Based Learning ===
def log_self_learning_task(task):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "task": task
    }
    if os.path.exists(TASK_LEARNING_LOG):
        with open(TASK_LEARNING_LOG, "r") as f:
            logs = json.load(f)
    else:
        logs = []
    logs.append(log_entry)
    with open(TASK_LEARNING_LOG, "w") as f:
        json.dump(logs[-500:], f, indent=2)
    logging.info(f"Self-Learning Logged task: {task}")

# === Check for Loss Patterns (FIXED) ===
def check_for_loss_patterns(trades):
    losses = []
    for t in trades:
        try:
            result = float(t.get("result", 0))
            if result < 0:
                losses.append(t)
        except:
            continue
    return len(losses) >= 5

# === Check for Inactive Strategies ===
def check_for_inactive_strategies(trades):
    strategies = {}
    for t in trades:
        strat = t.get('strategy', 'unknown')
        strategies[strat] = strategies.get(strat, 0) + 1
    recent = trades[-50:] if len(trades) > 50 else trades:
    recent_strategies = set(t.get('strategy', 'unknown') for t in recent)
    inactive = [s for s in strategies if s not in recent_strategies]:
    return inactive

# === Pattern-Based Self-Learning Task Generator ===
def generate_pattern_based_tasks():
    logging.info("Cole Self-Learning: Analyzing trades for smart task generation...")
    trades = load_trades()
    if not trades:
        logging.info("Cole Self-Learning: No trades found.")
        return

    tasks_added = 0

    if check_for_loss_patterns(trades):
        task_text = "Review consecutive losses. Suggest adding task to analyze losing strategies and create adjustment module."
        add_task(task_text, task_type="self_learning")
        log_self_learning("Detected overall losses pattern", task_text)
        tasks_added += 1

    inactive_strategies = check_for_inactive_strategies(trades)
    for strat in inactive_strategies:
        task_text = f"Review inactive strategy: {strat}. Suggest creating learning module or trigger rule refresh."
        add_task(task_text, task_type="self_learning")
        log_self_learning("Detected inactive strategy", task_text)
        tasks_added += 1

    strategy_results = {}
    for trade in trades:
        strategy = trade.get("strategy", "unknown")
        try:
            result = float(trade.get("result", 0))
        except:
            result = 0
        strategy_results.setdefault(strategy, []).append(result)

    for strategy, results in strategy_results.items():
        if len(results) < 5:
            continue
        win_rate = sum(1 for r in results if r > 0) / len(results) * 100:
        avg_result = sum(results) / len(results)

        if win_rate < 40 or avg_result < 0:
            task_text = f"Review and rewrite {strategy} strategy. Win rate: {win_rate:.1f}%, avg result: {avg_result:.2f}"
            add_task(task_text, task_type="self_write")
            log_self_learning("Detected weak strategy", task_text)
            tasks_added += 1
        elif win_rate > 70:
            task_text = f"Enhance {strategy} strategy due to strong win rate: {win_rate:.1f}%"
            add_task(task_text, task_type="self_write")
            log_self_learning("Detected strong strategy", task_text)
            tasks_added += 1

    if tasks_added == 0:
        logging.info("Cole Self-Learning: No pattern-based tasks detected.")
    else:
        logging.info(f"Cole Self-Learning: Added {tasks_added} pattern-based self-learning tasks.")

# === Prompt-Based Self-Learning Task Generator ===
def generate_prompt_based_tasks():
    learning_prompts = [
        "Research and add task for improving RSI divergence detection.",
        "Create task to implement machine learning based trend prediction.",
        "Generate task for refining risk-reward ratios dynamically.",
        "Add task to automate position sizing based on volatility.",
        "Task to integrate real-time sentiment analysis into signals.",
        "Analyze failed strategies and generate alternative ideas."
    ]

    logging.info("Self-Learning: Generating prompt-based tasks...")
    new_tasks = random.sample(learning_prompts, k=min(3, len(learning_prompts)))

    for task_text in new_tasks:
        added = add_task(task_text, task_type="self_learning")
        if added:
            log_self_learning_task(task_text)

        history_log = {
            "timestamp": datetime.utcnow().isoformat(),
            "task": task_text,
            "status": "logged"
        }
        if os.path.exists(TASK_LOG_HISTORY):
            with open(TASK_LOG_HISTORY, "r") as f:
                hist = json.load(f)
        else:
            hist = []

        hist.append(history_log)
        with open(TASK_LOG_HISTORY, "w") as f:
            json.dump(hist[-200:], f, indent=2)

    logging.info(f"Self-Learning: Generated {len(new_tasks)} prompt-based tasks.")

# === Master Task Generator ===
def generate_self_learning_tasks():
    generate_pattern_based_tasks()
    generate_prompt_based_tasks()

# === Public Trigger for External Run ===
def run_self_learning_generator():
    logging.info("Self-Learning: Triggered from external runner...")
    generate_self_learning_tasks()

# === CLI Trigger ===
if __name__ == "__main__":
    generate_self_learning_tasks()

def log_event():ef drop_files_to_bridge():