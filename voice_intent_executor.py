# === FILE: voice_intent_executor.py ===
# 🎙️ Voice Intent Executor – links recognized intents to direct module execution

import os
import time
import subprocess

INTENT_LOG = "logs/whisper_intents.log"

# Define simple mappings
INTENT_MAP = {
    "dashboard": "python3 empire_dashboard.py",
    "vault": "python3 vault_dashboard.py",
    "matrix": "python3 matrix_dashboard.py",
    "start trading": "python3 ghost_market_trader.py",
    "market oracle": "python3 market_oracle.py",
    "heatmap": "python3 ghost_heatmap_ui.py"
}

def watch_and_execute():
    print("[VoiceIntentExecutor] 🧠 Watching for spoken intents...")
    while True:
        if os.path.exists(INTENT_LOG):
            with open(INTENT_LOG) as f:
                lines = f.readlines()
            os.remove(INTENT_LOG)
            for line in lines:
                handle_intent(line.strip().lower())
        time.sleep(3)

def handle_intent(intent_text):
    for key, cmd in INTENT_MAP.items():
        if key in intent_text:
            print(f"[VoiceIntentExecutor] 🎯 Intent matched: '{key}' → running: {cmd}")
            subprocess.Popen(cmd, shell=True)
            return
    print(f"[VoiceIntentExecutor] 🤷 No match for: {intent_text}")

if __name__ == "__main__":
    watch_and_execute()