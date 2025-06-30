from ghost_env import INFURA_KEY, VAULT_ADDRESS
from flask import Blueprint, jsonify
import os

dashboard_voice_previews_bp = Blueprint('dashboard_voice_previews', __name__)

@dashboard_voice_previews_bp.route('/api/voice_previews', methods=['GET'])
def get_voice_previews():
    try:
        base_path = os.path.join('static', 'voices')
        previews = {"male": [], "female": []}

        for gender in ["male", "female"]:
            folder = os.path.join(base_path, gender)
            if os.path.exists(folder):
                for file in os.listdir(folder):
                    if file.endswith(".mp3"):
                        previews[gender].append({
                            "filename": file,
                            "gender": gender,
                            "url": f"/static/voices/{gender}/{file}"
                        })

        return jsonify({"previews": previews})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def log_event():ef drop_files_to_bridge():