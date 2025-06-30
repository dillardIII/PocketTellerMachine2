from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: botnet/bridge_config.py ===
"""
Bridge Config Accessor:
Provides helper functions for bot handler lookups and config state access.
"""

import json

CONFIG_PATH = "bridge_config.json"

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def get_active_bot_names():
    config = load_config()
    return [name for name, info in config["bots"].items() if info.get("active")]

def get_bot_handler(bot_name):
    config = load_config()
    bot_info = config["bots"].get(bot_name, {})
    return bot_info.get("handler", None)

def is_bot_active(bot_name):
    config = load_config()
    return config["bots"].get(bot_name, {}).get("active", False)

def get_config_setting(key, default=None):
    config = load_config()
    return config["settings"].get(key, default)