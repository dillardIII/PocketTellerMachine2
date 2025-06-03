# deployment_task_manager.py – Manages automated deployment tasks across all environments

import time
import subprocess

class DeploymentTaskManager:
    def __init__(self):
        self.tasks = [
            {"name": "GitHub Sync", "command": ["python3", "sync_github_repo.py"]},
            {"name": "Render Deploy", "command": ["python3", "deploy_render_bot.py"]},
            {"name": "Replit Push", "command": ["python3", "replit_uploader.py"]},
            {"name": "VPS Bridge Start", "command": ["python3", "vps_bridge_controller.py"]},
            {"name": "Skypiea Uplink", "command": ["python3", "skypiea_bridge.py"]},
        ]

    def run_all(self):
        print("[DeployerBot] 🚀 Starting full deployment routine...")
        for task in self.tasks:
            print(f"[DeployerBot] ⚙️ Running task: {task['name']}")
            try:
                subprocess.run(task["command"], check=True)
                print(f"[DeployerBot] ✅ {task['name']} completed.")
            except subprocess.CalledProcessError as e:
                print(f"[DeployerBot] ❌ Task {task['name']} failed: {e}")

if __name__ == "__main__":
    manager = DeploymentTaskManager()
    manager.run_all()