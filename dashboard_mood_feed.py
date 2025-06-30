from ghost_env import INFURA_KEY, VAULT_ADDRESS
from flask import Blueprint, jsonify
import os
import json
from datetime import datetime

dashboard_mood_feed_bp = Blueprint('dashboard_mood_feed', __name__)

MOOD_FEED_FILE = "data/mood_feed.json"

# === Get Mood Feed API ===
@dashboard_mood_feed_bp.route('/api/get_mood_feed', methods=['GET'])
def get_mood_feed():
    if not os.path.exists(MOOD_FEED_FILE):
        return jsonify([])

    try:
        with open(MOOD_FEED_FILE, "r") as f:
            mood_data = json.load(f)
    except Exception as e:
        print(f"[Mood Feed] Error loading file: {e}")
        mood_data = []

    # Return the latest 50 entries
    return jsonify(mood_data[-50:])

# === Add Mood Entry Helper ===
def log_mood_entry(persona, mood, quote):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "persona": persona,
        "mood": mood,
        "quote": quote
    }

    mood_data = []
    if os.path.exists(MOOD_FEED_FILE):
        try:
            with open(MOOD_FEED_FILE, "r") as f:
                mood_data = json.load(f)
        except Exception as e:
            print(f"[Mood Feed] Error reading mood file: {e}")

    mood_data.append(entry)

    try:
        with open(MOOD_FEED_FILE, "w") as f:
            json.dump(mood_data, f, indent=2)
    except Exception as e:
        print(f"[Mood Feed] Error writing mood file: {e}")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():