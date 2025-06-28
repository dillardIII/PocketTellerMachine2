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

def analyze_loss(trade):
    log_event("Strategy Engine", f"🔍 Analyzing failed trade on {trade['symbol']}.", "danger")

def boost_confidence(trade):
    log_event("Persona Uplift", f"🔥 Encouragement mode activated after win on {trade['symbol']}.", "success")

def adjust_strategy(trade):
    log_event("Auto-Tune", f"🛠️ Strategy adjusted after loss on {trade['symbol']}.", "info")

# Main function to trigger reactions based on memory or trade result
def trigger_reaction(event_type="trade", trade=None, mood="neutral"):
    log_event("Ghost Reactor", f"⚡ Triggered by {event_type} with mood: {mood}", "info")

    if mood not in MOOD_REACTION_MAP:
        log_event("Ghost Reactor", f"❓ Unknown mood '{mood}'. Defaulting to neutral.", "warning")
        mood = "neutral"

    reaction_chain = MOOD_REACTION_MAP[mood]
    
    for reaction_name in reaction_chain:
        func = globals().get(reaction_name)
        if callable(func):
            func(trade)
        else:
            log_event("Ghost Reactor", f"⚠️ No function found for '{reaction_name}'", "error")

# For testing
if __name__ == "__main__":
    sample_trade = {
        "datetime": "2025-06-03 14:20",
        "persona": "MoCash",
        "action": "Buy Call",
        "symbol": "TSLA",
        "price": 270.55,
        "strategy": "Momentum Rider",
        "result": "win"
    }
    trigger_reaction(event_type="trade", trade=sample_trade, mood="win")