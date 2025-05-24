import os
import json
from datetime import datetime
from cole_trade_decision_engine import evaluate_trade_decision
from cole_broker_interface import execute_trade_order
from assistants.malik import malik_report

WATCHLIST_FILE = "data/cole_watchlist.json"
SENTIMENT_FILE = "data/congress_sentiment_overlay.json"
TRADE_LOG_FILE = "data/sentiment_trade_trigger_log.json"

# === Logging Helper ===
def log_sentiment_trade(event):
    logs = []
    if os.path.exists(TRADE_LOG_FILE):
        try:
            with open(TRADE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append(event)

    with open(TRADE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

    print(f"[Sentiment Trigger] {event['action'].upper()} {event['ticker']} | Reason: {event['reason']} | Result: {event['order_result']['status']}")

# === Load Watchlist ===
def load_watchlist():
    if os.path.exists(WATCHLIST_FILE):
        try:
            with open(WATCHLIST_FILE, "r") as f:
                return json.load(f)
        except:
            print("[Sentiment Trigger] Failed to load watchlist.")
    return []

# === Load Sentiment Overlay ===
def load_sentiment_overlay():
    if os.path.exists(SENTIMENT_FILE):
        try:
            with open(SENTIMENT_FILE, "r") as f:
                return json.load(f)
        except:
            print("[Sentiment Trigger] Failed to load sentiment overlay.")
    return {}

# === Run Sentiment-Weighted Trade Trigger ===
def run_sentiment_weighted_trade_trigger():
    print("[Sentiment Trigger] Running Sentiment-Weighted Trade Trigger...")

    watchlist = load_watchlist()
    sentiment_data = load_sentiment_overlay()

    if not watchlist:
        print("[Sentiment Trigger] Watchlist is empty.")
        return

    if not sentiment_data:
        print("[Sentiment Trigger] Sentiment data unavailable.")
        return

    for ticker in watchlist:
        decision = evaluate_trade_decision(ticker)

        # Apply sentiment multiplier
        sentiment_score = sentiment_data.get(ticker.upper(), {}).get("score", 0)
        adjusted_confidence = decision.get("confidence", 0) + (sentiment_score * 0.5)

        if adjusted_confidence >= 0.7:
            action = decision.get("recommended_action", "buy")
            reason = f"Decision confidence: {decision.get('confidence')} + Sentiment boost: {sentiment_score}"

            result = execute_trade_order(ticker, action, confidence=adjusted_confidence)

            event = {
                "timestamp": datetime.now().isoformat(),
                "ticker": ticker,
                "action": action,
                "reason": reason,
                "original_confidence": decision.get("confidence"),
                "sentiment_adjustment": sentiment_score,
                "final_confidence": adjusted_confidence,
                "order_result": result
            }

            log_sentiment_trade(event)
            malik_report(f"[Trade Trigger] Executed {action.upper()} on {ticker} (Final Confidence: {adjusted_confidence:.2f})")

        else:
            print(f"[Sentiment Trigger] Skipping {ticker} (Confidence: {adjusted_confidence:.2f})")

    print("[Sentiment Trigger] Sentiment-weighted trade trigger completed.")

# === CLI Trigger ===
if __name__ == "__main__":
    run_sentiment_weighted_trade_trigger()