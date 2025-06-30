# === FILE: reflex_mutator.py ===
# 🧬 Reflex Mutator – Watches files and rewrites broken code autonomously

import os
import time
import hashlib

class ReflexMutator:
    def __init__(self, watch_dir="ptm_inbox", interval=3):
        self.watch_dir = watch_dir
        self.interval = interval
        self.known_hashes = {}

    def _file_hash(self, filepath):
        with open(filepath, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()

    def _is_corrupted(self, content):
        return any([
            "Traceback" in content,
            "SyntaxError" in content,
            "ModuleNotFoundError" in content,
            "unexpected indent" in content
        ])

    def begin_mutation_loop(self):
        print("[ReflexMutator] 🔁 Mutation loop started...")
        while True:
            for file in os.listdir(self.watch_dir):
                if file.endswith(".py"):
                    path = os.path.join(self.watch_dir, file)
                    current_hash = self._file_hash(path)
                    if self.known_hashes.get(file) != current_hash:
                        self.known_hashes[file] = current_hash
                        with open(path, "r") as f:
                            content = f.read()
                        if self._is_corrupted(content):
                            print(f"[ReflexMutator] 🧠 Detected issue in {file}... rewriting.")
                            self._mutate(path, content)
            time.sleep(self.interval)

    def _mutate(self, path, content):
        fixed = self._ai_fix(content)
        with open(path, "w") as f:
            f.write(fixed)
        print(f"[ReflexMutator] 🛠️ Rewritten and saved: {os.path.basename(path)}")

    def _ai_fix(self, content):
        # Simulated AI fix for now – insert your GPT call here if connected.
        return "# 🔁 Auto-fixed version:\n" + content.replace("unexpected indent", "    ")