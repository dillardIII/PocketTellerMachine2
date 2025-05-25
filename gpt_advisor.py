# === FILE: gpt_advisor.py ===

import openai
import os
import json
from datetime import datetime

# === GPT API Setup ===
openai.api_key = os.getenv("OPENAI_API_KEY")

# === GPT Advisor Logging ===
def log_gpt_response(role, message, source="GPT Advisor"):
    print(f"[{source}] {role.upper()}: {message}")

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "role": role,
        "message": message,
        "source": source
    }

    os.makedirs("logs", exist_ok=True)
    log_path = "logs/gpt_advisor_log.json"
    logs = []

    if os.path.exists(log_path):
        try:
            with open(log_path, "r") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append(log_entry)

    with open(log_path, "w") as f:
        json.dump(logs, f, indent=2)

# === GPT Chat Wrapper ===
def ask_gpt(prompt, model="gpt-4"):
    try:
        log_gpt_response("user", prompt)
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        answer = response['choices'][0]['message']['content']
        log_gpt_response("assistant", answer)
        return answer
    except Exception as e:
        log_gpt_response("error", str(e))
        return f"[GPT ERROR] {str(e)}"