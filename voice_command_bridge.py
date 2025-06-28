# === FILE: voice_command_bridge.py ===
"""
Voice Command Bridge
Listens for approved voice commands from assistant personas or mic input,
then triggers bridge operations like file deployment, sync, or memory updates.

Supports both real mic recognition and simulated CLI fallback.
"""

import os
import json
from datetime import datetime

# Optional speech recognition mode
USE_MIC = True
VOICE_LOG = "memory/voice_command_log.json"
ALLOWED_COMMANDS = [
    "deploy module", "run sync", "scan bridge", "activate protocol",
    "push file", "pull update", "initiate drop", "run memory bridge",
    "inject code", "drop ghost", "recall last", "check the bridge",
    "sync scripts", "sync code", "install"
]

def log_voice_command(command, source="user"):
    if not os.path.exists(VOICE_LOG):
        log = []
    else:
        with open(VOICE_LOG, "r") as f:
            log = json.load(f)

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "source": source,
        "command": command
    }

    log.append(entry)
    with open(VOICE_LOG, "w") as f:
        json.dump(log[-200:], f, indent=2)

    print(f"[VoiceBridge] 🎙️ {source.upper()} issued: {command}")

def listen_for_voice_command():
    if USE_MIC:
        try:
            import speech_recognition as sr
            recognizer = sr.Recognizer()
            mic = sr.Microphone()

            with mic as source:
                print("🎙️ Listening for bridge command...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio).lower()
            print(f"🗣️ Heard: {command}")
            return command
        except sr.UnknownValueError:
            print("❌ Voice not understood.")
        except sr.RequestError:
            print("❌ Voice service unavailable.")
        except Exception as e:
            print(f"❌ Mic error: {e}")
    else:
        command = input("💬 Type simulated voice command: ").strip().lower()
        return command
    return None

def handle_bridge_command(command):
    if not command:
        print("⚠️ No command received.")
        return

    log_voice_command(command)

    if any(cmd in command for cmd in ALLOWED_COMMANDS):
        print(f"[VoiceBridge] ✅ Recognized command: {command}")
        if "deploy" in command or "install" in command:
            from bridge_listener import process_bridge_drops
            process_bridge_drops()
        elif "sync" in command or "pull" in command:
            from bridge_listener import check_for_new_scripts
            check_for_new_scripts()
        elif "bridge" in command or "check" in command:
            from bridge_listener import check_for_new_scripts, process_bridge_drops
            check_for_new_scripts()
            process_bridge_drops()
        elif "memory" in command:
            from memory.memory_utils import run_memory_refresh
            run_memory_refresh()
        else:
            print(f"[VoiceBridge] ⚠️ No specific action bound to: {command}")
    else:
        print(f"[VoiceBridge] ❌ Unknown or unapproved command: {command}")

if __name__ == "__main__":
    print("[VoiceBridge] 🎛️ Voice command system ready.")
    while True:
        cmd = listen_for_voice_command()
        handle_bridge_command(cmd)