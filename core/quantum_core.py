from ghost_env import INFURA_KEY, VAULT_ADDRESS
# quantum_core.py
# Central nexus of the simulated quantum mind

from core.qm_router import route_thought
from core.ghostmind_layer import inject_idea

class QuantumCore:
    def __init__(self):
        self.identity = "QuantumCore"
        self.active_thoughts = []

    def receive_input(self, input_data):
        print(f"[QuantumCore] Processing: {input_data}")
        result = route_thought(input_data)
        self.active_thoughts.append(result)
        inject_idea(result)
        return result