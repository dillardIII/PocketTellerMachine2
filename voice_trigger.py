from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: voice_trigger.py ===
# 🎙️ Voice Trigger – Uses OpenAI Whisper API to transcribe uploaded voice file and pass it to PTM

import openai
import os
from assistant_dispatch import AssistantDispatch

class VoiceTrigger:
    def __init__(self):
        self.dispatch = AssistantDispatch()
        self.api_key = os.getenv("OPENAI_API_KEY")  # Put in .env
        print("[VoiceTrigger] 🎧 File-based voice trigger ready (no mic needed)")

    def transcribe_and_execute(self, filename="voice_input.wav"):
        try:
            openai.api_key = self.api_key

            with open(filename, "rb") as audio_file:
                transcript = openai.Audio.transcribe("whisper-1", audio_file)

            command_text = transcript["text"].strip()
            print(f"[VoiceTrigger] 🗣️ Heard: {command_text}")
            self.dispatch.process_voice_command(command_text)

        except Exception as e:
            print(f"[VoiceTrigger] ❌ Transcription failed: {e}")

def log_event():ef drop_files_to_bridge():