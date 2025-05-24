import random
from datetime import datetime
import pytz

CENTRAL_TZ = pytz.timezone("US/Central")

def get_local_time():
    return datetime.now(CENTRAL_TZ)

TRADES_FILE = "data/trades.json"

# === Paper Trade Executor ===
def execute_paper_trade(ticker, strategy):
    # Simulate trade outcome for now (real logic can use price comparison later)
    result = random.choice(["win", "loss"])
    profit = round(random.uniform(10, 100), 2) if result == "win" else round(random.uniform(-100, -10), 2)

    trade = {
        "timestamp": datetime.now().isoformat(),
        "ticker": ticker,
        "strategy": strategy,
        "result": result,
        "profit": profit
    }

    # Save to trades.json
    try:
        with open(TRADES_FILE, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(trade)

    with open(TRADES_FILE, "w") as f:
        json.dump(data, f, indent=2)

    return trade