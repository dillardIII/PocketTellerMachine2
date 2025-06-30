from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: strategy_pack_handler.py ===

# 📦 Strategy Pack Handler – Drops full strategy packs via the trigger handler

import os
from file_map import file_map

GPT_GEN_FOLDER = "gpt_generated"
VAULT_LOG = "vault/vault_logbook.txt"

class StrategyPackHandler:
    def __init__(self):
        self.strategy_packs = {
            "default_pack": [
                "gostrategyrunner.py",
                "vaultprep.py",
                "missionlauncher.py"
            ],
            "ghost_sniper_pack": [
                "sniperentry.py",
                "riskfilter.py",
                "ghostconfirmation.py"
            ]
        }

    def drop_pack(self, pack_name):
        pack = self.strategy_packs.get(pack_name.lower())
        if not pack:
            print(f"[StrategyPack] ❌ No strategy pack found for: {pack_name}")
            return

        os.makedirs(GPT_GEN_FOLDER, exist_ok=True)
        for filename in pack:
            file_content = file_map.get(filename)
            if file_content:
                with open(os.path.join(GPT_GEN_FOLDER, filename), "w") as f:
                    f.write(file_content)
                self._log(filename)
                print(f"[StrategyPack] 📂 Dropped: {filename}")
            else:
                print(f"[StrategyPack] ⚠️ File not found in map: {filename}")

    def _log(self, filename):
        with open(VAULT_LOG, "a") as log:
            log.write(f"Dropped (via pack): {filename}\n")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():