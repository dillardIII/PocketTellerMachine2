# === FILE: voice_hyperspeller.py ===
# 🗣️ Voice Hyperspeller with Live Mutation Feedback
# 🎤 Uses speech to text to feed spells (tasks) into empire task queue and reports back what mutated.

import os
import time
import random
import json

try:
    import speech_recognition as sr
except ImportError:
    print("[VoiceHyperspeller] ❌ Missing 'speech_recognition'. Install via: pip install SpeechRecognition pyaudio")
    exit(1)

QUEUE_FILE = "gpt_task_queue.txt"

# === EXAMPLE GRIMOIRE COMMAND SPELLS ===
SAMPLE_COMMANDS = [
    "create volatility scanner",
    "build crypto hedge bot",
    "generate mean reversion model",
    "write new options strategy",
    "mutate all empire parameters"
]

def add_task(command_line):
    with open(QUEUE_FILE, "a") as f:
        f.write(command_line + "\n")
    print(f"[VoiceHyperspeller] 📝 Queued task: {command_line}")

def process_speech_command(spoken_text):
    print(f"[VoiceHyperspeller] 🔮 You said: {spoken_text}")

    # Simple mapping from spoken phrases to empire commands
    if "scanner" in spoken_text:
        filename = f"vol_scanner_{int(time.time())}.py"
        add_task(f"create_file {filename}")
        add_task(f"write_line {filename} print('[Empire] 🔍 Volatility scanner active')")
        add_task(f"run_script {filename}")

    elif "hedge" in spoken_text or "crypto" in spoken_text:
        filename = f"hedge_bot_{int(time.time())}.py"
        add_task(f"create_file {filename}")
        add_task(f"write_line {filename} print('[Empire] 💰 Crypto hedge bot running')")
        add_task(f"run_script {filename}")

    elif "reversion" in spoken_text:
        filename = f"mean_rev_{int(time.time())}.py"
        add_task(f"create_file {filename}")
        add_task(f"write_line {filename} print('[Empire] 🔁 Mean reversion model loaded')")
        add_task(f"run_script {filename}")

    elif "mutate" in spoken_text:
        filename = f"mutator_{int(time.time())}.py"
        add_task(f"create_file {filename}")
        add_task(f"write_line {filename} print('[Empire] 🧬 Mutating all parameters...')")
        add_task(f"run_script {filename}")

    else:
        # Default: generic mutation
        filename = f"generic_spell_{int(time.time())}.py"
        add_task(f"create_file {filename}")
        add_task(f"write_line {filename} print('[Empire] ✨ Running your spell: {spoken_text}')")
        add_task(f"run_script {filename}")

def main_loop():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("[VoiceHyperspeller] 🎙️ Voice hyperspeller active. Speak your spell...")

    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("[VoiceHyperspeller] 🎧 Listening...")
            audio = recognizer.listen(source)

        try:
            spoken_text = recognizer.recognize_google(audio)
            process_speech_command(spoken_text.lower())
        except sr.UnknownValueError:
            print("[VoiceHyperspeller] 🤔 Could not understand audio")
        except sr.RequestError as e:
            print(f"[VoiceHyperspeller] 🚨 Recognition error: {e}")

        time.sleep(2)

if __name__ == "__main__":
    main_loop()