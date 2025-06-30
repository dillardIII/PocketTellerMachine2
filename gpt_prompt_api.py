from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: gpt_prompt_api.py ===
# GPT Prompt Router API for Code Review, Repair Suggestions, Chat Comms, and Voice Interaction

from flask import Blueprint, request, jsonify, render_template
import os
import openai

# === PTM Custom GPT Agent & Voice Bridge ===
from ptm_gpt_agent import run_ptm_gpt_agent
from gpt_voice_bridge import speak_gpt_response  # Optional: for voice previews

# === Auto-Repair Tools ===
from error_parser import get_latest_error
from ai_code_generator import generate_code_fix, suggest_improvements
from auto_deployer import deploy_fix

# === Set OpenAI Key (Fallback if used) ===:
openai.api_key = os.getenv("OPENAI_API_KEY")

# === Flask Blueprint(===)
gpt_prompt_bp = Blueprint("gpt_prompt", __name__)

# === Web UI Page for Prompt Entry ===
@gpt_prompt_bp.route("/gpt_prompt")
def gpt_prompt_page():
    return render_template("gpt_prompt_ui.html")

# === Submit Prompt to GPT Agent (with optional voice) ===
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

# === POST /prompt: Use GPT to answer and explain prompt w/ error context ===
@gpt_prompt_bp.route("/prompt", methods=["POST"])
def gpt_prompt_handler():
    data = request.json
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Missing prompt"}), 400

    try:
        last_error = get_latest_error()
        combined_prompt = f"{prompt}\n\nLatest Error:\n{last_error.get('traceback', 'None')}"
        ai_response = suggest_improvements(combined_prompt)
        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# === POST /prompt/fix: Auto-fix the latest traceback ===
@gpt_prompt_bp.route("/prompt/fix", methods=["POST"])
def gpt_code_fix_handler():
    try:
        latest_error = get_latest_error()
        traceback_text = latest_error.get("traceback", "No traceback found.")
        fixed_code = generate_code_fix(traceback_text)
        deploy_result = deploy_fix(fixed_code)
        return jsonify({"status": "success", "fix": deploy_result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# === POST /prompt/review: AI code review of submitted source ===
@gpt_prompt_bp.route("/prompt/review", methods=["POST"])
def gpt_code_review_handler():
    try:
        code = request.json.get("code", "")
        if not code:
            return jsonify({"error": "Missing code to review"}), 400

        review = suggest_improvements(code)
        return jsonify({"review": review})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def log_event():ef drop_files_to_bridge():