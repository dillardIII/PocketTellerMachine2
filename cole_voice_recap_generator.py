from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from datetime import datetime
from elevenlabs import generate, save, voices, set_api_key

set_api_key(os.getenv("ELEVENLABS_API_KEY"))

TRADE_FILE = "data/trades.json"
RECAP_FOLDER = "static/voices/recaps/"
os.makedirs(RECAP_FOLDER, exist_ok=True)

def generate_voice_recap(text, voice="Rachel", filename="recap.mp3"):
    try:
        print(f"[VOICE] Generating recap: {filename}")
        audio = generate(text=text, voice=voice)
        save(audio, os.path.join(RECAP_FOLDER, filename))
        return filename
    except Exception as e:
        print(f"[VOICE ERROR]: {e}")
        return None

def attach_recap_to_latest_trade():
    if not os.path.exists(TRADE_FILE):
        print("[RECAP] No trades to attach to.")
        return

    with open(TRADE_FILE, "r") as f:
        trades = json.load(f)

    if not trades:
        print("[RECAP] Trade list empty.")
        return

    latest = trades[-1]
    trade_id = latest.get("trade_id", f"trade_{len(trades)}")
    recap_text = f"Trade {trade_id} was executed using {latest.get('strategy', 'an unknown strategy')} and ended in a {latest.get('result', 'neutral')} outcome."

    filename = f"{trade_id}_recap.mp3"
    filepath = generate_voice_recap(recap_text, filename=filename)

    if filepath:
        latest["recap_mp3"] = f"/static/voices/recaps/{filename}"
        with open(TRADE_FILE, "w") as f:
            json.dump(trades, f, indent=2)
        print(f"[RECAP] Attached voice recap to {trade_id}")

if __name__ == "__main__":
    attach_recap_to_latest_trade()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():