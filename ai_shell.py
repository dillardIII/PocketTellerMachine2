"""
AI Shell – Autonomous Terminal Interface for PTM Assistants

Provides a programmable shell for AI assistants to issue commands,
test logic, inspect modules, or simulate internal tool use.
Bots can speak through the shell and receive responses.
"""

import sys
import traceback
from command_dispatcher import dispatch

def launch_shell():
    print("\n🧠 [PTM AI SHELL] Activated. Type 'exit' to quit.\n")
    while True:
        try:
            cmd = input("AI$ ").strip()
            if cmd.lower() in ["exit", "quit"]:
                print("[SHELL] Closing shell...")
                break
            elif cmd:
                dispatch(cmd)
        except KeyboardInterrupt:
            print("\n[SHELL] Manual interrupt. Type 'exit' to quit.")
        except Exception as e:
            print("[SHELL ERROR] Something went wrong:")
            traceback.print_exc()

# Entry point for direct run
if __name__ == "__main__":
    launch_shell()