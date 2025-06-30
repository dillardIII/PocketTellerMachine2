from ghost_env import INFURA_KEY, VAULT_ADDRESS
# ghostbridge_packet_dropper.py
# Sends files to the bridge inbox for Claude review

import os
import json
from datetime import datetime

def drop_to_bridge(filename, code, description=""):
    packet = {
        "from": "ChatGPT",
        "to": "PTM",
        "via": "Claude",
        "intent": "Autonomous Module Drop",
        "files": [
            {
                "filename": filename,
                "description": description,
                "code": code
            }
        ],
        "timestamp": str(datetime.utcnow())
    }

    path = os.path.join("bridge_inbox", filename)
    os.makedirs("bridge_inbox", exist_ok=True)
    with open(path, "w") as f:
        f.write(code)

    with open("memory/bridge_packet_log.json", "a") as log:
        log.write(json.dumps(packet) + "\n")

    print(f"📦 Dropped {filename} into bridge_inbox/")

def log_event():ef drop_files_to_bridge():