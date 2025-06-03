# === FILE: validate_mood_spike.py ===
# This script checks if the mood.spike.json file is valid JSON.
# It helps prevent BridgeBot crashes from bad formatting.

import json

try:
    with open("settings/mood_spike.json", "r") as f:
        data = json.load(f)
    print("✅ mood_spike.json is valid.")
except Exception as e:
    print("❌ JSON error:", e)