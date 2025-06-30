# cole_tools/cole_voice_assistant_daemon.py

import time
from datetime import datetime
import os
import json

ASSISTANT_LOG_FILE = "data/voice_assistant_log.json"

# === Sample supported commands ===
COMMANDS = {
    "status report": "Generating full status report...",
    "latest trade summary": "Fetching latest trade summary...",
    "voice last narration": "Playing last narrated trade summary...",
    "list strategies": "Listing known strategies...",
    "help": "Available commands: status report, latest trade summary, voice last narration, list strategies, help"
}

def log_assistant_interaction(user_command, ai_response):
    logs = []
    if os.path.exists(ASSISTANT_LOG_FILE):
        try:
            with open(ASSISTANT_LOG_FILE, "r") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "user_command": user_command,
        "ai_response": ai_response
    })
    with open(ASSISTANT_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

def ai_assistant_loop():
    print("[VOICE ASSISTANT DAEMON]: Ready to accept commands (simulated via console input)...")
    while True:
        try:
            command = input("[You]: ").strip().lower()
            if command in COMMANDS:
                response = COMMANDS[command]
                print(f"[AI Assistant]: {response}")
                log_assistant_interaction(command, response)
            else:
                print("[AI Assistant]: Sorry, I didn't understand that. Say 'help' to see available commands.")
                log_assistant_interaction(command, "Unknown command.")
        except Exception as e:
            print(f"[VOICE ASSISTANT ERROR]: {e}")
        time.sleep(1)

if __name__ == "__main__":
    ai_assistant_loop()