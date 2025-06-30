# === FILE: ptm_gpt_agent.py ===

import openai
import os
import json
from datetime import datetime

GPT_SYNC_LOG_FILE = "logs/gpt_cole_sync_log.json"
openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure your Replit secrets include this

# === Save GPT Suggestions ===
def log_gpt_feature_suggestion(suggestion):
    os.makedirs("logs", exist_ok=True)
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "suggestion": suggestion
    }
    try:
        if os.path.exists(GPT_SYNC_LOG_FILE):
            with open(GPT_SYNC_LOG_FILE, "r") as f:
                logs = json.load(f)
        else:
            logs = []
        logs.append(log_entry)
        with open(GPT_SYNC_LOG_FILE, "w") as f:
            json.dump(logs, f, indent=2)
    except Exception as e:
        print(f"[GPT Agent] Failed to log suggestion: {e}")

# === Core GPT Interaction ===
def run_ptm_gpt_agent(prompt):
    print(f"[GPT Agent] Processing command: {prompt}")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a software architect for a trading AI platform."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response['choices'][0]['message']['content']
        log_gpt_feature_suggestion(reply)
        print("[GPT Agent] Suggestion logged successfully.")
        return reply
    except Exception as e:
        print(f"[GPT Agent] Failed to parse GPT response: {e}")
        return None