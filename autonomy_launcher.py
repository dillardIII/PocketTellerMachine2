# === FILE: autonomy_launcher.py ===

from threading import Thread
import time

from cole_loop_controller import run_cole_controller_loop
from autonomy_meta_manager import review_and_reprioritize_roadmap
from gpt_self_command_engine import generate_self_command
from gpt_cole_sync import run_gpt_cole_sync

def start_loop(target, delay=30, label="Loop"):
    def loop():
        while True:
            try:
                print(f"[{label}] Running...")
                target()
                time.sleep(delay)
            except Exception as e:
                print(f"[{label}] Error:", e)
                time.sleep(15)
    return loop

if __name__ == "__main__":
    print("[PTM Autonomy Launcher] Starting full system...")

    threads = [
        Thread(target=start_loop(run_cole_controller_loop, delay=10, label="Cole Core")),
        Thread(target=start_loop(review_and_reprioritize_roadmap, delay=600, label="GPT Roadmap Meta")),
        Thread(target=start_loop(generate_self_command, delay=300, label="GPT Prompt Generator")),
        Thread(target=start_loop(run_gpt_cole_sync, delay=180, label="GPT-Cole Sync")),
    ]

    for t in threads:
        t.daemon = True
        t.start()

    while True:
        time.sleep(60)