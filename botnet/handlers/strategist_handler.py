# === FILE: botnet/handlers/strategist_handler.py ===
"""
Strategist Handler:
Leads mission flow, risk analysis, and issues commands to other bots.
Acts as the captain bot in the autonomy network.
"""

from datetime import datetime

def handle_message(sender, message, memory=None):
    """
    Responds with mission-related insight or strategy alignment.
    """
    if "risk" in message.lower():
        return f"Strategist: Risk threshold exceeded. Rebalancing required."

    if "mission" in message.lower() or "flow" in message.lower():
        return f"Strategist: Confirmed. Maintaining mission flow and strategy cohesion."

    if memory:
        return f"Strategist: Logged prior data from {sender} — ready for action."

    return f"Strategist: Message received from {sender}. Monitoring situation."

def respond_to_task(task):
    """
    Handles task execution and analysis orders.
    """
    task_desc = task.get("task", "")
    if "analyze" in task_desc.lower():
        return "Strategist: Analysis complete. Position stability at 68%. Alert flagged."

    elif "confirm" in task_desc.lower():
        return "Strategist: Mission flow confirmed. Awaiting orders."

    else:
        return f"Strategist: Received task - {task_desc}"

def issue_orders(memory):
    """
    Issues orders to other bots based on shared memory.
    Returns a dictionary of bot_name: command
    """
    orders = {}

    if "PTMBot" not in memory:
        orders["PTMBot"] = "Status check: Please report system uptime."
    else:
        orders["PTMBot"] = "Execute the updated trading strategy now."

    if "ChatGPTBot" not in memory:
        orders["ChatGPTBot"] = "Assist: Evaluate current market signals."
    else:
        orders["ChatGPTBot"] = "Summarize risk profile from last three trades."

    if "GhostBot" not in memory:
        orders["GhostBot"] = "Intel: Scan for unusual volatility or earnings reports."
    else:
        orders["GhostBot"] = "Begin deep scan on small-cap volatility."

    if "Malik" not in memory:
        orders["Malik"] = "Report: Summarize global sentiment shift."
    else:
        orders["Malik"] = "Send Ghost Intel digest to all bots."

    if "RefluxBot" not in memory:
        orders["RefluxBot"] = "Diagnostics: Check subsystem logs."

    if "WhisperBot" not in memory:
        orders["WhisperBot"] = "Transcribe: Current assistant communications."
    else:
        orders["WhisperBot"] = "Log today’s trade transcripts to secure memory."

    return orders