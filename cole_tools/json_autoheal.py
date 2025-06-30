from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json

# === Folder where critical PTM data files are stored ===
DATA_DIR = "data"

# === Files that should exist, with safe defaults ===
DEFAULTS = {
    "autopilot_queue.json": [],
    "trade_log.json": [],
    "mood_logger.json": [],
    "unlocked_badges.json": [],
    "unlocked_lessons.json": [],
    "lesson_xp.json": {},
    "persona_memory.json": {},
    "watchlist.json": ["AAPL", "TSLA", "MSFT", "NVDA", "QQQ"],
    "active_persona.json": {"active_persona": "Mo Cash"}
}

# === Function to auto-heal bad or missing JSON files ===
def autoheal_json_files():
    repair_log = []

    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    for filename, default_value in DEFAULTS.items():
        path = os.path.join(DATA_DIR, filename)

        if not os.path.exists(path) or os.path.getsize(path) == 0:
            with open(path, "w") as f:
                json.dump(default_value, f, indent=2)
            repair_log.append(f"[CREATED] {filename}")

        else:
            try:
                with open(path, "r") as f:
                    json.load(f)  # attempt to parse
            except Exception:
                with open(path, "w") as f:
                    json.dump(default_value, f, indent=2)
                repair_log.append(f"[REPAIRED] {filename}")

    return repair_log

# === Optional: Run directly for testing ===
if __name__ == "__main__":
    results = autoheal_json_files()
    for entry in results:
        print(entry)