# cole_phase14_emotional_spectrum_trainer.py

import json
import os

EMOTIONAL_SPECTRUM_FILE = "data/emotional_spectrum_state.json"

# === Default Emotional Spectrum ===
DEFAULT_SPECTRUM = {
    "happy": 50,
    "sad": 50,
    "angry": 50,
    "motivational": 50,
    "sarcastic": 50,
    "neutral": 50,
    "excited": 50,
    "calm": 50
}

# === Load or Initialize Emotional Spectrum ===
def load_emotional_spectrum():
    if not os.path.exists(EMOTIONAL_SPECTRUM_FILE):
        save_emotional_spectrum(DEFAULT_SPECTRUM)
    with open(EMOTIONAL_SPECTRUM_FILE, "r") as f:
        return json.load(f)

# === Save Emotional Spectrum ===
def save_emotional_spectrum(spectrum):
    with open(EMOTIONAL_SPECTRUM_FILE, "w") as f:
        json.dump(spectrum, f, indent=2)

# === Adjust Emotion Level ===
def adjust_emotion(emotion, delta):
    spectrum = load_emotional_spectrum()
    if emotion in spectrum:
        spectrum[emotion] = max(0, min(100, spectrum[emotion] + delta))
        save_emotional_spectrum(spectrum)
        return f"Adjusted {emotion} level to {spectrum[emotion]}."
    else:
        return f"Emotion {emotion} not found."

# === Reset Emotional Spectrum ===
def reset_emotional_spectrum():
    save_emotional_spectrum(DEFAULT_SPECTRUM)
    return "Emotional spectrum reset to default."

# === Example Usage ===
if __name__ == "__main__":
    print(load_emotional_spectrum())
    print(adjust_emotion("happy", 10))
    print(adjust_emotion("angry", -20))
    print(reset_emotional_spectrum())