from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Autonomy Initializer
Launches the full autonomous system loop, including:
- Voice-to-command pipeline
- Bridge file listening and processing
- GhostForge recursive evolution
- Assistant Council decision handling
- Temporal reflex triggers

This file is the heartbeat of PTM autonomy.
"""

import threading
import time
from bridge_listener import start_listener
from voice_command_bridge import listen_for_voice_command, handle_bridge_command
from ghostforge_core import GhostForge
from assistants.council_protocol import evaluate_decision
from temporal_sync_engine import has_time_passed, set_anchor

AUTONOMY_LOOP_INTERVAL = 10  # seconds between loop iterations
VOICE_ENABLED = True

def run_voice_loop():
    while True:
        command = listen_for_voice_command()
        if command:
            handle_bridge_command(command)
        time.sleep(2)

def run_ghostforge_loop():
    forge = GhostForge("AutonomyCore")
    while True:
        # Example evolution trigger
        if has_time_passed("next_forge_evolution"):
            forge.generate_module(
                "self_improving_routine",
                purpose="Inject improved logic to handle real-time signal conflicts",
                base_code="# v0.1 stub: auto-enhancement placeholder"
            )
            set_anchor("next_forge_evolution", 30 * 60)  # evolve every 30 mins
        time.sleep(AUTONOMY_LOOP_INTERVAL)

def run_council_loop():
    while True:
        prompt = "Should PTM initiate its next recursive update sequence?"
        result = evaluate_decision(prompt)
        print(f"[Autonomy] 🧠 Council voted: {result['decision']}")
        time.sleep(60 * 5)

def start_autonomous_core():
    print("[AutonomyCore] 🚀 Launching PTM Autonomous System...")

    threading.Thread(target=start_listener, daemon=True).start()
    threading.Thread(target=run_ghostforge_loop, daemon=True).start()
    threading.Thread(target=run_council_loop, daemon=True).start()

    if VOICE_ENABLED:
        threading.Thread(target=run_voice_loop, daemon=True).start()

    while True:
        print("[AutonomyCore] 🔁 System stable. Awaiting events...")
        time.sleep(30)

if __name__ == "__main__":
    start_autonomous_core()