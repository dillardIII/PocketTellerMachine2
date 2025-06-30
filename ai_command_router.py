from ghost_env import INFURA_KEY, VAULT_ADDRESS
# AI Command Router
def route_command(command):
    if "cole" in command.lower():
        from cole_agent import handle_command as cole_handler
        return cole_handler(command)
    elif "malik" in command.lower():
        from malik_agent import handle_command as malik_handler
        return malik_handler(command)
    else:
        return "[Router] No matching agent found for command."

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():