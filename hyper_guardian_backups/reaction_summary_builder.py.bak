"""
Reaction Summary Builder:
Analyzes emotional reactions to produce mood summaries or assistant reflections.
Used in daily briefings, recaps, or adaptive personality tuning.
"""

import json
import os
from collections import Counter
from datetime import datetime

REACTION_LOG = "data/reaction_log.json"

def build_summary(persona):
    """
    Generate a brief mood summary for a persona based on past 10 reactions.
    """
    if not os.path.exists(REACTION_LOG):
        return f"{persona} has no recent emotional logs."

    with open(REACTION_LOG, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return f"{persona} reaction data is corrupted."

    recent = [entry["emotion"] for entry in data if entry["persona"] == persona][-10:]
    
    if not recent:
        return f"{persona} has no recent reactions logged."

    counts = Counter(recent)
    mood, frequency = counts.most_common(1)[0]
    summary = f"{persona} is currently trending as {mood.upper()} (seen {frequency}/10 recent entries)."

    print(f"[📊 Mood Summary] {summary}")
    return summary

# === Manual test
if __name__ == "__main__":
    print(build_summary("MoCash"))