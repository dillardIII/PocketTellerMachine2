from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase14_avatar_mood_overlay.py

import os
from cole_phase14_emotion_response_mapper import generate_emotion_response_prefix

# === Avatar Mood Overlays Mapping ===
MOOD_OVERLAY_MAP = {
    "happy": "avatar_overlay_happy.png",
    "sad": "avatar_overlay_sad.png",
    "angry": "avatar_overlay_angry.png",
    "motivational": "avatar_overlay_motivational.png",
    "sarcastic": "avatar_overlay_sarcastic.png",
    "neutral": "avatar_overlay_neutral.png",
    "excited": "avatar_overlay_excited.png",
    "calm": "avatar_overlay_calm.png"
}

# === Determine Avatar Mood Overlay ===
def get_avatar_mood_overlay():
    emotion_prefix = generate_emotion_response_prefix()
    for emotion, overlay in MOOD_OVERLAY_MAP.items():
        if emotion in emotion_prefix.lower():
            return overlay
    return MOOD_OVERLAY_MAP.get("neutral")

# === Example Use for UI Avatar ===
def display_avatar_with_overlay(base_avatar="avatar_base.png"):
    overlay = get_avatar_mood_overlay()
    combined_display = f"Displaying: {base_avatar} with Overlay: {overlay}"
    return combined_display

# === Test Display Call ===
if __name__ == "__main__":
    print(display_avatar_with_overlay())

def log_event():ef drop_files_to_bridge():