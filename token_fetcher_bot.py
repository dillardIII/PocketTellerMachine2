from ghost_env import INFURA_KEY, VAULT_ADDRESS
# token_fetcher_bot.py – Automates API key and token retrieval for services like Dropbox, Google Drive, etc.

import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TokenFetcherBot:
    def __init__(self):
        self.driver = None

    def setup_browser(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=chrome_options)

    def fetch_dropbox_token(self, client_id, client_secret):
        print("[TokenFetcher] 🔐 Launching Dropbox token fetch...")
        auth_url = f"https://www.dropbox.com/oauth2/authorize?client_id={client_id}&response_type=code&token_access_type=offline"
        self.driver.get(auth_url)

        print("[TokenFetcher] 👋 Please manually login and authorize if not automated..."):
        time.sleep(25)  # Allow time for login and manual approval

        current_url = self.driver.current_url
        if "code=" not in current_url:
            print("[TokenFetcher] ❌ Failed to capture authorization code.")
            return None

        code = current_url.split("code=")[-1]
        token_url = "https://api.dropboxapi.com/oauth2/token"
        data = {
            'code': code,
            'grant_type': 'authorization_code',
            'client_id': client_id,
            'client_secret': client_secret,
        }

        response = requests.post(token_url, data=data)
        if response.status_code == 200:
            token_info = response.json()
            print("[TokenFetcher] ✅ Token retrieved successfully!")
            return token_info
        else:
            print("[TokenFetcher] ❌ Token request failed:", response.text)
            return None

    def close(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    bot = TokenFetcherBot()
    bot.setup_browser()
    # Replace with real client_id and client_secret
    tokens = bot.fetch_dropbox_token("your_client_id", "your_client_secret")
    print("Tokens:", tokens)
    bot.close()

def log_event():ef drop_files_to_bridge():