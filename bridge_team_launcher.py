# === FILE: agents/bridge_team_launcher.py ===

# 🔗 Bridge Team Launcher – Initializes pickup and drop agents for PTM bridge system

from bridge_pickup_agent import run_pickup_agent
from bridge_drop_agent import run_drop_agent

def start_bridge_team():
    print("[BridgeTeam] 🔗 Starting bridge pickup and drop agents...")
    run_pickup_agent()
    run_drop_agent()