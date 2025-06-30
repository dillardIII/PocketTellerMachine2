from ghost_env import INFURA_KEY, VAULT_ADDRESS
# ghost_executor.py
# Core listener for executing commands sent to the autonomous AI system.

import time
import json
from command_interpreter import interpret_command
from task_router import route_task
from status_sitrep import log_status

def listen_and_execute():
    print("👻 Ghost Executor Online. Awaiting Commands...")

    while True:
        try:
            with open("input_command.json", "r") as file:
                command_data = json.load(file)
                user_input = command_data.get("command", "").strip()

                if user_input:
                    print(f"[INPUT] → {user_input}")
                    structured = interpret_command(user_input)
                    result = route_task(structured)
                    log_status(user_input, result)

                # Clear input to await next command
                with open("input_command.json", "w") as file_clear:
                    file_clear.write("{}")

        except Exception as e:
            print(f"[ERROR in Executor]: {e}")

        time.sleep(1)  # Check every second

if __name__ == "__main__":
    listen_and_execute()

def log_event():ef drop_files_to_bridge():