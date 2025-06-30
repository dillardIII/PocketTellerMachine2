# cole_phase14_persona_voice_avatar_dashboard.py

from flask import Flask, render_template_string, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
AVATAR_VISUALS_FILE = "data/avatar_visual_styles.json"

# === Load Mood & Visual Data ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        with open(MOOD_STATE_FILE, "r") as f:
            return json.load(f)
    return {}

def load_avatar_styles():
    if os.path.exists(AVATAR_VISUALS_FILE):
        with open(AVATAR_VISUALS_FILE, "r") as f:
            return json.load(f)
    return {}

# === Web UI ===
@app.route('/')
def live_persona_dashboard():
    mood_state = load_mood_state()
    avatar_styles = load_avatar_styles()

    html = """
    <html>
    <head>
    <title>Persona Voice & Avatar Dashboard</title>
    <style>
        body { font-family: Arial; background: #111; color: #ddd; text-align: center; }
        .card { display: inline-block; background: #222; margin: 20px; padding: 20px; border-radius: 12px; box-shadow: 0 0 12px #444; }
        img { width: 120px; height: 120px; border-radius: 50%; }
        h2 { color: #6fd672; }
    </style>
    </head>
    <body>
    <h1>Persona Voice & Avatar Dashboard</h1>
    <div>
    """

    for persona, mood in mood_state.items():
        style_key = f"{persona}_{mood}"
        avatar_data = avatar_styles.get(style_key, avatar_styles.get(f"{persona}_neutral", {"avatar": "default_avatar.png", "style": "neutral"}))
        avatar_img = avatar_data.get("avatar", "default_avatar.png")
        style = avatar_data.get("style", "neutral")
        html += f"""
        <div class="card">
            <h2>{persona}</h2>
            <img src="/static/avatars/{avatar_img}">
            <p>Mood: {mood}</p>
            <p>Style: {style}</p>
        </div>
        """

    html += """
    </div>
    <footer><small>Updated: """ + datetime.now().isoformat() + """</small></footer>
    </body>
    </html>
    """
    return html

# === API for real-time mood state ===
@app.route('/api/mood_state')
def api_mood_state():
    return jsonify(load_mood_state())

@app.route('/api/avatar_styles')
def api_avatar_styles():
    return jsonify(load_avatar_styles())

if __name__ == '__main__':
    app.run(port=5055, debug=True)