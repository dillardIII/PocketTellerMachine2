from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: game_logic_engine.py ===

import time
import random
from assistants.voice_trigger import speak_from_persona
from core.memory_logger import log_game_action

# === Turn States ===
TURN_HUMAN = "human"
TURN_PTM = "ptm"
TURN_COOP = "co-op"

# === Game Logic Controller ===
class GameSession:
    def __init__(self, game_name, strategy, persona_name, turn_mode=TURN_COOP):
        self.game_name = game_name
        self.strategy = strategy
        self.persona = persona_name
        self.turn_mode = turn_mode
        self.active = True
        self.history = []

    def start(self):
        speak_from_persona(self.persona, f"Initiating {self.game_name} using strategy: {self.strategy}. Let’s go, Captain.")
        while self.active:
            if self.turn_mode == TURN_HUMAN:
                speak_from_persona(self.persona, "It’s your turn. I’m watching and logging.")
                self.wait_for_human_input()

            elif self.turn_mode == TURN_PTM:
                speak_from_persona(self.persona, "My turn. Executing logic now.")
                self.ptm_move()

            elif self.turn_mode == TURN_COOP:
                self.coop_turn()

            time.sleep(2)  # Delay between turns

    def wait_for_human_input(self):
        move = input("Describe your action: ")
        self.history.append(("HUMAN", move))
        log_game_action(self.game_name, move, source="Human")

    def ptm_move(self):
        simulated_move = f"AI_Move_{random.randint(1, 100)}"
        self.history.append(("PTM", simulated_move))
        log_game_action(self.game_name, simulated_move, source="PTM")
        speak_from_persona(self.persona, f"My move: {simulated_move}")

    def coop_turn(self):
        speak_from_persona(self.persona, "Co-op turn. We’re sharing control.")
        self.wait_for_human_input()
        self.ptm_move()

    def stop(self):
        self.active = False
        speak_from_persona(self.persona, f"{self.game_name} session terminated.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():