from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_congress_sentiment_overlay.py ===

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

# === Primary: Fetch from Quiver API ===
def fetch_congress_sentiment():
    url = "https://api.quiverquant.com/beta/live/congresstrading"
    headers = {"Authorization": f"Bearer {QUIVER_API_KEY}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        sentiment_summary = {}
        for trade in data:
            ticker = trade.get("Ticker")
            sentiment_summary.setdefault(ticker, {"buy": 0, "sell": 0})
            if trade.get("Transaction") == "Purchase":
                sentiment_summary[ticker]["buy"] += 1
            elif trade.get("Transaction") == "Sale":
                sentiment_summary[ticker]["sell"] += 1

        overlay = {
            "timestamp": datetime.now().isoformat(),
            "tickers": {
                ticker: {
                    "sentiment": (
                        "positive" if stats["buy"] > stats["sell"]:
                        else "negative" if stats["sell"] > stats["buy"]:
                        else "neutral"
                    ),
                    "score": round((stats["buy"] - stats["sell"]) / max(stats["buy"] + stats["sell"], 1), 2)
                }
                for ticker, stats in sentiment_summary.items()
            }
        }

        os.makedirs("data", exist_ok=True)
        with open(SENTIMENT_OVERLAY_FILE, "w") as f:
            json.dump(overlay, f, indent=2)

        log_sentiment_event(f"Updated sentiment overlay with {len(overlay['tickers'])} tickers.")
        malik_report(f"[Sentiment Overlay] Updated with {len(overlay['tickers'])} tickers.")
        return overlay

    except Exception as e:
        error_msg = f"[Sentiment Overlay Error] {e}"
        log_sentiment_event(error_msg)
        malik_report(error_msg)
        return fetch_dummy_sentiment()

# === Fallback Dummy Data ===
def fetch_dummy_sentiment():
    print("[Congress Sentiment] Using fallback dummy sentiment overlay...")

    dummy_sentiment = {
        "timestamp": datetime.now().isoformat(),
        "tickers": {
            "AAPL": {"sentiment": "positive", "score": 0.7},
            "TSLA": {"sentiment": "negative", "score": -0.6},
            "NVDA": {"sentiment": "positive", "score": 0.8},
            "MSFT": {"sentiment": "neutral", "score": 0.0},
        }
    }

    os.makedirs("data", exist_ok=True)
    with open(SENTIMENT_OVERLAY_FILE, "w") as f:
        json.dump(dummy_sentiment, f, indent=2)

    malik_report(f"[Sentiment Overlay] Dummy mode: {len(dummy_sentiment['tickers'])} tickers.")
    return dummy_sentiment

# === CLI Trigger ===
if __name__ == "__main__":
    fetch_congress_sentiment()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():