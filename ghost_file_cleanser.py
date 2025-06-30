#!/usr/bin/env python3
# ghost_file_cleanser.py
# 🔥 Mutates + cleans empire files automatically

import os
import re

FIXES = [
    (r"def ([a-zA-Z_][a-zA-Z0-9_]*)\s*\(.*\)\s*[^:]", r"def \1():"),
    (r"(if .*[^:])\n", r"\1:\n"),
    (r"(elif .*[^:])\n", r"\1:\n"),
    (r"(else[^:])\n", r"\1:\n"),
    (r"print ([^\(].*)", r"print(\1)")
]

DUMMY_STUBS = """
def log_event(data): print(f'[GhostEmpire] LOG: {data}')
def mutate(*args, **kwargs): print('[GhostEmpire] Dummy mutate called')
def drop_files_to_bridge(*args, **kwargs): print('[GhostEmpire] Dummy drop_files_to_bridge called')
"""

def apply_fixes(content):
    for pattern, repl in FIXES:
        content = re.sub(pattern, repl, content)
    return content

def inject_stubs(content):
    if "log_event" not in content:
        content += "\n" + DUMMY_STUBS
    return content

def cleanse_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    original_content = content
    content = apply_fixes(content)
    content = inject_stubs(content)
    if content != original_content:
        with open(file_path, "w") as f:
            f.write(content)
        print(f"[ghost_file_cleanser] 🧼 Cleaned & mutated: {file_path}")

def run_cleanser():
    files = [f for f in os.listdir(".") if f.endswith(".py") and f != "ghost_file_cleanser.py"]
    for f in files:
        cleanse_file(f)

if __name__ == "__main__":
    run_cleanser()
    print("[ghost_file_cleanser] ✅ Empire mutation complete.")