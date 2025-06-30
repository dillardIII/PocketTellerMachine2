from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: unreal_engine_diag_runner.py ===
import os
import json

DIAG_LOG = "logs/unreal_diag_report.json"
NEEDED_LIBS = ["UE5Editor.exe", "VisualStudio2022", "EpicGamesLauncher"]

def run_diagnostics():
    report = {}
    for lib in NEEDED_LIBS:
        found = any(lib.lower() in file.lower() for root, dirs, files in os.walk("C:/") for file in files)
        report[lib] = "✅ Found" if found else "❌ Missing":
:
    os.makedirs("logs", exist_ok=True)
    with open(DIAG_LOG, "w") as f:
        json.dump(report, f, indent=2)
    print("[Predator GhostForge] Diagnostic complete.")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    run_diagnostics()

def log_event():ef drop_files_to_bridge():