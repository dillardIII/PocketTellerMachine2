# === FILE: strategy_suggester.py ===
# 🔁 Strategy Suggester – Proposes new strategy versions based on feedback thread history

import os
import json
from datetime import datetime
from pathlib import Path
from strategy_tools import generate_strategy_fork  # AI-powered fork generator

# === Directories ===
THREADS_DIR = "team_logs/threads"
SUGGESTIONS_DIR = "team_files/suggestions"
Path(SUGGESTIONS_DIR).mkdir(parents=True, exist_ok=True)

def smart_fallback_logic(last_notes):
    """Simple rule-based suggestion if AI module unavailable."""
    if "price <" in last_notes and "volatility" not in last_notes:
        return "price < 175 and RSI < 40"
    elif "MACD" in last_notes or "confirmation" in last_notes:
        return "MACD is bullish and volume > average"
    return "5MA crosses above 20MA"

def suggest_next_version(thread_log_path, bot_name="Mentor", use_fallback=False):
    """
    Reads a feedback thread and proposes a new version.
    If use_fallback=True, uses rule-based strategy generator.
    Otherwise, uses AI strategy forking module.
    """
    if not os.path.exists(thread_log_path):
        print(f"[🧠 SUGGESTER] No thread found: {thread_log_path}")
        return None

    try:
        with open(thread_log_path, "r", encoding="utf-8") as f:
            thread = json.load(f)
    except Exception as e:
        print(f"[🧠 SUGGESTER] Thread read error: {e}")
        return None

    base_name = thread.get("file", "unknown").replace(".py", "")
    last_entry = thread.get("log", [])[-1] if thread.get("log") else {}
    last_notes = last_entry.get("notes", "").lower()

    new_file_name = f"{base_name}_{bot_name}_suggested.py"
    bot_folder = os.path.join(SUGGESTIONS_DIR, bot_name)
    os.makedirs(bot_folder, exist_ok=True)
    full_path = os.path.join(bot_folder, new_file_name)

    # AI Fork Path
    if not use_fallback:
        notes = [f"{post['reviewer']} (v{post['version']}): {post['notes']}" for post in thread.get("log", [])]
        strategy_code = generate_strategy_fork(notes=notes, bot_name=bot_name)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(strategy_code)
        print(f"[🧠 SUGGESTER] AI Fork written to: {full_path}")
        return full_path

    # Fallback logic path
    new_logic = smart_fallback_logic(last_notes)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(f"# Auto-suggested by {bot_name} on {datetime.utcnow().isoformat()}\n")
        f.write("def run_strategy(data):\n")
        f.write(f"    if {new_logic}:\n")
        f.write(f"        return 'Buy AAPL'\n")
        f.write("    return 'Hold'\n")
    print(f"[🧠 SUGGESTER] Rule-based version written to: {full_path}")
    return full_path

# === Example standalone test ===
if __name__ == "__main__":
    example_thread = os.path.join(THREADS_DIR, "mentor_review_aapl.json")
    suggest_next_version(example_thread, bot_name="Mentor", use_fallback=False)