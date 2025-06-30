from ghost_env import INFURA_KEY, VAULT_ADDRESS
import json
import os
from datetime import datetime
import pytz

CENTRAL_TZ = pytz.timezone("US/Central")

def get_local_time():
    return datetime.now(CENTRAL_TZ)
from cole_memory_brain import log_memory_event
from assistants.malik import malik_report
from recap_voice import speak_text  # <-- Voice playback added

TRADE_LOG_FILE = "logs/trade_log.json"
DAILY_RECAP_FILE = "data/daily_recap_logs.json"

# === Load all trades (optionally filter by today) ===
def load_trades():
    if not os.path.exists(TRADE_LOG_FILE):
        return []
    with open(TRADE_LOG_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def analyze_trades(trades):
    today = datetime.now().date()
    wins = losses = 0
    strategies = {}

    for trade in trades:
        ts = trade.get("logged_at") or trade.get("timestamp")
        if not ts:
            continue

        date = datetime.fromisoformat(ts).date()
        if date != today:
            continue

        strat = trade.get("strategy", "unknown")
        result = trade.get("result")

        if strat not in strategies:
            strategies[strat] = {"wins": 0, "losses": 0}

        if result == "win":
            wins += 1
            strategies[strat]["wins"] += 1
        elif result == "loss":
            losses += 1
            strategies[strat]["losses"] += 1

    return wins, losses, strategies

def write_recap(wins, losses, strat_stats):
    timestamp = datetime.now().isoformat()
    recap = {
        "timestamp": timestamp,
        "wins": wins,
        "losses": losses,
        "strategies": strat_stats,
        "summary": f"PTM logged {wins} wins and {losses} losses today."
    }

    # Save to recap file
    if os.path.exists(DAILY_RECAP_FILE):
        with open(DAILY_RECAP_FILE, "r") as f:
            try:
                data = json.load(f)
            except:
                data = []
    else:
        data = []

    data.append(recap)
    with open(DAILY_RECAP_FILE, "w") as f:
        json.dump(data, f, indent=2)

    # Save to memory log
    log_memory_event("daily_recap", recap)
    malik_report(f"[Daily Recap] {recap['summary']}")

    # === Voice Playback ===
    try:
        summary_line = recap["summary"]
        speak_text(summary_line, speaker="Malik")  # You can switch to "Mo Cash" or use dynamic speaker
    except Exception as e:
        print(f"[Voice Recap Error] {e}")

def run_daily_recap():
    trades = load_trades()
    wins, losses, strat_stats = analyze_trades(trades)
    write_recap(wins, losses, strat_stats)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():