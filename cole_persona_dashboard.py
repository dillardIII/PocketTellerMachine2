# cole_persona_dashboard.py

from flask import Flask, render_template, jsonify, request
import os
import json
from datetime import datetime

app = Flask(__name__, template_folder='templates')

MOOD_STATE_FILE = "data/mood_state.json"
AVATAR_STATE_FILE = "data/avatar_state.json"
VOICE_STATE_FILE = "data/voice_state.json"
PERSONA_LOG_FILE = "data/persona_interaction_log.json"

os.makedirs("data", exist_ok=True)

# === Load States ===
def load_state(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                return json.load(f)
            except:
                return {}
    return {}

# === Log Interaction ===
def log_interaction(message):
    logs = []
    if os.path.exists(PERSONA_LOG_FILE):
        with open(PERSONA_LOG_FILE, "r") as f:
            try:
                logs = json.load(f)
            except:
                logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(PERSONA_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Persona Dashboard UI ===
@app.route("/")
def persona_dashboard():
    mood_state = load_state(MOOD_STATE_FILE)
    avatar_state = load_state(AVATAR_STATE_FILE)
    voice_state = load_state(VOICE_STATE_FILE)
    return render_template("cole_persona_dashboard.html",
                           mood_state=mood_state,
                           avatar_state=avatar_state,
                           voice_state=voice_state)

# === API to refresh states ===
@app.route("/api/persona_status", methods=["GET"])
def persona_status():
    return jsonify({
        "mood_state": load_state(MOOD_STATE_FILE),
        "avatar_state": load_state(AVATAR_STATE_FILE),
        "voice_state": load_state(VOICE_STATE_FILE)
    })

# === API to simulate user input ===
@app.route("/api/update_persona", methods=["POST"])
def update_persona():
    data = request.get_json()
    persona = data.get("persona")
    mood = data.get("mood")
    voice = data.get("voice_style")
    avatar = data.get("avatar")

    if persona:
        if mood:
            mood_state = load_state(MOOD_STATE_FILE)
            mood_state[persona] = mood
            with open(MOOD_STATE_FILE, "w") as f:
                json.dump(mood_state, f, indent=2)
            log_interaction(f"[MOOD UPDATE]: {persona} mood set to {mood}")

        if voice:
            voice_state = load_state(VOICE_STATE_FILE)
            voice_state[persona] = voice
            with open(VOICE_STATE_FILE, "w") as f:
                json.dump(voice_state, f, indent=2)
            log_interaction(f"[VOICE UPDATE]: {persona} voice style set to {voice}")

        if avatar:
            avatar_state = load_state(AVATAR_STATE_FILE)
            avatar_state[persona] = avatar
            with open(AVATAR_STATE_FILE, "w") as f:
                json.dump(avatar_state, f, indent=2)
            log_interaction(f"[AVATAR UPDATE]: {persona} avatar changed to {avatar}")

    return jsonify({"status": "ok", "message": "Persona updated"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5051, debug=True)