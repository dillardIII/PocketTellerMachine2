# === FILE: bridge_listener.py ===
"""
Bridge Listener
Monitors bridge_sync.json and bridge_inbox/ for new modules or scripts to be deployed.
Auto-syncs files from shared PTM pipeline and bridge drop zone into the Replit environment.
Triggers module deployment, memory updates, and more.
Supports voice-activated deployment via voice_command_bridge.py (optional).
"""

import os
import json
import time
import shutil
from datetime import datetime
from ghostforge_core import GhostForge
from utils.logger import log_event
from utils.file_utils import save_file

# === Constants ===
BRIDGE_FILE = "data/bridge_sync.json"
SOURCE_DIR = "../shared/scripts"
DEST_DIR = "scripts"
WATCH_INTERVAL = 5

BRIDGE_INBOX = "bridge/inbox"
BRIDGE_OUTBOX = "bridge/outbox"
PROCESSED_LOG = "memory/bridge_processed.json"
MEMORY_LOG = "memory/bridge_events.json"
VOICE_ENABLED = False  # Set to True to run voice bridge loop

# === Setup ===
def ensure_dirs():
    os.makedirs(BRIDGE_INBOX, exist_ok=True)
    os.makedirs(BRIDGE_OUTBOX, exist_ok=True)
    os.makedirs("memory", exist_ok=True)

# === Logging ===
def record_bridge_event(event_type, detail):
    if not os.path.exists(MEMORY_LOG):
        history = []
    else:
        with open(MEMORY_LOG, "r") as f:
            history = json.load(f)

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "type": event_type,
        "detail": detail
    }

    history.append(entry)
    with open(MEMORY_LOG, "w") as f:
        json.dump(history[-300:], f, indent=2)

# === JSON Bridge Sync ===
def load_bridge_file():
    if not os.path.exists(BRIDGE_FILE):
        log_event("bridge_sync.json not found.")
        return {}
    try:
        with open(BRIDGE_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        log_event("Malformed bridge_sync.json.")
        return {}

def save_bridge_file(data):
    with open(BRIDGE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def deploy_from_bridge_file(script_name, description=""):
    source_path = os.path.join(SOURCE_DIR, f"{script_name}.py")
    dest_path = os.path.join(DEST_DIR, f"{script_name}.py")

    if not os.path.exists(source_path):
        log_event(f"Source file not found: {source_path}")
        return False

    os.makedirs(DEST_DIR, exist_ok=True)
    with open(source_path, "r") as src, open(dest_path, "w") as dst:
        dst.write(src.read())

    log_event(f"✅ Deployed from sync: {script_name}.py | {description}")
    return True

def check_for_new_scripts():
    bridge = load_bridge_file()
    updated = False

    for key, value in bridge.items():
        if isinstance(value, dict) and value.get("status") == "ready_to_pull":
            script_name = key
            description = value.get("description", "")
            success = deploy_from_bridge_file(script_name, description)
            if success:
                bridge[script_name]["status"] = "deployed"
                bridge[script_name]["last_deployed"] = datetime.utcnow().isoformat() + "Z"
                updated = True

    if updated:
        save_bridge_file(bridge)

# === Inbox Drops ===
def load_log():
    if not os.path.exists(PROCESSED_LOG):
        return []
    with open(PROCESSED_LOG, "r") as f:
        return json.load(f)

def save_log(log):
    with open(PROCESSED_LOG, "w") as f:
        json.dump(log[-300:], f, indent=2)

def process_script(path):
    with open(path, "r") as f:
        code = f.read()

    filename = os.path.basename(path)
    module_path = f"generated_modules/{filename}"
    save_file(module_path, code)

    log_event("Bridge Script Deployed", {
        "source": path,
        "target": module_path,
        "type": "script"
    })
    print(f"[BridgeListener] ✅ Deployed script → {module_path}")

def process_data(path):
    with open(path, "r") as f:
        data = json.load(f)

    filename = os.path.basename(path)
    memory_path = f"memory/{filename}"
    save_file(memory_path, json.dumps(data, indent=2))

    log_event("Bridge Memory Update", {
        "source": path,
        "target": memory_path,
        "type": "data"
    })
    print(f"[BridgeListener] 🧠 Updated memory → {memory_path}")

def process_bridge_drops():
    ensure_dirs()
    forge = GhostForge(persona="BridgeBot")
    processed = load_log()

    for filename in os.listdir(BRIDGE_INBOX):
        path = os.path.join(BRIDGE_INBOX, filename)
        if filename in processed or not filename.endswith((".py", ".json")):
            continue

        if filename.endswith(".py"):
            with open(path, "r") as f:
                content = f.read()
            target_path = "core/" + filename
            forge.evolve_modules({target_path: content})
        elif filename.endswith(".json"):
            process_data(path)

        archive_path = os.path.join(BRIDGE_OUTBOX, filename)
        shutil.move(path, archive_path)
        log_event(f"✅ Deployed from inbox: {filename}")
        processed.append(filename)

    save_log(processed)

# === Optional Voice Activation ===
def start_voice_listener():
    from voice_command_bridge import listen_for_voice_command, handle_bridge_command
    log_event("Voice bridge command listener started.")
    while True:
        command = listen_for_voice_command()
        handle_bridge_command(command)

# === Unified Listener Loop ===
def start_listener():
    log_event("Bridge Listener started. Watching for bridge_sync and bridge_inbox...")
    while True:
        check_for_new_scripts()
        process_bridge_drops()
        time.sleep(WATCH_INTERVAL)

if __name__ == "__main__":
    ensure_dirs()
    if VOICE_ENABLED:
        start_voice_listener()
    else:
        start_listener()