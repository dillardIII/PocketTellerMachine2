# === FILE: drop_auto_evolver_builder.py ===
# 🚀 PTM Drop Auto Evolver Builder (HTML + API + Voice Mutation)
# Builds full Flask apps with HTML + API + voice integration.

import json
import time
from datetime import datetime
import os

VOTES_FILE = "ghost_council_votes.json"
BUILD_QUEUE_FILE = "build_queue.json"
LOGBOOK_FILE = "vault_logbook.txt"
VOICE_FILE = "GhostVoids.ctrl.json"

def load_votes():
    try:
        with open(VOTES_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def load_voice_config():
    try:
        with open(VOICE_FILE, "r") as f:
            data = json.load(f)
        return data.get("voices_on", False), data.get("intensity", 0.5)
    except FileNotFoundError:
        return False, 0.0

def speak(message, intensity):
    bar = "!" * int(intensity * 10)
    print(f"[VOICE] {bar} {message} {bar}")

def log_action(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGBOOK_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def build_flask_app(app_name, voices_on, intensity):
    folder_name = f"{app_name}_app"
    os.makedirs(folder_name, exist_ok=True)
    file_name = f"{folder_name}/app.py"
    template_dir = f"{folder_name}/templates"
    static_dir = f"{folder_name}/static/css"
    os.makedirs(template_dir, exist_ok=True)
    os.makedirs(static_dir, exist_ok=True)

    # === index.html ===
    index_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{app_name} Dashboard</title>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
</head>
<body>
    <h1>🚀 {app_name} Dashboard</h1>
    <p>This is an auto-evolved app with HTML, API, and voice integration.</p>
</body>
</html>
"""
    with open(f"{template_dir}/index.html", "w") as f:
        f.write(index_content)

    # === style.css ===
    css_content = """
body { font-family: Arial, sans-serif; background: #111; color: #eee; text-align: center; padding: 2em; }
h1 { color: #0f0; }
"""
    with open(f"{static_dir}/style.css", "w") as f:
        f.write(css_content)

    # === app.py ===
    flask_content = f"""
# === FILE: {file_name} ===
# Auto-generated Flask app for {app_name} with HTML + API + Voice.

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/data")
def api_data():
    return jsonify({{"app": "{app_name}", "status": "running", "features": ["HTML", "API", "Voice"]}})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
"""
    with open(file_name, "w") as f:
        f.write(flask_content)

    log_action(f"AutoEvolver built full Flask app: {file_name} with HTML + API + Voice")
    print(f"[AutoEvolver] 🧬 Created {app_name} Flask app with HTML + API + Voice")
    if voices_on:
        speak(f"{app_name} app is built and ready.", intensity)
    return f"python {file_name}"

def push_to_build_queue(commands):
    try:
        with open(BUILD_QUEUE_FILE, "r") as f:
            current_queue = json.load(f)
    except FileNotFoundError:
        current_queue = []
    current_queue.extend(commands)
    with open(BUILD_QUEUE_FILE, "w") as f:
        json.dump(current_queue, f, indent=4)
    log_action(f"Queued for execution: {commands}")
    print(f"[AutoEvolver] ➕ Added to build_queue.json: {commands}")

def clear_votes():
    with open(VOTES_FILE, "w") as f:
        json.dump([], f)

def main():
    print("[AutoEvolver] 🚀 Starting Drop Auto Evolver Builder with HTML + API + Voice...")
    while True:
        votes = load_votes()
        voices_on, intensity = load_voice_config()
        if votes:
            commands = []
            for app_name in votes:
                command = build_flask_app(app_name, voices_on, intensity)
                commands.append(command)
            push_to_build_queue(commands)
            clear_votes()
        time.sleep(10)

if __name__ == "__main__":
    main()