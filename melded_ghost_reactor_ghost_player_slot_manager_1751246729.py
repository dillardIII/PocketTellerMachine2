from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Ghost Reactor:
Listens for memory, trade, or event triggers and dispatches appropriate persona reactions.
Part of PTM's intelligent response core.
"""

import random
from persona_recap_speaker import speak_trade_recap
from cole_logger import log_event
from cole_brain import get_latest_memory

# Define mood triggers and their associated actions
MOOD_REACTION_MAP = {
    "win": ["celebrate_win", "log_victory_memory", "boost_confidence"],
    "loss": ["offer_support", "analyze_loss", "adjust_strategy"],
    "neutral": ["reflect", "maintain_focus"]
}

# Reaction chain functions
def celebrate_win(trade):
    log_event("Ghost Reactor", f"🎉 Celebrating win on {trade['symbol']}!", "success")
    speak_trade_recap(trade)

def offer_support(trade):
    log_event("Ghost Reactor", f"📉 Loss detected on {trade['symbol']}. Triggering support protocol.", "warning")
    # Could trigger a persona like Mentor or ChillTrader to respond
    speak_trade_recap(trade)

def reflect(trade):
    log_event("Ghost Reactor", f"🧠 Reflecting on neutral trade outcome for {trade['symbol']}.", "info")
    speak_trade_recap(trade)

# Add future hooks here
def log_victory_memory(trade):
    # Placeholder: Could add XP boost, badge trigger, or encouragement quote
    log_event("Memory Update", f"🏆 Trade success on {trade['symbol']} stored for performance tracking.", "info")


# === MELD BREAK ===
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def deploy_ghost_players():
    print("[GhostSlotManager] Deploying Ghost Players...")
    config = load_config()
    count = config.get("ghost_players", 1)

    for i in range(1, count + 1):
        print(f"[GhostPlayer {i}] Spawned and synced with Ghost Gamer net.")

if __name__ == "__main__":
    deploy_ghost_players()