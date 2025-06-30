from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Autonomous Commander:
Final ignition layer that glues together dialog events, emotion inference,
reaction logging, and assistant communication triggers.

This script enables fully autonomous assistant reactions based on system state.
"""

from dialog_event_trigger import trigger_dialog_event, run_dialog_event
from cole_brain import get_last, log_state
from emotion_inference_engine import infer_emotion_from_text
from reaction_tracker import log_reaction
import time

# === CONFIG ===
DEFAULT_PERSONAS = ["MoCash", "Mentor", "Strategist"]
TRIGGER_CONTEXT = "trade_complete"
LOOP_INTERVAL = 15  # seconds – can be lowered or tied to trade events

def autonomy_loop():
    """
    Master loop that periodically checks last result, triggers reactions,
    and initiates assistant dialog with emotional tracking.
    """
    print("[🧠 Autonomy Online] Starting autonomous commander loop...")

    last_emotion = get_last("last_trade_result") or "neutral"
    participants = DEFAULT_PERSONAS

    for i in range(len(participants)):
        initiator = participants[i]
        receiver = participants[(i + 1) % len(participants)]

        convo = run_dialog_event(initiator, receiver)
        emotion = convo["emotion"]

        log_reaction(initiator, emotion, TRIGGER_CONTEXT)
        log_reaction(receiver, infer_emotion_from_text(convo["receiver_msg"]), TRIGGER_CONTEXT)

        log_state("last_trade_result", emotion)

        print(f"[🔁 Loop Cycle] {initiator} ➜ {receiver} | Emotion: {emotion}")
        print("—" * 40)

def fire_once():
    """
    Runs a single cycle of reactions and dialog.
    """
    print("[⚡ Trigger] Firing single autonomous sequence...")
    autonomy_loop()

# === Optional full loop mode
if __name__ == "__main__":
    while True:
        try:
            autonomy_loop()
            time.sleep(LOOP_INTERVAL)
        except KeyboardInterrupt:
            print("[❌] Autonomy halted manually.")
            break
        except Exception as e:
            print(f"[⚠️ ERROR] {e}")