from ghost_env import INFURA_KEY, VAULT_ADDRESS
from flask import Blueprint, jsonify, request
import os, json

avatar_voice_bp = Blueprint('avatar_voice', __name__)

AVATAR_VOICE_FILE = "data/avatar_voice_profiles.json"
os.makedirs("data", exist_ok=True)

# === Load or create default file ===
if not os.path.exists(AVATAR_VOICE_FILE):
    with open(AVATAR_VOICE_FILE, "w") as f:
        json.dump([], f, indent=2)

def load_profiles():
    with open(AVATAR_VOICE_FILE, "r") as f:
        return json.load(f)

def save_profiles(profiles):
    with open(AVATAR_VOICE_FILE, "w") as f:
        json.dump(profiles, f, indent=2)

# === API: Get all profiles ===
@avatar_voice_bp.route('/api/avatars', methods=['GET'])
def get_avatars():
    return jsonify(load_profiles())

# === API: Add new profile ===
@avatar_voice_bp.route('/api/avatars', methods=['POST'])
def add_avatar():
    try:
        data = request.get_json()
        profiles = load_profiles()
        profiles.append(data)
        save_profiles(profiles)
        return jsonify({"status": "success", "message": "Avatar profile added."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# === API: Delete profile by name ===
@avatar_voice_bp.route('/api/avatars/<name>', methods=['DELETE'])
def delete_avatar(name):
    try:
        profiles = load_profiles()
        profiles = [p for p in profiles if p.get("name") != name]:
        save_profiles(profiles)
        return jsonify({"status": "success", "message": f"Avatar '{name}' deleted."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def log_event():ef drop_files_to_bridge():