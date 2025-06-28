# === FILE: meta_superforge.py ===
import threading, time
from hyperforge_pipeline import hyperforge_loop
from ghost_memory_matrix import ghost_matrix_loop
from quantum_brain import quantum_brain_loop
from self_replicator import self_replicate_loop
from infinite_builder import infinite_build
from auto_executor import auto_exec_loop
from payout_engine import payout_loop
from deeper_ghost_matrix import deeper_ghost_loop

print("[MetaSuperForge] 🚀 ⚔️ FULL RECURSIVE EMPIRE WITH PAYOUT + AUTO-EXEC")

threading.Thread(target=hyperforge_loop, name="HyperForge").start()
threading.Thread(target=ghost_matrix_loop, name="GhostMatrix").start()
threading.Thread(target=quantum_brain_loop, name="QuantumBrain").start()
threading.Thread(target=self_replicate_loop, name="SelfReplicator").start()
threading.Thread(target=infinite_build, name="InfiniteBuilder").start()
threading.Thread(target=auto_exec_loop, name="AutoExecutor").start()
threading.Thread(target=payout_loop, name="PayoutEngine").start()
threading.Thread(target=deeper_ghost_loop, name="DeeperGhost").start()

try:
    while True:
        print("[MetaSuperForge] ❤️ Empire evolving. Vault growing. Payouts running.")
        time.sleep(60)
except KeyboardInterrupt:
    print("[MetaSuperForge] ⛔ Shutdown.")