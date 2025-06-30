from ghost_env import INFURA_KEY, VAULT_ADDRESS
## ai_claude.py

import anthropic

class ClaudeResearch:
    def __init__(self, api_key):
        self.client = anthropic.Anthropic(api_key=api_key)

    import requests

class ClaudeResearch:
    def __init__(self, api_key):
        self.api_key = api_key
        self.model = "claude-3-sonnet-20240229"  # Update to "claude-3.5-sonnet-20240604" or latest available

    def get_summary(self, ticker):
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        data = {
            "model": self.model,
            "max_tokens": 512,
            "messages": [
                {"role": "user", "content": f"Give a two-sentence market update for {ticker} stock."}
            ]
        }
        try:
            resp = requests.post(url, headers=headers, json=data, timeout=20)
            resp.raise_for_status()
            result = resp.json()
            return result["content"][0]["text"]
        except Exception as e:
            print(f"Claude error: {e}")
            return None

def log_event():ef drop_files_to_bridge():