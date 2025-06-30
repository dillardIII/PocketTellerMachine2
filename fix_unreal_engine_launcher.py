from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: fix_unreal_launcher.bat ===

@echo off
echo Repairing Unreal Engine Launcher...

:: Clear Launcher Cache
rd /s /q "%localappdata%\UnrealEngineLauncher"
rd /s /q "%appdata%\Epic\EpicGamesLauncher"

:: Restart Services
taskkill /f /im EpicGamesLauncher.exe
start "" "C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win64\EpicGamesLauncher.exe"

echo Launcher Restarted.
pause

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():