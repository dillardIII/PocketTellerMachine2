# cole_tools/cole_voice_summary_daemon.py

import time
import json
import os
from datetime import datetime

TRADES_FILE = "data/trades_cleaned.json"
OUTPUT_FILE = "data/trade_voice_summary.json"

def generate_voice_summary(trades):
    summaries = []
    for trade in trades:
        symbol = trade.get("symbol", "Unknown")
        strategy = trade.get("strategy", "Unknown")
        result = trade.get("result", 0.0)
        summary = f"Trade executed using {strategy} on {symbol} with result ${result}."
        summaries.append({
            "id": trade.get("id", ""),
            "symbol": symbol,
            "strategy": strategy,
            "result": result,
            "summary": summary,
            "timestamp": trade.get("timestamp", datetime.now().isoformat())
        })
    return summaries

def load_trades():
    if not os.path.exists(TRADES_FILE):
        return []
    with open(TRADES_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_voice_summaries(summaries):
    with open(OUTPUT_FILE, "w") as f:
        json.dump(summaries, f, indent=2)

def generate_voice_summaries():
    trades = load_trades()
    if trades:
        summaries = generate_voice_summary(trades)
        save_voice_summaries(summaries)
        print(f"[VOICE SUMMARY DAEMON]: Generated {len(summaries)} summaries.")
    else:
        print("[VOICE SUMMARY DAEMON]: No trades to process.")

print("[DAEMON]: Voice Summary Generator Daemon is running...")

def monitor_loop(interval=120):
    while True:
        try:
            if os.path.exists(TRADES_FILE):
                print("[DAEMON]: Checking and generating updated voice summaries...")
                generate_voice_summaries()
            else:
                print("[DAEMON]: No trades_cleaned.json found. Skipping...")

            time.sleep(interval)
        except Exception as e:
            print(f"[DAEMON ERROR]: {e}")
            time.sleep(30)

if __name__ == "__main__":
    monitor_loop()