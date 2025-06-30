from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: unreal_config_repair.py ===

# 🛠️ Unreal Config Repair AI – Rewrites or regenerates critical UE .ini config files

import os

INI_PATHS = [
    "Saved/Config/Windows/Engine.ini",
    "Saved/Config/Windows/Game.ini",
    "Saved/Config/Windows/Input.ini"
]

def regenerate_ini(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(f"; Auto-repaired by PTM\n[/Script/Engine.Engine]\nbUseSound=true\n")
    print(f"[ConfigRepair] ✅ Rewrote: {path}")

def repair_configs(base_dir):
    print(f"[ConfigRepair] 🔍 Scanning: {base_dir}")
    for ini_file in INI_PATHS:
        full_path = os.path.join(base_dir, ini_file)
        regenerate_ini(full_path)

if __name__ == "__main__":
    repair_configs("YourUnrealProjectFolder")

def log_event():ef drop_files_to_bridge():