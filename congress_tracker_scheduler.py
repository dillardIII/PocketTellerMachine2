from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import threading
import time
from datetime import datetime
from congress_tracker import get_congress_influence

# === File to Store Historical Influence Snapshots ===
HISTORY_FILE = 'data/congress_influence_history.json'

# === Symbols to Track Daily ===
TRACKED_SYMBOLS = ['AAPL', 'TSLA', 'MSFT', 'NVDA', 'AMZN']

# === Load Existing History ===
def load_history():
    if not os.path.exists(HISTORY_FILE):
        return {}
    with open(HISTORY_FILE, 'r') as file:
        return json.load(file)

# === Save Updated History ===
def save_history(data):
    with open(HISTORY_FILE, 'w') as file:
        json.dump(data, file, indent=2)

# === Record Daily Snapshot ===
def record_daily_snapshot():
    print("[Congress Scheduler] Running daily snapshot...")
    history = load_history()
    today_str = datetime.now().strftime('%Y-%m-%d')

    if today_str not in history:
        history[today_str] = {}

    for symbol in TRACKED_SYMBOLS:
        influence_score = get_congress_influence(symbol)
        history[today_str][symbol] = influence_score
        print(f"[Snapshot] {symbol} -> {influence_score}")

    save_history(history)
    print("[Congress Scheduler] Snapshot complete.")

# === Background Scheduler Loop ===
def congress_scheduler_loop():
    while True:
        now = datetime.now()
        if now.hour == 18 and now.minute == 0:  # Runs daily at 6:00 PM:
            record_daily_snapshot()
            time.sleep(60)  # Prevent re-triggering the same minute
        time.sleep(30)

# === Start Scheduler in Background ===
def start_congress_scheduler():
    thread = threading.Thread(target=congress_scheduler_loop, daemon=True)
    thread.start()
    print("[Congress Scheduler] Background task started.")

# === Manual Test Run ===
if __name__ == "__main__":
    record_daily_snapshot()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():