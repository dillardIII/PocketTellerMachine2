from flask import Blueprint, request, jsonify
import os
import json
from datetime import datetime

dashboard_mood_logger_bp = Blueprint('dashboard_mood_logger', __name__)

MOOD_FEED_FILE = "data/mood_feed.json"

# === API to Log Mood Entry ===
@dashboard_mood_logger_bp.route('/api/log_mood_entry', methods=['POST'])
def log_mood_entry_api():
    try:
        data = request.get_json()
        persona = data.get('persona')
        mood = data.get('mood')
        quote = data.get('quote')

        if not (persona and mood and quote):
            return jsonify({"status": "error", "message": "Missing persona, mood, or quote"}), 400

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
                print(f"[Mood Logger] Error reading file: {e}")

        mood_data.append(entry)

        try:
            with open(MOOD_FEED_FILE, "w") as f:
                json.dump(mood_data, f, indent=2)
        except Exception as e:
            print(f"[Mood Logger] Error writing file: {e}")
            return jsonify({"status": "error", "message": "Failed to save mood entry"}), 500

        return jsonify({"status": "success", "message": "Mood entry logged successfully"})

    except Exception as e:
        print(f"[Mood Logger] Unexpected error: {e}")
        return jsonify({"status": "error", "message": "Unexpected error occurred"}), 500

# === Mood Entry Logging API (Alternative Endpoint) ===
@dashboard_mood_logger_bp.route('/api/log_mood_entry_alt', methods=['POST'])
def log_mood_entry_alt():
    try:
        data = request.get_json()
        persona = data.get('persona')
        mood = data.get('mood')
        quote = data.get('quote')

        if not persona or not mood or not quote:
            return jsonify({"status": "error", "message": "Missing persona, mood, or quote"}), 400

        entry = {
            "timestamp": datetime.now().isoformat(),
            "persona": persona,
            "mood": mood,
            "quote": quote
        }

        mood_data = []
        if os.path.exists(MOOD_FEED_FILE):
            with open(MOOD_FEED_FILE, "r") as f:
                mood_data = json.load(f)

        mood_data.append(entry)

        with open(MOOD_FEED_FILE, "w") as f:
            json.dump(mood_data, f, indent=2)

        return jsonify({"status": "success", "message": "Mood entry logged."})

    except Exception as e:
        print(f"[Mood Logger] Error logging mood entry: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500