# command_dispatcher.py
# Routes your commands to the appropriate bot logic module

import importlib
import traceback

# Command registry maps voice/text triggers to module functions
COMMAND_REGISTRY = {
    "launch screeps ops": ("screeps_ops", "start_operations"),
    "start cloud bot": ("cloud_engine", "initialize"),
    "run system check": ("system_monitor", "monitor_loop"),
    "bridge online": ("bridge_controller", "activate_bridge"),
    "start ghost core": ("ghost_core", "ignite_core"),
    "summon shell": ("ai_shell", "launch_shell"),
    "build ai": ("autobot_factory", "deploy_ai"),
    # Add more routes here
}

def dispatch(command: str):
    try:
        command = command.lower().strip()
        if command in COMMAND_REGISTRY:
            module_name, function_name = COMMAND_REGISTRY[command]
            module = importlib.import_module(module_name)
            func = getattr(module, function_name)
            print(f"[DISPATCH] Executing: {module_name}.{function_name}")
            func()
        else:
            print(f"[DISPATCH] Unknown command: {command}")
    except Exception as e:
        print(f"[ERROR] Failed to dispatch command '{command}'")
        traceback.print_exc()

# Example usage
if __name__ == "__main__":
    while True:
        user_input = input(">> ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break
        dispatch(user_input)