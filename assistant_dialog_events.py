from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: assistant_dialog_events.py ===
"""
Assistant Dialog Events:
Triggers back-and-forth conversations between PTM personas based on shared context.
Supports trade analysis, collaborative decision-making, and morale updates.
"""

from persona_responder import generate_response
from cole_brain import get_last, log_state

DIALOG_PAIRS = [
    ("Mentor", "MoCash"),
    ("Strategist", "Mentor"),
    ("ChillTrader", "DrillInstructor"),
    ("MoCash", "Strategist")
]

def initiate_dialog_event(trigger="trade_complete"):
    """
    Fires a dialog event between two assistants based on shared state or event trigger.
    """
    for speaker, responder in DIALOG_PAIRS:
        print(f"\n🗨️ Dialog Triggered: {speaker} → {responder}")
        
        msg = generate_response(speaker)
        log_state(f"dialog_from_{speaker}", msg)
        
        reply = generate_response(responder)
        log_state(f"dialog_from_{responder}", reply)

        print(f"[🧠] {speaker} said: {msg}")
        print(f"[💬] {responder} replied: {reply}")

# === Optional manual test
if __name__ == "__main__":
    initiate_dialog_event()