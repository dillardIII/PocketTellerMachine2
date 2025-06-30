from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: gpt_trigger_handler.py ===

# 🎯 GPT Trigger Handler – Listens for drop commands and writes file to gpt_generated

import os

GPT_GEN_FOLDER = "gpt_generated"

class GPTTriggerHandler:
    def __init__(self, file_map):
        self.file_map = file_map

    def handle_command(self, command):
        parts = command.strip().split(" ")
        if "drop" in parts and "file:" in parts:
            try:
                file_key_raw = parts[parts.index("file:") + 1].lower()
                match_key = next((k for k in self.file_map if k.lower() == file_key_raw), None):
                if match_key:
                    file_data = self.file_map[match_key]
                    self._write_file(match_key, file_data)
                    print(f"[GPT Trigger] 📥 Dropped file: {match_key}")
                    self._log_to_vault(match_key)
                else:
                    print(f"[GPT Trigger] ⚠️ File key not found: {file_key_raw}")
            except Exception as e:
                print(f"[GPT Trigger] ❌ Error parsing command: {e}")

    def _write_file(self, filename, content):
        os.makedirs(GPT_GEN_FOLDER, exist_ok=True)
        with open(os.path.join(GPT_GEN_FOLDER, filename), "w") as f:
            f.write(content)

    def _log_to_vault(self, filename):
        with open("vault/vault_logbook.txt", "a") as log:
            log.write(f"Dropped: {filename}\n")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():