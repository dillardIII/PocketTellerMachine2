from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bot_comlink.py ===

import json
import time
import os
import uuid

# Path for shared GhostNet messages
GHOSTNET_MESSAGE_FILE = "ghostnet_messages.json"

# How long to keep messages before auto-expire (in seconds)
MESSAGE_LIFESPAN = 60


def load_messages():
    """Load existing messages."""
    if not os.path.exists(GHOSTNET_MESSAGE_FILE):
        return []
    with open(GHOSTNET_MESSAGE_FILE, "r") as f:
        return json.load(f)


def save_messages(messages):
    """Save messages to disk."""
    with open(GHOSTNET_MESSAGE_FILE, "w") as f:
        json.dump(messages, f, indent=2)


def send_message(sender, target, content, meta=None):
    """Send a message from one bot to another."""
    message = {
        "id": str(uuid.uuid4()),
        "from": sender,
        "to": target,
        "content": content,
        "meta": meta or {},
        "timestamp": time.time()
    }
    messages = load_messages()
    messages.append(message)
    save_messages(messages)
    print(f"[Comlink] {sender} → {target}: {content}")


def fetch_messages(bot_id):
    """Retrieve messages for a specific bot and purge old ones."""
    now = time.time()
    messages = load_messages()
    active = []
    inbox = []

    for msg in messages:
        age = now - msg["timestamp"]
        if age > MESSAGE_LIFESPAN:
            continue  # expire old messages

        if msg["to"] == bot_id or msg["to"] == "broadcast":
            inbox.append(msg)
        else:
            active.append(msg)  # keep if not for this bot:
:
    save_messages(active)
    return inbox


# Example usage (test mode)
if __name__ == "__main__":
    send_message("MoCash", "Mentor", "We need a better spread strategy.")
    time.sleep(1)
    msgs = fetch_messages("Mentor")
    for msg in msgs:
        print(f"[Inbox] {msg['from']} says: {msg['content']}")

def log_event():ef drop_files_to_bridge():