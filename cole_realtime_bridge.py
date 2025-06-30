from ghost_env import INFURA_KEY, VAULT_ADDRESS
from flask import Flask, request, jsonify
from datetime import datetime
import os
import json

# === Files for Inbox and Outbox ===
INBOX_FILE = "data/cole_inbox.json"
OUTBOX_FILE = "data/cole_outbox.json"

# === Initialize Flask App ===
app = Flask(__name__)

# === Cole receives and logs command ===
@app.route("/bridge/send_to_cole", methods=["POST"])
def send_to_cole():
    data = request.get_json()
    command_text = data.get("command", "")

    if not command_text:
        return jsonify({"status": "error", "message": "Missing command."}), 400

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

    print(f"[BRIDGE API]: Sent to Cole → {command_text}")
    return jsonify({"status": "success", "message": f"Command sent to Cole: {command_text}"})


# === Cole reads and replies ===
@app.route("/bridge/check_cole_replies", methods=["GET"])
def check_cole_replies():
    if not os.path.exists(OUTBOX_FILE):
        return jsonify({"status": "ok", "replies": [], "message": "No replies yet."})

    with open(OUTBOX_FILE, "r") as f:
        messages = json.load(f)

    return jsonify({"status": "ok", "replies": messages})


# === Cole processes the inbox like a listener ===
@app.route("/bridge/cole_loop", methods=["GET"])
def cole_loop():
    if not os.path.exists(INBOX_FILE):
        return jsonify({"status": "ok", "message": "No messages in inbox."})

    with open(INBOX_FILE, "r") as f:
        inbox = json.load(f)

    if not inbox:
        return jsonify({"status": "ok", "message": "Inbox empty."})

    outbox = []
    for msg in inbox:
        cmd = msg.get("command", "")
        print(f"[COLE BRIDGE RECEIVED]: {cmd}")
        if "generate" in cmd.lower():
            outbox.append(f"Generated code for: {cmd}")
        elif "status" in cmd.lower():
            outbox.append("Cole is online and healthy.")
        else:
            outbox.append(f"Unknown command received: {cmd}")

    # Save to outbox
    if os.path.exists(OUTBOX_FILE):
        with open(OUTBOX_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    for message in outbox:
        logs.append({
            "from": "Cole",
            "message": message,
            "timestamp": datetime.now().isoformat()
        })

    with open(OUTBOX_FILE, "w") as f:
        json.dump(logs, f, indent=2)

    # Clear inbox
    open(INBOX_FILE, "w").write("[]")

    return jsonify({"status": "success", "processed": outbox})


# === Run API Bridge ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6060, debug=True)

def log_event():ef drop_files_to_bridge():