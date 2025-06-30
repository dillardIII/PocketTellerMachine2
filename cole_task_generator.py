from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import datetime
from cole_task_queue import add_task

TASKS_FILE = "data/cole_tasks.json"
TASK_QUEUE_FILE = "data/cole_task_queue.json"

# === Smart Detector Example: Detect missing health endpoint ===
def detect_missing_trade_health_api():
    app_file = "app.py"
    if not os.path.exists(app_file):
        return False
    with open(app_file, "r") as f:
        content = f.read()
    return "/trade_health" not in content

# === Load / Save Task Queue ===
def load_task_queue():
    if not os.path.exists(TASK_QUEUE_FILE):
        return []
    with open(TASK_QUEUE_FILE, "r") as f:
        return json.load(f)

def save_task_queue(tasks):
    with open(TASK_QUEUE_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# === Check if Task Exists ===:
def task_exists(tasks, task_text):
    return any(t["task"] == task_text for t in tasks)

# === Market Phase Detector ===
def get_market_phase():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute

    if hour < 9 or (hour == 9 and minute < 30):
        return "pre_market"
    elif 9 <= hour < 12:
        return "morning_session"
    elif 12 <= hour < 15:
        return "mid_day"
    elif 15 <= hour < 16:
        return "power_hour"
    else:
        return "after_market"

# === Enhanced Phase-Based Generator with Smart Detection ===
def generate_tasks_based_on_phase():
    tasks = load_task_queue()
    new_tasks = []

    phase = get_market_phase()
    print(f"[Cole Task Generator] Current phase: {phase}")

    if phase == "pre_market":
        if not task_exists(tasks, "Check full market scan for stocks with RSI < 30"):
            new_tasks.append({
                "timestamp": str(datetime.datetime.now()),
                "task": "Check full market scan for stocks with RSI < 30"
            })
        if not task_exists(tasks, "Review overnight news impact on watchlist"):
            new_tasks.append({
                "timestamp": str(datetime.datetime.now()),
                "task": "Review overnight news impact on watchlist"
            })

    elif phase == "morning_session":
        if not task_exists(tasks, "Scan top movers and volume leaders"):
            new_tasks.append({
                "timestamp": str(datetime.datetime.now()),
                "task": "Scan top movers and volume leaders"
            })
        if not task_exists(tasks, "Check portfolio risk exposure"):
            new_tasks.append({
                "timestamp": str(datetime.datetime.now()),
                "task": "Check portfolio risk exposure"
            })

    elif phase == "mid_day":
        if not task_exists(tasks, "Review morning trades and flag underperformers"):
            new_tasks.append({
                "timestamp": str(datetime.datetime.now()),
                "task": "Review morning trades and flag underperformers"
            })
        if not task_exists(tasks, "Scan for reversal patterns"):
            new_tasks.append({
                "timestamp": str(datetime.datetime.now()),
                "task": "Scan for reversal patterns"
            })

    elif phase == "power_hour":
        if not task_exists(tasks, "Scan market for power hour breakout opportunities"):
            new_tasks.append({
                "timestamp": str(datetime.datetime.now()),
                "task": "Scan market for power hour breakout opportunities"
            })
        if not task_exists(tasks, "Review intraday P&L and adjust positions"):
            new_tasks.append({
                "timestamp": str(datetime.datetime.now()),
                "task": "Review intraday P&L and adjust positions"
            })

    elif phase == "after_market":
        if not task_exists(tasks, "Review all trades and log performance summary"):
            new_tasks.append({
                "timestamp": str(datetime.datetime.now()),
                "task": "Review all trades and log performance summary"
            })
        if not task_exists(tasks, "Run AI learning module to adjust next day strategies"):
            new_tasks.append({
                "timestamp": str(datetime.datetime.now()),
                "task": "Run AI learning module to adjust next day strategies"
            })

    # === Smart Self-Write Detection: Missing Health API ===
    if detect_missing_trade_health_api():
        task_text = "Write Flask API that returns trade health on /trade_health"
        if not task_exists(tasks, task_text):
            print(f"[Cole Queue] Adding self-writing task: {task_text}")
            new_tasks.append({
                "timestamp": str(datetime.datetime.now()),
                "task": task_text,
                "type": "self_write"
            })

    # Merge and save
    if new_tasks:
        tasks.extend(new_tasks)
        save_task_queue(tasks)
        print(f"[Cole Task Generator] Added {len(new_tasks)} new tasks.")
    else:
        print("[Cole Task Generator] No new tasks needed.")

# === Legacy Phase Generator (File-Based) ===
def generate_tasks_legacy():
    print("[Cole Task Generator] Checking phase (legacy file mode)...")
    hour = datetime.datetime.now().hour
    tasks = load_tasks()

    if 4 <= hour < 9:
        task = "Analyze pre-market movers and gaps."
    elif 9 <= hour < 10:
        task = "Check opening volatility and gap fills."
    elif 10 <= hour < 15:
        task = "Midday market drift scanning."
    else:
        task = "Prepare after-hours earnings scan."

    if task not in tasks:
        tasks.append(task)
        save_tasks(tasks)
        print(f"[Cole Task Generator] Task added: {task}")
    else:
        print(f"[Cole Task Generator] Task already exists: {task}")

# === Load / Save Legacy Tasks ===
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# === Simple Default Task Generator ===
def cole_generate_tasks():
    return [
        "Scan watchlist for momentum",
        "Evaluate RSI levels",
        "Check earnings calendar",
        "Update trade logs",
        "Review open positions"
    ]

# === CLI Trigger ===
if __name__ == "__main__":
    print("[Cole Task Generator] Running enhanced task generator...")
    generate_tasks_based_on_phase()

    print("[Cole Task Generator] Also running legacy file mode (optional)...")
    generate_tasks_legacy()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():