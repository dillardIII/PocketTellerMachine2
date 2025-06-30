from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: assistant_message_router.py ===
"""
Assistant Message Router:
Routes incoming messages to appropriate modules like reviewers, upgraders, or commenters.
Acts as a task dispatcher for PTM's internal assistant communication.
"""

from bot_inbox_handler import read_messages
from strategy_commenter import inject_inline_comments
from strategy_upgrader import auto_upgrade_strategy
from strategy_thread_logger import append_to_thread

def route_bot_tasks(bot_name):
    """
    Checks inbox for messages sent to this bot and dispatches tasks.
    """
    messages = read_messages(bot_name)

    for msg in messages:
        sender = msg.get("from")
        task = msg.get("task")
        payload = msg.get("payload", {})

        print(f"[Router] Handling task '{task}' from {sender} → {bot_name}")

        if task == "comment":
            file = payload.get("file")
            if file:
                commented_file = inject_inline_comments(file, reviewer=bot_name)
                if commented_file:
                    append_to_thread(file, "v1-comment", bot_name, "Injected inline suggestions.")
        elif task == "upgrade":
            file = payload.get("file")
            if file:
                upgraded_file = auto_upgrade_strategy(file, reviewer=bot_name)
                if upgraded_file:
                    append_to_thread(file, "v2-upgrade", bot_name, "Auto-upgraded strategy.")
        elif task == "log":
            file = payload.get("file")
            note = payload.get("note", "No comment.")
            append_to_thread(file, "vX-note", bot_name, note)
        else:
            print(f"[Router] ⚠️ Unknown task: {task}")

# === Local test ===
if __name__ == "__main__":
    route_bot_tasks("Mentor")
    route_bot_tasks("MoCash")
    route_bot_tasks("Strategist")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():