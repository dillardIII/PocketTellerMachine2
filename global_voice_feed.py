from ghost_env import INFURA_KEY, VAULT_ADDRESS
import time
import random

EVENTS = [
    "🚨 New earthquake reported in Japan.",
    "🔥 Tech stock rally pushes NASDAQ higher.",
    "💔 Mass casualty event reported downtown.",
    "🌌 James Webb telescope finds strange exoplanet.",
    "💸 Bitcoin surges past resistance."
]

def global_voice_loop():
    while True:
        event = random.choice(EVENTS)
        print(f"[VoiceFeed] 🎙️ {event}")
        time.sleep(120)

if __name__ == "__main__":
    global_voice_loop()

def log_event():ef drop_files_to_bridge():