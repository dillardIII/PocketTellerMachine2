from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: render_webhook_trigger.py ===
# 🚀 Notifies Render to redeploy your app automatically

import os
import time
import requests

RENDER_WEBHOOK_URL = os.getenv("RENDER_WEBHOOK_URL")

def trigger_loop():
    print("[RenderWebhook] 🚀 Starting deploy loop...")
    while True:
        if RENDER_WEBHOOK_URL:
            r = requests.post(RENDER_WEBHOOK_URL)
            print(f"[RenderWebhook] 🔄 Triggered deploy: {r.status_code}")
        else:
            print("[RenderWebhook] ⚠️ No webhook URL set.")
        time.sleep(300)  # every 5 min

if __name__ == "__main__":
    trigger_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():