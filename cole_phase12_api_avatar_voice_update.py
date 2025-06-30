from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase12_api_avatar_voice_update.py

from flask import Blueprint, request, jsonify
import os
import json
from datetime import datetime

# === Blueprint(for Avatar & Voice Management ===)
avatar_voice_api = Blueprint('avatar_voice_api', __name__)

# === Paths ===
AVATAR_VOICE_FILE = "data/cole_persona_avatar_voice.json"
os.makedirs("data", exist_ok=True)

# === Load or create file ===
def load_avatar_voice_data():
    if not os.path.exists(AVATAR_VOICE_FILE):
        return {}
    try:
        with open(AVATAR_VOICE_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

# === API to update persona avatar and voice ===
@avatar_voice_api.route('/api/update_persona_avatar_voice', methods=['POST'])
def update_persona_avatar_voice():
    try:
        data = request.get_json()
        persona_name = data.get("persona_name")
        avatar_url = data.get("avatar_url")
        avatar_style = data.get("avatar_style", "default")
        voice_id = data.get("voice_id")

        if not persona_name or not avatar_url or not voice_id:
            return jsonify({"status": "error", "message": "Missing persona_name, avatar_url, or voice_id."}), 400

        av_data = load_avatar_voice_data()
        av_data[persona_name] = {
            "avatar_url": avatar_url,
            "avatar_style": avatar_style,
            "voice_id": voice_id,
            "updated": datetime.now().isoformat()
        }

        with open(AVATAR_VOICE_FILE, "w") as f:
            json.dump(av_data, f, indent=2)

        return jsonify({"status": "success", "message": f"{persona_name} avatar & voice updated."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():