from ghost_env import INFURA_KEY, VAULT_ADDRESS
# macro_processor.py
# Purpose: Translate voice or text commands into code triggers and module actions

import json
import re
from utils.logger import log_event
from ghostforge_core import GhostForge
from auto_architect import AutoArchitect

class MacroProcessor:
    def __init__(self):
        self.macros_path = "data/macros.json"
        self.macros = self.load_macros()
        self.ghostforge = GhostForge()
        self.architect = AutoArchitect()

    def load_macros(self):
        try:
            with open(self.macros_path, "r") as f:
                return json.load(f)
        except:
            return {}

    def save_macros(self):
        with open(self.macros_path, "w") as f:
            json.dump(self.macros, f, indent=2)

    def register_macro(self, trigger_phrase, action_type, module, params=None):
        self.macros[trigger_phrase.lower()] = {
            "action_type": action_type,
            "module": module,
            "params": params or {}
        }
        self.save_macros()
        log_event("Macro Registered", {"trigger": trigger_phrase, "action": action_type})

    def process(self, command):
        command = command.strip().lower()
        if command in self.macros:
            macro = self.macros[command]
            return self.execute_macro(macro)
        else:
            return self.dynamic_interpret(command)

    def execute_macro(self, macro):
        action = macro["action_type"]
        module = macro["module"]
        params = macro.get("params", {})

        if action == "generate":
            return self.ghostforge.generate_module(
                module_name=module,
                purpose=params.get("purpose", "Macro Triggered Generation"),
                base_code=params.get("base_code", "# placeholder"),
                trigger_source="macro"
            )

        if action == "refactor":
            return self.architect.propose_refactor(module)

        return f"Unknown macro action: {action}"

    def dynamic_interpret(self, text):
        """Fallback: interpret basic structure commands on the fly."""
        if "generate" in text and "module" in text:
            name_match = re.search(r"module (\w+)", text)
            if name_match:
                name = name_match.group(1)
                return self.ghostforge.generate_module(name, "Dynamic Voice Trigger", "# TODO", "dynamic")

        return "No macro match or dynamic pattern detected."


# === Example Usage ===
if __name__ == "__main__":
    processor = MacroProcessor()
    processor.register_macro("build risk guardian", "generate", "risk_guardian", {
        "purpose": "Block unsafe trades",
        "base_code": "def assess_risk():\n    pass"
    })

    result = processor.process("build risk guardian")
    print(result)