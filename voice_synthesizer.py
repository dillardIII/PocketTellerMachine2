# voice_synthesizer.py
# Purpose: Convert AI persona responses into voice using ElevenLabs (or other voice AI API)
# Supports mood-based voice styling and persona-specific voices

import os
import json
import requests
from datetime import datetime
from utils.logger import log_event

class VoiceSynthesizer:
    def __init__(self):
        self.api_key = os.getenv("ELEVENLABS_API_KEY")
        self.voice_map = self._load_voice_map()
        self.output_dir = "memory/recaps/"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def _load_voice_map(self):
        """Load voice ID mappings for each persona and mood."""
        return {
            "Mo Cash": {
                "celebratory": "voice_mocash_hype",
                "neutral": "voice_mocash_chill",
                "regretful": "voice_mocash_reflect"
            },
            "The Mentor": {
                "celebratory": "voice_mentor_proud",
                "neutral": "voice_mentor_base",
                "regretful": "voice_mentor_soft"
            },
            "Drill Instructor": {
                "celebratory": "voice_drill_win",
                "neutral": "voice_drill_brief",
                "regretful": "voice_drill_shame"
            },
            "GhostBot": {
                "celebratory": "voice_ghost_uplift",
                "neutral": "voice_ghost_neutral",
                "regretful": "voice_ghost_dark"
            }
        }

    def generate_voice(self, persona, mood, text):
        """Generate and save a voice MP3 for a given persona + mood + message."""
        voice_id = self.voice_map.get(persona, {}).get(mood)
        if not voice_id:
            raise Exception(f"No voice ID found for {persona} with mood '{mood}'")

        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        headers = {
            "xi-api-key": self.api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.4,
                "similarity_boost": 0.9
            }
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            log_event("VoiceGen Error", {"status": response.status_code, "detail": response.text})
            raise Exception("Voice generation failed.")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{persona.replace(' ', '_')}_{mood}_{timestamp}.mp3"
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, "wb") as f:
            f.write(response.content)

        log_event("Voice MP3 Created", {"persona": persona, "mood": mood, "file": filename})
        return filename