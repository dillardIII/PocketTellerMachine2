"""
Dream Manifest Engine:
Responsible for interpreting dream patterns, symbolic inputs, and subconscious cues to generate actionable tasks or ideas for PTM.
"""

import json
from datetime import datetime
from core.reaction_logger import log_reaction

MANIFEST_LOG = "memory/dream_manifest_log.json"
DREAM_INPUT = "memory/dream_patterns.json"

def load_dream_patterns():
    try:
        with open(DREAM_INPUT, "r") as f:
            return json.load(f)
    except:
        return {}

def save_manifested_ideas(data):
    try:
        with open(MANIFEST_LOG, "w") as f:
            json.dump(data[-200:], f, indent=2)
    except Exception as e:
        print(f"[DreamManifestEngine] Log write failed: {e}")

def manifest_dreams():
    patterns = load_dream_patterns()
    ideas = []
    timestamp = datetime.now().isoformat()

    for symbol, intent in patterns.items():
        action = f"Manifesting intent: '{intent}' from dream symbol '{symbol}'"
        print(f"[DreamManifestEngine] {action}")
        log_reaction(symbol, intent)
        ideas.append({
            "symbol": symbol,
            "intent": intent,
            "timestamp": timestamp
        })

    save_manifested_ideas(ideas)