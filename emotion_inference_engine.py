from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Emotion Inference Engine:
Analyzes text-based responses from assistants to infer emotional state.
Useful for cross-bot understanding, feedback loops, and reactive behavior.
"""

def infer_emotion_from_text(text):
    text = text.lower()
    
    if any(word in text for word in ["win", "profit", "success", "fire", "victory", "gain", "stack", "hustle"]):
        return "win"
    elif any(word in text for word in ["loss", "hurt", "sting", "ouch", "bad", "fail", "down"]):
        return "loss"
    elif any(word in text for word in ["neutral", "flat", "stable", "okay", "fine", "expected"]):
        return "neutral"
    elif any(word in text for word in ["angry", "slack", "discipline", "reps", "lock"]):
        return "discipline"
    else:
        return "unknown"

# === Debug mode
if __name__ == "__main__":
    test_msgs = [
        "Another win, we stacked that quick! Hustle mode on.",
        "Ouch. That loss stung more than usual.",
        "Stable trade. Right on track.",
        "Discipline, reps, and no slack—that’s how we win."
    ]
    for msg in test_msgs:
        print(f"Msg: {msg}\n➤ Emotion: {infer_emotion_from_text(msg)}\n")

def log_event():ef drop_files_to_bridge():