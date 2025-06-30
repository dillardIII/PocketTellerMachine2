# === FILE: ghost_installer_trigger.py ===
# 👻 GhostInstallerTrigger – Remotely launches the rebuild on the Predator

import subprocess

def deploy_repair():
    print("[GhostTrigger] 👻 Deploying Unreal Rebuild...")
    subprocess.run(["python3", "predator_ops_agent.py"], check=True)

if __name__ == "__main__":
    deploy_repair()