import os
import json
import requests
from datetime import datetime
from assistants.malik import malik_report

SENTIMENT_LOG_FILE = "data/congress_sentiment_log.json"
SENTIMENT_OVERLAY_FILE = "data/congress_sentiment_overlay.json"
QUIVER_API_KEY = os.getenv("QUIVER_API_KEY")

# === Logging Helper ===
def log_sentiment_event(message):
    logs = []
    if os.path.exists(SENTIMENT_LOG_FILE):
        try:
            with open(SENTIMENT_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(SENTIMENT_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Fetch Congress Sentiment ===
def fetch_congress_sentiment():
    url = f"https://api.quiverquant.com/beta/live/congresstrading"
    headers = {"Authorization": f"Bearer {QUIVER_API_KEY}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        sentiment_summary = {}
        for trade in data:
            ticker = trade.get('Ticker')
            sentiment_summary.setdefault(ticker, {"buy": 0, "sell": 0})
            if trade.get('Transaction') == "Purchase":
                sentiment_summary[ticker]["buy"] += 1
            elif trade.get('Transaction') == "Sale":
                sentiment_summary[ticker]["sell"] += 1

        with open(SENTIMENT_OVERLAY_FILE, "w") as f:
            json.dump(sentiment_summary, f, indent=2)

        log_sentiment_event(f"Updated sentiment overlay with {len(sentiment_summary)} tickers.")
        malik_report(f"[Sentiment Overlay] Updated with {len(sentiment_summary)} tickers.")

    except Exception as e:
        log_sentiment_event(f"[ERROR]: {e}")
        malik_report(f"[Sentiment Overlay Error] {e}")

# === CLI Trigger ===
if __name__ == "__main__":
    fetch_congress_sentiment()