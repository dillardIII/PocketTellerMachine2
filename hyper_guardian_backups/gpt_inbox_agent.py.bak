# === FILE: gpt_inbox_agent.py ===

# 📥 GPT Inbox Agent – Monitors PTM inbox and reacts with file generation

import os
import time
from ghostforge_writer import generate_autocode_file

def scan_and_trigger(folder="ptm_inbox"):
    print("[GPTInboxAgent] 🕵️ Watching inbox...")
    seen = set(os.listdir(folder))

    while True:
        files = set(os.listdir(folder))
        new = files - seen

        for f in new:
            print(f"[GPTInboxAgent] ⚡ Detected new file: {f}")
            if "trigger" in f.lower():
                generate_autocode_file("Auto_Response_" + f.replace("trigger_", ""), "# Generated in response to trigger")
        seen = files
        time.sleep(5)