from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Dialog Event Trigger:
Kicks off voice interactions, reactions, and responses between PTM assistants.
Can be used when trades finish, commands are given, or system events occur.
Also coordinates assistant-to-assistant reactions.
"""

from persona_responder import generate_response
from cole_brain import get_last, log_state
from emotion_inference_engine import infer_emotion_from_text

def trigger_dialog_event(event_type="trade_complete", participants=None):
    """
    Handles assistant dialogue during a key event (e.g., trade outcome, milestone).
    Can trigger single or multi-persona interactions.
    """
    if participants is None:
        participants = ["MoCash"]

    print(f"[🎤 Dialog Event] Triggered: {event_type} with {participants}")

    for persona in participants:
        generate_response(persona)
        log_state(f"{persona}_last_event", event_type)

def run_dialog_event(initiator, receiver):
    """
    Triggers a short dialog event between two assistants.
    """
    print(f"[🔁 Dialog Event] {initiator} ➜ {receiver}")
    
    # Step 1: Initiator speaks
    initiator_msg = generate_response(initiator)
    
    # Step 2: Infer emotion from initiator’s message
    emotion = infer_emotion_from_text(initiator_msg)
    
    # Step 3: Log emotional reaction state
    print(f"[🔍 Emotion Inferred] {initiator}: {emotion}")
    
    # Step 4: Trigger receiver’s reaction
    receiver_msg = generate_response(receiver)
    
    return {
        "initiator": initiator,
        "initiator_msg": initiator_msg,
        "emotion": emotion,
        "receiver": receiver,
        "receiver_msg": receiver_msg
    }

# === Example trigger for debugging ===
if __name__ == "__main__":
    trigger_dialog_event("trade_complete", ["MoCash", "Mentor", "Strategist"])
    convo = run_dialog_event("MoCash", "Mentor")
    for k, v in convo.items():
        print(f"{k}: {v}")