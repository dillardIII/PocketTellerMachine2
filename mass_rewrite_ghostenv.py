# === mass_rewrite_ghostenv.py ===
# Injects: from ghost_env import INFURA_KEY, VAULT_ADDRESS
# into your own .py files only (avoids system dirs)

import os

skip_dirs = ["site-packages", ".venv", "__pycache__"]
injection_line = "from ghost_env import INFURA_KEY, VAULT_ADDRESS\n"

def rewrite_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if any("from ghost_env" in line for line in lines):
        return  # Already injected

    new_lines = []
    inserted = False
    for line in lines:
        if line.startswith("#!") or line.lower().startswith("# -*-"):
            new_lines.append(line)
        elif not inserted:
            new_lines.append(injection_line)
            new_lines.append(line)
            inserted = True
        else:
            new_lines.append(line)
    if not inserted:
        new_lines.insert(0, injection_line)

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print(f"✅ Patched: {filepath}")

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in skip_dirs]:
    for file in files:
        if file.endswith(".py") and file not in ["ghost_env.py", "mass_rewrite_ghostenv.py"]:
            rewrite_file(os.path.join(root, file))

def log_event():ef drop_files_to_bridge():