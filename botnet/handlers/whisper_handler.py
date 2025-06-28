# === FILE: botnet/handlers/whisper_handler.py ===
"""
WhisperBot Handler:
Handles transcription tasks, voice-to-text processing, and assistant communication logging.
Supports real-time message parsing and memory-aware feedback.
"""

from datetime import datetime

def handle_message(sender, message, memory=None):
    """
    Responds to log or transcription requests.
    If memory exists, can reference past audio or text captures.
    """
    if "transcribe" in message.lower():
        return "WhisperBot: Starting transcription... Audio input queued."

    if "log" in message.lower() or "conversation" in message.lower():
        return "WhisperBot: Conversation log active. Storing dialog for system memory."

    if memory:
        last_entry = memory.get(sender, "No prior logs from this bot.")
        return f"WhisperBot: Previously logged from {sender} — \"{last_entry}\""

    return f"WhisperBot: Message received from {sender}. Ready for voice parsing."


def respond_to_task(task):
    """
    Handles direct transcription or memory processing tasks.
    """
    task_desc = task.get("task", "")
    if "transcribe" in task_desc.lower():
        return "WhisperBot: Transcription task complete. Text data saved to shared memory."
    elif "log" in task_desc.lower():
        return "WhisperBot: Assistant dialog logs updated successfully."
    else:
        return f"WhisperBot: Task acknowledged — {task_desc}"