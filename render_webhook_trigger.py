# 🚀 RenderWebhook – triggers Render redeploy via webhook
# Makes PTM instantly redeploy app after pushes

import requests
import time

WEBHOOK_URL = "https://api.render.com/deploy/YOUR_RENDER_DEPLOY_HOOK_HERE"

def trigger_deploy():
    response = requests.post(WEBHOOK_URL)
    if response.status_code == 200:
        print("[RenderWebhook] 🚀 Deploy triggered successfully.")
    else:
        print(f"[RenderWebhook] ⚠️ Deploy failed: {response.status_code} - {response.text}")

def deploy_loop():
    print("[RenderWebhook] 🌐 Starting auto-deploy loop...")
    while True:
        trigger_deploy()
        time.sleep(300)  # redeploy every 5 min

if __name__ == "__main__":
    deploy_loop()