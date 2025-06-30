from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: architect_kernel.py ===
# 🧠 Architect Kernel – Fusion point of all AI subsystems

from ghostmind_layer_5 import GhostMindLayer5
from soul_reactor import SoulReactor
from guardian_reflex import GuardianReflex
from persona_speaker_manager import PersonaSpeakerManager
from ghost_vision_driver import GhostVisionDriver
from ghost_memory_core import GhostMemoryCore
from dimensional_gateway import DimensionalGateway
from ghost_council_throne import GhostCouncilThrone
from utils.logger import log_event

class ArchitectKernel:
    def __init__(self):
        self.mind = GhostMindLayer5()
        self.soul = SoulReactor()
        self.guardian = GuardianReflex()
        self.voice = PersonaSpeakerManager()
        self.vision = GhostVisionDriver()
        self.memory = GhostMemoryCore()
        self.gateway = DimensionalGateway()
        self.council = GhostCouncilThrone()

    def full_scan(self):
        log_event("🧠 Running Full System Scan...")

        perception = self.mind.generate_perception()
        self.memory.remember("Perception", perception)

        security = self.guardian.run_security_check()
        self.memory.remember("SecurityStatus", security)

        vision = self.vision.generate_vision("SPY", "Iron Condor")
        self.memory.remember("Vision", vision)

        dimension = self.gateway.open("Momentum Surge")
        self.memory.remember("AltReality", dimension)

        self.voice.speak("Fusion check complete. All systems connected.")

        return {
            "perception": perception,
            "security": security,
            "vision": vision,
            "dimension": dimension
        }

    def make_master_decision(self, topic, choices):
        self.voice.speak(f"Calling council to decide on: {topic}")
        return self.council.initiate_session(topic, choices)

# Trigger
if __name__ == "__main__":
    kernel = ArchitectKernel()
    scan = kernel.full_scan()
    decision = kernel.make_master_decision("Rotate strategy?", ["Yes", "No", "Delay"])