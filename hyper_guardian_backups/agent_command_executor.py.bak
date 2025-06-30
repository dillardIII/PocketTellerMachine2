# === FILE: agent_command_executor.py ===
import time
from ptm_message_relay import receive_messages

def run_executor(bot_name):
    print(f"🤖 [{bot_name}] Awaiting commands...")
    while True:
        messages = receive_messages(bot_name)
        for msg in messages:
            print(f"📨 [{bot_name}] Received from {msg['from']}: {msg['command']}")
            # TODO: Expand with logic for actual command execution
        time.sleep(5)