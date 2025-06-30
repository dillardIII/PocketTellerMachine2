from ghost_env import INFURA_KEY, VAULT_ADDRESS
# autowrite_to_bridge.py
# Writes interpreted code into the bridge inbox

import os

BRIDGE_INBOX = "bridge_inbox"

def drop_to_bridge(filename, code):
    if not os.path.exists(BRIDGE_INBOX):
        os.makedirs(BRIDGE_INBOX)

    path = os.path.join(BRIDGE_INBOX, filename)
    with open(path, "w") as f:
        f.write(code)

    print(f"📦 Dropped: {filename} into {BRIDGE_INBOX}/")