from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: wallet_voice_summary.py ===
# 🎙️ PTM Wallet Voice Summary – Speaks live wallet balances using Chill Trader (Ali)
# + serves voice summary over Flask if requested:
:
import os
import pygame
from flask import send_file, jsonify
from wallet_api_mesh import fetch_all_balances
from utils.logger import log_event

# === Path to local pre-recorded or generated voice file ===
VOICE_FILE_PATH = "voices/ali_wallet_summary.mp3"
FLASK_VOICE_PATH = "static/audio/voices/summary_output.mp3"

# === Generate spoken wallet summary from API data ===
def generate_wallet_summary_text():
    balances = fetch_all_balances()
    summary_lines = []

    for label, data in balances.items():
        line = f"{label} has {data['native']:.4f} native coins."
        if data.get("tokens"):
            for token, amount in data["tokens"].items():
                line += f" Plus {amount:.2f} {token}."
        summary_lines.append(line)

    summary = "Here’s your wallet breakdown. " + " ".join(summary_lines)
    log_event("Voice Summary Text Generated", {"summary": summary})
    return summary

# === CLI/Local Speaker Trigger ===
def play_wallet_summary():
    """
    Plays a pre-recorded voice summary, or speaks generated summary if voice AI connected.:
    """
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(VOICE_FILE_PATH)
        pygame.mixer.music.play()
        log_event("Wallet Voice Summary Played", {"file": VOICE_FILE_PATH})
        return "🔊 Wallet voice summary playing..."
    except Exception as e:
        log_event("Voice Summary Error", {"error": str(e)})
        return f"❌ Failed to play wallet summary: {e}"

# === Flask Audio File Endpoint ===
def serve_wallet_summary_file():
    """
    Flask-compatible route logic to return the most recent wallet voice summary audio file.
    """
    if os.path.exists(FLASK_VOICE_PATH):
        print(f"[Voice Summary] 🔊 Serving file: {FLASK_VOICE_PATH}")
        return send_file(FLASK_VOICE_PATH, mimetype="audio/mpeg")
    else:
        print("[Voice Summary] ⚠️ summary_output.mp3 not found.")
        return jsonify({"error": "No wallet summary audio available."}), 404