from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import requests
from datetime import datetime

CONGRESS_LOG_FILE = "data/congress_trade_log.json"
PTM_TASK_QUEUE = "data/cole_task_queue.json"

# === QuiverQuant API Key ===
QUIVER_API_KEY = os.getenv("QUIVER_API_KEY")

if not QUIVER_API_KEY:
    raise ValueError("Missing QUIVER_API_KEY in environment variables.")

HEADERS = {"Authorization": f"Bearer {QUIVER_API_KEY}"}

# === API Endpoints ===
SENATE_ENDPOINT = "https://api.quiverquant.com/beta/live/senatetrading"
HOUSE_ENDPOINT = "https://api.quiverquant.com/beta/live/housetrading"

# === Logging Helper ===
def log_congress_event(entry):
    logs = []
    if os.path.exists(CONGRESS_LOG_FILE):
        with open(CONGRESS_LOG_FILE, "r") as f:
            logs = json.load(f)
    logs.append(entry)
    with open(CONGRESS_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Add to PTM Task Queue ===
def add_task_to_queue(task_text):
    tasks = []
    if os.path.exists(PTM_TASK_QUEUE):
        with open(PTM_TASK_QUEUE, "r") as f:
            tasks = json.load(f)

    tasks.append({
        "timestamp": datetime.now().isoformat(),
        "task": task_text,
        "type": "congress_tracker",
        "status": "pending"
    })

    with open(PTM_TASK_QUEUE, "w") as f:
        json.dump(tasks, f, indent=2)

# === Fetch Congress Trades ===
def fetch_congress_trades(endpoint):
    try:
        response = requests.get(endpoint, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        log_congress_event({"timestamp": datetime.now().isoformat(), "error": str(e)})
        return []

# === Analyze & Flag Trades ===
def analyze_congress_trades(trades, chamber):
    flagged = []
    for trade in trades:
        ticker = trade.get("Ticker", "")
        rep = trade.get("Representative", "")
        transaction_type = trade.get("Transaction", "")
        amount = trade.get("Range", "")

        # Example Filter: High-value buys
        if "Purchase" in transaction_type and ">$100K" in amount:
            task_text = f"Analyze {chamber} trade: {rep} purchased {ticker} ({amount}). Consider adding to watchlist."
            add_task_to_queue(task_text)
            flagged.append(task_text)

    log_congress_event({
        "timestamp": datetime.now().isoformat(),
        "chamber": chamber,
        "flagged_trades": flagged
    })

# === Main Tracker Function ===
def run_congress_ai_tracker():
    print("[Congress AI Tracker] Fetching and analyzing Senate trades...")
    senate_trades = fetch_congress_trades(SENATE_ENDPOINT)
    analyze_congress_trades(senate_trades, "Senate")

    print("[Congress AI Tracker] Fetching and analyzing House trades...")
    house_trades = fetch_congress_trades(HOUSE_ENDPOINT)
    analyze_congress_trades(house_trades, "House")

    print("[Congress AI Tracker] Analysis complete.")

# === CLI Trigger ===
if __name__ == "__main__":
    run_congress_ai_tracker()

def log_event():ef drop_files_to_bridge():