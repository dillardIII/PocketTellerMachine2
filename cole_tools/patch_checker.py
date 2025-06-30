from ghost_env import INFURA_KEY, VAULT_ADDRESS
# patch_checker.py (now at root)
import time
import json
import os
from datetime import datetime

# Replaced with correct absolute import now that file is outside cole_tools
from cole_tools.cole_command_interpreter import cole_interpret_command

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
                    result = cole_interpret_command(command)

                    log_entry = {
                        "timestamp": timestamp,
                        "author": author,
                        "command": command,
                        "result": result
                    }

                    # Log patch execution
                    if os.path.exists(PATCH_LOG):
                        with open(PATCH_LOG, "r") as f:
                            logs = json.load(f)
                    else:
                        logs = []

                    logs.append(log_entry)
                    with open(PATCH_LOG, "w") as f:
                        json.dump(logs[-500:], f, indent=2)

                # Clear inbox after processing
                with open(PATCH_INBOX, "w") as f:
                    json.dump({"patches": []}, f, indent=2)

        except Exception as e:
            print("[PatchChecker] Error:", str(e))

        time.sleep(10)

if __name__ == "__main__":
    patch_loop()