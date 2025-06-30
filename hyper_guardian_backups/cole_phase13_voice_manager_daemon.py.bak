# cole_phase13_voice_manager_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
VOICE_FOLDER = "data/voices"
VOICE_LOG_FILE = "data/cole_voice_manager_log.json"
CHECK_INTERVAL = 1800  # 30 minutes

# === Ensure folders exist ===
os.makedirs(VOICE_FOLDER, exist_ok=True)
os.makedirs("data", exist_ok=True)

# === Logging Helper ===
def log_voice_event(message):
    logs = []
    if os.path.exists(VOICE_LOG_FILE):
        try:
            with open(VOICE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Simulate voice sample generation ===
def generate_voice_sample(persona_name):
    filename = f"{persona_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
    filepath = os.path.join(VOICE_FOLDER, filename)

    # In a real system: integrate with ElevenLabs or other TTS API.
    with open(filepath, "w") as f:
        f.write(f"Simulated voice sample for {persona_name} generated at {datetime.now().isoformat()}")

    log_voice_event(f"[GENERATED]: {filename}")
    print(f"[VOICE MANAGER DAEMON]: Generated simulated voice → {filename}")

# === Main Daemon Loop ===
def voice_manager_daemon_loop():
    print("[VOICE MANAGER DAEMON]: Running...")
    while True:
        try:
            generate_voice_sample("Cole AI")
        except Exception as e:
            log_voice_event(f"[ERROR]: {e}")
            print(f"[VOICE MANAGER DAEMON ERROR]: {e}")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    voice_manager_daemon_loop()