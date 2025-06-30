# cole_phase14_emotion_response_mapper.py

import json
import os

EMOTIONAL_SPECTRUM_FILE = "data/emotional_spectrum_state.json"

# === Emotion Response Templates ===
EMOTION_TEMPLATES = {
    "happy": "with a cheerful tone",
    "sad": "in a somber voice",
    "angry": "with an assertive tone",
    "motivational": "with a powerful motivational style",
    "sarcastic": "with a sarcastic undertone",
    "neutral": "with a calm, balanced voice",
    "excited": "with high energy and excitement",
    "calm": "with a soothing, calm voice"
}

# === Load Emotional Spectrum ===
def load_emotional_spectrum():
    if not os.path.exists(EMOTIONAL_SPECTRUM_FILE):
        return {}
    with open(EMOTIONAL_SPECTRUM_FILE, "r") as f:
        return json.load(f)

# === Map Emotion to Dominant Style ===
def get_dominant_emotion():
    spectrum = load_emotional_spectrum()
    if not spectrum:
        return "neutral"
    # Get the emotion with the highest score
    dominant = max(spectrum, key=spectrum.get)
    return dominant

# === Get Emotion-based Response Template ===
def generate_emotion_response_prefix():
    dominant_emotion = get_dominant_emotion()
    return EMOTION_TEMPLATES.get(dominant_emotion, "with a neutral tone")

# === Example Use ===
if __name__ == "__main__":
    print("Dominant Emotion:", get_dominant_emotion())
    print("Use this tone:", generate_emotion_response_prefix())