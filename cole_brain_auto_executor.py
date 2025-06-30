from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_brain_auto_executor.py

import os
import json
import time
import random
import requests
from datetime import datetime
from cole_code_writer import cole_write_code
from cole_task_optimizer import cole_optimize_tasks
from cole_memory_brain import load_memory, log_memory_event
from cole_executor import cole_auto_run
from cole_command_interpreter import cole_interpret_command
from test_auto_evolve_from_trades import analyze_strategy_performance
from test_fusion_predictor import predict_stock_bias
from test_fusion_strategy_adjuster import adjust_strategy_based_on_bias
from brain import execute_trade, calculate_grade

# === Configurations ===
COLE_WEBHOOK_URL = "http://localhost:5050/cole_webhook"
BRAIN_LOG_FILE = "data/cole_brain_log.json"
GHOST_LOG_FILE = "data/ghost_log.json"
HEARTBEAT_FILE = "data/heartbeat.json"
BRAIN_EXECUTOR_LOG_FILE = "data/cole_brain_auto_executor_log.json"
SYMBOLS = ["AAPL", "TSLA", "AMC", "NVDA"]
BASE_STRATEGIES = ["RSI_Reversal", "SMA_Cross", "Iron_Condor"]
CHECK_INTERVAL = 900  # 15 minutes

# === Ensure data directory ===
os.makedirs("data", exist_ok=True)

# === Logging Helper ===
def log_brain_executor_event(message):
    logs = []
    if os.path.exists(BRAIN_EXECUTOR_LOG_FILE):
        try:
            with open(BRAIN_EXECUTOR_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(BRAIN_EXECUTOR_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

def log_event(message):
    logs = []
    if os.path.exists(BRAIN_LOG_FILE):
        with open(BRAIN_LOG_FILE, "r") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(BRAIN_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

def ghost_log_event(message):
    logs = []
    if os.path.exists(GHOST_LOG_FILE):
        with open(GHOST_LOG_FILE, "r") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(GHOST_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Heartbeat ===
def update_heartbeat(status):
    with open(HEARTBEAT_FILE, "w") as f:
        json.dump({"status": status, "timestamp": datetime.now().isoformat()}, f)

# === Core Auto Executor Brain Loop ===
def cole_brain_auto_executor_loop(cycles=999999, wait_seconds=30):
    print("[COLE BRAIN]: Ghost Logger + Auto-Recovery Brain started...")
    error_count = 0

    for cycle in range(cycles):
        try:
            log_event(f"Cycle {cycle + 1} started.")
            ghost_log_event(f"Cycle {cycle + 1} started.")
            update_heartbeat("THINKING")

            for symbol in SYMBOLS:
                base_strategy = random.choice(BASE_STRATEGIES)
                bias = predict_stock_bias(symbol)
                adjusted_strategy = adjust_strategy_based_on_bias(base_strategy, bias)

                result = simulate_trade_result(bias)
                trade = execute_trade(symbol, adjusted_strategy, result)
                grade = calculate_grade(result)
                trade["grade"] = grade
                log_memory_event("trades", trade)
                log_event(f"[TRADE]: {trade}")
                ghost_log_event(f"[TRADE]: {trade}")

                if grade in ["C", "D", "F"]:
                    filename = cole_write_code(f"{symbol} Correction Strategy", f"Generated correction strategy after poor grade {grade}")
                    log_event(f"[EVOLUTION]: Generated correction strategy: {filename}")
                    ghost_log_event(f"[EVOLUTION]: Generated correction strategy: {filename}")

            cole_optimize_tasks()
            analyze_strategy_performance()

            memory = load_memory()
            missing_patterns = detect_missing_patterns(memory)
            for pattern in missing_patterns:
                filename = cole_write_code(f"Auto_{pattern}_Strategy", f"Auto-generated for pattern {pattern}")
                log_event(f"[GAP FILLER]: Generated strategy: {filename}")
                ghost_log_event(f"[GAP FILLER]: Generated strategy: {filename}")

            cole_auto_run()

            ai_command = generate_self_coaching_command()
            if ai_command:
                response = cole_interpret_command(ai_command)
                log_event(f"[SELF-COACH]: {ai_command} → {response}")
                ghost_log_event(f"[SELF-COACH]: {ai_command} → {response}")

            update_heartbeat("IDLE")
            dynamic_wait = smart_sleep(memory)
            log_event(f"[SMART SLEEP]: Next cycle will wait {dynamic_wait} seconds.")
            ghost_log_event(f"[SMART SLEEP]: Next cycle will wait {dynamic_wait} seconds.")
            error_count = 0
            time.sleep(dynamic_wait)

        except Exception as e:
            log_event(f"[CRITICAL ERROR]: {e}")
            ghost_log_event(f"[CRITICAL ERROR]: {e}")
            update_heartbeat("ERROR")
            error_count += 1
            if error_count >= 5:
                ghost_log_event("[AUTO-RECOVERY]: Critical error threshold reached. Restarting brain loop.")
                error_count = 0
            time.sleep(wait_seconds)

# === Utility Functions ===
def simulate_trade_result(bias):
    if "Bullish" in bias:
        return round(random.uniform(10, 100), 2)
    elif "Bearish" in bias:
        return round(random.uniform(-100, -10), 2)
    else:
        return round(random.uniform(-20, 20), 2)

def detect_missing_patterns(memory):
    known = [t.get("strategy", "") for t in memory.get("trades", [])]
    patterns = []
    if not any("RSI" in s for s in known):
        patterns.append("RSI_Reversal")
    if not any("SMA" in s for s in known):
        patterns.append("SMA_Cross")
    return patterns

def generate_self_coaching_command():
    return "analyze strategy performance"

def smart_sleep(memory):
    if is_market_open():
        return 10
    elif count_recent_trades(memory) > 5:
        return 15
    else:
        return 60

def is_market_open():
    now = datetime.now().hour
    return 9 <= now < 16

def count_recent_trades(memory, minutes=30):
    count = 0
    cutoff = datetime.now().timestamp() - (minutes * 60)
    for trade in memory.get("trades", []):
        try:
            trade_time = datetime.fromisoformat(trade.get("timestamp", ""))
            if trade_time.timestamp() > cutoff:
                count += 1
        except:
            continue
    return count

# === Run the Daemon ===
if __name__ == "__main__":
    cole_brain_auto_executor_loop()

    # === Optional simulation fallback (commented) ===
    # while True:
    #     print("[Daemon]: Brain Auto Executor running... (simulated)")
    #     time.sleep(900)