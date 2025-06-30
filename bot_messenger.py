from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Bot Messenger:
Lets bots send messages, alerts, or comments to each other.
Supports simulated inter-bot conversations and logic feedback loops.
"""

import json
import os
from datetime import datetime
from pathlib import Path

MESSAGE_LOG_DIR = "brain/bot_messages"
Path(MESSAGE_LOG_DIR).mkdir(parents=True, exist_ok=True)

def send_bot_message(sender, receiver, content, context="general"):
    """
    Creates a message log from one bot to another.
    """
    timestamp = datetime.utcnow().isoformat()
    message = {
        "from": sender,
        "to": receiver,
        "timestamp": timestamp,
        "context": context,
        "content": content
    }

    fname = f"{receiver}_inbox.json"
    inbox_path = os.path.join(MESSAGE_LOG_DIR, fname)

    if os.path.exists(inbox_path):
        with open(inbox_path, "r") as f:
            inbox = json.load(f)
    else:
        inbox = []

    inbox.append(message)

    with open(inbox_path, "w") as f:
        json.dump(inbox, f, indent=2)

    print(f"[📨 Bot Messenger] {sender} ➡ {receiver}: {content}")

def read_inbox(bot_name):
    """
    Reads all messages sent to a given bot.
    """
    path = os.path.join(MESSAGE_LOG_DIR, f"{bot_name}_inbox.json")
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)

def clear_inbox(bot_name):
    """
    Empties the inbox of a bot.
    """
    path = os.path.join(MESSAGE_LOG_DIR, f"{bot_name}_inbox.json")
    if os.path.exists(path):
        os.remove(path)
        print(f"[🧹 Bot Messenger] Cleared inbox for {bot_name}")

def log_event():ef drop_files_to_bridge():