"""
Persona Relay Bus:
Acts as the middleware for sending structured messages between assistant personas.
Enables conversation, reactions, message routing, and contextual commentary exchange.
"""

import json
import os
from datetime import datetime
from pathlib import Path

RELAY_LOG = "brain/persona_bus"
Path(RELAY_LOG).mkdir(parents=True, exist_ok=True)

def relay_message(sender, receiver, topic, content):
    """
    Send a message between assistant personas.
    """
    message = {
        "from": sender,
        "to": receiver,
        "topic": topic,
        "content": content,
        "timestamp": datetime.utcnow().isoformat()
    }

    path = os.path.join(RELAY_LOG, f"{receiver}_inbox.json")

    existing = []
    if os.path.exists(path):
        with open(path, "r") as f:
            existing = json.load(f)

    existing.append(message)

    with open(path, "w") as f:
        json.dump(existing, f, indent=2)

    print(f"[🧵 Persona Bus] {sender} ➡ {receiver} | Topic: {topic}")

def read_inbox(persona_name):
    """
    Fetch incoming messages for a specific assistant.
    """
    path = os.path.join(RELAY_LOG, f"{persona_name}_inbox.json")
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)

def clear_inbox(persona_name):
    """
    Clears the inbox for a persona.
    """
    path = os.path.join(RELAY_LOG, f"{persona_name}_inbox.json")
    if os.path.exists(path):
        os.remove(path)
        print(f"[🗑️ Persona Bus] Inbox cleared for {persona_name}")