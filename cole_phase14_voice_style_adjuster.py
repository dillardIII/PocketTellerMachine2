from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase14_voice_style_adjuster.py

import os
from cole_phase14_emotion_response_mapper import generate_emotion_response_prefix

# === Voice Configurations ===
DEFAULT_VOICE_STYLE = "Neutral"
VOICE_STYLE_MAP = {
    "happy": "Upbeat",
    "sad": "Soft",
    "angry": "Strong",
    "motivational": "Commanding",
    "sarcastic": "Snarky",
    "neutral": "Balanced",
    "excited": "High Energy",
    "calm": "Relaxed"
}

# === Adjust Voice Style ===
def adjust_voice_style_based_on_emotion():
    emotion_prefix = generate_emotion_response_prefix()
    # Extract dominant emotion
    for emotion, style in VOICE_STYLE_MAP.items():
        if emotion in emotion_prefix.lower():
            return style
    return DEFAULT_VOICE_STYLE

# === Simulate Voice Style Command (For voice engine or narrator daemon) ===
def create_voice_command(text):
    voice_style = adjust_voice_style_based_on_emotion()
    # This is where you integrate with the real TTS engine
    command = f"[Voice Style: {voice_style}] {text}"
    return command

# === Example Use ===
if __name__ == "__main__":
    sample_text = "Here is your portfolio performance update."
    print("Simulated Voice Command:", create_voice_command(sample_text))

def log_event():ef drop_files_to_bridge():