from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import uuid
from datetime import datetime

GHOSTBOT_LOG = "logs/data/ghostbot.json"

def load_brain_log():
    if not os.path.exists(GHOSTBOT_LOG):
        return []
    with open(GHOSTBOT_LOG, "r") as f:
        return json.load(f)

def save_brain_log(log):
    with open(GHOSTBOT_LOG, "w") as f:
        json.dump(log, f, indent=2)

def calculate_streak(log, win):
    streak = 0
    for entry in reversed(log[-10:]):
        if entry.get("win") == win:
            streak += 1
        else:
            break
    return streak + 1

def log_brain_entry(trade_data, insight="", win=False):
    log = load_brain_log()

    trade_id = trade_data.get("id", str(uuid.uuid4())[:8])
    score = 100 if win else 40
    streak = calculate_streak(log, win)
    suggestion = "Great job, repeat that setup!" if win else "Review entry timing or volume."
    xp = score * 1.25
    level = int(xp / 50) + 1
    mood = "hype" if win and streak >= 3 else "frustrated" if not win and streak >= 2 else "neutral"

    new_entry = {
        "id": trade_id,
        "symbol": trade_data.get("symbol"),
        "strategy": trade_data.get("strategy"),
        "buy_price": trade_data.get("buy_price"),
        "sell_price": trade_data.get("sell_price", None),
        "quantity": trade_data.get("quantity", None),
        "result": trade_data.get("result", "N/A"),
        "status": trade_data.get("status", "closed"),
        "notes": trade_data.get("notes", ""),
        "score": score,
        "xp": xp,
        "level": level,
        "streak": streak,
        "insight": insight,
        "assistant_feedback": suggestion,
        "win": win,
        "mood": mood,
        "timestamp": datetime.utcnow().isoformat()
    }

    log.append(new_entry)
    save_brain_log(log)