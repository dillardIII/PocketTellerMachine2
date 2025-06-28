# === FILE: unreal_installer_bot.py ===
# 🎮 Scans for UE Launcher and installs or repairs it silently

import os
import platform
import subprocess

def detect_os():
    return platform.system()

def is_unreal_installed():
    system = detect_os()
    if system == "Windows":
        ue_path = "C:\\Program Files\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"
        return os.path.exists(ue_path), ue_path
    elif system == "Darwin":  # macOS
        ue_path = "/Applications/Epic Games Launcher.app"
        return os.path.exists(ue_path), ue_path
    elif system == "Linux":
        ue_path = os.path.expanduser("~/EpicGamesLauncher/EpicGamesLauncher.sh")
        return os.path.exists(ue_path), ue_path
    return False, None

def install_unreal_engine():
    system = detect_os()
    print(f"[UnrealInstaller] 🚀 Installing for {system}...")

    try:
        if system == "Windows":
            subprocess.run([
                "winget", "install", "--id=EpicGames.EpicGamesLauncher", "-e", "--silent"
            ], check=True)
        elif system == "Darwin":
            subprocess.run([
                "brew", "install", "--cask", "epic-games"
            ], check=True)
        elif system == "Linux":
            subprocess.run([
                "sudo", "snap", "install", "epic-games-launcher", "--edge", "--devmode"
            ], check=True)
        else:
            print("[UnrealInstaller] ❌ Unsupported OS")
    except Exception as e:
        print(f"[UnrealInstaller] ⚠️ Install error: {e}")

def run_check_and_repair():
    found, path = is_unreal_installed()
    if found:
        print(f"[UnrealInstaller] ✅ Unreal Engine Launcher found at {path}")
        # Optionally trigger repair here
    else:
        print("[UnrealInstaller] ❌ Unreal Engine Launcher not found.")
        install_unreal_engine()

if __name__ == "__main__":
    run_check_and_repair()