from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import requests
from flask import Blueprint, request, jsonify

did_routes = Blueprint('did_routes', __name__)

DID_API_KEY = os.getenv("DID_API_KEY")
DID_AVATAR_ID = os.getenv("DID_AVATAR_ID")

@did_routes.route("/create_did_video", methods=["POST"])
def create_did_video():
    try:
        text = request.json.get("text")
        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Upload audio to D-ID
        audio_path = "malik_output.mp3"
        with open(audio_path, "rb") as audio_file:
            audio_data = audio_file.read()

        upload_url = "https://api.d-id.com/audios"
        headers = {
            "Authorization": f"Bearer {DID_API_KEY}",
            "Content-Type": "audio/mpeg"
        }
        upload_response = requests.post(upload_url, headers=headers, data=audio_data)
        if upload_response.status_code != 200:
            return jsonify({"error": "Audio upload failed", "details": upload_response.text}), 400

        audio_url = upload_response.json().get("url")

        # Now generate video using uploaded audio and avatar
        video_url = "https://api.d-id.com/talks"
        payload = {
            "script": {
                "type": "audio",
                "audio_url": audio_url
            },
            "source_url": f"https://studio.d-id.com/avatars/{DID_AVATAR_ID}"
        }
        headers["Content-Type"] = "application/json"

        video_response = requests.post(video_url, headers=headers, json=payload)
        if video_response.status_code != 200:
            return jsonify({"error": "Video creation failed", "details": video_response.text}), 400

        video_data = video_response.json()
        return jsonify({"success": True, "video_url": video_data.get("result_url")})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def log_event():ef drop_files_to_bridge():