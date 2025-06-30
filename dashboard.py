from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: dashboard.py ===
from flask import Flask, render_template_string
import json, threading
app = Flask(__name__)

@app.route("/")
def home():
    mem = json.load(open("command_memory_log.json"))[-10:]
    emo = json.load(open("emotion_state.json"))
    return render_template_string("""
    <h1>PTM Dashboard</h1>
    <h2>Recent Memory</h2>
    <ul>
    {% for e in mem %}
      <li>{{ e.timestamp }} - {{ e.event }}: {{ e.detail }}</li>
    {% endfor %}
    </ul>
    <h2>Emotion</h2>
    <p>Confidence: {{ emo.confidence }} | Fear: {{ emo.fear }}</p>
    """, mem=mem, emo=emo)

def run_dash():
    app.run(host="0.0.0.0", port=5000)

threading.Thread(target=run_dash, daemon=True).start()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():