from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: packet_responder.py ===
import os
import json
from datetime import datetime

RESPONSE_DIR = "bridge_responses"
os.makedirs(RESPONSE_DIR, exist_ok=True)

def send_response(original_packet, status, notes):
    response = {
        "timestamp": datetime.utcnow().isoformat(),
        "response_to": original_packet.get("task_name"),
        "original_sender": original_packet.get("sender"),
        "responder": original_packet.get("recipient"),
        "status": status,
        "notes": notes
    }

    filename = f"{response['responder']}_to_{response['original_sender']}_{response['response_to'].replace(' ', '_')}_RESPONSE.json"
    path = os.path.join(RESPONSE_DIR, filename)
    with open(path, "w") as f:
        json.dump(response, f, indent=2)

    print(f"[RESPONSE] Sent response: {filename}")
    return path

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():