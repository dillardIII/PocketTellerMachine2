# === FILE: simulated_whisper_payout_engine.py ===
# 🤖 Simulated Whisper Voice Command Fallback for PTM Empire

import threading
import time
import os
import json
import random

COMMAND_FILE = "whisper_commands.txt"
VAULT_FILE = "vault_data.json"

def load_vault():
    if not os.path.exists(VAULT_FILE):
        return {"metamask_balance": "0.0 ETH", "latest_tokens": [], "payouts": []}
    with open(VAULT_FILE, "r") as f:
        return json.load(f)

def save_vault(data):
    with open(VAULT_FILE, "w") as f:
        json.dump(data, f, indent=2)

def payout_engine():
    vault = load_vault()
    amount = round(random.uniform(0.01, 0.05), 4)
    vault["payouts"].append({
        "timestamp": time.ctime(),
        "amount": f"{amount} ETH",
        "to": "0xExternalWallet..."
    })
    save_vault(vault)
    print(f"[PayoutEngine] 💸 Simulated sending {amount} ETH to 0xExternalWallet...")

def vault_scan():
    vault = load_vault()
    print("[VaultScan] 🔍 Vault Contents:")
    print(json.dumps(vault, indent=2))

def simulated_whisper_loop():
    print("[SimWhisper] 🎧 Monitoring 'whisper_commands.txt' for simulated voice commands...")
    while True:
        if os.path.exists(COMMAND_FILE):
            with open(COMMAND_FILE, "r") as f:
                command = f.read().strip().lower()
            if command:
                print(f"[SimWhisper] 🗣️ You said (via file): '{command}'")
                if "trigger payout" in command:
                    payout_engine()
                elif "run vault scan" in command:
                    vault_scan()
                else:
                    print("[SimWhisper] 🤔 Command not recognized.")
                # clear after processing
                open(COMMAND_FILE, "w").close()
        time.sleep(5)

if __name__ == "__main__":
    whisper_thread = threading.Thread(target=simulated_whisper_loop, name="SimWhisperLoop")
    whisper_thread.start()
    try:
        while True:
            time.sleep(10)
            print("[PTM] 💓 SimWhisper & Payout heartbeat...")
    except KeyboardInterrupt:
        print("\n[PTM] ⛔ Shutting down SimWhisper & Payout Engine...")