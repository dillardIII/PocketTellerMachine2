# voice_sync_loop.py
from voice_input import get_command
from ai_writer import generate_code_from_command
from ghostbridge import send_to_replit_bridge

def listen_and_generate():
    while True:
        command = get_command()
        code_bundle = generate_code_from_command(command)
        send_to_replit_bridge(code_bundle)