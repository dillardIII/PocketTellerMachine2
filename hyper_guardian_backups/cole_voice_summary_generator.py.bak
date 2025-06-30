# cole_voice_summary_generator.py

import json
import os
from datetime import datetime

TRADES_FILE = "data/trades_cleaned.json"
OUTPUT_FILE = "data/trade_voice_summary.json"

def generate_voice_summaries():
    if not os.path.exists(TRADES_FILE):
        print("[VOICE SUMMARY]: No trades file found.")
        return

    with open(TRADES_FILE, "r") as f:
        try:
            trades = json.load(f)
        except json.JSONDecodeError:
            print("[VOICE SUMMARY]: Invalid trades JSON format.")
            return

    summaries = []
    for trade in trades:
        summary = create_summary(trade)
        summaries.append({
            "id": trade.get("id", f"summary_{datetime.now().isoformat()}"),
            "symbol": trade.get("symbol", "UNKNOWN"),
            "strategy": trade.get("strategy", "Unknown_Strategy"),
            "result": trade.get("result", 0.0),
            "summary_text": summary,
            "timestamp": trade.get("timestamp", datetime.now().isoformat())
        })

    with open(OUTPUT_FILE, "w") as f:
        json.dump(summaries, f, indent=2)
    print(f"[VOICE SUMMARY]: Summaries generated to {OUTPUT_FILE} | Total: {len(summaries)}")

def create_summary(trade):
    symbol = trade.get("symbol", "UNKNOWN")
    strategy = trade.get("strategy", "Unknown_Strategy")
    result = trade.get("result", 0.0)

    if result >= 0:
        return f"Trade on {symbol} using {strategy} strategy made a profit of ${result}."
    else:
        return f"Trade on {symbol} using {strategy} strategy resulted in a loss of ${abs(result)}."

if __name__ == "__main__":
    generate_voice_summaries()