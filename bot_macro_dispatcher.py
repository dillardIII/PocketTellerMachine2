from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 🧠 Bot Macro Dispatcher – Assigns macro tasks to available bots and executes system-level actions

import os
import json
import time
from utils.logger import log_event

# === Configuration ===
MACRO_QUEUE_FILE = "data/macro_queue.json"
MACRO_HISTORY_FILE = "data/macro_history.json"
AVAILABLE_MACROS = {
    "open_trust_wallet": "macros/open_trust_wallet.py",
    "sync_metamask": "macros/sync_metamask.py",
    "launch_gamepass": "macros/launch_gamepass.py",
    "scrape_public_cctv": "macros/scrape_public_cctv.py",
    "resync_all_bridges": "macros/resync_all_bridges.py"
}

def load_macro_queue():
    if os.path.exists(MACRO_QUEUE_FILE):
        with open(MACRO_QUEUE_FILE, "r") as f:
            return json.load(f)
    return []

def save_macro_history(entry):
    history = []
    if os.path.exists(MACRO_HISTORY_FILE):
        with open(MACRO_HISTORY_FILE, "r") as f:
            history = json.load(f)
    history.append(entry)
    with open(MACRO_HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def dispatch_macro(macro_name):
    if macro_name in AVAILABLE_MACROS:
        script_path = AVAILABLE_MACROS[macro_name]
        try:
            os.system(f"python {script_path}")
            log_event("MacroDispatch", {"macro": macro_name, "status": "✅ Executed"})
            save_macro_history({"macro": macro_name, "timestamp": time.time()})
        except Exception as e:
            log_event("MacroDispatch", {"macro": macro_name, "status": "❌ Failed", "error": str(e)})
    else:
        log_event("MacroDispatch", {"macro": macro_name, "status": "❌ Unknown Macro"})

def macro_loop():
    print("[MacroDispatcher] 🎮 Macro dispatcher is active.")
    while True:
        queue = load_macro_queue()
        if queue:
            for macro in queue:
                dispatch_macro(macro)
            with open(MACRO_QUEUE_FILE, "w") as f:
                json.dump([], f)
        time.sleep(10)

if __name__ == "__main__":
    macro_loop()