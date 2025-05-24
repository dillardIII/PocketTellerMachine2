import os
import json
from flask import Flask, request, jsonify
from voice_command_processor import process_voice_command
from datetime import datetime

VOICE_API_LOG_FILE = "data/voice_command_api_log.json"

# === Logging Helper ===
def log_api_request(phrase, result):
    logs = []
    if os.path.exists(VOICE_API_LOG_FILE):
        try:
            with open(VOICE_API_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append({
        "timestamp": datetime.now().isoformat(),
        "phrase": phrase,
        "result": result
    })

    with open(VOICE_API_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

    print(f"[Voice API] Logged: {phrase}")

# === Flask App ===
app = Flask(__name__)

@app.route("/voice_command", methods=["POST"])
def voice_command():
    data = request.json
    phrase = data.get("phrase")

    if not phrase:
        return jsonify({"status": "error", "message": "Missing 'phrase' in request."}), 400

    print(f"[Voice API] Received phrase: {phrase}")
    result = process_voice_command(phrase)

    log_api_request(phrase, result)

    return jsonify({
        "status": "success",
        "phrase": phrase,
        "result": result
    })

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"message": "Voice Command API is up", "timestamp": datetime.now().isoformat()})

# === Start Server ===
if __name__ == "__main__":
    print("[Voice API] Listening on port 7070...")
    app.run(host="0.0.0.0", port=7070, debug=True)