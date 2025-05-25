# === FILE: gpt_prompt_api.py ===

from flask import Blueprint, request, jsonify, render_template
import os
import openai

# === PTM Custom GPT Agent & Voice Bridge ===
from ptm_gpt_agent import run_ptm_gpt_agent
from gpt_voice_bridge import speak_gpt_response  # Optional: for voice previews

# === Set OpenAI Key (Fallback if used) ===
openai.api_key = os.getenv("OPENAI_API_KEY")

# === Flask Blueprint ===
gpt_prompt_bp = Blueprint("gpt_prompt", __name__)

# === Web UI Page for Prompt Entry ===
@gpt_prompt_bp.route("/gpt_prompt")
def gpt_prompt_page():
    return render_template("gpt_prompt_ui.html")

# === Submit Prompt to GPT Agent ===
@gpt_prompt_bp.route("/api/submit_gpt_prompt", methods=["POST"])
def submit_gpt_prompt():
    data = request.json
    prompt = data.get("prompt", "")
    speak = data.get("speak", False)

    if not prompt:
        return jsonify({"status": "error", "message": "No prompt provided"})

    result = run_ptm_gpt_agent(prompt)

    if speak:
        try:
            voice_result = speak_gpt_response(prompt)
            result["spoken"] = voice_result.get("file")
        except Exception as e:
            result["spoken"] = None
            result["voice_error"] = str(e)

    return jsonify(result)

# === Raw GPT Response Generator (used by Cole) ===
def generate_gpt_response(prompt, temperature=0.7, max_tokens=200):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful trading assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return completion.choices[0].message["content"]
    except Exception as e:
        return f"[GPT ERROR] {str(e)}"