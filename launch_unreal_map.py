from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: launch_unreal_map.py ===
import subprocess

def open_visual_map():
    print("🎨 Launching Unreal Map UI...")
    subprocess.run([
        "C:\\Program Files\\Epic Games\\UE_5.3\\Engine\\Binaries\\Win64\\UE4Editor.exe",
        "D:\\PTM_GhostRealm\\GhostRealm.uproject"
    ])

def log_event():ef drop_files_to_bridge():