from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: persona_voice_preview_route.py ===

from flask import Blueprint, request, jsonify, send_from_directory
import os

voice_preview_bp = Blueprint("voice_preview_bp", __name__)

VOICE_FOLDER = "static/voice_previews"

# === Serve voice preview MP3s ===
@voice_preview_bp.route("/voice_previews/<filename>")
def serve_voice_preview(filename):
    return send_from_directory(VOICE_FOLDER, filename)

# === List available voice previews ===
@voice_preview_bp.route("/api/voice_previews")
def list_voice_previews():
    if not os.path.exists(VOICE_FOLDER):
        return jsonify([])

    files = [f for f in os.listdir(VOICE_FOLDER) if f.endswith(".mp3")]:
    return jsonify(files)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():