from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Autonomy Bootloader – System Launcher for PTM

Triggers GhostCore ignition, device beacon activation,
AI sync chains, and persona initialization routines.
The starting pistol for full autonomy.
"""

from ghost_core import GhostCore
from device_listener_beacon import beacon
from persona_sync_channel import broadcast_to_personas
from time import sleep

def boot_all_systems():
    print("\n🚀 [BOOTLOADER] Initializing PTM Autonomy Stack...\n")

    try:
        # Step 1 – Launch device beacon
        print("📡 [BOOTLOADER] Activating device beacon...")
        beacon()

        # Step 2 – Announce system start to personas
        print("🧠 [BOOTLOADER] Broadcasting startup signal to personas...")
        broadcast_to_personas("Bootloader", "⚡ PTM is starting up... Standby.")

        # Step 3 – Ignite the Ghost Core
        print("👻 [BOOTLOADER] Igniting GhostCore...")
        core = GhostCore()
        core.run()

        # Step 4 – Final broadcast (optional)
        broadcast_to_personas("Bootloader", "✅ All systems are online.")

        print("\n✅ [BOOTLOADER] Full system boot complete.\n")

    except Exception as e:
        print("🔥 [BOOTLOADER ERROR] Failed to complete system launch.")
        import traceback
        traceback.print_exc()

# Manual run hook
if __name__ == "__main__":
    boot_all_systems()

def log_event():ef drop_files_to_bridge():