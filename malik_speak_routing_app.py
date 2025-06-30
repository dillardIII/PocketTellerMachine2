from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import uuid
import requests
from flask import Blueprint, request, jsonify, url_for

from assistants.malik import Malik

malik = Malik()
malik_speak_api = Blueprint('malik_speak_api', __name__)

# Environment keys
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
D_ID_API_KEY = os.getenv("D_ID_API_KEY")
MALIK_VOICE_ID = os.getenv("MALIK_VOICE_ID") or malik.voice_id
D_ID_AVATAR_ID = os.getenv("D_ID_AVATAR_ID")  # <- Use avatar_id for D-ID

@malik_speak_api.route('/malik_speak', methods=['POST'])
def malik_speak():
    try:
        data = request.get_json()
        text = data.get("text", "").strip()

        if not text:
            return jsonify({"status": "error", "message": "No input text provided."}), 400

        # === ElevenLabs Voice Generation ===
        voice_url = f"https://api.elevenlabs.io/v1/text-to-speech/{MALIK_VOICE_ID}"
        headers = {
            "xi-api-key": ELEVENLABS_API_KEY,
            "Content-Type": "application/json"
        }
        payload = {
            "text": text,
            "voice_settings": {
                "stability": 0.6,
                "similarity_boost": 0.75
            }
        }

        voice_response = requests.post(voice_url, headers=headers, json=payload)
        if voice_response.status_code != 200:
            return jsonify({
                "status": "error",
                "message": "Voice generation failed.",
                "details": voice_response.text
            }), 500

        # Save voice file locally
        os.makedirs("static/audio", exist_ok=True)
        filename = f"malik_{uuid.uuid4().hex}.mp3"
        audio_path = os.path.join("static/audio", filename)
        with open(audio_path, "wb") as f:
            f.write(voice_response.content)

        # Serve URL to client
        audio_url = url_for('serve_audio', filename=filename, _external=True)

        # === D-ID Animation using avatar_id ===
        did_url = "https://api.d-id.com/clips"
        did_headers = {
            "Authorization": f"Bearer {D_ID_API_KEY}",
            "Content-Type": "application/json"
        }
        did_payload = {
            "avatar_id": D_ID_AVATAR_ID,
            "script": {
                "type": "audio",
                "audio_url": audio_url,
                "provider": {"type": "elevenlabs"},
                "ssml": False
            }
        }

        did_response = requests.post(did_url, headers=did_headers, json=did_payload)
        if did_response.status_code != 200:
            return jsonify({
                "status": "error",
                "message": "D-ID animation failed.",
                "details": did_response.text
            }), 500

        clip_id = did_response.json().get("id")
        did_video_url = f"https://studio.d-id.com/player/{clip_id}"

        return jsonify({
            "status": "success",
            "audio_url": audio_url,
            "did_url": did_video_url
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Unexpected server error.",
            "exception": str(e)
        }), 500

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():