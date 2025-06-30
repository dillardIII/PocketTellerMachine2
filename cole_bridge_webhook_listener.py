from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from flask import Flask, request, jsonify
from datetime import datetime
from cole_code_writer import cole_write_code
from cole_command_interpreter import cole_interpret_command
from assistants.malik import malik_report

# === Setup Directories & Files ===
INBOX_FILE = "data/chatgpt_to_cole_inbox.json"
INBOX_DIR = "data/chatgpt_direct_inbox"
LOG_FILE = "data/cole_webhook_listener_log.json"
WEBHOOK_LOG_FILE = "data/cole_webhook_log.json"
COMMAND_QUEUE_FILE = "data/cole_command_queue.json"

os.makedirs("data", exist_ok=True)
os.makedirs(INBOX_DIR, exist_ok=True)

app = Flask(__name__)

# === Logging Helper ===
def log_event(message):
    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Webhook Logging ===
def log_webhook_event(message):
    logs = []
    if os.path.exists(WEBHOOK_LOG_FILE):
        try:
            with open(WEBHOOK_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(WEBHOOK_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Save Command to Queue ===
def queue_command(command):
    commands = []
    if os.path.exists(COMMAND_QUEUE_FILE):
        try:
            with open(COMMAND_QUEUE_FILE, "r") as f:
                commands = json.load(f)
        except:
            commands = []

    commands.append({
        "timestamp": datetime.now().isoformat(),
        "command": command
    })

    with open(COMMAND_QUEUE_FILE, "w") as f:
        json.dump(commands[-500:], f, indent=2)

    log_webhook_event(f"Queued command: {command}")
    malik_report(f"[Webhook] Command queued: {command}")

# === ChatGPT Direct Code Upload ===
@app.route('/chatgpt/code', methods=['POST'])
def receive_code():
    try:
        data = request.get_json()
        filename = data.get("filename")
        code = data.get("code")

        if not filename or not code:
            log_event("[ERROR]: Missing filename or code in /chatgpt/code")
            return jsonify({"error": "Missing filename or code"}), 400

        filepath = os.path.join(INBOX_DIR, filename)
        with open(filepath, "w") as f:
            f.write(code)

        log_event(f"[CHATGPT → COLE]: Received and saved code {filename}")
        return jsonify({"status": "received", "file": filename})
    except Exception as e:
        log_event(f"[ERROR]: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

# === ChatGPT Direct Command Execution ===
@app.route('/chatgpt/command', methods=['POST'])
def receive_command():
    try:
        data = request.get_json()
        command = data.get("command")

        if not command:
            log_event("[ERROR]: Missing command in /chatgpt/command")
            return jsonify({"error": "Missing command"}), 400

        result = cole_interpret_command(command)
        log_event(f"[CHATGPT → COLE]: Executed command → {command}")
        return jsonify({"status": "executed", "result": result})
    except Exception as e:
        log_event(f"[ERROR]: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

# === Universal Webhook Ingestor ===
@app.route('/cole_webhook', methods=['POST'])
def cole_webhook():
    data = request.json
    command = data.get("command")

    if not command:
        return jsonify({"status": "error", "message": "Missing 'command' field in request."}), 400

    queue_command(command)
    return jsonify({"status": "success", "message": f"Command '{command}' queued successfully."})

# === Inbox & Log Viewing ===
@app.route('/cole_webhook_inbox', methods=['GET'])
def view_inbox():
    if os.path.exists(INBOX_FILE):
        with open(INBOX_FILE, "r") as f:
            return jsonify(json.load(f))
    else:
        return jsonify({"message": "Inbox empty."})

@app.route('/cole_webhook_log', methods=['GET'])
def view_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return jsonify(json.load(f))
    else:
        return jsonify({"message": "No webhook logs yet."})

# === Health Check ===
@app.route('/status', methods=['GET'])
def status():
    return jsonify({"message": "Cole Webhook Ready", "timestamp": datetime.now().isoformat()})

# === Start Server ===
if __name__ == '__main__':
    print("[COLE BRIDGE WEBHOOK LISTENER]: Listening on port 5050...")
    app.run(host='0.0.0.0', port=5050, debug=True)