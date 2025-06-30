from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: whisper_transcriber.py ===

# 📜 Whisper Transcriber – Converts spoken audio to command text

import whisper

def transcribe_audio_to_text(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    print(f"[Transcriber] 📝 {result['text']}")
    return result["text"]

def log_event():ef drop_files_to_bridge():