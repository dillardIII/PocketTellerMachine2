from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: whisper_command_listener.py ===

# 🎤 Whisper Command Listener – Listens for voice, generates mission files

import speech_recognition as sr
from whisper_to_mission import process_voice_command

def listen_and_convert():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("[Whisper] 🎙️ Listening...")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        transcript = recognizer.recognize_google(audio)
        print(f"[Whisper] 🗣️ Heard: {transcript}")
        process_voice_command(transcript)
    except sr.UnknownValueError:
        print("[Whisper] ❌ Could not understand audio.")
    except sr.RequestError as e:
        print(f"[Whisper] ❌ API error: {e}")

if __name__ == "__main__":
    while True:
        listen_and_convert()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():