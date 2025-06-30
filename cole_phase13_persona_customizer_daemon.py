from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase13_persona_customizer_daemon.py

import os
import json
import time
from datetime import datetime
from flask import Flask, request, jsonify

# === Configurations ===
CUSTOM_PERSONAS_FILE = "data/cole_custom_personas.json"
CUSTOMIZER_LOG_FILE = "data/cole_persona_customizer_log.json"

# === Ensure data directory exists ===
os.makedirs("data", exist_ok=True)

# === Initialize if missing ===:
if not os.path.exists(CUSTOM_PERSONAS_FILE):
    with open(CUSTOM_PERSONAS_FILE, "w") as f:
        json.dump([], f, indent=2)

# === Logging Helper ===
def log_customizer_event(message):
    logs = []
    if os.path.exists(CUSTOMIZER_LOG_FILE):
        try:
            with open(CUSTOMIZER_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(CUSTOMIZER_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Flask API Server for Persona Customization ===
app = Flask(__name__)

@app.route('/api/add_persona', methods=['POST'])
def add_persona():
    data = request.get_json()
    name = data.get('name')
    style = data.get('style')
    emotion = data.get('emotion', 'neutral')

    if not name or not style:
        return jsonify({"status": "error", "message": "Missing name or style"}), 400

    try:
        with open(CUSTOM_PERSONAS_FILE, "r") as f:
            personas = json.load(f)

        new_persona = {"name": name, "style": style, "emotion": emotion}
        personas.append(new_persona)

        with open(CUSTOM_PERSONAS_FILE, "w") as f:
            json.dump(personas, f, indent=2)

        log_customizer_event(f"[NEW PERSONA]: {name} added with style '{style}' and emotion '{emotion}'")
        return jsonify({"status": "success", "message": f"Persona {name} added."})

    except Exception as e:
        log_customizer_event(f"[ERROR]: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/list_personas', methods=['GET'])
def list_personas():
    try:
        with open(CUSTOM_PERSONAS_FILE, "r") as f:
            personas = json.load(f)
        return jsonify({"personas": personas})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/remove_persona', methods=['POST'])
def remove_persona():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({"status": "error", "message": "Missing persona name"}), 400

    try:
        with open(CUSTOM_PERSONAS_FILE, "r") as f:
            personas = json.load(f)

        updated_personas = [p for p in personas if p["name"].lower() != name.lower()]:
:
        with open(CUSTOM_PERSONAS_FILE, "w") as f:
            json.dump(updated_personas, f, indent=2)

        log_customizer_event(f"[REMOVE PERSONA]: {name} removed.")
        return jsonify({"status": "success", "message": f"Persona {name} removed."})

    except Exception as e:
        log_customizer_event(f"[ERROR]: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

# === Run the daemon API ===
if __name__ == '__main__':
    print("[PERSONA CUSTOMIZER DAEMON]: Running on port 6060...")
    app.run(host='0.0.0.0', port=6060, debug=True)

def log_event():ef drop_files_to_bridge():