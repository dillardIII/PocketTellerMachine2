from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: team_dropbox.py ===
import os
import json
from datetime import datetime

DROPBOX_DIR = "team_dropboxes"
os.makedirs(DROPBOX_DIR, exist_ok=True)

def drop_file(sender, recipient, filename, content, purpose="General"):
    recipient_box = os.path.join(DROPBOX_DIR, f"{recipient}_dropbox.json")

    drop_entry = {
        "sender": sender,
        "filename": filename,
        "content": content,
        "purpose": purpose,
        "timestamp": datetime.utcnow().isoformat()
    }

    if os.path.exists(recipient_box):
        with open(recipient_box, "r") as f:
            entries = json.load(f)
    else:
        entries = []

    entries.append(drop_entry)

    with open(recipient_box, "w") as f:
        json.dump(entries, f, indent=2)

    print(f"[DROPBOX] {sender} dropped '{filename}' for {recipient} — {purpose}")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():