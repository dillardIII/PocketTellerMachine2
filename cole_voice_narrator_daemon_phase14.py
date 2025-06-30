from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_voice_narrator_daemon_phase14.py

import os
import json
import time
from datetime import datetime
from cole_persona_voice_player import play_voice_line

# === Configurations ===
TRADE_REVIEW_FILE = "data/trade_review_report.json"
VOICE_LOG_FILE = "data/voice_narrator_log.json"
CHECK_INTERVAL = 300  # 5 minutes

# === Ensure data folder ===
os.makedirs("data", exist_ok=True)

# === Load recent trades ===
def load_recent_trades():
    if os.path.exists(TRADE_REVIEW_FILE):
        try:
            with open(TRADE_REVIEW_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

# === Narrate trades ===
def narrate_recent_trades():
    trades = load_recent_trades()
    if not trades:
        return

    for trade in trades[-5:]:
        persona = trade.get("executed_by", "DefaultPersona")
        result = trade.get("result", "Unknown result")
        message = f"{persona} reports the trade result: {result}"
        play_voice_line(persona, message)
        log_event(f"[VOICE NARRATOR]: {message}")

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(VOICE_LOG_FILE):
        try:
            with open(VOICE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def voice_narrator_loop():
    print("[VOICE NARRATOR DAEMON]: Running...")
    while True:
        try:
            narrate_recent_trades()
        except Exception as e:
            log_event(f"[VOICE NARRATOR ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    voice_narrator_loop()