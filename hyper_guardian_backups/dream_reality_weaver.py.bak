# 🌌 Dream Reality Weaver – hybridizes dreams with real projects for next-level expansion

import os
import json
import time
from datetime import datetime
from random import randint, choice

DREAMS_DIR = "dreams"
REAL_DIR = "businesses"

def weave_future():
    dream_files = os.listdir(DREAMS_DIR)
    real_files = os.listdir(REAL_DIR)
    if dream_files and real_files:
        dream = choice(dream_files)
        real = choice(real_files)
        with open(os.path.join(DREAMS_DIR, dream)) as d, open(os.path.join(REAL_DIR, real)) as r:
            dream_data = json.load(d)
            real_data = json.load(r)
        hybrid = {
            "merged_idea": f"{dream_data['idea']} + {real_data['name']}",
            "generated_at": datetime.utcnow().isoformat(),
            "score": randint(1, 100)
        }
        with open(f"hybrids/hybrid_{int(time.time())}.json", "w") as f:
            json.dump(hybrid, f, indent=2)
        print(f"[RealityWeaver] 🌟 Created hybrid: {hybrid['merged_idea']}")

os.makedirs("hybrids", exist_ok=True)
while True:
    weave_future()
    time.sleep(180)