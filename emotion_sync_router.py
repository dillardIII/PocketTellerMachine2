from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Emotion Sync Router:
Connects inferred emotions to other subsystems like memory, reaction logs, and assistant responses.
Used to ensure assistant logic reflects emotional state across modules.
"""

from emotion_inference_engine import infer_emotion_from_text
from reaction_tracker import log_reaction
from cole_brain import log_state

def sync_emotion(persona, message, context="trade"):
    """
    Routes emotion analysis to logs, memory, and mood tracking.
    """
    emotion = infer_emotion_from_text(message)
    log_reaction(persona, emotion, context)
    log_state(f"{persona}_mood", emotion)

    print(f"[🧠 Emotion Sync] {persona}: {emotion} | Context: {context}")
    return emotion

# === Manual test
if __name__ == "__main__":
    test_message = "That trade was on fire! Huge gain today."
    sync_emotion("MoCash", test_message, "trade_complete")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():