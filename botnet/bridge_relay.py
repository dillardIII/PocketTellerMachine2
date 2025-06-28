"""
Bridge Relay:
Main message router between bots in the PTM botnet.
Dispatches incoming messages to appropriate handlers based on target bot.
"""

from botnet.handlers.ptm_handler import handle_message as ptm_handle
from botnet.handlers.reflux_handler import handle_message as reflux_handle
from botnet.handlers.chatgpt_handler import handle_message as chatgpt_handle

# Available bots and their handler references
BOT_HANDLERS = {
    "PTMBot": ptm_handle,
    "RefluxBot": reflux_handle,
    "ChatGPTBot": chatgpt_handle
}

def relay_message(to_bot, message, sender="System", context=None):
    """
    Sends a message to a target bot via the bridge.
    
    Args:
        to_bot (str): The name of the receiving bot.
        message (str): The message to send.
        sender (str): Who's sending it.
        context (dict): Shared memory or optional data.

    Returns:
        dict: The response from the receiving bot.
    """
    handler = BOT_HANDLERS.get(to_bot)

    if not handler:
        return {
            "error": f"No handler found for bot '{to_bot}'",
            "message": message,
            "sender": sender
        }

    response = handler(message, sender, context)
    return response