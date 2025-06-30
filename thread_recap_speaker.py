from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: thread_recap_speaker.py ===
import os
import json
from elevenlabs import generate, play, save  # Requires ElevenLabs API
from strategy_thread_logger import get_thread_log_path

def generate_recap_message(thread_file):
    if not os.path.exists(thread_file):
        return "Thread log not found."

    with open(thread_file, "r") as f:
        thread = json.load(f)

    summary = [f"Strategy Review for {thread['thread_id']}"]
    summary.append(f"Originated by {thread['originator']} on {thread['created']}")
    summary.append("")

    for entry in thread["history"]:
        summary.append(f"- {entry['version']} by {entry['submitted_by']} on {entry['timestamp']}")
        if entry.get("notes"):
            summary.append(f"  Note: {entry['notes']}")
        summary.append("")

    return "\n".join(summary)

def speak_thread_summary(thread_file, voice="default", save_path="static/audio/thread_summary.mp3"):
    recap = generate_recap_message(thread_file)
    audio = generate(text=recap, voice=voice)
    save(audio, save_path)
    print(f"[THREAD_RECAP] Recap generated and saved to {save_path}")
    return save_path

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():