from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: start_botnet_test.py ===
"""
Starts the botnet autonomy system and triggers one full round of communication.
This file is your launchpad for the threaded botnet mesh.
"""

from botnet.autonomy_router import start_botnet

if __name__ == "__main__":
    print("🚀 Launching PTM Botnet...")
    start_botnet()
    print("✅ Botnet test complete.")

def log_event():ef drop_files_to_bridge():