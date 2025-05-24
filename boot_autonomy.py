# === FILE: boot_autonomy.py ===

import threading
import time
from cole_loop_controller import run_cole_controller_loop
from autonomy_launcher import *
from gpt_voice_loop import gpt_voice_loop  # Voice Response Engine
from ptm_thinking_daemon import gpt_thinking_loop  # << NEW: GPT Thinking Engine

def start_all_autonomy():
    print("[Autonomy Boot] Starting full AI system...")
    threads = [
        threading.Thread(target=start_loop(run_cole_controller_loop, delay=10, label="Cole Core")),
        threading.Thread(target=start_loop(review_and_reprioritize_roadmap, delay=600, label="Roadmap Review")),
        threading.Thread(target=start_loop(generate_self_command, delay=300, label="GPT Generator")),
        threading.Thread(target=start_loop(run_gpt_cole_sync, delay=180, label="GPT-Cole Sync")),
        threading.Thread(target=gpt_voice_loop),  # Voice responses
    ]

    # === NEW: Add GPT thinking thread ===
    threads.append(threading.Thread(target=gpt_thinking_loop))

    for t in threads:
        t.daemon = True
        t.start()

# Optional standalone boot
if __name__ == "__main__":
    start_all_autonomy()
    while True:
        time.sleep(60)