# cole_persona_custom_mood_trigger_api.py

from flask import Flask, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)
PERSONA_FILE = "data/persona_registry.json"
TRIGGER_LOG_FILE = "data/persona_custom_mood_trigger_log.json"

# === Ensure data dir ===
os.makedirs("data", exist_ok=True)

# === Load personas ===
def load_personas():
    if os.path.exists(PERSONA_FILE):
        with open(PERSONA_FILE, "r") as f:
            return json.load(f)
    return []

# === Save personas ===
def save_personas(personas):
    with open(PERSONA_FILE, "w") as f:
        json.dump(personas, f, indent=2)

# === Logging ===
def log_trigger_event(message):
    logs = []
    if os.path.exists(TRIGGER_LOG_FILE):
        try:
            with open(TRIGGER_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(TRIGGER_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === API ===
@app.route('/api/trigger_persona_mood', methods=['POST'])
def trigger_persona_mood():
    try:
        data = request.get_json()
        name = data.get('name')
        mood = data.get('mood')
        voice = data.get('voice')

        if not name or not mood or not voice:
            return jsonify({"status": "error", "message": "Missing name, mood, or voice."}), 400

        personas = load_personas()
        found = False
        for p in personas:
            if p.get('name', '').lower() == name.lower():
                p['mood'] = mood
                p['voice'] = voice
                found = True
                log_trigger_event(f"[TRIGGER]: {name} → Mood: {mood} | Voice: {voice}")
                break

        if not found:
            return jsonify({"status": "error", "message": f"Persona '{name}' not found."}), 404

        save_personas(personas)
        return jsonify({"status": "success", "message": f"{name} mood and voice updated to {mood}, {voice}."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5100, debug=True)