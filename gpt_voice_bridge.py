from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: gpt_voice_bridge.py ===
# 🎙️ GPT Voice Bridge – Converts GPT text into spoken MP3 output & handles voice command relay

import os
import uuid
import socket
import json
import time
import threading
import requests
from datetime import datetime
from pathlib import Path
from elevenlabs import generate, save
from cole_gpt_advisor import ask_gpt

# 📁 Voice output folders
STATIC_AUDIO_FOLDER = "static/audio"
SDK_AUDIO_FOLDER = "audio_responses"
os.makedirs(STATIC_AUDIO_FOLDER, exist_ok=True)
os.makedirs(SDK_AUDIO_FOLDER, exist_ok=True)

# 🔧 Default voice config
VOICE_NAME = "Mo Cash"  # Change to: Mentor, OG, Strategist, etc.
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "EXAVITQu4vr4xnSDxMaL")

# 🎧 Socket config
VOICE_PORT = 5052
HOST = "127.0.0.1"
BUFFER_SIZE = 2048
voice_queue = []

# === 🔊 GPT to Voice via ElevenLabs SDK ===
def speak_gpt_response(prompt_text):
    print("[GPT Voice] Generating spoken response...")
    gpt_response = ask_gpt(prompt_text)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{SDK_AUDIO_FOLDER}/gpt_response_{timestamp}.mp3"

    try:
        audio = generate(text=gpt_response, voice=VOICE_NAME)
        save(audio, filename)
        print(f"[GPT Voice] ✅ Saved: {filename}")
        return {"response": gpt_response, "file": filename}
    except Exception as e:
        print(f"[GPT Voice] ❌ SDK error: {e}")
        return {"response": gpt_response, "error": str(e)}

# === 🧪 API Fallback – Direct ElevenLabs API call ===
def speak_gpt_response_api(text):
    if not ELEVENLABS_API_KEY:
        raise ValueError("Missing ELEVENLABS_API_KEY in environment.")
    if not text:
        raise ValueError("No text provided to speak.")

    print(f"[VOICE BRIDGE] 🎤 Synthesizing speech via API...")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        filename = f"gpt_voice_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex}.mp3"
        filepath = os.path.join(STATIC_AUDIO_FOLDER, filename)
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"[VOICE BRIDGE] ✅ API MP3 saved: {filepath}")
        return filepath
    except Exception as e:
        print(f"[VOICE BRIDGE] ❌ API error: {e}")
        return None

# === 🧠 Voice Bridge Socket Server ===
def receive_voice_commands():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, VOICE_PORT))
        server.listen()
        print(f"[VOICE BRIDGE] 🎧 Listening on {HOST}:{VOICE_PORT}...")
        while True:
            client, _ = server.accept()
            threading.Thread(target=handle_client, args=(client,), daemon=True).start()

def handle_client(client_socket):
    try:
        data = client_socket.recv(BUFFER_SIZE).decode("utf-8")
        voice_data = json.loads(data)
        print(f"[VOICE BRIDGE] 🔊 Received: {voice_data}")
        voice_queue.append(voice_data)
    except Exception as e:
        print(f"[VOICE BRIDGE] ⚠️ Error: {e}")
    finally:
        client_socket.close()

def playback_loop():
    while True:
        if voice_queue:
            message = voice_queue.pop(0)
            speak_text(message.get("text", ""))
        time.sleep(1)

def speak_text(text):
    print(f"[GPT VOICE] 🗣️ Speaking: {text}")
    # Optional: play local MP3, stream audio, or connect to frontend

def start_voice_bridge():
    threading.Thread(target=receive_voice_commands, daemon=True).start()
    threading.Thread(target=playback_loop, daemon=True).start()
    print("[GPT VOICE] ✅ Voice bridge active")

if __name__ == "__main__":
    start_voice_bridge()
    while True:
        time.sleep(60)

def log_event():ef drop_files_to_bridge():