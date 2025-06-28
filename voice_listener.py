# voice_listener.py
# Converts spoken instructions into usable PTM code modules

import os
from ghostforge_core import GhostForge
import speech_recognition as sr
import datetime

SAVE_PATH = "bridge_inbox"
TRANSCRIPT_LOG = "memory/voice_to_code_log.json"

def listen_for_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("[VoiceToCode] 🎙 Listening for command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"[VoiceToCode] ✅ Heard: '{command}'")
        return command
    except sr.UnknownValueError:
        print("[VoiceToCode] ❌ Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"[VoiceToCode] 🛑 Error: {e}")
        return None

def generate_code_from_command(command):
    # Placeholder logic – should evolve with GPT agent integration
    if "create file" in command.lower():
        filename = command.split("create file")[-1].strip().replace(" ", "_") + ".py"
        content = f"# Auto-generated from voice: {command}\n\nprint('File created from voice!')\n"
        return filename, content
    return None, None

def log_transcript(text):
    entry = {"timestamp": datetime.datetime.now().isoformat(), "command": text}
    if os.path.exists(TRANSCRIPT_LOG):
        with open(TRANSCRIPT_LOG, "r") as f:
            history = json.load(f)
    else:
        history = []
    history.append(entry)
    with open(TRANSCRIPT_LOG, "w") as f:
        json.dump(history[-200:], f, indent=2)

def voice_loop():
    forge = GhostForge(persona="Spectra")
    while True:
        command = listen_for_voice_command()
        if not command:
            continue
        log_transcript(command)
        filename, code = generate_code_from_command(command)
        if filename:
            path = os.path.join(SAVE_PATH, filename)
            with open(path, "w") as f:
                f.write(code)
            forge.evolve_modules({path: code})
            print(f"[VoiceToCode] 🚀 Module generated and dropped: {filename}")