from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from datetime import datetime

INBOX_FILE = "data/cole_inbox.json"
OUTBOX_FILE = "data/cole_outbox.json"

# === Read Inbox for new commands ===
def check_inbox():
    if not os.path.exists(INBOX_FILE):
        return []
    with open(INBOX_FILE, "r") as f:
        try:
            messages = json.load(f)
            return messages
        except:
            return []

# === Clear Inbox after reading ===
def clear_inbox():
    open(INBOX_FILE, "w").write("[]")

# === Cole sends message back to ChatGPT ===
def send_to_outbox(message):
    if os.path.exists(OUTBOX_FILE):
        with open(OUTBOX_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []
    logs.append({
        "from": "Cole",
        "message": message,
        "timestamp": datetime.now().isoformat()
    })
    with open(OUTBOX_FILE, "w") as f:
        json.dump(logs, f, indent=2)

# === Example Behavior: Cole checks inbox, executes, replies ===
def cole_message_loop():
    inbox = check_inbox()
    if not inbox:
        print("[COLE BRIDGE]: No new messages.")
        return

    for msg in inbox:
        cmd = msg.get("command", "")
        if cmd:
            print(f"[COLE BRIDGE RECEIVED]: {cmd}")
            if "generate" in cmd.lower():
                send_to_outbox(f"Generated new code for request: {cmd}")
            elif "status" in cmd.lower():
                send_to_outbox("Cole is online and working fine.")
            else:
                send_to_outbox(f"Cole received unknown command: {cmd}")

    clear_inbox()

# === ChatGPT sends command to Cole ===
def send_command_to_cole(command_text):
    if os.path.exists(INBOX_FILE):
        with open(INBOX_FILE, "r") as f:
            messages = json.load(f)
    else:
        messages = []
    
    messages.append({
        "from": "ChatGPT",
        "command": command_text,
        "timestamp": datetime.now().isoformat()
    })
    with open(INBOX_FILE, "w") as f:
        json.dump(messages, f, indent=2)
    
    print(f"[CHATGPT BRIDGE]: Sent command to Cole → {command_text}")

# === ChatGPT reads Cole's replies ===
def read_cole_responses():
    if not os.path.exists(OUTBOX_FILE):
        print("[CHATGPT BRIDGE]: No replies from Cole yet.")
        return
    
    with open(OUTBOX_FILE, "r") as f:
        messages = json.load(f)
    
    for msg in messages:
        print(f"[COLE REPLY]: {msg['message']} ({msg['timestamp']})")

# === MAIN Test Block ===
if __name__ == "__main__":
    # 1. Send test command to Cole
    send_command_to_cole("Generate new RSI scanner bot")

    # 2. Run Cole's loop to process inbox
    cole_message_loop()

    # 3. Read Cole's reply from outbox
    read_cole_responses()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():