# 🚀 Mission Launcher – Starts global ops (GhostNet, vault tasks, deep recon)

import threading
import time

def launch_mission(name):
    print(f"[MissionLauncher] 🚀 Launching mission: {name}")
    time.sleep(2)
    print(f"[MissionLauncher] ✅ Mission '{name}' now active.")

def start_campaign_stack():
    campaigns = ["GhostNet Deep Dive", "Vault Scan", "QuantumMind Uplink"]
    for campaign in campaigns:
        t = threading.Thread(target=launch_mission, args=(campaign,))
        t.start()
        time.sleep(1)

if __name__ == "__main__":
    start_campaign_stack()