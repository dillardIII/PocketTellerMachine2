# === FILE: voice_parser.py ===
"""
Voice Parser:
Takes raw user speech (transcribed text) and parses it into actionable commands.
Determines intent, target bot/team, and execution type.
"""

import re
from datetime import datetime

def parse_voice_command(command):
    """
    Takes a voice command string and returns structured intent.
    Output: {
        'intent': 'build' | 'review' | 'upgrade' | 'summarize' | 'status',
        'target': 'Replit' | 'GPT' | 'All' | specific bot,
        'content': original command,
        'timestamp': datetime string
    }
    """
    cmd = command.lower().strip()

    # Intent detection
    if "build" in cmd or "generate" in cmd:
        intent = "build"
    elif "review" in cmd or "analyze" in cmd:
        intent = "review"
    elif "upgrade" in cmd or "improve" in cmd:
        intent = "upgrade"
    elif "summarize" in cmd or "recap" in cmd:
        intent = "summarize"
    elif "status" in cmd or "progress" in cmd:
        intent = "status"
    else:
        intent = "unknown"

    # Target team/bot
    if "replit" in cmd:
        target = "Replit"
    elif "chatgpt" in cmd or "gpt" in cmd:
        target = "GPT"
    elif "everyone" in cmd or "all bots" in cmd:
        target = "All"
    else:
        # Try detecting a known assistant name
        match = re.search(r"(mo cash|mentor|strategist|drill instructor|malik)", cmd)
        target = match.group(0).title() if match else "Unassigned"

    return {
        "intent": intent,
        "target": target,
        "content": command,
        "timestamp": datetime.utcnow().isoformat()
    }

# === Manual Test ===
if __name__ == "__main__":
    test = "Mo Cash, upgrade the last strategy and send it to Replit."
    print(parse_voice_command(test))