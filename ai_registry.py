from ghost_env import INFURA_KEY, VAULT_ADDRESS
# ai_registry.py
# Purpose: Registry of all AI tools, personas, modules, and APIs for PTM introspection & coordination

import os
import json
from datetime import datetime
from utils.logger import log_event

REGISTRY_FILE = "memory/ai_registry.json"

class AIRegistry:
    def __init__(self):
        self.registry_path = REGISTRY_FILE
        self.data = self.load()

    def load(self):
        if not os.path.exists(self.registry_path):
            return {
                "personas": {},
                "tools": {},
                "external_apis": {},
                "last_update": str(datetime.now())
            }
        with open(self.registry_path, "r") as f:
            return json.load(f)

    def save(self):
        self.data["last_update"] = str(datetime.now())
        with open(self.registry_path, "w") as f:
            json.dump(self.data, f, indent=2)

    def register_persona(self, name, traits):
        self.data["personas"][name] = {
            "traits": traits,
            "active": True,
            "registered_at": str(datetime.now())
        }
        self.save()
        log_event("Persona Registered", {"name": name, "traits": traits})

    def register_tool(self, name, description):
        self.data["tools"][name] = {
            "description": description,
            "enabled": True,
            "registered_at": str(datetime.now())
        }
        self.save()
        log_event("Tool Registered", {"name": name, "description": description})

    def register_api(self, name, url, status="available"):
        self.data["external_apis"][name] = {
            "url": url,
            "status": status,
            "linked_at": str(datetime.now())
        }
        self.save()
        log_event("API Linked", {"name": name, "url": url, "status": status})

    def disable_tool(self, name):
        if name in self.data["tools"]:
            self.data["tools"][name]["enabled"] = False
            self.save()
            log_event("Tool Disabled", {"name": name})

    def get_summary(self):
        return {
            "personas": list(self.data["personas"].keys()),
            "tools": list(self.data["tools"].keys()),
            "apis": list(self.data["external_apis"].keys())
        }

# === Manual Test ===
if __name__ == "__main__":
    reg = AIRegistry()
    reg.register_persona("Strategist", ["tactical", "calm", "logical"])
    reg.register_tool("GhostForge", "Autonomous code writer and repair system")
    reg.register_api("Claude", "https://api.anthropic.com/v1/messages")
    print(json.dumps(reg.get_summary(), indent=2))