from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import openai
from datetime import datetime

# === GPT Config ===
openai.api_key = os.getenv("OPENAI_API_KEY")
CHAT_LOG_FILE = "logs/cole_gpt_chat.json"

# === Ensure folder exists ===
os.makedirs("logs", exist_ok=True)

# === Ask GPT for response ===
def ask_gpt(prompt, temperature=0.7, max_tokens=300):
    print("[GPT Advisor] Asking GPT...")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a trading assistant for PTM."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        reply = response.choices[0].message["content"].strip()
        log_gpt_chat(prompt, reply)
        return reply
    except Exception as e:
        error_msg = f"[GPT Advisor] GPT error: {e}"
        log_gpt_chat(prompt, error_msg)
        return error_msg

# === Log GPT Chat ===
def log_gpt_chat(prompt, reply):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "reply": reply
    }

    try:
        if os.path.exists(CHAT_LOG_FILE):
            with open(CHAT_LOG_FILE, "r") as f:
                try:
                    logs = json.load(f)
                    if not isinstance(logs, list):
                        logs = []
                except json.JSONDecodeError:
                    logs = []
        else:
            logs = []

        logs.append(entry)

        with open(CHAT_LOG_FILE, "w") as f:
            json.dump(logs[-500:], f, indent=2)

        print("[GPT Advisor] Chat logged.")
    except Exception as e:
        print(f"[GPT Logger] Error logging chat: {e}")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():