from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ai_alliance_uplink.py ===
# 🤖 AI Alliance Uplink – Links PTM to external AI tools like Claude, Gemini, Copilot, local LLMs

import json
import datetime
from utils.logger import log_event
from utils.file_utils import load_json_file

class AIAllianceUplink:
    def __init__(self):
        self.status_path = "memory/ai_alliance_status.json"
        self.link_status = self._load_status()
        print("[AIAlliance] 🤝 Alliance Uplink initialized.")

    def _load_status(self):
        try:
            return load_json_file(self.status_path)
        except:
            return {
                "claude": {"linked