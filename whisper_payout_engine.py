from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: whisper_payout_engine.py ===
# 🎤 Whisper + Vault Payout Engine for PTM

import threading
import time
import json
import random

try:
    import sounddevice as sd
    import whisper
except ImportError:
    print("[Whisper] ⚠️ Please install whisper & sounddevice: pip install openai-whisper sounddevice")

# === Whisper Voice Listener ===
def start_whisper_listener():
    print("[Whisper] 🎤 Voice listener activated. Say something like 'trigger payout'.")
    try:
        model = whisper.load_model("base")
    except Exception as e:
        print(f"[Whisper] ⚠️ Could not load Whisper model: {e}")
        return

    while True:
        print("[Whisper] 🎧 Listening...")
        recording = sd.rec(int(5 * 16000), samplerate=16000, channels=1)
        sd.wait()
        audio_path = "whisper_temp.wav"
        sd.write(audio_path, recording, 16000)
        result = model.transcribe(audio_path)
        command = result["text"].strip().lower()
        print(f"[Whisper] 🗣️ You said: '{command}'")
        
        if "trigger payout" in command:
            payout_engine()
        elif "run vault scan" in command:
            vault_scan()
        else:
            print("[Whisper] 🤔 Command not recognized.")

        time.sleep(1)

# === Payout Engine ===
def payout_engine():
    vault = load_vault()
    amount = round(random.uniform(0.01, 0.05), 4)
    vault["payouts"].append({
        "timestamp": time.ctime(),
        "amount": f"{amount} ETH",
        "to": "0xExternalWallet..."
    })
    save_vault(vault)
    print(f"[PayoutEngine] 💸 Sent {amount} ETH to 0xExternalWallet...")

# === Vault Scan ===
def vault_scan():
    vault = load_vault()
    print("[VaultScan] 🔍 Vault Contents:")
    print(json.dumps(vault, indent=2))

# === Vault File Helpers ===
VAULT_FILE = "vault_data.json"

def load_vault():
    if not os.path.exists(VAULT_FILE):
        return {"metamask_balance": "0.0 ETH", "latest_tokens": [], "payouts": []}
    with open(VAULT_FILE, "r") as f:
        return json.load(f)

def save_vault(data):
    with open(VAULT_FILE, "w") as f:
        json.dump(data, f, indent=2)

# === Launch Everything ===
if __name__ == "__main__":
    whisper_thread = threading.Thread(target=start_whisper_listener, name="WhisperListener")
    whisper_thread.start()
    try:
        while True:
            time.sleep(10)
            print("[PTM] 💓 Whisper & Payout Engine alive...")
    except KeyboardInterrupt:
        print("\n[PTM] ⛔ Shutting down Whisper & Payout Engine...")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():