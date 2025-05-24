import os
import json
from datetime import datetime
from cole_command_interpreter import cole_interpret_command
from assistants.malik import malik_report

INTENT_MAP_FILE = "data/cole_voice_intent_map.json"
VOICE_LOG_FILE = "data/voice_command_log.json"

# === Load Intent Map ===
def load_intent_map():
    if os.path.exists(INTENT_MAP_FILE):
        try:
            with open(INTENT_MAP_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"[Voice Processor] Error loading intent map: {e}")
    return {}

# === Log Voice Command Event ===
def log_voice_command(spoken_phrase, matched_command, result):
    logs = []
    if os.path.exists(VOICE_LOG_FILE):
        try:
            with open(VOICE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append({
        "timestamp": datetime.now().isoformat(),
        "spoken_phrase": spoken_phrase,
        "matched_command": matched_command,
        "result": result
    })

    with open(VOICE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

    print(f"[Voice Processor] Logged: {spoken_phrase} -> {matched_command}")

# === Process Voice Command ===
def process_voice_command(spoken_phrase):
    intent_map = load_intent_map()
    spoken_lower = spoken_phrase.lower()

    matched_command = intent_map.get(spoken_lower)

    if not matched_command:
        result = f"No matching command found for: '{spoken_phrase}'"
        print(f"[Voice Processor] {result}")
    else:
        print(f"[Voice Processor] Mapped to: {matched_command}")
        result = cole_interpret_command(matched_command)

    log_voice_command(spoken_phrase, matched_command if matched_command else "No Match", result)
    malik_report(f"Voice command executed: {spoken_phrase} -> {matched_command if matched_command else 'No Match'}")

    return result

# === CLI Test Mode ===
if __name__ == "__main__":
    print("Cole Voice Command Processor (Test Mode)")
    while True:
        user_input = input("Say something: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break
        response = process_voice_command(user_input)
        print(f"Cole: {response}")