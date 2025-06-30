from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: persona_speaker_manager.py ===
# 🎤 Persona Speaker Manager – Picks speaker based on mood, urgency, or system needs

from mood_state_engine import MoodStateEngine
from assistant_dispatch import AssistantDispatch

class PersonaSpeakerManager:
    def __init__(self):
        self.dispatch = AssistantDispatch()
        self.mood = MoodStateEngine()

        self.mood_map = {
            "Euphoric": "Mo Cash",
            "Frustrated": "Drill Instructor",
            "Neutral": "Mentor",
            "Focused": "Strategist",
            "Worried": "Shadow",
            "Curious": "Optimist",
            "Calm": "Chill Trader"
        }

    def speak(self, message, override=None):
        mood = self.mood.get_mood()
        speaker = override or self.mood_map.get(mood, "Mentor")
        self.dispatch.speak(message, speaker)

# Example
if __name__ == "__main__":
    sm = PersonaSpeakerManager()
    sm.speak("Market scan complete. Confidence is rising.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():