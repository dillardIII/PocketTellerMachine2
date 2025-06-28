# === FILE: event_listener_core.py ===

# 🎧 Event Listener – Reacts to file drops, voice triggers, or external signals

import os
import time

def listen_for_events(folder="ptm_inbox"):
    print("[EventListener] 🔍 Watching for events...")
    known_files = set(os.listdir(folder))

    while True:
        current_files = set(os.listdir(folder))
        new_files = current_files - known_files
        if new_files:
            for file in new_files:
                print(f"[EventListener] ⚡ New file dropped: {file}")
        known_files = current_files
        time.sleep(2)