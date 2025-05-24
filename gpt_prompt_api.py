# === FILE: gpt_prompt_api.py ===

from flask import Blueprint, request, jsonify, render_template
from ptm_gpt_agent import run_ptm_gpt_agent
from gpt_voice_bridge import speak_gpt_response  # NEW

gpt_prompt_bp = Blueprint("gpt_prompt", __name__)

@gpt_prompt_bp.route("/gpt_prompt")
def gpt_prompt_page():
    return render_template("gpt_prompt_ui.html")

@gpt_prompt_bp.route("/api/submit_gpt_prompt", methods=["POST"])
def submit_gpt_prompt():
    data = request.json
    prompt = data.get("prompt", "")
    speak = data.get("speak", False)

    if not prompt:
        return jsonify({"status": "error", "message": "No prompt provided"})

    result = run_ptm_gpt_agent(prompt)

    if speak:
        voice_result = speak_gpt_response(prompt)
        result["spoken"] = voice_result.get("file")

    return jsonify(result)