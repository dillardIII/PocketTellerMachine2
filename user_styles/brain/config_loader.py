# user_styles/brain/config_loader.py

import json
import os

CONFIG_PATH = "assistants/ai_brains/config.json"

def get_mode():
    if not os.path.exists(CONFIG_PATH):
        return "paper"
    with open(CONFIG_PATH, "r") as f:
        try:
            config = json.load(f)
            return config.get("mode", "paper")
        except:
            return "paper"