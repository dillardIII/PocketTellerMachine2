# === FILE: persona_voice_player.py ===
# 🔊 Persona Voice Player – Plays selected MP3 lines per persona

import os
from utils.logger import log_event
from playsound import playsound  # Make sure playsound or equivalent is installed

VOICE_DIR = "assets/voices/"

class PersonaVoicePlayer:
    def __init__(self):
        self.voice_map = {
            "Mentor": "mentor_calm.mp3",
            "Mo Cash": "mo_cash_hype.mp3",
            "Drill Instructor": "drill_sergeant_alert.mp3",
            "Strategist": "strategist_briefing.mp3",
            "Shadow": "shadow_whisper.mp3",
            "Chill Trader": "chill_surfer.mp3",
            "Optimist": "optimist_bounce.mp3"
        }

    def speak(self, persona):
        if persona in self.voice_map:
            file_path = os.path.join(VOICE_DIR, self.voice_map[persona])
            if os.path.exists(file_path):
                playsound(file_path)
                log_event(f"🔊 {persona} spoke: {self.voice_map[persona]}")
            else:
                log_event(f"⚠️ Missing voice file: {file_path}")
        else:
            log_event(f"❌ Unknown persona: {persona}")

# Example use
if __name__ == "__main__":
    speaker = PersonaVoicePlayer()
    speaker.speak("Mo Cash")