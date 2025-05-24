# cole_phase14_mood_state_dashboard_api.py

from flask import Flask, jsonify, request, render_template
import os, json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
MOOD_LOG_FILE = "data/mood_state_change_log.json"
os.makedirs("data", exist_ok=True)

# === Flask App ===
app = Flask(__name__, template_folder='templates')

# === Logging ===
def log_mood_change(message):
    logs = []
    if os.path.exists(MOOD_LOG_FILE):
        try:
            with open(MOOD_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(MOOD_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load Mood State ===
def load_current_mood_state():
    if not os.path.exists(MOOD_STATE_FILE):
        return {}
    with open(MOOD_STATE_FILE, "r") as f:
        return json.load(f)

# === Save Mood State ===
def save_mood_state(state):
    with open(MOOD_STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

# === API: Get Mood State ===
@app.route("/api/mood_state", methods=["GET"])
def get_mood_state():
    state = load_current_mood_state()
    return jsonify({
        "timestamp": datetime.now().isoformat(),
        "mood_state": state
    })

# === API: Update Mood State ===
@app.route("/api/update_mood_state", methods=["POST"])
def update_mood_state():
    data = request.get_json()
    if not data or "persona" not in data or "mood" not in data:
        return jsonify({"status": "error", "message": "Missing persona or mood"}), 400

    current_state = load_current_mood_state()
    current_state[data["persona"]] = data["mood"]
    save_mood_state(current_state)
    log_mood_change(f"Updated {data['persona']} → {data['mood']}")
    return jsonify({"status": "success", "message": f"Mood updated for {data['persona']} to {data['mood']}."})

# === Mood Web Dashboard ===
@app.route("/mood_dashboard")
def mood_dashboard():
    state = load_current_mood_state()
    return render_template("mood_dashboard.html", mood_state=state)

# === Run the Daemon ===
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5020, debug=True)