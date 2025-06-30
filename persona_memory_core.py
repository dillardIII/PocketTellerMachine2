from ghost_env import INFURA_KEY, VAULT_ADDRESS
# persona_memory_core.py
# Purpose: Give each assistant persona their own evolving memory profile
# Tracks dialogue, trade participation, mood history, reflections, and user interaction logs

import os
import json
from datetime import datetime

class PersonaMemoryCore:
    def __init__(self, persona_name):
        self.persona = persona_name
        self.memory_path = f"memory/persona_memory/{self.persona.replace(' ', '_')}.json"
        self._initialize_memory()

    def _initialize_memory(self):
        if not os.path.exists("memory/persona_memory"):
            os.makedirs("memory/persona_memory")
        if not os.path.exists(self.memory_path):
            default_memory = {
                "name": self.persona,
                "created": str(datetime.now()),
                "reflections": [],
                "moods": [],
                "trade_logs": [],
                "quotes": [],
                "last_updated": str(datetime.now())
            }
            self._save_memory(default_memory)

    def _load_memory(self):
        with open(self.memory_path, "r") as f:
            return json.load(f)

    def _save_memory(self, data):
        with open(self.memory_path, "w") as f:
            json.dump(data, f, indent=4)

    def log_trade_influence(self, symbol, strategy, result, mood):
        memory = self._load_memory()
        entry = {
            "timestamp": str(datetime.now()),
            "symbol": symbol,
            "strategy": strategy,
            "result": result,
            "mood_at_time": mood
        }
        memory["trade_logs"].append(entry)
        memory["moods"].append(mood)
        memory["last_updated"] = str(datetime.now())
        self._save_memory(memory)

    def add_reflection(self, topic, thought):
        memory = self._load_memory()
        memory["reflections"].append({
            "timestamp": str(datetime.now()),
            "topic": topic,
            "thought": thought
        })
        memory["last_updated"] = str(datetime.now())
        self._save_memory(memory)

    def log_quote(self, quote, context=""):
        memory = self._load_memory()
        memory["quotes"].append({
            "timestamp": str(datetime.now()),
            "quote": quote,
            "context": context
        })
        memory["last_updated"] = str(datetime.now())
        self._save_memory(memory)

    def get_memory_snapshot(self):
        return self._load_memory()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():