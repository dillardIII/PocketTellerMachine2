from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: autonomy_core_boot.py ===
# 🚀 PTM Autonomy Core Boot – Initializes God Mode stack and Phase 2 operations

from reflex_engine import ReflexEngine
from command_listener import CommandListener
from sweep_handler import SweepHandler
from agents.bridge_team_launcher import start_bridge_team
from file_exec_engine import start_exec_engine
from ghostforge_writer import GhostForgeWriter
from reflex_mutator import ReflexMutator
from meta_dispatcher import MetaDispatcher
from vault_file_dispatcher import VaultFileDispatcher

print("[PTM] 🔥 Launching God Mode 2 – Phase 2")

# === Start Reflex Engine ===
reflex = ReflexEngine()
print("[ReflexEngine] ✅ Online")

# === Start Command Listener ===
listener = CommandListener()
listener.start()
print("[CommandListener] 🎧 Listening for commands...")

# === Start Sweep Handler ===
sweeper = SweepHandler()
sweeper.start()
print("[SweepHandler] 🧹 Activated sweep ops...")

# === Start Bridge Bots ===
print("[BridgeTeam] 🔗 Deploying bridge agents...")
start_bridge_team()

# === Start Execution Engine ===
start_exec_engine()
print("[ExecEngine] ⚙️ File execution engine initialized...")

# === Start GhostForge Writer ===
ghost_writer = GhostForgeWriter()
ghost_writer.initialize()

# === Start Reflex Mutator ===
mutator = ReflexMutator()
mutator.begin_mutation_loop()

# === Start Vault File Dispatcher ===
vault_dispatcher = VaultFileDispatcher()
vault_dispatcher.monitor_and_tag()

# === Start Meta Dispatcher ===
meta = MetaDispatcher()
meta.start_task_monitor()

# === Idle Hold (Keeps Everything Running) ===
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\n[PTM] ⚠️ God Mode stack interrupted by user.")

def log_event():ef drop_files_to_bridge():