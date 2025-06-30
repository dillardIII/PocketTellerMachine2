from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: voice_upload_endpoint.py ===
# 🔊 Voice Upload Endpoint – Accepts MP3 files for assistant previews

from flask import Blueprint, request, jsonify
import os

voice_upload_endpoint = Blueprint('voice_upload_endpoint', __name__)

UPLOAD_FOLDER = "voices"

@voice_upload_endpoint.route("/upload_voice", methods=["POST"])
def upload_voice():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    return jsonify({"message": f"Voice file saved: {file.filename}"}), 200

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():