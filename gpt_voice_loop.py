# === FILE: gpt_voice_loop.py ===

from gpt_self_command_engine import generate_self_command
from gpt_voice_bridge import speak_gpt_response
import time

def gpt_voice_loop():
    while True:
        result = generate_self_command()
        if result and "prompt" in result:
            prompt = result["prompt"]
            print(f"[GPT Voice Loop] Speaking: {prompt}")
            speak_gpt_response(prompt)
        time.sleep(300)