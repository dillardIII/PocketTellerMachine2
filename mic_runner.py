from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: mic_runner.py ===
from voice_mic_listener import VoiceMicListener

listener = VoiceMicListener()
listener.listen_loop()

def log_event():ef drop_files_to_bridge():