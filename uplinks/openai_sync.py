# === FILE: uplinks/openai_sync.py ===
# 🧠 OpenAI Sync – Sends queries to OpenAI and returns responses

import openai
from utils.logger import log_event

openai.api_key = "your-openai-key"

def sync_openai():
    print("[OpenAI] 🔮 Querying OpenAI model...")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You're a trading strategist AI helping Boo."},
                {"role": "user", "content": "What's the outlook on tech stocks today?"}
            ]
        )
        reply = response["choices"][0]["message"]["content"]
        print(f"[OpenAI] 🧠 Response: {reply}")
        log_event("OpenAIResponse", {"reply": reply})
    except Exception as e:
        print(f"[OpenAI] ⚠️ Error: {e}")
        log_event("OpenAIError", {"error": str(e)})