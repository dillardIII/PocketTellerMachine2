# === FILE: voice_router.py ===
# 🧠 PTM Voice Router – Handles assistant voice selection, mood routing, and playback targeting

import os
import json
import random
from flask import Blueprint, request, jsonify
from utils.logger import log_event
from mood_engine import get_mood

voice_router = Blueprint('voice_router', __name__)

VOICE_CONFIG_PATH = "vault/voice_settings.json"

# === Mood-based voice map ===
VOICE_MAP = {
    "neutral": ["mentor_voice_1", "strategist_voice_1"],
    "win": ["mo_cash_voice", "drill_voice"],
    "loss": ["mentor_voice_2", "optimist_voice"],
    "error": ["shadow_voice", "drill_voice"],
    "launch": ["hype_mode_voice", "og_voice"]
}

# === Load or initialize voice config
def load_voice_config():
    if os.path.exists(VOICE_CONFIG_PATH):
        with open(VOICE_CONFIG_PATH, "r") as f:
            return json.load(f)
    return {"selected": "amandamask"}

def save_voice_config(config):
    with open(VOICE_CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)

# === ROUTE: Select voice manually (overrides mood routing)
@voice_router.route("/api/voice/choose", methods=["POST"])
def choose_voice():
    data = request.get_json()
    if not data or "voice" not in data:
        return jsonify({"error": "Missing 'voice' field."}), 400

    config = load_voice_config()
    config["selected"] = data["voice"]
    save_voice_config(config)

    log_event("Voice Selected", {"voice": data["voice"]})
    return jsonify({"status": "ok", "message": f"Voice '{data['voice']}' selected!"})

# === ROUTE: Get currently selected voice
@voice_router.route("/api/voice/active", methods=["GET"])
def get_active_voice():
    config = load_voice_config()
    return jsonify({"selected_voice": config.get("selected", "amandamask")})

# === LOGIC: Pick a voice based on mood or manual override
def pick_voice(state_override=None):
    mood = get_mood()
    state = state_override or mood.get("state", "neutral")
    voice_options = VOICE_MAP.get(state, VOICE_MAP["neutral"])
    chosen = random.choice(voice_options)
    print(f"[VoiceRouter] 🎙️ Selected voice for state '{state}': {chosen}")
    return chosen