from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_self_review_trainer.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
TRADE_REVIEW_FILE = "data/trade_review_report.json"
PERSONA_SELF_REVIEW_LOG = "data/persona_self_review_log.json"
CHECK_INTERVAL = 1800  # Every 30 minutes

# === Ensure data directory ===
os.makedirs("data", exist_ok=True)

# === Logging ===
def log_self_review(message):
    logs = []
    if os.path.exists(PERSONA_SELF_REVIEW_LOG):
        try:
            with open(PERSONA_SELF_REVIEW_LOG, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(PERSONA_SELF_REVIEW_LOG, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load recent trades ===
def load_recent_trades():
    if os.path.exists(TRADE_REVIEW_FILE):
        try:
            with open(TRADE_REVIEW_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

# === Persona Self-Review Logic ===
def persona_self_review(trades):
    reviews = {}
    for trade in trades[-20:]:
        persona = trade.get("executed_by", "Unknown")
        result = trade.get("result", "").lower()
        if persona not in reviews:
            reviews[persona] = {"wins": 0, "losses": 0, "total": 0}

        reviews[persona]["total"] += 1
        if "win" in result:
            reviews[persona]["wins"] += 1
        elif "loss" in result or "bad" in result:
            reviews[persona]["losses"] += 1

    # Logging each persona self-review
    for persona, stats in reviews.items():
        win_rate = (stats["wins"] / stats["total"]) * 100 if stats["total"] > 0 else 0:
        log_self_review(f"[SELF REVIEW]: {persona} - Total Trades: {stats['total']} | Wins: {stats['wins']} | Losses: {stats['losses']} | Win Rate: {win_rate:.2f}%")

# === Main Daemon Loop ===
def persona_self_review_loop():
    print("[PERSONA SELF-REVIEW TRAINER]: Running...")
    while True:
        try:
            trades = load_recent_trades()
            if trades:
                persona_self_review(trades)
            else:
                log_self_review("[SELF REVIEW]: No recent trades found.")
        except Exception as e:
            log_self_review(f"[SELF REVIEW ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_self_review_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():