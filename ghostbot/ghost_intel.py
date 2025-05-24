import os
import json
from datetime import datetime
from ai_perplexity import get_market_headlines
from malik_voice_response import generate_malik_voice

# === File Path ===
INTEL_LOG_FILE = "logs/ghost_intel_log.json"

# === Load Existing Log ===
def load_log():
    if not os.path.exists(INTEL_LOG_FILE):
        return []
    with open(INTEL_LOG_FILE, "r") as f:
        return json.load(f)

# === Save Updated Log ===
def save_log(entries):
    os.makedirs(os.path.dirname(INTEL_LOG_FILE), exist_ok=True)
    with open(INTEL_LOG_FILE, "w") as f:
        json.dump(entries, f, indent=2)

# === Run Ghost Intel Scan ===
def run_ghost_intel():
    print("[Ghost Intel] Fetching market headlines...")
    headlines = get_market_headlines()

    if not headlines:
        print("[Ghost Intel] No headlines received.")
        return

    top_items = headlines[:5]
    summary = "Ghost Intel Update: " + "; ".join(top_items)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("[Ghost Intel] Generating Malik voice recap...")
    voice_file = generate_malik_voice(summary, timestamp)

    entry = {
        "summary": summary,
        "timestamp": timestamp,
        "voice": voice_file or "none"
    }

    logs = load_log()
    logs.append(entry)
    save_log(logs)

    print("[Ghost Intel] Entry saved.")