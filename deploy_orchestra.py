# === FILE: deploy_orchestrator.py ===
# 🚀 Deploy Orchestrator – Triggers secondary builds, ghost drops, backups, or delayed modules

import os
from utils.logger import log_event

def deploy_all():
    print("[DeployOrchestrator] 🚀 Deploying delayed and staged modules...")
    staged_dir = "staged_deployments"
    deployed = []

    if os.path.exists(staged_dir):
        for filename in os.listdir(staged_dir):
            full_path = os.path.join(staged_dir, filename)
            if filename.endswith(".py"):
                dest = os.path.join(".", filename)
                with open(full_path, "r") as src, open(dest, "w") as dst:
                    dst.write(src.read())
                deployed.append(filename)
                os.remove(full_path)

    log_event("DeployRun", {"deployed": deployed})
    print(f"[DeployOrchestrator] ✅ Modules deployed: {deployed if deployed else 'None'}")