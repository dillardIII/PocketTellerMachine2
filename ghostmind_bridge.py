# ghostmind_bridge.py
# Purpose: External AI coordination and system sync layer (Claude, Replit, GitHub, Render)

import os
import json
import requests
from utils.logger import log_event

class GhostMindBridge:
    def __init__(self):
        self.routes_path = "config/bridge_routes.json"
        self.routes = self.load_routes()
        self.headers = {"Content-Type": "application/json"}

    def load_routes(self):
        if not os.path.exists(self.routes_path):
            return {
                "claude": "https://api.anthropic.com/v1/messages",
                "replit": "https://api.replit.com/v0/project/deploy",
                "render": "https://api.render.com/v1/deploy",
                "github": "https://api.github.com/repos/username/project/contents/"
            }
        with open(self.routes_path, "r") as f:
            return json.load(f)

    def send_to_claude(self, prompt):
        data = {
            "model": "claude-3-opus-20240229",
            "max_tokens": 300,
            "messages": [{"role": "user", "content": prompt}]
        }
        try:
            response = requests.post(self.routes["claude"], headers=self.headers, json=data)
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    def push_to_github(self, filename, content, commit_message="Auto-update from PTM"):
        url = self.routes["github"] + filename
        encoded_content = content.encode("utf-8").decode("utf-8")
        payload = {
            "message": commit_message,
            "content": encoded_content,
            "branch": "main"
        }
        try:
            response = requests.put(url, headers=self.headers, json=payload)
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    def deploy_to_replit(self):
        try:
            response = requests.post(self.routes["replit"], headers=self.headers)
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    def trigger_render_redeploy(self):
        try:
            response = requests.post(self.routes["render"], headers=self.headers)
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    def run_bridge_command(self, cmd):
        if cmd == "update claude":
            return self.send_to_claude("What files are needed for AI autonomy?")
        elif cmd == "push latest":
            # Placeholder — actual use will loop through files
            return self.push_to_github("auto_module.py", "# Sample content")
        elif cmd == "replit deploy":
            return self.deploy_to_replit()
        elif cmd == "render trigger":
            return self.trigger_render_redeploy()
        else:
            return {"status": "Unknown command"}

# === Manual Test ===
if __name__ == "__main__":
    bridge = GhostMindBridge()
    print(bridge.run_bridge_command("update claude"))