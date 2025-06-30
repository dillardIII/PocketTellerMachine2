# === FILE: team_autopilot_runner.py ===
# This file controls the Replit team's autonomous build cycle.
# It listens for incoming packets from other teams, executes the build tasks,
# and attempts automatic repairs on failure.

import time
from team_listener import listen_for_packets
from replit_autobuilder import execute_build_payload
from error_handler import auto_repair_if_failed

TEAM_NAME = "Replit"

print(f"[BOOT] 🚰️ {TEAM_NAME} Autopilot Initialized")

while True:
    # Step 1: Check for new build packets sent to the Replit team
    packet = listen_for_packets(TEAM_NAME)

    if packet:
        try:
            # Step 2: Execute the build task included in the packet
            execute_build_payload(packet)
        except Exception as e:
            print(f"[ERROR] Build failed: {e}")
            # Step 3: Attempt auto-repair if the build process failed
            auto_repair_if_failed(packet)

    # Step 4: Sleep briefly to avoid hammering the CPU
    time.sleep(2)