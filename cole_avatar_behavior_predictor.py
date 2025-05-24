# cole_avatar_behavior_predictor.py

import os
import json
from datetime import datetime

# === Configurations ===
AVATAR_STATE_FILE = "data/avatar_state.json"
BEHAVIOR_LOG_FILE = "data/avatar_behavior_prediction_log.json"
PREDICTED_BEHAVIOR_FILE = "data/predicted_avatar_behavior.json"

# === Ensure folders ===
os.makedirs("data", exist_ok=True)

# === Prediction Rules ===
BEHAVIOR_RULES = {
    "happy": "cheerful",
    "frustrated": "aggressive",
    "calm": "neutral",
    "sad": "passive"
}

# === Load Avatar State ===
def load_avatar_state():
    if os.path.exists(AVATAR_STATE_FILE):
        try:
            with open(AVATAR_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Predict Behavior ===
def predict_avatar_behavior():
    avatar_state = load_avatar_state()
    predictions = {}

    for persona, state in avatar_state.items():
        mood = state.get("mood", "calm")
        predicted_behavior = BEHAVIOR_RULES.get(mood, "neutral")

        predictions[persona] = {
            "current_mood": mood,
            "predicted_behavior": predicted_behavior,
            "timestamp": datetime.now().isoformat()
        }

        log_event(f"[BEHAVIOR PREDICTION]: {persona} → mood: {mood} → predicted behavior: {predicted_behavior}")

    with open(PREDICTED_BEHAVIOR_FILE, "w") as f:
        json.dump(predictions, f, indent=2)

# === Log Event ===
def log_event(message):
    logs = []
    if os.path.exists(BEHAVIOR_LOG_FILE):
        try:
            with open(BEHAVIOR_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(BEHAVIOR_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Example Usage (testable) ===
if __name__ == "__main__":
    predict_avatar_behavior()
    print("[BEHAVIOR PREDICTOR]: Predicted avatar behaviors based on mood state.")