import json
import os
import time
from datetime import datetime

CONTEXT_FILE = "vault/context.json"

def load_context():
    if os.path.exists(CONTEXT_FILE):
        with open(CONTEXT_FILE) as f:
            return json.load(f)
    return {"events": [], "preferences": {"tone": "real", "style": "direct"}}

def save_context(context):
    with open(CONTEXT_FILE, "w") as f:
        json.dump(context, f, indent=2)

def update_context(event):
    ctx = load_context()
    ctx["events"].append({
        "timestamp": datetime.utcnow().isoformat(),
        "event": event
    })
    save_context(ctx)
    print(f"[ContextAI] 🧠 Logged event: {event}")

def context_loop():
    while True:
        update_context("Heartbeat: still learning you...")
        time.sleep(600)

if __name__ == "__main__":
    context_loop()