# cole_smart_feedback_responder_handler.py

import os
import json
import time
from datetime import datetime
import requests
from flask import Flask, request, jsonify
import threading

# === Config ===
FEEDBACK_LOG_FILE = "data/chatgpt_feedback_log.json"
SMART_FEEDBACK_LOG_FILE = "data/smart_feedback_responder_log.json"
COLE_WEBHOOK_URL = "http://localhost:5050/cole_webhook"
CHECK_INTERVAL = 300  # 5 minutes

# === Ensure data folder ===
os.makedirs("data", exist_ok=True)

# === Logging ===
def log_feedback_response(message):
    logs = []
    if os.path.exists(SMART_FEEDBACK_LOG_FILE):
        try:
            with open(SMART_FEEDBACK_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(SMART_FEEDBACK_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load Feedback Inbox ===
def load_feedback():
    if os.path.exists(FEEDBACK_LOG_FILE):
        try:
            with open(FEEDBACK_LOG_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

# === Process Feedback Entry ===
def process_feedback_entry(entry):
    feedback_text = entry.get("feedback", "")
    if not feedback_text:
        return

    # Detect UPLOAD_CODE pattern in feedback
    if "UPLOAD_CODE" in feedback_text:
        try:
            filename = feedback_text.split("filename='")[1].split("'")[0]
            code = feedback_text.split("code='''")[1].split("'''")[0]
            print(f"[SMART FEEDBACK]: Executing uploaded code → {filename}")
            send_command_to_cole(f"UPLOAD_CODE filename='{filename}' code='''{code}'''")
            log_feedback_response(f"[SMART FEEDBACK]: Code executed from feedback → {filename}")
        except Exception as e:
            log_feedback_response(f"[SMART FEEDBACK ERROR]: Failed to parse code block → {e}")
    else:
        print(f"[SMART FEEDBACK]: No code detected in feedback → {feedback_text[:100]}")
        log_feedback_response(f"[SMART FEEDBACK]: Feedback ignored (no code): {feedback_text[:100]}")

# === Send command to Cole ===
def send_command_to_cole(command):
    try:
        response = requests.post(COLE_WEBHOOK_URL, json={"command": command})
        if response.ok:
            print(f"[SMART FEEDBACK]: Command sent successfully.")
        else:
            print(f"[SMART FEEDBACK ERROR]: Failed to send command. Status: {response.status_code}")
    except Exception as e:
        print(f"[SMART FEEDBACK ERROR]: {e}")

# === Daemon Loop ===
def smart_feedback_responder_loop():
    print("[SMART FEEDBACK RESPONDER DAEMON]: Running (autonomous)...")
    processed_ids = set()

    while True:
        try:
            feedback_list = load_feedback()
            for entry in feedback_list:
                entry_id = entry.get("id") or entry.get("timestamp") or str(entry)
                if entry_id not in processed_ids:
                    process_feedback_entry(entry)
                    processed_ids.add(entry_id)
        except Exception as e:
            log_feedback_response(f"[ERROR]: {e}")
            print(f"[SMART FEEDBACK ERROR]: {e}")

        time.sleep(CHECK_INTERVAL)

# === Flask Webhook Listener ===
app = Flask(__name__)

@app.route('/chatgpt_feedback', methods=['POST'])
def receive_feedback_and_respond():
    try:
        data = request.get_json()
        feedback = data.get("feedback")

        if not feedback:
            log_feedback_response("[ERROR]: Missing feedback.")
            return jsonify({"status": "error", "message": "Missing feedback field."}), 400

        print(f"[RESPONDER]: Received feedback: {feedback}")
        process_feedback_entry({"feedback": feedback})
        return jsonify({"status": "success", "message": "Feedback processed."})
    except Exception as e:
        log_feedback_response(f"[ERROR]: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/chatgpt_feedback_responses_log', methods=['GET'])
def view_feedback_response_log():
    if os.path.exists(SMART_FEEDBACK_LOG_FILE):
        with open(SMART_FEEDBACK_LOG_FILE, "r") as f:
            return jsonify(json.load(f))
    else:
        return jsonify({"message": "No feedback responses logged yet."})

# === Launch Daemon and Webhook Server Together ===
def launch_all():
    # Launch daemon in background thread
    threading.Thread(target=smart_feedback_responder_loop, daemon=True).start()
    # Launch Flask webhook server
    print("[SMART FEEDBACK RESPONDER]: Listening on port 7000 (webhook) and autonomous loop running...")
    app.run(host='0.0.0.0', port=7000, debug=True)

if __name__ == "__main__":
    launch_all()