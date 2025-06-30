# === FILE: voice_tone_selector.py ===
# 🎙️ Voice Tone Selector – Picks voice style by mood, situation, or user preference

class VoiceToneSelector:
    def __init__(self):
        self.tone_map = {
            "Euphoric": "Hype Mode",
            "Frustrated": "Drill Mode",
            "Focused": "Smooth",
            "Neutral": "Classic AI",
            "Calm": "Whisper",
            "Curious": "Playful",
            "Worried": "Serious"
        }

    def get_tone(self, mood):
        return self.tone_map.get(mood, "Classic AI")

# Example
if __name__ == "__main__":
    selector = VoiceToneSelector()
    print(selector.get_tone("Focused"))