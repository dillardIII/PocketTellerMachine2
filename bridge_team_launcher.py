from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bridge_team_launcher.py ===

# 🔗 Bridge Team Launcher – Controls both direct move loop and agent initialization for PTM bridge system

import os
import time

# Optional advanced agent modules
try:
    from bridge_pickup_agent import run_pickup_agent
    from bridge_drop_agent import run_drop_agent
    AGENTS_AVAILABLE = True
except ImportError:
    print("[BridgeTeam] ⚠️ Pickup/drop agents not found, using fallback bridge mover.")
    AGENTS_AVAILABLE = False

def start_bridge_team():
    if AGENTS_AVAILABLE:
        print("[BridgeTeam] 🔗 Starting bridge pickup and drop agents...")
        run_pickup_agent()
        run_drop_agent()
    else:
        print("[BridgeTeam] 🔗 Using direct bridge file mover...")
        start_basic_bridge_loop()

def start_basic_bridge_loop():
    print("[BridgeTeam] 🔄 Basic bridge file mover engaged.")
    while True:
        try:
            for file in os.listdir("bridge_drop"):
                src = os.path.join("bridge_drop", file)
                dst = os.path.join("bridge_pickup", file)
                os.rename(src, dst)
                print(f"[BridgeTeam] 📥 Picked up {file} from bridge_drop -> bridge_pickup.")
        except Exception as e:
            print(f"[BridgeTeam] ⚠️ Bridge mover error: {e}")
        time.sleep(8)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():