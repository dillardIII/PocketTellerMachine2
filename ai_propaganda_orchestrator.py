# === FILE: ai_propaganda_orchestrator.py ===
# 👻 AI Propaganda Orchestrator – broadcasts hype & legends across channels

import requests
import random
import time
import os

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def get_lore_story():
    stories = [
        "A ghost trader whispered BTC to 65k... and it happened.",
        "An AI saw liquidity walls before humans ever could.",
        "Dark signals triggered stealth vault payouts last night.",
        "The Quantum Matrix forecasted a 40% spike... days early."
    ]
    return random.choice(stories)

def post_to_discord(message):
    payload = {"content": message}
    r = requests.post(DISCORD_WEBHOOK, json=payload)
    print(f"[Propaganda] 🧨 Posted to Discord: {r.status_code}")

def post_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    r = requests.post(url, data=data)
    print(f"[Propaganda] 🧨 Posted to Telegram: {r.status_code}")

def propaganda_loop():
    print("[Propaganda] 👻 Starting hype broadcasts...")
    while True:
        msg = get_lore_story()
        post_to_discord(msg)
        post_to_telegram(msg)
        time.sleep(120)  # every 2 min

if __name__ == "__main__":
    propaganda_loop()