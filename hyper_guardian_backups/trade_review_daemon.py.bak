import os
import time
import json
from datetime import datetime
import pytz

CENTRAL_TZ = pytz.timezone("US/Central")

def get_local_time():
    return datetime.now(CENTRAL_TZ)

TRADES_FILE = "data/trades_cleaned.json"
REVIEW_FILE = "data/trade_review_report.json"
LOG_FILE = "data/cole_trade_review_log.json"
INTERVAL_SECONDS = 120  # How often to review

def generate_trade_review():
    if not os.path.exists(TRADES_FILE):
        log_event(f"[WARNING]: {TRADES_FILE} not found.")
        return

    with open(TRADES_FILE, "r") as f:
        try:
            trades = json.load(f)
        except json.JSONDecodeError:
            log_event("[ERROR]: Invalid trades JSON.")
            return

    reviews = []
    for trade in trades:
        review = review_trade(trade)
        reviews.append(review)

    with open(REVIEW_FILE, "w") as f:
        json.dump(reviews, f, indent=2)

    log_event(f"[REVIEW]: Reviewed {len(reviews)} trades.")

def review_trade(trade):
    result = trade.get("result", 0)
    grade = calculate_grade(result)
    review = {
        "id": trade.get("id", ""),
        "symbol": trade.get("symbol", ""),
        "strategy": trade.get("strategy", ""),
        "result": result,
        "grade": grade,
        "timestamp": trade.get("timestamp", ""),
        "reviewed_at": datetime.now().isoformat()
    }
    return review

def calculate_grade(result):
    if result >= 10:
        return "A"
    elif result >= 0:
        return "B"
    elif result > -10:
        return "C"
    else:
        return "D"

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

def trade_review_daemon_loop():
    print("[TRADE REVIEW DAEMON]: Trade Review Generator started...")
    while True:
        try:
            generate_trade_review()
        except Exception as e:
            log_event(f"[ERROR]: {e}")
        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    # Real Daemon Loop
    trade_review_daemon_loop()

    # Simulated fallback loop (uncomment if you want to run in test mode)
    # while True:
    #     print("[Daemon]: Trade Review Generator running... (simulated)")
    #     # Evaluate and generate trade reviews
    #     time.sleep(90)