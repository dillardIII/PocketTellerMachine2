from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: uplinks/perplexity_feed.py ===
# 📡 Perplexity Feed – Grabs live intel from Perplexity

import requests
from utils.logger import log_event

def fetch_intel():
    print("[Perplexity] 📡 Grabbing intel report...")

    try:
        response = requests.get("https://api.perplexity.ai/v1/query", params={
            "q": "latest market trends",
            "apikey": "your-perplexity-key"
        })
        data = response.json()
        summary = data.get("summary", "No intel available.")
        print(f"[Perplexity] 📈 Intel: {summary}")
        log_event("PerplexityIntel", {"summary": summary})
    except Exception as e:
        print(f"[Perplexity] ⚠️ Error: {e}")
        log_event("PerplexityError", {"error": str(e)})