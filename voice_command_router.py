# === FILE: voice_command_router.py ===
# 🗣️ Voice Command Router – Converts user speech into executable PTM commands

import json
from assistant_dispatch import AssistantDispatch
from executor_engine import execute_pending_tasks
from reflex_engine import ReflexEngine
from ghostforge_core import GhostForge
from utils.logger import log_event

class VoiceCommandRouter:
    def __init__(self):
        self.dispatch = AssistantDispatch()
        self.reflex = ReflexEngine()
        self.forge = GhostForge()

    def handle_voice_command(self, command_text):
        command = command_text.strip().lower()
        log_event(f"🎙️ Voice Command Received: {command}")

        # Simple routing logic (expandable)
        if "status" in command or "report" in command:
            self.dispatch.speak("System status is green across all subsystems.")
        
        elif "run reflex" in command:
            self.dispatch.speak("Activating reflex engine.")
            self.reflex.scan_environment()
        
        elif "generate" in command and "module" in command:
            self.dispatch.speak("Spawning GhostForge to generate a new module.")
            self.forge.generate_module("auto_generated", "On-demand voice spawn", "# TODO: Fill logic here", "voice")

        elif "run tasks" in command:
            self.dispatch.speak("Executing all pending tasks.")
            execute_pending_tasks()

        elif "stop listening" in command:
            self.dispatch.speak("Stopping voice command listener.")
            return "STOP"

        else:
            self.dispatch.speak("I heard you, but I didn’t understand that command yet.")

        return "OK"