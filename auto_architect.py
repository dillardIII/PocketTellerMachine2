# auto_architect.py
# Purpose: Code refactoring and architecture generator for PTM
# Allows PTM to analyze its codebase and write upgrade proposals or new structures

import os
import json
import ast
from datetime import datetime
from utils.logger import log_event
from utils.file_utils import read_file, save_file

ARCHITECT_LOG = "memory/auto_architect_log.json"

class AutoArchitect:
    def __init__(self):
        self.history = []
        self.log_path = ARCHITECT_LOG
        self.load_log()

    def load_log(self):
        if os.path.exists(self.log_path):
            with open(self.log_path, "r") as f:
                self.history = json.load(f)

    def log_action(self, file, changes, reason):
        entry = {
            "timestamp": str(datetime.now()),
            "file": file,
            "reason": reason,
            "changes": changes
        }
        self.history.append(entry)
        with open(self.log_path, "w") as f:
            json.dump(self.history[-100:], f, indent=2)
        log_event("AutoArchitect Update", entry)

    def analyze_code(self, filepath):
        """Reads Python file, returns parsed AST and summary."""
        try:
            code = read_file(filepath)
            tree = ast.parse(code)
            functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
            classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
            return {
                "functions": functions,
                "classes": classes,
                "lines": len(code.splitlines())
            }
        except Exception as e:
            return {"error": str(e)}

    def propose_refactor(self, filepath):
        summary = self.analyze_code(filepath)
        if "error" in summary:
            return {"status": "fail", "reason": summary["error"]}

        refactor_ideas = []

        if summary["lines"] > 300:
            refactor_ideas.append("Split file into multiple modules based on function groups.")

        if len(summary["functions"]) > 10:
            refactor_ideas.append("Group related functions into classes or helper modules.")

        if not summary["classes"]:
            refactor_ideas.append("Convert procedural code into object-oriented structure.")

        self.log_action(filepath, refactor_ideas, "Auto-scan for architecture improvement")

        return {
            "status": "success",
            "file": filepath,
            "ideas": refactor_ideas,
            "summary": summary
        }

    def apply_template(self, filename, new_structure_code, reason="template upgrade"):
        full_path = os.path.join("generated_structures", filename)
        os.makedirs("generated_structures", exist_ok=True)
        save_file(full_path, new_structure_code)
        self.log_action(full_path, "Template applied", reason)
        return full_path


# === Manual Run Example ===
if __name__ == "__main__":
    architect = AutoArchitect()
    result = architect.propose_refactor("core/main.py")
    print(json.dumps(result, indent=2))