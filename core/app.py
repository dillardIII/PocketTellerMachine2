from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: core/app.py ===

# 🚀 PTM Core App Launcher – Entry point for bot command logic (optional split from Flask)

from utils.logger import log_event

def launch_ptm():
    log_event("PTM Core", {"status": "App launched"})

    print("""
    ================================
    🧠 PocketTellerMachine Activated
    ================================
    ✅ Smart Audit Mode: ON
    ✅ GhostForge Repair: ON
    ✅ InspectorBot Status: Online
    """)

    # Simulate PTM loading brain modules
    print("[PTM Core] 🔌 Loading assistant stack...")
    print("[PTM Core] 💬 Voice personalities registered.")
    print("[PTM Core] 🧠 Strategy engine warming up...")
    print("[PTM Core] 📡 Awaiting user interaction...")

if __name__ == "__main__":
    launch_ptm()