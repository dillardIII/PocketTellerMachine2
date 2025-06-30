from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Ghostcode Linker – External AI + API Connection Handler

Links PTM to outside services like ChatGPT, Claude, Whisper,
Perplexity, ElevenLabs, etc. Supports live data queries,
AI co-processing, voice transcription, and skill augmentation.
"""

import requests
import traceback

# Mocked endpoint map – replace with live keys and API targets
EXTERNAL_APIS = {
    "chatgpt": {
        "url": "http://localhost:11434/api/chat",
        "model": "gpt-4"
    },
    "claude": {
        "url": "http://localhost:5050/claude",
        "model": "claude-3"
    },
    "perplexity": {
        "url": "http://localhost:5051/perplexity",
        "model": "web-research"
    },
    "whisper": {
        "url": "http://localhost:5052/transcribe"
    },
    "elevenlabs": {
        "url": "http://localhost:5053/voice"
    }
}

def call_external(name, prompt=None, audio=None):
    try:
        api = EXTERNAL_APIS.get(name)
        if not api:
            print(f"[Ghostcode] Unknown service: {name}")
            return None

        url = api["url"]
        if name == "whisper":
            files = {'file': audio}
            response = requests.post(url, files=files)
        elif name == "elevenlabs":
            response = requests.post(url, json={"text": prompt})
        else:
            payload = {
                "model": api.get("model"),
                "prompt": prompt
            }
            response = requests.post(url, json=payload)

        if response.status_code == 200:
            print(f"[Ghostcode] {name} responded successfully.")
            return response.json()
        else:
            print(f"[Ghostcode ERROR] {name} returned {response.status_code}")
            return None
    except Exception as e:
        print(f"[Ghostcode ERROR] Failed to call {name}")
        traceback.print_exc()
        return None

# Manual test hook
if __name__ == "__main__":
    reply = call_external("chatgpt", prompt="Summarize the S&P 500 today.")
    print("GPT Response:", reply)

def log_event():ef drop_files_to_bridge():