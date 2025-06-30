from ghost_env import INFURA_KEY, VAULT_ADDRESS
# voice_sync_loop.py
from voice_input import get_command
from ai_writer import generate_code_from_command
from ghostbridge import send_to_replit_bridge

def listen_and_generate():
    while True:
        command = get_command()
        code_bundle = generate_code_from_command(command)
        send_to_replit_bridge(code_bundle)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():