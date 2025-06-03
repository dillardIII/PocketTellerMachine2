# === FILE: autonomy_launcher.py ===
# Launches the primary bot swarm and engages registered modules

from bot_registry import get_registered_bots
from bot_controller import start_bot_instance
from phase_status_monitor import set_phase_status

# Additional imports for full autonomy loop launching
from threading import Thread
import time

from cole_loop_controller import run_cole_controller_loop
from autonomy_meta_manager import review_and_reprioritize_roadmap
from gpt_self_command_engine import generate_self_command
from gpt_cole_sync import run_gpt_cole_sync

def launch_all_bots():
    """
    Boots every registered bot using the bot controller.
    Flags 'bots' phase when complete.
    """
    print("[Launcher] 🚀 Launching registered bots...")
    bots = get_registered_bots()

    for bot in bots:
        start_bot_instance(bot)

    set_phase_status("bots", True)
    print(f"[Launcher] ✅ All {len(bots)} bots launched.")

def start_loop(target, delay=30, label="Loop"):
    """
    Wraps a function in a persistent thread loop with logging and error handling.
    """
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

    # Launch bot swarm first
    launch_all_bots()

    # Start continuous autonomy system loops
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