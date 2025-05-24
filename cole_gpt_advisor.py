# === FILE: cole_gpt_advisor.py ===

import os
import json
from datetime import datetime
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

CHAT_LOG_PATH = "data/cole_gpt_chat_log.json"
os.makedirs("data", exist_ok=True)

def log_gpt_chat(prompt, reply):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "reply": reply
    }

    if os.path.exists(CHAT_LOG_PATH):
        with open(CHAT_LOG_PATH, "r") as f:
            chat_history = json.load(f)
    else:
        chat_history = []

    chat_history.append(log_entry)
    with open(CHAT_LOG_PATH, "w") as f:
        json.dump(chat_history[-500:], f, indent=2)  # Keep last 500 entries

def ask_gpt(prompt):
    """
    Sends a prompt to GPT-4 and logs the conversation for Cole's memory.
    """
    print(f"[Cole → GPT] {prompt}")

    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Cole's trading assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=800
        )

        reply = response.choices[0].message.content.strip()
        log_gpt_chat(prompt, reply)
        return reply

    except Exception as e:
        error_msg = f"GPT Error: {str(e)}"
        log_gpt_chat(prompt, error_msg)
        return error_msg