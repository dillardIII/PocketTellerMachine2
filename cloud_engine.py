from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cloud_engine.py
# Initializes Skypia cloud system core and command interface

import os
import json
import platform
import uuid
from datetime import datetime

class CloudEngine:
    def __init__(self, name="Skypia"):
        self.name = name
        self.id = str(uuid.uuid4())
        self.status = "initialized"
        self.created_at = datetime.utcnow().isoformat()
        self.system_info = self._gather_system_info()
        self.commands = []

    def _gather_system_info(self):
        return {
            "system": platform.system(),
            "node": platform.node(),
            "release": platform.release(),
            "version": platform.version(),
            "processor": platform.processor(),
        }

    def register_command(self, command_str):
        print(f"[{self.name}] Command registered: {command_str}")
        self.commands.append({
            "command": command_str,
            "timestamp": datetime.utcnow().isoformat()
        })

    def run_command(self, command_str):
        try:
            print(f"[{self.name}] Executing: {command_str}")
            result = os.popen(command_str).read()
            self.register_command(command_str)
            return result
        except Exception as e:
            return f"[ERROR] {e}"

    def get_status(self):
        return {
            "id": self.id,
            "status": self.status,
            "created_at": self.created_at,
            "system": self.system_info,
            "commands_run": len(self.commands)
        }

    def export_log(self, path="skypia_log.json"):
        with open(path, "w") as f:
            json.dump({
                "id": self.id,
                "created_at": self.created_at,
                "commands": self.commands
            }, f, indent=2)
        return path

# Example Usage
if __name__ == "__main__":
    engine = CloudEngine()
    print(engine.get_status())
    result = engine.run_command("echo Skypia online.")
    print(result)
    engine.export_log()

def log_event():ef drop_files_to_bridge():