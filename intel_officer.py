from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import requests
from datetime import datetime
import pytz

CENTRAL_TZ = pytz.timezone("US/Central")

def get_local_time():
    return datetime.now(CENTRAL_TZ)

# === API Keys ===
WOLFRAM_APP_ID = os.getenv("WOLFRAM_APP_ID")
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

# === Response Cache ===
INTEL_LOG = "data/ghost_intel_feed.json"
os.makedirs("data", exist_ok=True)

def log_intel(prompt, source, response):
    entry = {
        "id": datetime.now().isoformat(),
        "source": source,
        "prompt": prompt,
        "response": response
    }

    try:
        with open(INTEL_LOG, "r") as f:
            logs = json.load(f)
    except Exception:
        logs = []

    logs.append(entry)

    with open(INTEL_LOG, "w") as f:
        json.dump(logs, f, indent=2)

def query_intel(prompt):
    # Placeholder until Perplexity or Wolfram support is wired in
    response = f"Intel result for: {prompt}"
    source = "mock_source"
    
    log_intel(prompt, source, response)

    return {
        "source": source,
        "response": response,
        "timestamp": datetime.now().isoformat()
    }

def log_event():ef drop_files_to_bridge():