from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: whisper_voice_intent.py ===
# 🎙️ Whisper Voice Intent Parser – listens, transcribes, and injects commands into your empire queue

import time
import os
from datetime import datetime
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
QUEUE_FILE = "gpt_task_queue.txt"

def transcribe_audio(audio_path):
    with open(audio_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]

def queue_task(command):
    with open(QUEUE_FILE, "a") as f:
        f.write(command + "\n")
    print(f"[WhisperIntent] 📝 Queued: {command}")

def listen_forever():
    print("[WhisperIntent] 🎙️ Listening for voice commands...")
    while True:
        audio_path = f"voice_{int(time.time())}.wav"
        os.system(f"arecord -d 5 -f cd -t wav {audio_path}")
        try:
            text = transcribe_audio(audio_path)
            print(f"[WhisperIntent] 🗣️ Heard: {text}")

            # Example parse: naive mapping
            if "create file" in text:
                filename = text.split("create file")[-1].strip().replace(" ", "_") + ".py"
                queue_task(f"create_file {filename}")
            elif "run" in text:
                filename = text.split("run")[-1].strip().replace(" ", "_") + ".py"
                queue_task(f"run_script {filename}")
            else:
                # General GPT invocation
                queue_task(f"spell: {text}")

        except Exception as e:
            print(f"[WhisperIntent] ❌ Transcription failed: {e}")
        time.sleep(2)

if __name__ == "__main__":
    listen_forever()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():