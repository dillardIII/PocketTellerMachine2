# === FILE: cole_trade_decision_engine.py ===

import os
import json
import random
from datetime import datetime
from price_data import get_current_rsi
from cole_congress_sentiment_overlay import fetch_congress_sentiment
from cole_paper_broker import paper_execute_trade_order as execute_trade_order  # <-- Replaced live broker
from assistants.malik import malik_report

# === File Paths ===
WATCHLIST_FILE = "data/cole_watchlist.json"
SENTIMENT_FILE = "data/congress_sentiment_overlay.json"
TRADE_DECISION_LOG = "data/cole_trade_decision_log.json"
TRADE_GRADES_FILE = "data/strategy_grades.json"

# === Load Watchlist ===
def load_watchlist():
    if os.path.exists(WATCHLIST_FILE):
        try:
            with open(WATCHLIST_FILE, "r") as f:
                return json.load(f)
        except:
            print("[Decision Engine] Failed to load watchlist.")
    return []

# === Load Sentiment Overlay ===
def load_sentiment_overlay():
    if os.path.exists(SENTIMENT_FILE):
        try:
            with open(SENTIMENT_FILE, "r") as f:
                return json.load(f)
        except:
            print("[Decision Engine] Failed to load sentiment overlay.")
    return {}

# === Logging Helper ===
def log_trade_decision(entry):
    logs = []
    if os.path.exists(TRADE_DECISION_LOG):
        try:
            with open(TRADE_DECISION_LOG, "r") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append(entry)
    with open(TRADE_DECISION_LOG, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Evaluate Trade Decision ===
def evaluate_trade_decision(ticker, sentiment_data):
    print(f"[Trade Decision Engine] Evaluating {ticker}...")

    # Technical Indicator: RSI
    rsi = get_current_rsi(ticker)

    # Base confidence logic from RSI
    if rsi < 30:
        base_confidence = 0.7  # Oversold, consider buying
    elif rsi > 70:
        base_confidence = 0.3  # Overbought, cautious
    else:
        base_confidence = 0.5  # Neutral

    # Sentiment adjustment
    sentiment_score = sentiment_data.get(ticker.upper(), {}).get("score", 0)
    adjusted_confidence = base_confidence + (sentiment_score * 0.3)
    adjusted_confidence = max(0, min(1, adjusted_confidence))

    # Decision
    action = "buy" if adjusted_confidence >= 0.6 else "hold" if adjusted_confidence >= 0.4 else "avoid"

    decision = {
        "timestamp": datetime.now().isoformat(),
        "ticker": ticker,
        "rsi": rsi,
        "base_confidence": base_confidence,
        "sentiment_score": sentiment_score,
        "final_confidence": adjusted_confidence,
        "action": action
    }

    return decision

# === Run Decision Engine ===
def run_trade_decision_engine():
    print("[Decision Engine] Running full trade decision process...")

    watchlist = load_watchlist()
    sentiment_data = load_sentiment_overlay()

    if not watchlist:
        print("[Decision Engine] Watchlist is empty.")
        return

    for ticker in watchlist:
        decision = evaluate_trade_decision(ticker, sentiment_data)

        # Log the decision
        log_trade_decision(decision)

        # Execute trade if actionable
        if decision["action"] == "buy":
            result = execute_trade_order(ticker, "buy", confidence=decision["final_confidence"])
            malik_report(f"[Trade Executed] {ticker} | Confidence: {decision['final_confidence']:.2f} | Result: {result.get('status', 'unknown')}")
        else:
            print(f"[Decision Engine] No actionable trade for {ticker} (Action: {decision['action']})")

    print("[Decision Engine] Processing complete.")

# === Load Strategy Grades ===
def load_strategy_grades():
    if os.path.exists(TRADE_GRADES_FILE):
        with open(TRADE_GRADES_FILE, "r") as f:
            return json.load(f)
    return {}

# === Choose Top Strategies ===
def choose_top_strategies(strategies, top_n=3):
    grades = load_strategy_grades()
    graded = []

    for strategy in strategies:
        grade = grades.get(strategy, "C")
        score = grade_to_score(grade)
        graded.append((strategy, score))

    # Sort by score (higher is better)
    graded.sort(key=lambda x: x[1], reverse=True)

    return [s[0] for s in graded[:top_n]]

# === Grade-to-Score Conversion ===
def grade_to_score(grade):
    scale = {"A": 5, "B": 4, "C": 3, "D": 2, "F": 1}
    return scale.get(grade.upper(), 3)

# === CLI Trigger ===
if __name__ == "__main__":
    run_trade_decision_engine()