from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: replit_autobuilder.py ===
import os
from build_manifest_handler import log_build_manifest
from packet_responder import send_response  # ADD this to the top

RECEIVED_DIR = "incoming_builds"
os.makedirs(RECEIVED_DIR, exist_ok=True)

def execute_build_payload(packet):
    team = packet['recipient']
    files = packet['files']
    task = packet['task_name']
    notes = packet['instructions']

    build_folder = os.path.join(RECEIVED_DIR, f"{team}_{task.replace(' ', '_')}")
    os.makedirs(build_folder, exist_ok=True)

    for filename, content in files.items():
        file_path = os.path.join(build_folder, filename)
        with open(file_path, "w") as f:
            f.write(content)

    print(f"[AUTOBUILDER] Installed {len(files)} files for task: {task}")
    log_build_manifest(team, task, files, notes)

    # At the END of execute_build_payload():
    send_response(packet, status="✅ Build complete", notes="Files installed successfully.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():