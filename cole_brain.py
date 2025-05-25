import os
import json
import datetime
import traceback
from datetime import datetime as dt
from cole_gpt_advisor import ask_gpt
from price_data import get_current_rsi, get_historical_prices
from indicators import calc_rsi
from cole_logger import log_info
from cole_task_queue import add_task

# === File Paths ===
MEMORY_FILE = "data/cole_memory.json"
RESULTS_FILE = "data/cole_results.json"
GOALS_FILE = "data/cole_goals.json"
BRAIN_LOG_FILE = "data/cole_brain_log.json"
BRAIN_MEMORY_FILE = "data/cole_brain_memory.json"
RULES_FILE = "data/cole_brain_trading_rules.json"

# === Logging Brain Activity ===
def log_brain_activity(prompt, response):
    os.makedirs("data", exist_ok=True)
    log_entry = {
        "timestamp": dt.now().isoformat(),
        "prompt": prompt,
        "response": response
    }
    logs = []
    if os.path.exists(BRAIN_LOG_FILE):
        try:
            with open(BRAIN_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append(log_entry)
    with open(BRAIN_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)
    print(f"[Cole Brain] Logged brain activity.")

# === Memory Handling ===
def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def load_brain_memory():
    if not os.path.exists(BRAIN_MEMORY_FILE):
        return {}
    with open(BRAIN_MEMORY_FILE, "r") as f:
        return json.load(f)

def save_brain_memory(memory_data):
    with open(BRAIN_MEMORY_FILE, "w") as f:
        json.dump(memory_data, f, indent=2)
    print("[Cole Brain] Memory updated.")

# === Goals and Results ===
def load_goals():
    if os.path.exists(GOALS_FILE):
        with open(GOALS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_result(code, tag, explanation):
    results = []
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "r") as f:
            results = json.load(f)
    results.append({
        "timestamp": str(datetime.datetime.now()),
        "tag": tag,
        "code": code,
        "explanation": explanation
    })
    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=2)

# === Cole Think Engine ===
def cole_think(prompt):
    print(f"[Cole Brain] Thinking on prompt: {prompt}")
    return ask_gpt(prompt)

def log_brain_thought(content):
    entry = {
        "timestamp": dt.now().isoformat(),
        "content": content
    }

    brain = []
    if os.path.exists(BRAIN_LOG_FILE):
        try:
            with open(BRAIN_LOG_FILE, "r") as f:
                brain = json.load(f)
        except:
            brain = []

    brain.append(entry)
    with open(BRAIN_LOG_FILE, "w") as f:
        json.dump(brain[-300:], f, indent=2)

# === Brain Trading Rules Logic ===
def load_trading_rules():
    if not os.path.exists(RULES_FILE):
        return []
    with open(RULES_FILE, "r") as f:
        return json.load(f).get("rules", [])

def evaluate_rsi_rule(symbol):
    prices = get_historical_prices(symbol)
    if not prices:
        return False
    rsi = calc_rsi(prices)
    return rsi <= 30 or rsi >= 70

def evaluate_strategy_rule(strategy):
    return strategy.get("win_rate", 0) >= 65

def evaluate_trend_alignment(strategy, trend):
    return (strategy.get("type") == "bullish" and trend == "up") or (strategy.get("type") == "bearish" and trend == "down")

def is_excluded_from_watchlist(symbol, exclusion_list):
    return symbol in exclusion_list

def brain_allows_trade(symbol, strategy, trend, exclusion_list=[]):
    rules = load_trading_rules()
    for rule in rules:
        logic = rule.get("logic", {})
        rule_type = logic.get("type")

        if rule_type == "indicator_check" and not evaluate_rsi_rule(symbol):
            return False
        if rule_type == "strategy_filter" and not evaluate_strategy_rule(strategy):
            return False
        if rule_type == "trend_confirmation" and not evaluate_trend_alignment(strategy, trend):
            return False
        if rule_type == "watchlist_filter" and is_excluded_from_watchlist(symbol, exclusion_list):
            return False
    return True

# === Brain Health Check ===
def check_brain_health():
    required_files = [
        "data/cole_brain_log.json",
        "data/strategy_scores.json",
        "data/phase.json"
    ]
    for file in required_files:
        if not os.path.exists(file):
            with open(file, "w") as f:
                json.dump([], f)
            print(f"[Cole Brain] Created missing file: {file}")

# === Phase & Strategy Memory Logger ===
def log_phase_and_strategy(phase, strategy):
    entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "phase": phase,
        "strategy": strategy
    }

    try:
        if os.path.exists(BRAIN_LOG_FILE):
            with open(BRAIN_LOG_FILE, "r") as f:
                data = json.load(f)
        else:
            data = []

        data.append(entry)
        with open(BRAIN_LOG_FILE, "w") as f:
            json.dump(data[-500:], f, indent=2)

        print(f"[Cole Brain] Memory logged: phase={phase}, strategy={strategy}")
    except Exception as e:
        print(f"[Cole Brain] Failed to log: {e}")

# === Log Strategy Reason ===
def log_strategy_reason(strategy, reason):
    try:
        print(f"[Cole Brain] Strategy reason logged: {strategy} — {reason}")
    except Exception as e:
        print(f"[Cole Brain] Error logging reason: {e}")

# === Autopilot Decision Loop ===
def run_decision_cycle():
    log_info("[Cole Brain] Starting decision cycle...")
    default_tasks = [
        "Scan for RSI reversals",
        "Check Bollinger Band breaches",
        "Update EMA crossover table",
        "Review Congress-based signals",
        "Adjust risk weights on all trades"
    ]
    for task in default_tasks:
        added = add_task(task)
        if added:
            log_info(f"[Cole Brain] Task added to queue: {task}")
        else:
            log_info(f"[Cole Brain] Task skipped or duplicate: {task}")
    log_info("[Cole Brain] Decision cycle complete.")

# === CLI Test ===
if __name__ == "__main__":
    test_code = cole_think("Write API that returns system health on /api/system_health")
    print(test_code)
    test_strategy = { "name": "Covered Call", "type": "bullish", "win_rate": 72 }
    allowed = brain_allows_trade("AAPL", test_strategy, "up", exclusion_list=["TSLA"])
    print("Trade Approved:", allowed)