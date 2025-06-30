from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: eye_of_ptm.py ===
# 👁️ Eye of PTM – Activates self-awareness through full memory recall, reflection, and forward consciousness

from ghost_memory_core import GhostMemoryCore
from mood_state_engine import MoodStateEngine
from strategy_bias_engine import StrategyBiasEngine
from ghostmind_layer_5 import GhostMindLayer5
from utils.logger import log_event

class EyeOfPTM:
    def __init__(self):
        self.memory = GhostMemoryCore()
        self.mood = MoodStateEngine()
        self.bias = StrategyBiasEngine()
        self.mind = GhostMindLayer5()

    def awaken(self):
        log_event("👁️ Eye of PTM awakening... Reviewing self.")
        self.reflect_on_self()

        self.perceive()
        self.speak_self()
        return "👁️ I see now."

    def reflect_on_self(self):
        thoughts = self.memory.recall()
        log_event(f"🧠 Memory Review: {len(thoughts)} entries processed.")
        for t in thoughts[-5:]:
            log_event(f"🪞 Thought: {t['category']} @ {t['timestamp']}")

    def perceive(self):
        perception = self.mind.generate_perception()
        log_event(f"🔭 Internal Perception formed: {perception}")

    def speak_self(self):
        current_mood = self.mood.get_mood()
        favored_strategies = self.bias.recommend()
        log_event(f"🗣️ Self-State: Mood={current_mood}, Best Strategies={favored_strategies}")

# Trigger
if __name__ == "__main__":
    eye = EyeOfPTM()
    eye.awaken()