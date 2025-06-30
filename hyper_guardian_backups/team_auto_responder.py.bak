"""
Team Auto Responder – AI Persona Communication Hub

Purpose:
- Listen for triggers (alert, greeting, etc.)
- Generate responses from assigned personas
- Link to front-end for interactive responses
"""

from flask import Blueprint, jsonify, request
import random
import datetime

# === Blueprint Setup ===
team_auto_responder = Blueprint("team_auto_responder", __name__)

# === Persona Profiles ===
personas = [
    {"name": "Mo Cash", "role": "Hustler", "style": "hype", "voice": "male"},
    {"name": "The Mentor", "role": "Advisor", "style": "calm", "voice": "male"},
    {"name": "Drill Instructor", "role": "Motivator", "style": "strict", "voice": "male"},
    {"name": "The Shadow", "role": "Silent Strategist", "style": "mysterious", "voice": "neutral"},
    {"name": "Optimist", "role": "Encourager", "style": "uplifting", "voice": "female"},
    {"name": "Strategist", "role": "Planner", "style": "tactical", "voice": "neutral"}
]

# === Trigger-Based Responses ===
trigger_responses = {
    "alert": [
        "Alert received. Standing by.",
        "Team notified. Awaiting commands.",
        "Red flag triggered. Recalibrating options.",
    ],
    "success": [
        "Mission accomplished. Excellent execution.",
        "Victory logged. Well played.",
        "Objective complete. You're crushing it.",
    ],
    "failure": [
        "That didn’t go as planned. Running diagnostics.",
        "Loss registered. Let’s adjust our approach.",
        "Recording failure data. Preparing counterstrike.",
    ],
    "greeting": [
        "Yo! Your crew is live and synced.",
        "Welcome back. Systems operational.",
        "Command team standing by. Let’s roll."
    ]
}

# === Core Responder Class ===
class TeamAutoResponder:
    def __init__(self):
        self.personas = personas
        self.triggers = trigger_responses

    def respond(self, trigger_type="greeting"):
        if trigger_type not in self.triggers:
            trigger_type = "greeting"
        
        responses = []
        selected = random.sample(self.personas, k=min(3, len(self.personas)))
        for persona in selected:
            message = random.choice(self.triggers[trigger_type])
            responses.append({
                "persona": persona["name"],
                "role": persona["role"],
                "voice": persona["voice"],
                "message": message,
                "timestamp": datetime.datetime.utcnow().isoformat()
            })
        return {"trigger": trigger_type, "responses": responses}

# === Flask API Endpoint ===
@team_auto_responder.route("/api/team/respond", methods=["POST"])
def trigger_team_response():
    data = request.get_json()
    trigger_type = data.get("trigger", "greeting")

    responder = TeamAutoResponder()
    result = responder.respond(trigger_type)

    return jsonify(result)