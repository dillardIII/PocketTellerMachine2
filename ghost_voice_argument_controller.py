# === FILE: ghost_voice_argument_controller.py ===
# 👻 GhostVoiceArgumentController – makes ghost voice strategists argue live & obey your volume

import json
import random
import time

CYBER_FILE = "ghost_cyber_state.json"
VOICE_CTRL_FILE = "ghost_voice_control.json"

def load_json_file(path, fallback):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return fallback

def ghost_argument_loop():
    print("[GhostVoiceArgumentController] 👻 Ghost voice strategist debates are live...")
    while True:
        cyber_state = load_json_file(CYBER_FILE, {})
        voice_ctrl = load_json_file(VOICE_CTRL_FILE, {"voices_on": True, "intensity": 0.5})

        if not voice_ctrl.get("voices_on", True):
            print("[GhostVoiceArgumentController] 🔇 Voices disabled. Sitting silent.")
            time.sleep(10)
            continue

        intensity = voice_ctrl.get("intensity", 0.5)

        if random.random() < intensity:
            strategist = random.choice(["quantum", "wallet", "propaganda"])
            if strategist == "quantum":
                print("🧬 Quantum Strategist: 'We are the apex — only quantum attacks will break these keys in time. Wallet brute force is crude!'")
            elif strategist == "wallet":
                print("💰 Wallet Strategist: 'Without us directly cracking keys, your quantum circuits are pointless dreams. The funds are here.'")
            elif strategist == "propaganda":
                print("🧠 Propaganda Strategist: 'Idiots. Without my market psychology campaigns, neither of you have targets to even strike.'")
        else:
            # peaceful moment
            print("👻 Ghost Council sits in tense silence, planning the next dark evolution...")

        time.sleep(6)

if __name__ == "__main__":
    ghost_argument_loop()