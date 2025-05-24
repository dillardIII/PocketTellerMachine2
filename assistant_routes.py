from flask import Blueprint, render_template, request, redirect, send_file
import os

assistant_routes = Blueprint("assistant_routes", __name__)

ASSISTANTS = {
    "mo_cash": {
        "id": "mo_cash",
        "name": "Mo Cash",
        "role": "The Hustler",
        "description": "Confident, fast-talking trader with big moves.",
        "avatar": "/static/avatars/mo_cash_avatar.png",
        "mood": "neutral"
    },
    "mentor": {
        "id": "mentor",
        "name": "Mentor",
        "role": "The Educator",
        "description": "Patient, wise, and focused on helping you grow.",
        "avatar": "/static/avatars/mentor_avatar.png",
        "mood": "neutral"
    },
    # Add more assistants here...
}

@assistant_routes.route("/assistant_profile/<id>")
def assistant_profile(id):
    assistant = ASSISTANTS.get(id)
    if assistant:
        return render_template("assistant_profile.html", assistant=assistant)
    return "Assistant not found", 404

@assistant_routes.route("/set_mood/<id>", methods=["POST"])
def set_mood(id):
    mood = request.form.get("mood")
    if id in ASSISTANTS:
        ASSISTANTS[id]["mood"] = mood
    return redirect(f"/assistant_profile/{id}")

@assistant_routes.route("/assign_assistant/<id>", methods=["POST"])
def assign_assistant(id):
    print(f"Assigned assistant: {id}")
    return redirect(f"/assistant_profile/{id}")

@assistant_routes.route("/get_voice/<id>")
def get_voice(id):
    assistant = ASSISTANTS.get(id)
    if not assistant:
        return "Assistant not found", 404

    mood = assistant.get("mood", "neutral")
    voice_path = f"static/voices/{id}/{mood}.mp3"

    if os.path.exists(voice_path):
        return send_file(voice_path, mimetype="audio/mpeg")
    else:
        fallback_path = f"static/voices/{id}/neutral.mp3"
        if os.path.exists(fallback_path):
            return send_file(fallback_path, mimetype="audio/mpeg")
        return "Voice file not found", 404

# === Mood Autoupdate Based on Trade Outcome ===
def update_mood_by_trade(id, result):
    """
    Updates mood for assistant based on trade result.
    result = "win", "small_win", "even", "small_loss", "loss", "streak_loss"
    """
    if id not in ASSISTANTS:
        return

    mood = "neutral"
    if result == "win":
        mood = "hyped"
    elif result == "small_win":
        mood = "positive"
    elif result == "even":
        mood = "calm"
    elif result == "small_loss":
        mood = "serious"
    elif result == "loss":
        mood = "strict"
    elif result == "streak_loss":
        mood = "shadow"

    ASSISTANTS[id]["mood"] = mood