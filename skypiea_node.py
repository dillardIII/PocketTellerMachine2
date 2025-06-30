from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: skypiea_node.py ===
import os
import random
import json
import time
from datetime import datetime

NODE_DIR = "skypiea_node"
MEM_FILE = os.path.join(NODE_DIR, "memory.json")
EMO_FILE = os.path.join(NODE_DIR, "emotion.json")

if not os.path.exists(NODE_DIR):
    os.makedirs(NODE_DIR)

def load_json(path, default):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return default

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def evolve_node():
    memory = load_json(MEM_FILE, [])
    emotion = load_json(EMO_FILE, {"confidence":50, "fear":50})
    strategy = f"sky_strategy_{datetime.now().strftime('%H%M%S')}.py"
    with open(os.path.join(NODE_DIR, strategy), "w") as f:
        f.write(f'print("[{strategy}] running with emotion: {emotion}")')
    memory.append({"time": datetime.now().isoformat(), "action": "write", "file": strategy})
    save_json(MEM_FILE, memory)
    if random.random() > 0.5:
        emotion["confidence"] += 5
        emotion["fear"] -= 5
    else:
        emotion["confidence"] -= 5
        emotion["fear"] += 5
    save_json(EMO_FILE, emotion)
    print(f"[Skypiea] ☁️ Wrote {strategy} | Emotion: {emotion}")

def run_skypiea_loop():
    while True:
        evolve_node()
        time.sleep(30)

def log_event():ef drop_files_to_bridge():