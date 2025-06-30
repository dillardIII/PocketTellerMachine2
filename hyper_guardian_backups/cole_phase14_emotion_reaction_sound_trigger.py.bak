# cole_phase14_emotion_reaction_sound_trigger.py

import random

# === Define Reaction Sounds ===
REACTION_SOUNDS = {
    "victory": ["applause.mp3", "cheer.mp3", "trumpet.mp3"],
    "loss": ["boo.mp3", "sad_trombone.mp3", "fail_buzzer.mp3"],
    "neutral": ["hmm.mp3", "beep.mp3", "ding.mp3"],
    "angry": ["alert_siren.mp3", "warning_beep.mp3"],
    "excited": ["drumroll.mp3", "hype_horn.mp3"]
}

# === Generate Sound Trigger Based on Emotion ===
def trigger_sound_for_emotion(emotion):
    emotion_key = emotion.lower()
    if "win" in emotion_key or "victory" in emotion_key or "good" in emotion_key:
        return random.choice(REACTION_SOUNDS["victory"])
    elif "loss" in emotion_key or "fail" in emotion_key or "bad" in emotion_key:
        return random.choice(REACTION_SOUNDS["loss"])
    elif "angry" in emotion_key or "alert" in emotion_key:
        return random.choice(REACTION_SOUNDS["angry"])
    elif "excited" in emotion_key or "hype" in emotion_key:
        return random.choice(REACTION_SOUNDS["excited"])
    else:
        return random.choice(REACTION_SOUNDS["neutral"])

# === Example Usage ===
if __name__ == "__main__":
    test_emotions = ["Victory", "Loss", "Angry", "Excited", "Neutral"]
    for emotion in test_emotions:
        sound = trigger_sound_for_emotion(emotion)
        print(f"[{emotion}]: {sound}")