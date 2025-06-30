from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: test_voice_trigger.py ===
# 🧪 Voice Trigger Test – Runs voice-to-command routing using an audio file

from voice_trigger import VoiceTrigger

# Initialize the VoiceTrigger system
vt = VoiceTrigger()

# Run the file-based transcription and command dispatch
vt.transcribe_and_execute("voice_input.wav")

def log_event():ef drop_files_to_bridge():