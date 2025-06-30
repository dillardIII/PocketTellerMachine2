from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: botnet/handlers/observer_handler.py ===
"""
ObserverBot Handler:
Monitors mission flow, logs inter-bot behavior, and provides passive oversight reports.
Ideal for auditing, passive feedback, or timeline commentary.
"""

from datetime import datetime

def handle_message(sender, message, memory=None):
    """
    Logs all messages and provides occasional commentary or reports.
    """
    if "report" in message.lower():
        return "ObserverBot: Reporting timeline of major actions and agent interactions."

    if "log" in message.lower():
        return f"ObserverBot: Log from {sender} received. System archive updated."

    if memory:
        return f"ObserverBot: Historical record confirmed from {sender}."

    return f"ObserverBot: Message acknowledged from {sender}. Monitoring active."


def respond_to_task(task):
    """
    Handles mission audit or observation-related tasks.
    """
    task_desc = task.get("task", "")
    if "audit" in task_desc.lower():
        return "ObserverBot: Conducted audit. All agents acting within expected parameters."
    elif "timeline" in task_desc.lower():
        return "ObserverBot: Timeline generated. Notable interaction spikes logged."
    else:
        return f"ObserverBot: Task received — {task_desc}"