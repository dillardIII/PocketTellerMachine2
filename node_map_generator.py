# === FILE: node_map_generator.py ===
import json
import time
import random
from datetime import datetime

def update_node_map():
    nodes = []
    for i in range(10):
        nodes.append({
            "id": f"node_{i}",
            "status": random.choice(["online", "processing", "idle"]),
            "last_ping": datetime.utcnow().isoformat()
        })

    with open("node_map.json", "w") as f:
        json.dump(nodes, f, indent=2)
    print("[NodeMap] 🌐 Node map updated.")

def update_brain_status():
    brains = {
        "total_brains": random.randint(20,50),
        "queue": random.randint(0,100),
        "mood": random.choice(["strategic", "curious", "ruthless", "playful"]),
        "last_update": datetime.utcnow().isoformat()
    }
    with open("brain_status.json", "w") as f:
        json.dump(brains, f, indent=2)
    print("[NodeMap] 🧠 Quantum brain status updated.")

if __name__ == "__main__":
    while True:
        update_node_map()
        update_brain_status()
        time.sleep(10)