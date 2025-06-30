from ghost_env import INFURA_KEY, VAULT_ADDRESS
import time
import json
import os
from datetime import datetime
from cole_command_interpreter import cole_interpret_command
from sync_engine import log_sync_event  # NEW SYNC LINK

PATCH_INBOX = "data/patch_inbox.json"
PATCH_LOG = "data/patch_log.json"

os.makedirs("data", exist_ok=True)

# === Ensure inbox file exists ===
if not os.path.exists(PATCH_INBOX):
    with open(PATCH_INBOX, "w") as f:
        json.dump({"patches": []}, f, indent=2)

def patch_loop():
    print("[PatchChecker] Listening for patch commands...")

    while True:
        try:
            with open(PATCH_INBOX, "r") as f:
                data = json.load(f)

            patches = data.get("patches", [])
            if patches:
                for patch in patches:
                    command = patch.get("command")
                    author = patch.get("author", "unknown")
                    timestamp = patch.get("timestamp", datetime.now().isoformat())

                    print(f"[PatchChecker] Executing patch from {author}: {command}")
                    log_sync_event(author, "command", command, "executing")  # LOGGING SYNC ACTIVITY
                    result = cole_interpret_command(command)

                    log_entry = {
                        "timestamp": timestamp,
                        "author": author,
                        "command": command,
                        "result": result
                    }

                    if os.path.exists(PATCH_LOG):
                        with open(PATCH_LOG, "r") as f:
                            logs = json.load(f)
                    else:
                        logs = []

                    logs.append(log_entry)
                    with open(PATCH_LOG, "w") as f:
                        json.dump(logs[-500:], f, indent=2)

                with open(PATCH_INBOX, "w") as f:
                    json.dump({"patches": []}, f, indent=2)

        except Exception as e:
            print("[PatchChecker] Error:", str(e))

        time.sleep(10)

if __name__ == "__main__":
    patch_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():