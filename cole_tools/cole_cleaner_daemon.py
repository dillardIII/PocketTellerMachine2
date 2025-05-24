import os
import time
import json
from datetime import datetime

INPUT_FILE = "data/trades.json"
OUTPUT_FILE = "data/trades_cleaned.json"
LOG_FILE = "data/cole_cleaner_log.json"
INTERVAL_SECONDS = 60  # How often to clean

REQUIRED_FIELDS = {
    "symbol": str,
    "strategy": str,
    "entry": float,
    "exit": float,
    "result": float,
    "timestamp": str
}

DEFAULTS = {
    "strategy": "Unknown_Strategy",
    "entry": 0.0,
    "exit": 0.0,
    "result": 0.0
}

def clean_trades(input_file, output_file):
    if not os.path.exists(input_file):
        log_event(f"[WARNING]: {input_file} not found.")
        return

    with open(input_file, "r") as f:
        try:
            trades = json.load(f)
        except json.JSONDecodeError:
            log_event("[ERROR]: Invalid JSON format.")
            return

    cleaned_trades = []

    for trade in trades:
        clean_trade = {}
        for field, field_type in REQUIRED_FIELDS.items():
            if field not in trade or trade[field] == "" or trade[field] is None:
                clean_trade[field] = DEFAULTS.get(field, "")
            else:
                try:
                    if field_type == float:
                        clean_trade[field] = float(trade[field])
                    elif field_type == str:
                        clean_trade[field] = str(trade[field])
                    else:
                        clean_trade[field] = trade[field]
                except (ValueError, TypeError):
                    clean_trade[field] = DEFAULTS.get(field, "")

        clean_trade["id"] = trade.get("id", f"auto_{datetime.now().isoformat()}")
        clean_trade["timestamp"] = trade.get("timestamp", datetime.now().isoformat())

        cleaned_trades.append(clean_trade)

    with open(output_file, "w") as f:
        json.dump(cleaned_trades, f, indent=2)

    log_event(f"[CLEANER]: Cleaned {len(cleaned_trades)} trades.")

def log_event(message):
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            try:
                logs = json.load(f)
            except:
                logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(LOG_FILE, "w") as f:
        json.dump(logs[-100:], f, indent=2)

def cleaner_daemon_loop():
    print("[CLEANER DAEMON]: JSON Cleaner Daemon started...")
    while True:
        try:
            clean_trades(INPUT_FILE, OUTPUT_FILE)
        except Exception as e:
            log_event(f"[ERROR]: {e}")
        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    # === Real cleaner daemon mode ===
    cleaner_daemon_loop()

    # === Simulated mode ===
    # while True:
    #     print("[Daemon]: JSON Cleaner running... (simulated)")
    #     # Simulated tasks like cleanup placeholder
    #     time.sleep(60)