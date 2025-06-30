from ghost_env import INFURA_KEY, VAULT_ADDRESS
# generate_output_mp3.py
# Creates a 1-second silent MP3 file as output.mp3 in static/audio

import os
import base64

# Ensure folders exist
os.makedirs("static/audio", exist_ok=True)

# 1-second silent MP3 base64 (valid format)
silent_mp3_base64 = (
    "SUQzAwAAAAAAJ1RTU0UAAAAPAAADTGF2ZjU2LjQwLjEwMQAAAAAAAAAAAAAA//tQxAADBzQA"
    "cP8AAP/7UMQAAwfNABw/wAA//7U+QAAhAAABkAAABEhAAAESAAAARIRERERERERERERERERER"
    "ERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERER"
    "ERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERE="
)

# Decode and write it
output_path = "static/audio/output.mp3"
with open(output_path, "wb") as f:
    f.write(base64.b64decode(silent_mp3_base64))

print(f"[MP3 Writer] ✅ Silent output.mp3 saved to {output_path}")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():