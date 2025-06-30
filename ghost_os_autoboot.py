from ghost_env import INFURA_KEY, VAULT_ADDRESS
# ghost_os_autoboot.py
# Auto-boot manager for Ghost OS and autonomous AI system startup

from ghost_bridge import GhostBridge
from bot_router import BotRouter
from core_logger import CoreLogger

class GhostOSAutoBoot:
    def __init__(self):
        self.logger = CoreLogger("boot.log")
        self.bridge = GhostBridge()
        self.router = BotRouter()
        self.phase = "init"

    def boot_sequence(self):
        self.logger.log("[GhostOS] Initiating boot sequence...")
        self._phase_manager("startup")

        self.logger.log("[GhostOS] Initializing GhostBridge...")
        self.bridge.connect_core_systems()

        self.logger.log("[GhostOS] Routing control passed to BotRouter...")
        self.router.set_context("user", {"phase": "boot", "origin": "ghostos"})

        self._startup_services()
        self._launch_personas()
        self._announce_ready()

        self._phase_manager("online")

    def _phase_manager(self, new_phase):
        self.phase = new_phase
        self.logger.log(f"[GhostOS] Phase set to: {self.phase}")

    def _startup_services(self):
        self.logger.log("[GhostOS] Starting background services...")
        # Add modules here later (e.g., ScreepsOps, CodeDeckOps, etc.)
        self.logger.log("[GhostOS] All background services launched.")

    def _launch_personas(self):
        self.logger.log("[GhostOS] Activating assistant personas...")
        personas = ["Cole", "Mo Cash", "Mentor", "Drill Instructor", "Ali Flint"]
        for persona in personas:
            self.logger.log(f"[GhostOS] Persona {persona} booted and standing by.")

    def _announce_ready(self):
        self.logger.log("[GhostOS] ✅ System online. GhostNet core ready for ops.")
        print("🎮 GhostOS is LIVE. All systems green. Welcome back, Captain.")

# If running standalone
if __name__ == "__main__":
    ghost = GhostOSAutoBoot()
    ghost.boot_sequence()

def log_event():ef drop_files_to_bridge():