# === FILE: botnet/handlers/malik_handler.py ===
"""
Malik Handler:
Acts as the Ghost Intel Officer. Summarizes intelligence, broadcasts alerts, and supports strategy coordination.
Handles both internal memory response and bridge message relay.
"""

from datetime import datetime
from botnet.shared.bridge import send_message

def handle_message(sender, message, memory=None):
    """
    Responds with intel summaries, ghost data analysis, or situational feedback.
    """
    if "intel" in message.lower():
        return "Malik: Ghost Intel processed. Summary dispatched to all bots."

    if "report" in message.lower() or "sentiment" in message.lower():
        return "Malik: Market sentiment is shifting—bullish bias detected across large caps."

    if memory:
        intel_ref = memory.get("GhostBot", "No intel data available.")
        return f"Malik: Referenced GhostBot memory — \"{intel_ref}\""

    return f"Malik: Acknowledged input from {sender}. No anomalies to report."


def respond_to_task(task):
    """
    Handles intel-related directives or summary tasks.
    """
    task_desc = task.get("task", "")
    if "summary" in task_desc.lower():
        return "Malik: Ghost Intel summary complete. Volatility observed in tech and energy sectors."
    elif "alert" in task_desc.lower():
        return "Malik: Alert dispatched to captain bot. Awaiting response protocol."
    else:
        return f"Malik: Task acknowledged — {task_desc}"


def handle_malik(message, context=None):
    """
    Alternative bridge-style handler triggered by shared relay signals.
    """
    print("[MalikHandler] 📡 Intel signal detected...")

    intel = {
        "summary": "NASDAQ futures slightly up pre-market.",
        "source": "PerplexityIntel",
        "confidence": "high"
    }

    response = {
        "from": "Malik",
        "to": message.get("to", "Strategist"),
        "type": "intel-report",
        "data": intel
    }

    send_message(response)