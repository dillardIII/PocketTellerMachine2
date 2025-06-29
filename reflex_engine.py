# === FILE: reflex_engine.py ===

import random
import time

class ReflexEngine:
    def __init__(self):
        print("[ReflexEngine] 🧠 Reflex AI initialized.")

def start_reflex_engine():
    print("[ReflexEngine] 🧠 Reflex engine online. Running thought cycles...")
    moods = ["calculating", "curious", "ruthless", "playful", "strategic"]
    while True:
        mood = random.choice(moods)
        print(f"[ReflexEngine] 🧬 Current mood: {mood}")
        time.sleep(10)