# === FILE: instruction_packet_router.py ===
import json
import os
from datetime import datetime

INSTRUCTION_DIR = "bridge_packets"
os.makedirs(INSTRUCTION_DIR, exist_ok=True)

def build_instruction_packet(sender, recipient, files, instructions, task_name="Autobuild Mission"):
    packet = {
        "timestamp": datetime.utcnow().isoformat(),
        "sender": sender,
        "recipient": recipient,
        "task_name": task_name,
        "instructions": instructions,
        "files": files  # {"filename.py": "file content"}
    }
    filename = f"{sender}_to_{recipient}_{task_name.replace(' ', '_')}.json"
    path = os.path.join(INSTRUCTION_DIR, filename)
    with open(path, "w") as f:
        json.dump(packet, f, indent=2)
    print(f"[INSTRUCTION_PACKET_ROUTER] Packet saved: {filename}")
    return path