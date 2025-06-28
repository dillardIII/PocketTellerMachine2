# === FILE: high_risk_manager.py ===
import json
import os
import time

def load_emotion():
    if os.path.exists("emotion_state.json"):
        with open("emotion_state.json") as f:
            return json.load(f)
    return {"confidence":50, "fear":50}

def run_high_risk_loop():
    while True:
        emotion = load_emotion()
        risk_multiplier = (emotion["confidence"] - emotion["fear"]) / 50
        risk_multiplier = max(1.0, min(3.0, 1 + risk_multiplier))
        print(f"[HighRisk] ⚔️ Adjusted scale: {risk_multiplier:.2f}x | Emotion: {emotion}")
        time.sleep(60)