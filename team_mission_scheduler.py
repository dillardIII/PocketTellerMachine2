from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: team_mission_scheduler.py ===
"""
Team Mission Scheduler:
Receives parsed instructions and dispatches actions to the appropriate bot or module.
Connects voice commands to actual behavior.
"""

from cole_brain import log_memory
from voice_response_dispatcher import speak_response
from strategy_upgrader import auto_upgrade_strategy
from inline_commenter import inject_inline_comments
from strategy_thread_logger import append_to_thread

def schedule_mission(parsed_command):
    """
    Takes parsed voice input and determines which module or bot to activate.
    """
    intent = parsed_command.get("intent")
    target = parsed_command.get("target")
    content = parsed_command.get("content")
    timestamp = parsed_command.get("timestamp")

    # === Log it to memory ===
    log_memory("voice_command", {
        "intent": intent,
        "target": target,
        "content": content,
        "timestamp": timestamp
    })

    print(f"[🛰️ Scheduler] Intent: {intent} | Target: {target}")

    # === Handle Intent Routing ===
    response = ""

    if intent == "upgrade":
        strategy_path = "data/strategies/last_strategy.py"
        upgraded = auto_upgrade_strategy(strategy_path, reviewer=target)
        if upgraded:
            append_to_thread("last_strategy.py", "v2", reviewer=target, notes="Auto-upgraded via voice")
            response = f"{target}, your upgrade has been applied to the latest strategy."
        else:
            response = f"{target}, upgrade failed or nothing needed changing."

    elif intent == "review":
        strategy_path = "data/strategies/last_strategy.py"
        commented = inject_inline_comments(strategy_path, reviewer=target)
        if commented:
            append_to_thread("last_strategy.py", "v1.1", reviewer=target, notes="Inline comments added")
            response = f"{target}, the strategy was reviewed and comments were added."
        else:
            response = f"{target}, no patterns found worth commenting."

    elif intent == "status":
        response = f"{target}, your latest memory and trade status is being fetched..."

    elif intent == "build":
        response = f"{target}, building procedures initiated. Dispatching strategy builder soon."

    elif intent == "summarize":
        response = f"{target}, a summary is being generated from the last memory event."

    else:
        response = "Sorry, I couldn't understand what to do with that command."

    # === Voice or text response ===
    speak_response(response)

    return response

# === Manual Test ===
if __name__ == "__main__":
    mock = {
        "intent": "upgrade",
        "target": "Mo Cash",
        "content": "Mo Cash, upgrade the strategy file now",
        "timestamp": "2025-06-04T00:00:00Z"
    }
    schedule_mission(mock)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():