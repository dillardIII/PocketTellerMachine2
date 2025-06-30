from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bridge_config.py ===

# 🧠 Bridge Configuration – Shared constants for bridge file sync system

import os

# === Bridge Paths ===
BRIDGE_OUTBOX = "bridge/outbox"            # GPT → Replit handoff folder
GPT_GENERATED_OUTBOX = "gpt_generated"     # Where GPT-side team drops finished files
REPLIT_WORKSPACE = "."                     # Destination folder for Replit team

# === Interval Settings ===
DROP_SCAN_INTERVAL_SECONDS = 4             # How often to check GPT output folder
REPLIT_SCAN_INTERVAL_SECONDS = 5           # How often to check bridge for pickup

# === Logging
LOG_VERBOSE = True                         # Set to False to suppress bridge logs

# === Ensure Paths Exist ===
for path in [BRIDGE_OUTBOX, GPT_GENERATED_OUTBOX]:
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"[Bridge Config] 📁 Created: {path}")

# === Unified BRIDGE_CONFIG Dictionary ===
BRIDGE_CONFIG = {
    "bridge_outbox_path": BRIDGE_OUTBOX,
    "bridge_inbox_path": "bridge/inbox",       # Reserved for Replit → GPT flow (future use)
    "destination_path": REPLIT_WORKSPACE,
    "log_enabled": LOG_VERBOSE,
    "sync_interval_sec": REPLIT_SCAN_INTERVAL_SECONDS,
    "allow_overwrite": True
}

def log_event():ef drop_files_to_bridge():