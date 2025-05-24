# chatgpt_feedback_listener.py

from flask import Flask, request, jsonify
import os
import json
from datetime import datetime
import requests
import time

FEEDBACK_LOG_FILE = "data/chatgpt_feedback_log.json"
COLE_WEBHOOK_URL = "http://localhost:5050/cole_webhook"
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Ensure you set this securely in your environment

# === Ensure data folder ===
os.makedirs("data", exist_ok=True)

# === Flask Setup ===
app = Flask(__name__)

# === Logging functions ===
def log_feedback_entry(data):
    logs = []
    if os.path.exists(FEEDBACK_LOG_FILE):
        try:
            with open(FEEDBACK_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append(data)
    with open(FEEDBACK_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

def log_feedback_text(message):
    logs = []
    if os.path.exists(FEEDBACK_LOG_FILE):
        try:
            with open(FEEDBACK_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "feedback": message
    })
    with open(FEEDBACK_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Generate code from ChatGPT ===
def generate_code_from_chatgpt(prompt):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are a self-healing trading bot code generator."},
            {"role": "user", "content": f"Based on the following request: {prompt}, generate Python code to improve the system."}
        ],
        "max_tokens": 500
    }
    response = requests.post(OPENAI_API_URL, headers=headers, json=data)
    response.raise_for_status()
    result = response.json()
    code = result['choices'][0]['message']['content']
    return code.strip()

# === Send code to Cole ===
def send_code_to_cole(code_content):
    filename = f"chatgpt_generated_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
    payload = {
        "command": f"UPLOAD_CODE filename='{filename}' code='''{code_content}'''"
    }
    response = requests.post(COLE_WEBHOOK_URL, json=payload)
    if response.ok:
        print(f"[CHATGPT_FEEDBACK_RESPONDER]: Code sent to Cole successfully → {filename}")
    else:
        print(f"[CHATGPT_FEEDBACK_RESPONDER ERROR]: {response.status_code} - {response.text}")

# === Webhook ===
@app.route('/chatgpt_feedback', methods=['POST'])
def receive_feedback():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing payload"}), 400

        if "feedback" in data:
            feedback = data.get("feedback")
            log_feedback_text(feedback)
            print(f"[COLE → CHATGPT]: Feedback received → {feedback}")

            # Auto-generate code
            generated_code = generate_code_from_chatgpt(feedback)
            print(f"[CHATGPT GENERATED CODE]:\n{generated_code[:100]}...")

            # Send to Cole
            send_code_to_cole(generated_code)

            return jsonify({"status": "received", "message": "Code generated and sent to Cole."})
        else:
            # Fallback if just logging extended data
            data["received_at"] = datetime.now().isoformat()
            log_feedback_entry(data)
            print(f"[FEEDBACK RECEIVED]: {json.dumps(data, indent=2)}")
            return jsonify({"status": "feedback_received", "received": data})

    except Exception as e:
        log_feedback_text(f"[ERROR]: {str(e)}")
        print(f"[FEEDBACK LISTENER ERROR]: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

# === View logs ===
@app.route('/chatgpt_feedback/logs', methods=['GET'])
def view_feedback_logs():
    if os.path.exists(FEEDBACK_LOG_FILE):
        with open(FEEDBACK_LOG_FILE, "r") as f:
            return jsonify(json.load(f))
    else:
        return jsonify({"message": "No feedback logged yet."})

# === Optional simulated daemon loop ===
def feedback_listener_daemon_loop():
    print("[CHATGPT FEEDBACK LISTENER DAEMON]: Running simulated mode...")
    while True:
        print("[Daemon]: Waiting for ChatGPT feedback... (simulated)")
        time.sleep(300)

if __name__ == "__main__":
    print("[CHATGPT FEEDBACK LISTENER]: Starting listener on port 6000...")
    app.run(host='0.0.0.0', port=6000, debug=True)
    # Uncomment to enable simulation when running standalone:
    # feedback_listener_daemon_loop()