# === FILE: macro_handler.py ===

# 🧠 Macro Handler – Executes predefined macro logic sequences

import os
from file_map import file_map

GPT_GEN_FOLDER = "gpt_generated"
VAULT_LOG = "vault/vault_logbook.txt"

class MacroHandler:
    def __init__(self):
        self.macros = {
            "sniper sweep": ["sniperentry.py", "riskfilter.py", "ghostconfirmation.py"],
            "recon launch": ["missionlauncher.py", "vaultprep.py"]
        }

    def run_macro(self, name):
        name = name.strip().lower()
        sequence = self.macros.get(name)
        if not sequence:
            print(f"[MacroHandler] ❌ Unknown macro: {name}")
            return
        os.makedirs(GPT_GEN_FOLDER, exist_ok=True)
        for fname in sequence:
            content = file_map.get(fname)
            if content:
                with open(os.path.join(GPT_GEN_FOLDER, fname), "w") as f:
                    f.write(content)
                self._log(fname)
                print(f"[MacroHandler] ✅ Dropped via macro: {fname}")
            else:
                print(f"[MacroHandler] ⚠️ File not found in map: {fname}")

    def _log(self, fname):
        with open(VAULT_LOG, "a") as f:
            f.write(f"Dropped (macro): {fname}\n")