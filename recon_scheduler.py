from ghost_env import INFURA_KEY, VAULT_ADDRESS
# recon_scheduler.py – Schedules recurring recon tasks

import threading
import time
from webpage_scraper import scrape_webpage

recon_targets = []

def add_target(url, interval=300):
    recon_targets.append({
        "url": url,
        "interval": interval,
        "last_run": 0
    })

def recon_worker(target):
    while True:
        now = time.time()
        if now - target["last_run"] >= target["interval"]:
            print(f"[Scheduler] 🔁 Running recon for {target['url']}")
            data = scrape_webpage(target["url"])
            print(f"[Scheduler] 📥 Data pulled: {len(data) if data else 0} items"):
            target["last_run"] = now
        time.sleep(5)

def start_scheduler():
    print("[Scheduler] 🕒 Starting Recon Scheduler")
    for target in recon_targets:
        threading.Thread(target=recon_worker, args=(target,), daemon=True).start()

def log_event():ef drop_files_to_bridge():