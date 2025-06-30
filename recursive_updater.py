from ghost_env import INFURA_KEY, VAULT_ADDRESS
# recursive_updater.py
# Purpose: Allow PTM to update, replicate, and evolve modules based on internal logic

import os
import json
from datetime import datetime
from utils.logger import log_event
from utils.file_utils import save_file

RECURSIVE_LOG = "memory/recursive_updates.json"

class RecursiveUpdater:
    def __init__(self):
        self.log_path = RECURSIVE_LOG
        self.history = self.load_log()

    def load_log(self):
        if not os.path.exists(self.log_path):
            return []
        with open(self.log_path, "r") as f:
            return json.load(f)

    def record_update(self, module_name, old_code, new_code, reason):
        entry = {
            "module": module_name,
            "timestamp": str(datetime.now()),
            "reason": reason,
            "diff_preview": self._diff_preview(old_code, new_code)
        }
        self.history.append(entry)
        self._save_log()
        log_event("Recursive Update", entry)

    def _save_log(self):
        with open(self.log_path, "w") as f:
            json.dump(self.history[-100:], f, indent=2)

    def _diff_preview(self, old, new):
        old_lines = old.splitlines()
        new_lines = new.splitlines()
        diff = []
        for i in range(min(len(old_lines), len(new_lines))):
            if old_lines[i] != new_lines[i]:
                diff.append({"line": i+1, "old": old_lines[i], "new": new_lines[i]})
        return diff[:10]  # limit preview

    def inject_patch_log(self, files_fixed):
        for f in files_fixed:
            with open(f, "r") as fp:
                content = fp.read()
            self.record_update(os.path.basename(f), "", content, reason="Self-healing patch")

    def refactor_module(self, filename, transform_func, reason="Refactor"):
        if not os.path.exists(filename):
            log_event("Refactor Failed", {"file": filename, "reason": "File not found"})
            return False
        with open(filename, "r") as f:
            old_code = f.read()
        new_code = transform_func(old_code)
        with open(filename, "w") as f:
            f.write(new_code)
        self.record_update(os.path.basename(filename), old_code, new_code, reason)
        return True

# === Manual Test ===
if __name__ == "__main__":
    updater = RecursiveUpdater()
    def transform(code):
        return code.replace("print(", "log_event('print(intercepted',");  # silly test)

    updater.refactor_module("example_module.py", transform, "Sample refactor injection")