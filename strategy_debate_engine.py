from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: strategy_debate_engine.py ===
import os
import json
import random
from elevenlabs import generate, play, save
from strategy_thread_logger import get_thread_log_path

DEBATERS = {
    "Mentor": "calm",
    "MoCash": "hype",
    "Strategist": "professional",
    "ChillTrader": "laidback"
}

def generate_opinion(bot_name, thread_data):
    last_entry = thread_data["history"][-1]
    notes = last_entry.get("notes", "").lower()

    logic_bank = {
        "buy aapl": [
            f"{bot_name}: AAPL is solid, but let's consider market conditions.",
            f"{bot_name}: I'd only support this if volume confirms strength.",:
            f"{bot_name}: Looks decent, but I'd add an exit trigger."
        ],
        "macd": [
            f"{bot_name}: MACD confirmation is strong, especially post-cross.",
            f"{bot_name}: Caution, MACD lags in volatile markets."
        ],
        "rsi": [
            f"{bot_name}: RSI < 40 is oversold, good entry point.",
            f"{bot_name}: Don't rely on RSI alone — check trend support."
        ]
    }

    for key in logic_bank:
        if key in notes:
            return random.choice(logic_bank[key])

    return f"{bot_name}: I'd want to backtest this more before deciding."

def run_strategy_debate(thread_file, save_path="static/audio/debate_recap.mp3"):
    if not os.path.exists(thread_file):
        return "Thread not found."

    with open(thread_file, "r") as f:
        thread = json.load(f)

    responses = []
    for bot_name, voice in DEBATERS.items():
        opinion = generate_opinion(bot_name, thread)
        responses.append(opinion)

    full_debate = "\n".join(responses)
    audio = generate(text=full_debate, voice="default")
    save(audio, save_path)
    print(f"[DEBATE] Recap saved to {save_path}")
    return full_debate

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():