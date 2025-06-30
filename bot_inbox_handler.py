from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bot_inbox_handler.py ===
"""
Bot Inbox Handler:
Each assistant uses this to check for incoming messages,
validate permissions, and perform assigned tasks.
"""

import os
import json
from assistant_comms_matrix import can_send

INBOX_DIR = "data/assistant_inboxes"
os.makedirs(INBOX_DIR, exist_ok=True)

def get_inbox_path(bot_name):
    return os.path.join(INBOX_DIR, f"{bot_name.lower()}_inbox.json")

def send_message(sender, receiver, task_type, payload):
    """
    Send a message to a bot's inbox if allowed by the comms matrix.:
    """
    if not can_send(sender, receiver, task_type):
        print(f"[❌ Unauthorized] {sender} cannot send {task_type} to {receiver}")
        return False

    message = {
        "from": sender,
        "task": task_type,
        "payload": payload
    }

    inbox_path = get_inbox_path(receiver)
    if not os.path.exists(inbox_path):
        with open(inbox_path, "w") as f:
            json.dump([], f)

    with open(inbox_path, "r") as f:
        inbox = json.load(f)

    inbox.append(message)

    with open(inbox_path, "w") as f:
        json.dump(inbox, f, indent=2)

    print(f"[📬 Message Delivered] {sender} → {receiver}: {task_type}")
    return True

def read_messages(bot_name):
    """
    Reads and returns all messages in the bot's inbox.
    Clears the inbox afterward.
    """
    inbox_path = get_inbox_path(bot_name)
    if not os.path.exists(inbox_path):
        return []

    with open(inbox_path, "r") as f:
        messages = json.load(f)

    # Clear inbox after reading
    with open(inbox_path, "w") as f:
        json.dump([], f)

    print(f"[📥 {bot_name}] Received {len(messages)} messages.")
    return messages

# === Local test ===
if __name__ == "__main__":
    send_message("MoCash", "Mentor", "review", {"file": "bull_breakout.py"})
    send_message("ChillTrader", "MoCash", "comment", {"tip": "RSI looks high"})
    print(read_messages("Mentor"))
    print(read_messages("MoCash"))

def log_event():ef drop_files_to_bridge():