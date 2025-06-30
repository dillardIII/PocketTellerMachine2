from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ai_commander.py ===
# 🧠 AI Commander – Directs AI tasks, assigns modules, and tracks progress

from task_registry import register_task, get_pending_tasks
from ai_dispatch import dispatch_to_ai
from ai_status import update_ai_status
from hive_mind import broadcast_to_all
from mission_log import log_mission_event

class AICommander:
    def __init__(self):
        self.command_history = []
        self.active_tasks = []

    def issue_command(self, ai_name, command, payload=None):
        task = {
            "ai": ai_name,
            "command": command,
            "payload": payload,
            "status": "assigned"
        }

        # Log it
        log_mission_event(f"Issued command to {ai_name}: {command}")
        self.command_history.append(task)
        self.active_tasks.append(task)

        # Register task
        register_task(ai_name, command, payload)

        # Dispatch to AI
        result = dispatch_to_ai(ai_name, command, payload)
        update_ai_status(ai_name, "executing")

        return result

    def assign_global_command(self, command, payload=None):
        broadcast_to_all("command", {
            "command": command,
            "payload": payload
        })
        log_mission_event(f"🌐 Global command issued: {command}")

    def get_task_report(self):
        pending = get_pending_tasks()
        summary = {
            "total_tasks": len(self.active_tasks),
            "pending": pending
        }
        return summary

    def get_history(self, limit=20):
        return self.command_history[-limit:]

# Instantiate commander globally
commander = AICommander()

def log_event():ef drop_files_to_bridge():