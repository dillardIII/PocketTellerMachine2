# cole_voice_persona_selector_ui.py

from flask import Flask, request, jsonify, render_template_string
import os
import json

# === Configurations ===
PERSONAS_FILE = "data/persona_list.json"
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_COMMAND_QUEUE_FILE = "data/voice_command_queue.json"
os.makedirs("data", exist_ok=True)

app = Flask(__name__)

# === Load Helpers ===
def load_json(file_path, default_value):
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except:
            return default_value
    return default_value

def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

# === UI Route ===
@app.route("/")
def index():
    personas = load_json(PERSONAS_FILE, [])
    mood_state = load_json(MOOD_STATE_FILE, {})
    return render_template_string("""
    <h1>Persona Voice Selector UI</h1>
    <form method="POST" action="/assign_voice_tone">
        <label>Persona:</label>
        <select name="persona">
            {% for p in personas %}
            <option value="{{p}}">{{p}}</option>
            {% endfor %}
        </select><br><br>
        <label>Voice Tone:</label>
        <input type="text" name="voice_tone" placeholder="e.g., calm_voice"><br><br>
        <button type="submit">Assign Voice</button>
    </form>
    <h2>Current Mood States:</h2>
    <pre>{{mood_state}}</pre>
    """, personas=personas, mood_state=json.dumps(mood_state, indent=2))

# === API to assign voice ===
@app.route("/assign_voice_tone", methods=["POST"])
def assign_voice_tone():
    persona = request.form.get("persona")
    voice_tone = request.form.get("voice_tone")
    if not persona or not voice_tone:
        return "Missing fields", 400

    queue = load_json(VOICE_COMMAND_QUEUE_FILE, [])
    command = f"{persona} use_voice_tone {voice_tone}"
    queue.append(command)
    save_json(VOICE_COMMAND_QUEUE_FILE, queue)
    return f"Voice tone '{voice_tone}' assigned to {persona}. <a href='/'>Go Back</a>"

# === Run UI App ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100, debug=True)