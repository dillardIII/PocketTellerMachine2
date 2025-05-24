import os
import json
import time
from datetime import datetime
from cole_code_writer import cole_write_code

TRADE_LOG_FILE = "data/trades_cleaned.json"
REVIEW_FILE = "data/trade_review_report.json"
BRAIN_LOG_FILE = "data/cole_brain_log.json"
CODE_TRIGGER_LOG_FILE = "data/code_trigger_log.json"
LOOP_SECONDS = 600  # Every 10 minutes

def log_trigger(reason, filename):
    logs = []
    if os.path.exists(CODE_TRIGGER_LOG_FILE):
        try:
            with open(CODE_TRIGGER_LOG_FILE, "r") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []
    logs.append({
        "reason": reason,
        "filename": filename,
        "timestamp": datetime.now().isoformat()
    })
    with open(CODE_TRIGGER_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

def detect_triggers():
    reasons = []
    try:
        # Check trade reviews for bad grades
        if os.path.exists(REVIEW_FILE):
            with open(REVIEW_FILE, "r") as f:
                reviews = json.load(f)
            for review in reviews.get("reviews", []):
                if review.get("grade", "B") in ["D", "F"]:
                    reasons.append(f"Bad grade detected on {review.get('symbol', '')}")

        # Check recent trade results for losses
        if os.path.exists(TRADE_LOG_FILE):
            with open(TRADE_LOG_FILE, "r") as f:
                trades = json.load(f)
            for trade in trades[-50:]:  # Check last 50 trades
                if float(trade.get("result", 0)) < 0:
                    reasons.append(f"Recent loss on {trade.get('symbol', '')}")

        # Check brain logs for repeated errors
        if os.path.exists(BRAIN_LOG_FILE):
            with open(BRAIN_LOG_FILE, "r") as f:
                logs = json.load(f)
            errors = [log for log in logs[-100:] if "[ERROR]" in log.get("message", "")]
            if len(errors) > 5:
                reasons.append("Multiple brain errors detected")

    except Exception as e:
        print(f"[TRIGGER DETECTOR ERROR]: {e}")

    return reasons

def trigger_daemon_loop():
    print("[SMART TRIGGER DAEMON]: Running...")
    while True:
        reasons_detected = detect_triggers()
        if reasons_detected:
            for reason in set(reasons_detected):
                filename = cole_write_code(f"Triggered_Strategy_{datetime.now().strftime('%Y%m%d%H%M%S')}", f"Triggered because: {reason}")
                log_trigger(reason, filename)
                print(f"[SMART TRIGGER]: {reason} → {filename}")
        else:
            print("[SMART TRIGGER]: No triggers found. Sleeping...")
        time.sleep(LOOP_SECONDS)

if __name__ == "__main__":
    trigger_daemon_loop()